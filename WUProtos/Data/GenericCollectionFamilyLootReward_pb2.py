# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/GenericCollectionFamilyLootReward.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/GenericCollectionFamilyLootReward.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n5WUProtos/Data/GenericCollectionFamilyLootReward.proto\x12\rWUProtos.Data\"3\n!GenericCollectionFamilyLootReward\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x05\x62\x06proto3')
)




_GENERICCOLLECTIONFAMILYLOOTREWARD = _descriptor.Descriptor(
  name='GenericCollectionFamilyLootReward',
  full_name='WUProtos.Data.GenericCollectionFamilyLootReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='WUProtos.Data.GenericCollectionFamilyLootReward.amount', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=72,
  serialized_end=123,
)

DESCRIPTOR.message_types_by_name['GenericCollectionFamilyLootReward'] = _GENERICCOLLECTIONFAMILYLOOTREWARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenericCollectionFamilyLootReward = _reflection.GeneratedProtocolMessageType('GenericCollectionFamilyLootReward', (_message.Message,), dict(
  DESCRIPTOR = _GENERICCOLLECTIONFAMILYLOOTREWARD,
  __module__ = 'WUProtos.Data.GenericCollectionFamilyLootReward_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.GenericCollectionFamilyLootReward)
  ))
_sym_db.RegisterMessage(GenericCollectionFamilyLootReward)


# @@protoc_insertion_point(module_scope)
