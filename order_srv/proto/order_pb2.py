# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: order.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0border.proto\x12\x05proto\x1a\x1bgoogle/protobuf/empty.proto\"\x16\n\x08UserInfo\x12\n\n\x02id\x18\x01 \x01(\x05\"b\n\x14ShopCartInfoResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06userId\x18\x02 \x01(\x05\x12\x0f\n\x07goodsId\x18\x03 \x01(\x05\x12\x0c\n\x04nums\x18\x04 \x01(\x05\x12\x0f\n\x07\x63hecked\x18\x05 \x01(\x08\"P\n\x14\x43\x61rtItemListResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12)\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x1b.proto.ShopCartInfoResponse\"Q\n\x0f\x43\x61rtItemRequest\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x0f\n\x07goodsId\x18\x02 \x01(\x05\x12\x0c\n\x04nums\x18\x03 \x01(\x05\x12\x0f\n\x07\x63hecked\x18\x04 \x01(\x08\"g\n\x0cOrderRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06userId\x18\x02 \x01(\x05\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x0e\n\x06mobile\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0c\n\x04post\x18\x06 \x01(\t\"\xbe\x01\n\x11OrderInfoResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06userId\x18\x02 \x01(\x05\x12\x0f\n\x07orderSn\x18\x03 \x01(\t\x12\x0f\n\x07payType\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x0c\n\x04post\x18\x06 \x01(\t\x12\r\n\x05total\x18\x07 \x01(\x02\x12\x0f\n\x07\x61\x64\x64ress\x18\x08 \x01(\t\x12\x0c\n\x04name\x18\t \x01(\t\x12\x0e\n\x06mobile\x18\n \x01(\t\x12\x0f\n\x07\x61\x64\x64Time\x18\x0b \x01(\t\"G\n\x12OrderFilterRequest\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\r\n\x05pages\x18\x02 \x01(\x05\x12\x12\n\npagePerNum\x18\x03 \x01(\x05\"J\n\x11OrderListResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12&\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x18.proto.OrderInfoResponse\"\x8a\x01\n\x11OrderItemResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07orderId\x18\x02 \x01(\x05\x12\x0f\n\x07goodsId\x18\x03 \x01(\x05\x12\x11\n\tgoodsName\x18\x04 \x01(\t\x12\x12\n\ngoodsImage\x18\x05 \x01(\t\x12\x12\n\ngoodsPrice\x18\x06 \x01(\x02\x12\x0c\n\x04nums\x18\x07 \x01(\x05\"\x80\x01\n\x17OrderInfoDetailResponse\x12+\n\torderInfo\x18\x01 \x01(\x0b\x32\x18.proto.OrderInfoResponse\x12\x10\n\x08item_num\x18\x02 \x01(\x05\x12&\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\x18.proto.OrderItemResponse\".\n\x0bOrderStatus\x12\x0f\n\x07OrderSn\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t2\x95\x04\n\x05Order\x12<\n\x0c\x43\x61rtItemList\x12\x0f.proto.UserInfo\x1a\x1b.proto.CartItemListResponse\x12\x45\n\x0e\x43reateCartItem\x12\x16.proto.CartItemRequest\x1a\x1b.proto.ShopCartInfoResponse\x12@\n\x0eUpdateCartItem\x12\x16.proto.CartItemRequest\x1a\x16.google.protobuf.Empty\x12@\n\x0e\x44\x65leteCardItem\x12\x16.proto.CartItemRequest\x1a\x16.google.protobuf.Empty\x12<\n\x0b\x43reateOrder\x12\x13.proto.OrderRequest\x1a\x18.proto.OrderInfoResponse\x12@\n\tOrderList\x12\x19.proto.OrderFilterRequest\x1a\x18.proto.OrderListResponse\x12\x42\n\x0bOrderDetail\x12\x13.proto.OrderRequest\x1a\x1e.proto.OrderInfoDetailResponse\x12?\n\x11UpdateOrderStatus\x12\x12.proto.OrderStatus\x1a\x16.google.protobuf.EmptyB\tZ\x07.;protob\x06proto3')



_USERINFO = DESCRIPTOR.message_types_by_name['UserInfo']
_SHOPCARTINFORESPONSE = DESCRIPTOR.message_types_by_name['ShopCartInfoResponse']
_CARTITEMLISTRESPONSE = DESCRIPTOR.message_types_by_name['CartItemListResponse']
_CARTITEMREQUEST = DESCRIPTOR.message_types_by_name['CartItemRequest']
_ORDERREQUEST = DESCRIPTOR.message_types_by_name['OrderRequest']
_ORDERINFORESPONSE = DESCRIPTOR.message_types_by_name['OrderInfoResponse']
_ORDERFILTERREQUEST = DESCRIPTOR.message_types_by_name['OrderFilterRequest']
_ORDERLISTRESPONSE = DESCRIPTOR.message_types_by_name['OrderListResponse']
_ORDERITEMRESPONSE = DESCRIPTOR.message_types_by_name['OrderItemResponse']
_ORDERINFODETAILRESPONSE = DESCRIPTOR.message_types_by_name['OrderInfoDetailResponse']
_ORDERSTATUS = DESCRIPTOR.message_types_by_name['OrderStatus']
UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:proto.UserInfo)
  })
