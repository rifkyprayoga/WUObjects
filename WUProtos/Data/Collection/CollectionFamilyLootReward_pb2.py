# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Collection/CollectionFamilyLootReward.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Collection/CollectionFamilyLootReward.proto',
  package='WUProtos.Data.Collection',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n9WUProtos/Data/Collection/CollectionFamilyLootReward.proto\x12\x18WUProtos.Data.Collection\"?\n\x1a\x43ollectionFamilyLootReward\x12\x11\n\tfamily_id\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\x62\x06proto3')
)




_COLLECTIONFAMILYLOOTREWARD = _descriptor.Descriptor(
  name='CollectionFamilyLootReward',
  full_name='WUProtos.Data.Collection.CollectionFamilyLootReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='family_id', full_name='WUProtos.Data.Collection.CollectionFamilyLootReward.family_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='WUProtos.Data.Collection.CollectionFamilyLootReward.amount', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=87,
  serialized_end=150,
)

DESCRIPTOR.message_types_by_name['CollectionFamilyLootReward'] = _COLLECTIONFAMILYLOOTREWARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectionFamilyLootReward = _reflection.GeneratedProtocolMessageType('CollectionFamilyLootReward', (_message.Message,), dict(
  DESCRIPTOR = _COLLECTIONFAMILYLOOTREWARD,
  __module__ = 'WUProtos.Data.Collection.CollectionFamilyLootReward_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Collection.CollectionFamilyLootReward)
  ))
_sym_db.RegisterMessage(CollectionFamilyLootReward)


# @@protoc_insertion_point(module_scope)
