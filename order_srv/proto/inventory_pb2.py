# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finventory.proto\x1a\x1bgoogle/protobuf/empty.proto\",\n\x0cGoodsInvInfo\x12\x0f\n\x07goodsId\x18\x01 \x01(\x05\x12\x0b\n\x03num\x18\x02 \x01(\x05\",\n\x08SellInfo\x12 \n\tgoodsInfo\x18\x01 \x03(\x0b\x32\r.GoodsInvInfo2\xbf\x01\n\tInventory\x12/\n\x06SetInv\x12\r.GoodsInvInfo\x1a\x16.google.protobuf.Empty\x12)\n\tInvDetail\x12\r.GoodsInvInfo\x1a\r.GoodsInvInfo\x12)\n\x04Sell\x12\t.SellInfo\x1a\x16.google.protobuf.Empty\x12+\n\x06Reback\x12\t.SellInfo\x1a\x16.google.protobuf.EmptyB\nZ\x08../protob\x06proto3')



_GOODSINVINFO = DESCRIPTOR.message_types_by_name['GoodsInvInfo']
_SELLINFO = DESCRIPTOR.message_types_by_name['SellInfo']
GoodsInvInfo = _reflection.GeneratedProtocolMessageType('GoodsInvInfo', (_message.Message,), {
  'DESCRIPTOR' : _GOODSINVINFO,
  '__module__' : 'inventory_pb2'
  # @@protoc_insertion_point(class_scope:GoodsInvInfo)
  })
_sym_db.RegisterMessage(GoodsInvInfo)

SellInfo = _reflection.GeneratedProtocolMessageType('SellInfo', (_message.Message,), {
  'DESCRIPTOR' : _SELLINFO,
  '__module__' : 'inventory_pb2'
  # @@protoc_insertion_point(class_scope:SellInfo)
  })
_sym_db.RegisterMessage(SellInfo)

_INVENTORY = DESCRIPTOR.services_by_name['Inventory']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\010../proto'
  _GOODSINVINFO._serialized_start=48
  _GOODSINVINFO._serialized_end=92
  _SELLINFO._serialized_start=94
  _SELLINFO._serialized_end=138
  _INVENTORY._serialized_start=141
  _INVENTORY._serialized_end=332
# @@protoc_insertion_point(module_scope)
