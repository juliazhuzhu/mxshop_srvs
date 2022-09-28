import grpc
from loguru import logger
from goods_srv.proto import goods_pb2, goods_pb2_grpc
from goods_srv.model.models import Goods, Category, Brands
from peewee import DoesNotExist
from google.protobuf import empty_pb2
import json

def convert_model_to_message(goods):
    info_rsp = goods_pb2.GoodInfoResponse()

    info_rsp.id = goods.id
    info_rsp.categoryId = goods.category_id
    info_rsp.name = goods.name
    info_rsp.goodsSn = goods.goods_sn
    info_rsp.clickNum = goods.click_num
    info_rsp.soldNum = goods.sold_num
    info_rsp.favNum = goods.fav_num
    info_rsp.marketPrice = goods.market_price
    info_rsp.shopPrice = goods.shop_price
    info_rsp.goodsBrief = goods.goods_brief
    info_rsp.shipFree = goods.ship_free
    info_rsp.goodsFrontImage = goods.goods_front_image
    info_rsp.isNew = goods.is_new
    info_rsp.descImages.extend(goods.desc_images)
    info_rsp.images.extend(goods.images)
    info_rsp.isHot = goods.is_hot
    # info_rsp.onSale = goods.on_sale

    info_rsp.category.id = goods.category.id
    info_rsp.category.name = goods.category.name
    info_rsp.brand.id = goods.brand.id
    info_rsp.brand.name = goods.brand.name
    info_rsp.brand.logo = goods.brand.logo

    return info_rsp

def category_model_to_dict(category):
    re = {}

    re["id"] = category.id
    re["name"] = category.name
    re["level"] = category.level
    re["parent"] = category.parent_category_id
    re["is_tab"] = category.is_tab
    return re

