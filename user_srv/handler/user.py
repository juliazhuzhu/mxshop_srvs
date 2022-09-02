from datetime import date

import grpc

from user_srv.proto import user_pb2, user_pb2_grpc
from user_srv.model.models import User
import time
from loguru import logger
from peewee import DoesNotExist
from passlib.hash import pbkdf2_sha256
from google.protobuf import empty_pb2

class UserServicer(user_pb2_grpc.UserServicer):

    def convert_user_to_rsp(self, user):
        user_info_rsp = user_pb2.UserInfoResponse()
        user_info_rsp.id = user.id
        user_info_rsp.password = user.password
        user_info_rsp.mobile = user.mobile
        user_info_rsp.role = user.role

        if user.nick_name:
            user_info_rsp.nickName = user.nick_name
        if user.gender:
            user_info_rsp.gender = user.gender
        if user.birthday:
            user_info_rsp.birthDay = int(time.mktime(user.birthday.timetuple()))
        return user_info_rsp

    @logger.catch
    def GetUserList(self, request:user_pb2.PageInfo, context):
        rsp = user_pb2.UserListResponse()
        users = User.select()
        rsp.total = users.count()
        start = 0
        num_per_size = 10
        if request.pSize:
            num_per_size = request.pSize
        if request.pn:
            page = request.pn
            start = num_per_size*(page - 1)

        users  = users.limit(num_per_size).offset(start)

        for user in users:

            rsp.data.append(self.convert_user_to_rsp(user))

        return rsp

    @logger.catch
    def GetUserById(self, request: user_pb2.IdRequest, context):

        try:
            user = User.get(User.id == request.id)
            return self.convert_user_to_rsp(user)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("用户不存在")
            return user_pb2.UserInfoResponse()

    @logger.catch
    def GetUserByMobile(self, request: user_pb2.MobileRequest, context):

        try:
            user = User.get(User.mobile == request.mobile)
            return self.convert_user_to_rsp(user)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("用户不存在")
            return user_pb2.UserInfoResponse()

    @logger.catch
    def CreateUser(self, request: user_pb2.CreateUserInfo, context):

        try:
            user = User.get(User.mobile == request.mobile)
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details("用户已经存在")
            return user_pb2.UserInfoResponse()
        except DoesNotExist as e:
            pass

        user = User()
        user.nick_name = request.nickName
        user.mobile = request.mobile
        user.password = pbkdf2_sha256.hash(request.password)
        user.save()

        return self.convert_user_to_rsp(user)

    @logger.catch
    def UpdateUser(self, request: user_pb2.UpdateUserInfo, context):
        try:
            user = User.get(User.id == request.id)
            user.birthday = date.fromtimestamp(request.birthDay)
            user.gender = request.gender
            user.nick_name = request.nickName
            user.save()
            return empty_pb2.Empty()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("用户不存在")
            return user_pb2.UserInfoResponse()

    @logger.catch
    def CheckPassword(self, request: user_pb2.PasswordCheckInfo, context):
        return user_pb2.CheckResponse(success=pbkdf2_sha256.verify(request.password, request.encryptedPassword))
