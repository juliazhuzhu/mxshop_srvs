# -*-coding:utf-8-*-
from datetime import datetime

from peewee import *
# from playhouse.pool import PooledMySQLDatabase
# from playhouse.shortcuts import ReconnectMixin
# from playhouse.mysql_ext import JSONField
from order_srv.settings import settings

# class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
#     # pyrthon mro
#     pass
#
#
# db = ReconnectMysqlDatabase("mxshop_order_srv", host="172.20.0.204", port=3306, user="root", password="123456")


class BaseModel(Model):
    add_time = DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = DateTimeField(default=datetime.now, verbose_name="更新时间")
    is_deleted = BooleanField(default=False, verbose_name="是否删除")

    def save(self, *args, **kwargs):
        # 判断是否新增数据，还是更新数据
        if self._pk is not None:
            # 这是已有数据
            self.update_time = datetime.now()

        return super().save(*args, **kwargs)

    @classmethod
    def delete(cls, permanently=False):
        if permanently:
            return super().delete()
        else:
            return super().update(is_deleted=True)

    def delete_instance(self, permanently=False, recursive=False, delete_nullable=False):
        if permanently:
            return self.delete(permanently=True).where(self._pk_expr()).execute()

        self.is_deleted = True
        self.save()

    @classmethod
    def select(cls, *fields):
        return super().select(*fields).where(cls.is_deleted == False)

    class Meta:
        database = settings.DB

# class Stock(BaseModel):
#     #仓库表
#     name = CharField(verbose_name="仓库名")
#     address = CharField(verbose_name="仓库地址")

class ShoppingCart(BaseModel):
    #购物车
    user = IntegerField(verbose_name="user id")
    goods = IntegerField(verbose_name="商品id")
    nums = IntegerField(verbose_name="购买数量")
    checked = BooleanField(verbose_name="是否选中", default=True)

class OrderInfo(BaseModel):
    #订单
    ORDER_STATUS = (
        ("TRADE_SUCCESS","成功"),
        ("TRADE_CLOSED","超时关闭"),
        ("WAIT_BUYER_PAY","交易创建"),
        ("TRADE_FINISHED","交易结束")
    )
    PAY_TYPE = (
        ("alipay", "alipay")
    )
    user = IntegerField(verbose_name="user id")
    order_sn = CharField(max_length=30, null=True, unique=True, verbose_name="订单号")
    pay_type = CharField(choices=PAY_TYPE, default="alipay", max_length=30, verbose_name="支付方式")
    status = CharField(choices=ORDER_STATUS, default="WAIT_BUYER_PAY", max_length=30, verbose_name="订单状态")
    trade_no = CharField(max_length=100, unique=True, null=True, verbose_name="交易号")
    order_mount = DecimalField(default=0.0, verbose_name="订单金额")
    pay_time = DateTimeField(null=True, verbose_name="支付时间")

    address = CharField(max_length=100, default="", verbose_name="收货地址")
    signer_name = CharField(max_length=20, default="", verbose_name="签收人")
    signer_mobile = CharField(max_length=11, verbose_name="联系电话")
    post = CharField(max_length=200, default="", verbose_name="留言")


class OrderGoods(BaseModel):
    # 订单商品
    order = IntegerField(verbose_name="订单id")
    goods = IntegerField(verbose_name="商品id")
    goods_name = CharField(max_length=20, default="", verbose_name="商品名称")
    goods_image = CharField(max_length=200, default="", verbose_name="商品图片")
    goods_price = CharField(verbose_name="商品价格")
    nums = IntegerField(default=0, verbose_name="商品数量")


if __name__ == "__main__":

    settings.DB.create_tables([ShoppingCart,OrderInfo,OrderGoods])
    # c1 = Category(name="bobby1", level=1)
    # c2 = Category(name="bobby2", level=1)
    # c1.save()
    # c2.save()

    # c1 = Category.get(Category.id == 1)
    # c1.delete_instance()
    # c3 = Category.get(Category.id == 3)
    # c3.delete_instance(permanently=True)
    # Category.delete().where(Category.id == 2).execute()
    # for c in Category.select():
    #     print(c.name, c.id)

    # for i in range(421, 841):
    #     try:
    #         inv = Inventory.get(Inventory.goods==i)
    #         inv.stocks = 100
    #         inv.save()
    #     except DoesNotExist as e:
    #         inv = Inventory(goods=i, stocks=100)
    #         inv.save(force_insert=True)
