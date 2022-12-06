# -*-coding:utf-8-*-
import json

import grpc
import consul
from order_srv.proto import order_pb2, order_pb2_grpc
from order_srv.settings import settings
from google.protobuf import empty_pb2

class OrderTest:

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
        self.stub = order_pb2_grpc.OrderStub(channel)


    def create_cart_item(self):
        rsp = self.stub.CreateCartItem(order_pb2.CartItemRequest(userId=1, goodsId=422, nums=3))
        print(rsp)
        return


    def create_item_list(self):
        rsp = self.stub.CartItemList(order_pb2.UserInfo(id=1))
        print(rsp)

    def create_order(self):
        rsp = self.stub.CreateOrder(
            order_pb2.OrderRequest(userId=1, address="Beijing", mobile="13501171570", name="xiaoye", post="send immediately")
        )

        print(rsp)

    def order_list(self):
        rsp = self.stub.OrderList(order_pb2.OrderFilterRequest(userId=1))
        print(rsp)

if __name__== "__main__":
    order = OrderTest()
    # order.create_cart_item()
    # order.create_order()
    order.order_list()