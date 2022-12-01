# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import order_pb2 as order__pb2


class OrderStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CartItemList = channel.unary_unary(
                '/proto.Order/CartItemList',
                request_serializer=order__pb2.UserInfo.SerializeToString,
                response_deserializer=order__pb2.CartItemListResponse.FromString,
                )
        self.CreateCartItem = channel.unary_unary(
                '/proto.Order/CreateCartItem',
                request_serializer=order__pb2.CartItemRequest.SerializeToString,
                response_deserializer=order__pb2.ShopCartInfoResponse.FromString,
                )
        self.UpdateCartItem = channel.unary_unary(
                '/proto.Order/UpdateCartItem',
                request_serializer=order__pb2.CartItemRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DeleteCardItem = channel.unary_unary(
                '/proto.Order/DeleteCardItem',
                request_serializer=order__pb2.CartItemRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.CreateOrder = channel.unary_unary(
                '/proto.Order/CreateOrder',
                request_serializer=order__pb2.OrderRequest.SerializeToString,
                response_deserializer=order__pb2.OrderInfoResponse.FromString,
                )
        self.OrderList = channel.unary_unary(
                '/proto.Order/OrderList',
                request_serializer=order__pb2.OrderFilterRequest.SerializeToString,
                response_deserializer=order__pb2.OrderListResponse.FromString,
                )
        self.OrderDetail = channel.unary_unary(
                '/proto.Order/OrderDetail',
                request_serializer=order__pb2.OrderRequest.SerializeToString,
                response_deserializer=order__pb2.OrderInfoDetailResponse.FromString,
                )
        self.UpdateOrderStatus = channel.unary_unary(
                '/proto.Order/UpdateOrderStatus',
                request_serializer=order__pb2.OrderStatus.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class OrderServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CartItemList(self, request, context):
        """购物车
        <获取用户购物车信息>
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCartItem(self, request, context):
        """<添加商品到购物车>
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCartItem(self, request, context):
        """修改购物车条目信息
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCardItem(self, request, context):
        """删除购物车条目
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateOrder(self, request, context):
        """订单
        新建订单
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OrderList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OrderDetail(self, request, context):
        """<订单详情>
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateOrderStatus(self, request, context):
        """修改订单的支付状态
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CartItemList': grpc.unary_unary_rpc_method_handler(
                    servicer.CartItemList,
                    request_deserializer=order__pb2.UserInfo.FromString,
                    response_serializer=order__pb2.CartItemListResponse.SerializeToString,
            ),
            'CreateCartItem': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCartItem,
                    request_deserializer=order__pb2.CartItemRequest.FromString,
                    response_serializer=order__pb2.ShopCartInfoResponse.SerializeToString,
            ),
            'UpdateCartItem': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCartItem,
                    request_deserializer=order__pb2.CartItemRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DeleteCardItem': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCardItem,
                    request_deserializer=order__pb2.CartItemRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'CreateOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOrder,
                    request_deserializer=order__pb2.OrderRequest.FromString,
                    response_serializer=order__pb2.OrderInfoResponse.SerializeToString,
            ),
            'OrderList': grpc.unary_unary_rpc_method_handler(
                    servicer.OrderList,
                    request_deserializer=order__pb2.OrderFilterRequest.FromString,
                    response_serializer=order__pb2.OrderListResponse.SerializeToString,
            ),
            'OrderDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.OrderDetail,
                    request_deserializer=order__pb2.OrderRequest.FromString,
                    response_serializer=order__pb2.OrderInfoDetailResponse.SerializeToString,
            ),
            'UpdateOrderStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateOrderStatus,
                    request_deserializer=order__pb2.OrderStatus.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.Order', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Order(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CartItemList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Order/CartItemList',
            order__pb2.UserInfo.SerializeToString,
            order__pb2.CartItemListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCartItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Order/CreateCartItem',
            order__pb2.CartItemRequest.SerializeToString,
            order__pb2.ShopCartInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCartItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Order/UpdateCartItem',
            order__pb2.CartItemRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCardItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Order/DeleteCardItem',
            order__pb2.CartItemRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Order/CreateOrder',
            order__pb2.OrderRequest.SerializeToString,
            order__pb2.OrderInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OrderList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Order/OrderList',
            order__pb2.OrderFilterRequest.SerializeToString,
            order__pb2.OrderListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OrderDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Order/OrderDetail',
            order__pb2.OrderRequest.SerializeToString,
            order__pb2.OrderInfoDetailResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateOrderStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Order/UpdateOrderStatus',
            order__pb2.OrderStatus.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
