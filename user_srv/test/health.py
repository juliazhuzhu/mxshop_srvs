import grpc
from common.grpc_health.v1 import health_pb2, health_pb2_grpc


class HealthTest:
    def __init__(self):
        channel = grpc.insecure_channel("172.20.0.204:50052")
        self.stub = health_pb2_grpc.HealthStub(channel)

    def check(self):
        rsp: health_pb2.HealthCheckResponse = self.stub.Check(health_pb2.HealthCheckRequest(service="hi"))
        print(rsp.status)


if __name__ == "__main__":
    test = HealthTest()
    test.check()
