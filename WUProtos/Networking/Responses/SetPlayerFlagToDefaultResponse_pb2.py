# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Responses/SetPlayerFlagToDefaultResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Responses/SetPlayerFlagToDefaultResponse.proto',
  package='WUProtos.Networking.Responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nBWUProtos/Networking/Responses/SetPlayerFlagToDefaultResponse.proto\x12\x1dWUProtos.Networking.Responses\"6\n\x1eSetPlayerFlagToDefaultResponse\x12\x14\n\x0c\x64id_set_flag\x18\x01 \x01(\x08\x62\x06proto3')
)




_SETPLAYERFLAGTODEFAULTRESPONSE = _descriptor.Descriptor(
  name='SetPlayerFlagToDefaultResponse',
  full_name='WUProtos.Networking.Responses.SetPlayerFlagToDefaultResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='did_set_flag', full_name='WUProtos.Networking.Responses.SetPlayerFlagToDefaultResponse.did_set_flag', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=101,
  serialized_end=155,
)

DESCRIPTOR.message_types_by_name['SetPlayerFlagToDefaultResponse'] = _SETPLAYERFLAGTODEFAULTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetPlayerFlagToDefaultResponse = _reflection.GeneratedProtocolMessageType('SetPlayerFlagToDefaultResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETPLAYERFLAGTODEFAULTRESPONSE,
  __module__ = 'WUProtos.Networking.Responses.SetPlayerFlagToDefaultResponse_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Responses.SetPlayerFlagToDefaultResponse)
  ))
_sym_db.RegisterMessage(SetPlayerFlagToDefaultResponse)


# @@protoc_insertion_point(module_scope)
