# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/GenericRunestoneReward.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/GenericRunestoneReward.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n*WUProtos/Data/GenericRunestoneReward.proto\x12\rWUProtos.Data\"6\n\x16GenericRunestoneReward\x12\x0c\n\x04rank\x18\x01 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x62\x06proto3')
)




_GENERICRUNESTONEREWARD = _descriptor.Descriptor(
  name='GenericRunestoneReward',
  full_name='WUProtos.Data.GenericRunestoneReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rank', full_name='WUProtos.Data.GenericRunestoneReward.rank', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='WUProtos.Data.GenericRunestoneReward.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=61,
  serialized_end=115,
)

DESCRIPTOR.message_types_by_name['GenericRunestoneReward'] = _GENERICRUNESTONEREWARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenericRunestoneReward = _reflection.GeneratedProtocolMessageType('GenericRunestoneReward', (_message.Message,), dict(
  DESCRIPTOR = _GENERICRUNESTONEREWARD,
  __module__ = 'WUProtos.Data.GenericRunestoneReward_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.GenericRunestoneReward)
  ))
_sym_db.RegisterMessage(GenericRunestoneReward)


# @@protoc_insertion_point(module_scope)