class GoodsServicer(goods_pb2_grpc.GoodsServicer):

    @logger.catch
    def GoodsList(self, request: goods_pb2.GoodsFilterRequest, context):
        rsp = goods_pb2.GoodsListResponse()
        goods = Goods.select()
        if request.keywords:
            goods = goods.filter(Goods.name.contains(request.keywords))
        if request.isHot:
            goods = goods.filter(Goods.is_hot == True)
        if request.isNew:
            goods = goods.filter(Goods.is_new == True)
        if request.priceMin:
            goods = goods.filter(Goods.shop_price >= request.priceMin)
        if request.priceMax:
            goods = goods.filter(Goods.shop_price <= request.priceMax)
        if request.brand:
            goods = goods.filter(Goods.brand_id == request.brand)
        if request.topCategory:
            try:
                ids = []
                category = Category.get(Category.id == request.topCategory)
                level = category.level
                if level == 2:
                    categorys = Category.select().where(Category.parent_category_id == request.topCategory)
                    for category in categorys:
                        ids.append(category.id)
                elif level == 1:
                    c2 = Category.alias()
                    categorys = Category.select().where(Category.parent_category_id.in_(
                        c2.select(c2.id).where(c2.parent_category_id == request.topCategory)))
                    for category in categorys:
                        ids.append(category.id)
                elif level == 3:
                    ids.append(request.topCategory)

                goods = goods.where(Goods.category_id.in_(ids))

            except Exception as e:
                pass

        start = 0
        per_page_nums = 10
        if request.pagePerNums:
            per_page_nums = request.pagePerNums
        if request.pages:
            start = per_page_nums * (request.pages - 1)
        goods = goods.limit(per_page_nums).offset(start)
        rsp.total = goods.count()
        for good in goods:
            rsp_good = convert_model_to_message(good)
            # print(rsp_good)
            rsp.data.append(rsp_good)

        return rsp

    @logger.catch
    def BatchGetGoods(self, request: goods_pb2.BatchGoodsIdInfo, context):
        # 批量获取商品详情，订单新建的时候可以试用
        rsp = goods_pb2.GoodsListResponse()
        goods = Goods.select().where(Goods.id.in_(request.id))

        rsp.total = goods.count()
        for good in goods:
            rsp_good = convert_model_to_message(good)
            # print(rsp_good)
            rsp.data.append(rsp_good)

        return rsp

    @logger.catch
    def DeleteGoods(self, request: goods_pb2.DeleteGoodsInfo, context):

        try:
            goods = Goods.get(Goods.id == request.id)
            goods.delete_instance()
            return empty_pb2.Empty()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("record does not exist.")
            return empty_pb2.Empty()
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_detail(str(e))
            return empty_pb2.Empty()

    @logger.catch
    def GetGoodsDetail(self, request: goods_pb2.GoodInfoRequest, context):
        try:
            goods = Goods.get(Goods.id == request.id)
            goods.click_num += 1
            goods.save()
            return convert_model_to_message(goods)
        except DoesNotExist:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_detail("record doest not exsit")
            return goods_pb2.GoodsInfoResponse()

    @logger.catch
    def CreateGoods(self, request: goods_pb2.CreateGoodsInfo, context):
        try:
            category = Category.get(Category.id == request.categoryId)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("商品分类不存在")
            return goods_pb2.GoodInfoResponse()

        try:
            brand = Brands.get(Brands.id == request.brand)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("品牌分类不存在")
            return goods_pb2.GoodInfoResponse()

        goods = Goods()
        goods.brand = brand
        goods.category = category
        goods.name = request.name
        goods.goods_sn = request.goodsSn
        goods.market_price = request.marketPrice
        goods.shop_price = request.shopPrice
        goods.goods_brief = request.goodsBrief
        goods.ship_free = request.shipFree
        goods.images = list(request.images)
        goods.desc_images = list(request.descImages)
        goods.goods_front_image = request.goodsFrontImage
        goods.is_new = request.isNew
        goods.is_hot = request.isHot
        goods.on_sale = request.onSale

        goods.save()

        # TODO 此处完善库存的设置 - 分布式事务

        return convert_model_to_message(goods)

    @logger.catch
    def UpdateGoods(self, request: goods_pb2.CreateGoodsInfo, context):

        try:
            category = Category.get(Category.id == request.categoryId)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("商品分类不存在")
            return empty_pb2.Empty()

        try:
            brand = Brands.get(Brands.id == request.brand)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("品牌分类不存在")
            return goods_pb2.GoodInfoResponse()

        try:
            goods = Goods.get(Goods.id == request.id)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("商品不存在")
            return empty_pb2.Empty()

        goods.brand = brand
        goods.category = category
        goods.name = request.name
        goods.goods_sn = request.goodsSn
        goods.market_price = request.marketPrice
        goods.shop_price = request.shopPrice
        goods.goods_brief = request.goodsBrief
        goods.ship_free = request.shipFree
        goods.images = list(request.images)
        goods.desc_images = list(request.descImages)
        goods.goods_front_image = request.goodsFrontImage
        goods.is_new = request.isNew
        goods.is_hot = request.isHot
        goods.on_sale = request.onSale

        goods.save()
        # TODO 此处完善库存的设置 - 分布式事务
        return empty_pb2.Empty()

    @logger.catch
    def GetAllCategorysList(self, request: empty_pb2.Empty, context):
        '''
            [{
                    "name". "xxxx"
                    "id":xxx,
                    "sub_category":[
                    {
                        "name". "xxxx"
                        "id":xxx,
                        "sub_category":[
                            "name". "xxxx"
                            "id":xxx
                        ]
                    },{},{}]
                }]
            },{},{}]
        '''

        level1 = []
        level2 = []
        level3 = []
        category_list_response = goods_pb2.CategoryListResponse()
        category_list_response.total = Category.select().count()
        for category in Category.select():
            category_rsp = goods_pb2.CategoryInfoResponse()

            category_rsp.id = category.id
            category_rsp.name = category.name
            if category.parent_category_id:
                category_rsp.parentCategory = category.parent_category_id
            category_rsp.level = category.level
            category_rsp.isTab = category.is_tab
            category_list_response.data.append(category_rsp)

            if category_rsp.level == 1:
                level1.append(category_model_to_dict(category))
            elif category_rsp.level == 2:
                level2.append(category_model_to_dict(category))
            elif category_rsp.level == 3:
                level3.append(category_model_to_dict(category))

        for data3 in level3:
            for data2 in level2:
                if data3["parent"] == data2["id"]:
                    if "sub_category" not in data2:
                        data2["sub_category"] = [data3]
                    else:
                        data2["sub_category"].append(data3)

        for data2 in level2:
            for data1 in level1:
                if data2["parent"] == data1["id"]:
                    if "sub_category" not in data1:
                        data1["sub_category"] = [data2]
                    else:
                        data1["sub_category"].append(data2)

        category_list_response.jsonData = json.dumps(level1)
        return category_list_response