_sym_db.RegisterMessage(UserInfo)

ShopCartInfoResponse = _reflection.GeneratedProtocolMessageType('ShopCartInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _SHOPCARTINFORESPONSE,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:proto.ShopCartInfoResponse)
  })
_sym_db.RegisterMessage(ShopCartInfoResponse)

CartItemListResponse = _reflection.GeneratedProtocolMessageType('CartItemListResponse', (_message.Message,), {
  'DESCRIPTOR' : _CARTITEMLISTRESPONSE,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:proto.CartItemListResponse)
  })
_sym_db.RegisterMessage(CartItemListResponse)

CartItemRequest = _reflection.GeneratedProtocolMessageType('CartItemRequest', (_message.Message,), {
  'DESCRIPTOR' : _CARTITEMREQUEST,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:proto.CartItemRequest)
  })
_sym_db.RegisterMessage(CartItemRequest)

OrderRequest = _reflection.GeneratedProtocolMessageType('OrderRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORDERREQUEST,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:proto.OrderRequest)
  })
_sym_db.RegisterMessage(OrderRequest)

OrderInfoResponse = _reflection.GeneratedProtocolMessageType('OrderInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _ORDERINFORESPONSE,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:proto.OrderInfoResponse)
  })
_sym_db.RegisterMessage(OrderInfoResponse)

OrderFilterRequest = _reflection.GeneratedProtocolMessageType('OrderFilterRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORDERFILTERREQUEST,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:proto.OrderFilterRequest)
  })
_sym_db.RegisterMessage(OrderFilterRequest)

OrderListResponse = _reflection.GeneratedProtocolMessageType('OrderListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ORDERLISTRESPONSE,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:proto.OrderListResponse)
  })
_sym_db.RegisterMessage(OrderListResponse)

OrderItemResponse = _reflection.GeneratedProtocolMessageType('OrderItemResponse', (_message.Message,), {
  'DESCRIPTOR' : _ORDERITEMRESPONSE,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:proto.OrderItemResponse)
  })
_sym_db.RegisterMessage(OrderItemResponse)

OrderInfoDetailResponse = _reflection.GeneratedProtocolMessageType('OrderInfoDetailResponse', (_message.Message,), {
  'DESCRIPTOR' : _ORDERINFODETAILRESPONSE,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:proto.OrderInfoDetailResponse)
  })
_sym_db.RegisterMessage(OrderInfoDetailResponse)

OrderStatus = _reflection.GeneratedProtocolMessageType('OrderStatus', (_message.Message,), {
  'DESCRIPTOR' : _ORDERSTATUS,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:proto.OrderStatus)
  })
_sym_db.RegisterMessage(OrderStatus)

_ORDER = DESCRIPTOR.services_by_name['Order']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\007.;proto'
  _USERINFO._serialized_start=51
  _USERINFO._serialized_end=73
  _SHOPCARTINFORESPONSE._serialized_start=75
  _SHOPCARTINFORESPONSE._serialized_end=173
  _CARTITEMLISTRESPONSE._serialized_start=175
  _CARTITEMLISTRESPONSE._serialized_end=255
  _CARTITEMREQUEST._serialized_start=257
  _CARTITEMREQUEST._serialized_end=338
  _ORDERREQUEST._serialized_start=340
  _ORDERREQUEST._serialized_end=443
  _ORDERINFORESPONSE._serialized_start=446
  _ORDERINFORESPONSE._serialized_end=636
  _ORDERFILTERREQUEST._serialized_start=638
  _ORDERFILTERREQUEST._serialized_end=709
  _ORDERLISTRESPONSE._serialized_start=711
  _ORDERLISTRESPONSE._serialized_end=785
  _ORDERITEMRESPONSE._serialized_start=788
  _ORDERITEMRESPONSE._serialized_end=926
  _ORDERINFODETAILRESPONSE._serialized_start=929
  _ORDERINFODETAILRESPONSE._serialized_end=1057
  _ORDERSTATUS._serialized_start=1059
  _ORDERSTATUS._serialized_end=1105
  _ORDER._serialized_start=1108
  _ORDER._serialized_end=1641
# @@protoc_insertion_point(module_scope)
