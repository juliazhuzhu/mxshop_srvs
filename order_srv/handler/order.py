# -*-coding:utf-8-*-
from order_srv.proto import order_pb2_grpc
from loguru import logger
from order_srv.model.models import ShoppingCart, OrderInfo, OrderGoods
from order_srv.proto import order_pb2
from peewee import DoesNotExist
import grpc
from google.protobuf import empty_pb2


class OrderServicer(order_pb2_grpc.OrderServicer):
    @logger.catch
    def CartItemList(self, request, context):
        # 获取用户的购物车信息
        items = ShoppingCart.select().where(ShoppingCart.user == request.id)
        rsp = order_pb2.CartItemListResponse(total=items.count())
        for item in items:
            item_rsp = order_pb2.ShopCartInfoResponse()

            item_rsp.id = item.id
            item_rsp.userId = item.user
            item_rsp.goodsId = item.goods
            item_rsp.nums = item.nums
            item_rsp.checked = item.checked

            rsp.data.append(item_rsp)

        return rsp

    @logger.catch
    def CreateCartItem(self, request, context):
        # 添加商品到购物车

        existed_items = ShoppingCart.select().where(ShoppingCart.goods == request.goodsId,
                                                    ShoppingCart.user == request.userId)
        # 如果记录存在，则合并购物车
        if existed_items:
            item = existed_items[0]
            item.nums += request.nums
        else:
            item = ShoppingCart()
            item.user = request.userId
            item.goods = request.goodsId
            item.nums = request.nums
        item.save()

        return order_pb2.ShopCartInfoResponse(id=item.id)

    @logger.catch
    def UpdateCartItem(self, request, context):
        # 更新购物车条目-数量和选中状态
        try:
            item = ShoppingCart.get(ShoppingCart.id == request.id)
            item.checked = request.checked
            if request.nums > 0:
                item.nums = request.nums
            item.save()
            return empty_pb2.Empty()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("购物车记录不存在")
            return empty_pb2.Empty()

    @logger.catch
    def DeleteCardItem(self, request, context):
        # 删除购物车条目
        try:
            item = ShoppingCart.get(ShoppingCart.id == request.id)
            item.delete_instance()
            return empty_pb2.Empty()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("购物车记录不存在")
            return empty_pb2.Empty()

    @logger.catch
    def OrderList(self, request, context):
        # 订单列表
        rsp = order_pb2.OrderListResponse()
        orders = OrderInfo.select()
        if request.userId:
            orders = orders.where(OrderInfo.user == request.userId)
        rsp.total = orders.count()

        start = 0
        per_page_nums = request.pagePerNum if request.pagePerNum else 10
        start = per_page_nums * (request.pages - 1) if request.pages else 0
        orders = orders.limit(per_page_nums).offset(start)

        for order in orders:
            tmp_rsp = order_pb2.OrderInfoResponse()

            tmp_rsp.id = order.id
            tmp_rsp.userId = order.user
            tmp_rsp.orderSn = order.order_sn
            tmp_rsp.payType = order.pay_type
            tmp_rsp.status = order.status
            tmp_rsp.post = order.post
            tmp_rsp.total = order.order_mount
            tmp_rsp.address = order.address
            tmp_rsp.name = order.signer_name
            tmp_rsp.mobile = order.signer_mobile

            rsp.data.append(tmp_rsp)
        return rsp

    @logger.catch
    def OrderDetail(self, request, context):
        # 订单详情
        rsp = order_pb2.OrderInfoDetailResponse()
        try:
            order = OrderInfo.get(OrderInfo.id == request.id)

            rsp.orderInfo.id = order.id
            rsp.orderInfo.userId = order.user
            rsp.orderInfo.orderSn = order.order_sn
            rsp.orderInfo.payType = order.pay_type
            rsp.orderInfo.status = order.status
            rsp.orderInfo.post = order.post
            rsp.orderInfo.total = order.order_mount
            rsp.orderInfo.address = order.address
            rsp.orderInfo.name = order.signer_name
            rsp.orderInfo.mobile = order.signer_mobile

            order_goods = OrderGoods.select().where(OrderGoods.order == order.id)
            rsp.item_num = order_goods.count()
            for order_good in order_goods:
                order_goods_rsp = order_pb2.OrderItemResponse()

                order_goods_rsp.goodsId = order_good.goods
                order_goods_rsp.goodsName = order_good.goods_name
                order_goods_rsp.goodsImage = order_good.goods_image
                order_goods_rsp.goodsPrice = float(order_good.goods_price)
                order_goods_rsp.nums = order_good.nums

                rsp.data.append(order_goods_rsp)
            return rsp
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("订单记录不存在")
            return rsp

    @logger.catch
    def UpdateOrderStatus(self, request, context):
        # 修改订单的支付状态
        OrderInfo.update(status=request.status).where(OrderInfo.order_sn == request.orderSn).excute()
        return empty_pb2.Empty()
