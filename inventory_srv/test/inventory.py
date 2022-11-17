# -*-coding:utf-8-*-
import json

import grpc
import consul
from inventory_srv.proto import inventory_pb2, inventory_pb2_grpc
from inventory_srv.settings import settings
from google.protobuf import empty_pb2

class InventoryTest:
    def __init__(self):
        c = consul.Consul(host=settings.CONSUL_HOST, port=settings.CONSUL_PORT)
        services = c.agent.services()
        ip = ""
        port = 0
        for key, value in services.items():
            if value["Service"] == settings.SERVICE_NAME:
                ip = value["Address"]
                port = value["Port"]
                break
        if not ip:
            raise Exception()
        channel = grpc.insecure_channel(f"{ip}:{port}")
        self.stub = inventory_pb2_grpc.InventoryStub(channel)

    def set_inv(self):
        rsp = self.stub.SetInv(
            inventory_pb2.GoodsInvInfo(goodsId=11, num=100)
        )



    def get_inv(self):
        rsp = self.stub.InvDetail(
            inventory_pb2.GoodsInvInfo(goodsId=10)
        )
        print(rsp.num)

    def sell(self):
        goods_list = [(10,20),(11,30)]
        request = inventory_pb2.SellInfo()
        for goodsId, num in goods_list:
            request.goodsInfo.append(inventory_pb2.GoodsInvInfo(goodsId=goodsId, num=num))
        rsp = self.stub.Sell(request)

    def reback(self):
        goods_list = [(10,20),(30, 4)]
        request = inventory_pb2.SellInfo()
        for goodsId, num in goods_list:
            request.goodsInfo.append(inventory_pb2.GoodsInvInfo(goodsId=goodsId, num=num))
        rsp = self.stub.Reback(request)

if __name__ == "__main__":
    inventory = InventoryTest()

    # inventory.set_inv()
    # inventory.sell()
    #inventory.get_inv()
    # inventory.reback()
    inventory.get_inv()