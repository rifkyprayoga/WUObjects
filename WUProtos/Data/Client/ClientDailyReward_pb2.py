# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientDailyReward.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientDailyReward.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,WUProtos/Data/Client/ClientDailyReward.proto\x12\x14WUProtos.Data.Client\"@\n\x11\x43lientDailyReward\x12\x15\n\rhide_as_crate\x18\x01 \x01(\x08\x12\x14\n\x0cmake_sparkly\x18\x02 \x01(\x08\x62\x06proto3')
)




_CLIENTDAILYREWARD = _descriptor.Descriptor(
  name='ClientDailyReward',
  full_name='WUProtos.Data.Client.ClientDailyReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hide_as_crate', full_name='WUProtos.Data.Client.ClientDailyReward.hide_as_crate', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='make_sparkly', full_name='WUProtos.Data.Client.ClientDailyReward.make_sparkly', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=70,
  serialized_end=134,
)

DESCRIPTOR.message_types_by_name['ClientDailyReward'] = _CLIENTDAILYREWARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientDailyReward = _reflection.GeneratedProtocolMessageType('ClientDailyReward', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTDAILYREWARD,
  __module__ = 'WUProtos.Data.Client.ClientDailyReward_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientDailyReward)
  ))
_sym_db.RegisterMessage(ClientDailyReward)


# @@protoc_insertion_point(module_scope)
