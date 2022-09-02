import time

import grpc
from user_srv.proto import user_pb2_grpc, user_pb2


class UserTest:

    def __init__(self):
        channel = grpc.insecure_channel("172.20.0.204:50052")
        self.stub = user_pb2_grpc.UserStub(channel)

    def user_list(self):
        rsp: user_pb2.UserListResponse = self.stub.GetUserList(user_pb2.PageInfo(pn=2, pSize=2))
        print(rsp.total)
        for user in rsp.data:
            print(user.mobile, user.birthDay)

    def get_user_by_id(self, id):
        rsp: user_pb2.UserInfoResponse = self.stub.GetUserById(user_pb2.IdRequest(id=id))
        print(rsp.mobile)

    def get_user_by_mobile(self, mobile):
        rsp: user_pb2.UserInfoResponse = self.stub.GetUserByMobile(user_pb2.MobileRequest(mobile=mobile))
        print(rsp.mobile)

    def create_user(self, nick_name, mobile, password):
        rsp: user_pb2.UserInfoResponse = self.stub.CreateUser(user_pb2.CreateUserInfo(
            nickName=nick_name,
            password=password,
            mobile=mobile
        ))
        print(rsp.id)

    def update_user(self, id, nick_name, birthday, gender):
        self.stub.UpdateUser(user_pb2.UpdateUserInfo(
            id=id,
            nickName=nick_name,
            birthDay=birthday,
            gender=gender
        ))


if __name__ == "__main__":
    user = UserTest()
    user.user_list()
    user.get_user_by_id(2)
    # user.get_user_by_mobile('13501171570')
    # user.create_user("bobby","13621117278", "121212")
    user.update_user(11, "bob", 1661241360, "男")
