import json

import grpc
import consul
from goods_srv.proto import goods_pb2_grpc, goods_pb2
from goods_srv.settings import settings
from google.protobuf import empty_pb2

class GoodsTest:

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
        self.stub = goods_pb2_grpc.GoodsStub(channel)

    def goods_list(self):
        rsp: goods_pb2.GoodsListResponse = self.stub.GoodsList(
            goods_pb2.GoodsFilterRequest(keywords="越南")
        )

        for item in rsp.data:
            print(item.name, item.shopPrice)

    def batch_get(self):
        ids = [421,422]

        rsp: goods_pb2.GoodsListResponse = self.stub.BatchGetGoods(
            goods_pb2.BatchGoodsIdInfo(id=ids)
        )
        for item in rsp.data:
            print(item.name, item.shopPrice)

    def get_detail(self, id):
        rsp = self.stub.GetGoodsDetail(goods_pb2.GoodInfoRequest(
            id=id
        ))
        print(rsp.name)

    def category_list(self):
        rsp = self.stub.GetAllCategorysList(empty_pb2.Empty())
        print(rsp.jsonData)
        data = json.loads(rsp.jsonData)
        print(data)

if __name__ == "__main__":
    goods_test = GoodsTest()
    # goods_test.goods_list()
    # goods_test.batch_get()
    #goods_test.get_detail(421)
    goods_test.category_list()
