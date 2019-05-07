# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/StorePack.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Loot import LootCollection_pb2 as WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2
from WUProtos.Data import SkuData_pb2 as WUProtos_dot_Data_dot_SkuData__pb2
from WUProtos.Data import Requirements_pb2 as WUProtos_dot_Data_dot_Requirements__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/StorePack.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dWUProtos/Data/StorePack.proto\x12\rWUProtos.Data\x1a\'WUProtos/Data/Loot/LootCollection.proto\x1a\x1bWUProtos/Data/SkuData.proto\x1a WUProtos/Data/Requirements.proto\"\xec\x01\n\tStorePack\x12\n\n\x02id\x18\x01 \x01(\t\x12\x34\n\x08\x63ontents\x18\x02 \x01(\x0b\x32\".WUProtos.Data.Loot.LootCollection\x12\x30\n\x04\x63ost\x18\x03 \x01(\x0b\x32\".WUProtos.Data.Loot.LootCollection\x12\x0e\n\x06iap_id\x18\x04 \x01(\t\x12(\n\x08sku_data\x18\x05 \x01(\x0b\x32\x16.WUProtos.Data.SkuData\x12\x31\n\x0crequirements\x18\x06 \x01(\x0b\x32\x1b.WUProtos.Data.Requirementsb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_SkuData__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_Requirements__pb2.DESCRIPTOR,])




_STOREPACK = _descriptor.Descriptor(
  name='StorePack',
  full_name='WUProtos.Data.StorePack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.StorePack.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents', full_name='WUProtos.Data.StorePack.contents', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost', full_name='WUProtos.Data.StorePack.cost', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iap_id', full_name='WUProtos.Data.StorePack.iap_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sku_data', full_name='WUProtos.Data.StorePack.sku_data', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requirements', full_name='WUProtos.Data.StorePack.requirements', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=389,
)

_STOREPACK.fields_by_name['contents'].message_type = WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2._LOOTCOLLECTION
_STOREPACK.fields_by_name['cost'].message_type = WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2._LOOTCOLLECTION
_STOREPACK.fields_by_name['sku_data'].message_type = WUProtos_dot_Data_dot_SkuData__pb2._SKUDATA
_STOREPACK.fields_by_name['requirements'].message_type = WUProtos_dot_Data_dot_Requirements__pb2._REQUIREMENTS
DESCRIPTOR.message_types_by_name['StorePack'] = _STOREPACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StorePack = _reflection.GeneratedProtocolMessageType('StorePack', (_message.Message,), dict(
  DESCRIPTOR = _STOREPACK,
  __module__ = 'WUProtos.Data.StorePack_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.StorePack)
  ))
_sym_db.RegisterMessage(StorePack)


# @@protoc_insertion_point(module_scope)
