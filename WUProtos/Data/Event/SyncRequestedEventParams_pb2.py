# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Event/SyncRequestedEventParams.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Event/SyncRequestedEventParams.proto',
  package='WUProtos.Data.Event',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n2WUProtos/Data/Event/SyncRequestedEventParams.proto\x12\x13WUProtos.Data.Event\"\x1a\n\x18SyncRequestedEventParamsb\x06proto3')
)




_SYNCREQUESTEDEVENTPARAMS = _descriptor.Descriptor(
  name='SyncRequestedEventParams',
  full_name='WUProtos.Data.Event.SyncRequestedEventParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=75,
  serialized_end=101,
)

DESCRIPTOR.message_types_by_name['SyncRequestedEventParams'] = _SYNCREQUESTEDEVENTPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SyncRequestedEventParams = _reflection.GeneratedProtocolMessageType('SyncRequestedEventParams', (_message.Message,), dict(
  DESCRIPTOR = _SYNCREQUESTEDEVENTPARAMS,
  __module__ = 'WUProtos.Data.Event.SyncRequestedEventParams_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Event.SyncRequestedEventParams)
  ))
_sym_db.RegisterMessage(SyncRequestedEventParams)


# @@protoc_insertion_point(module_scope)
