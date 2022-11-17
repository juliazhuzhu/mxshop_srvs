# -*-coding:utf-8-*-
from datetime import datetime

from peewee import *
# from playhouse.pool import PooledMySQLDatabase
# from playhouse.shortcuts import ReconnectMixin
# from playhouse.mysql_ext import JSONField
from inventory_srv.settings import settings

# class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
#     # pyrthon mro
#     pass


# db = ReconnectMysqlDatabase("mxshop_inventory_srv", host="172.20.0.204", port=3306, user="root", password="123456")


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

class Inventory(BaseModel):
    #商品库存表
    # stock = PrimaryKeyField(stock)
    goods = IntegerField(verbose_name="商品id", unique=True)
    stocks = IntegerField(verbose_name="库存数量", default=0)
    version = IntegerField(verbose_name="版本号", default=0)#分布式锁的乐观锁


# class InventoryHistory(BaseModel):
#     user = IntegerField(verbose_name="userid", unique=True)
#     goods = IntegerField(verbose_name="商品id", unique=True)
#     nums = IntegerField(verbose_name="数量", unique=False)
#     order = IntegerField(verbose_name="orderid", unique=True)
#     status = IntegerField(choices=((1,"未出库"),(2,"已出库")), default=1)


if __name__ == "__main__":

    # settings.DB.create_tables([Inventory])
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

    for i in range(421, 841):
        try:
            inv = Inventory.get(Inventory.goods==i)
            inv.stocks = 100
            inv.save()
        except DoesNotExist as e:
            inv = Inventory(goods=i, stocks=100)
            inv.save(force_insert=True)
