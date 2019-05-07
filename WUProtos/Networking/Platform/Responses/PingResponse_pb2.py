# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Platform/Responses/PingResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Platform/Responses/PingResponse.proto',
  package='WUProtos.Networking.Platform.Responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n9WUProtos/Networking/Platform/Responses/PingResponse.proto\x12&WUProtos.Networking.Platform.Responses\"U\n\x0cPingResponse\x12\x11\n\tuser_info\x18\x01 \x01(\t\x12\x13\n\x0bserver_info\x18\x02 \x01(\t\x12\x1d\n\x15random_response_bytes\x18\x03 \x01(\tb\x06proto3')
)




_PINGRESPONSE = _descriptor.Descriptor(
  name='PingResponse',
  full_name='WUProtos.Networking.Platform.Responses.PingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_info', full_name='WUProtos.Networking.Platform.Responses.PingResponse.user_info', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_info', full_name='WUProtos.Networking.Platform.Responses.PingResponse.server_info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='random_response_bytes', full_name='WUProtos.Networking.Platform.Responses.PingResponse.random_response_bytes', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_end=186,
)

DESCRIPTOR.message_types_by_name['PingResponse'] = _PINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PingResponse = _reflection.GeneratedProtocolMessageType('PingResponse', (_message.Message,), dict(
  DESCRIPTOR = _PINGRESPONSE,
  __module__ = 'WUProtos.Networking.Platform.Responses.PingResponse_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Platform.Responses.PingResponse)
  ))
_sym_db.RegisterMessage(PingResponse)


# @@protoc_insertion_point(module_scope)
