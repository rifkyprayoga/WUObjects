# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Responses/EchoResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Responses/EchoResponse.proto',
  package='WUProtos.Networking.Responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n0WUProtos/Networking/Responses/EchoResponse.proto\x12\x1dWUProtos.Networking.Responses\" \n\x0c\x45\x63hoResponse\x12\x10\n\x08response\x18\x01 \x01(\tb\x06proto3')
)




_ECHORESPONSE = _descriptor.Descriptor(
  name='EchoResponse',
  full_name='WUProtos.Networking.Responses.EchoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='WUProtos.Networking.Responses.EchoResponse.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=83,
  serialized_end=115,
)

DESCRIPTOR.message_types_by_name['EchoResponse'] = _ECHORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EchoResponse = _reflection.GeneratedProtocolMessageType('EchoResponse', (_message.Message,), dict(
  DESCRIPTOR = _ECHORESPONSE,
  __module__ = 'WUProtos.Networking.Responses.EchoResponse_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Responses.EchoResponse)
  ))
_sym_db.RegisterMessage(EchoResponse)


# @@protoc_insertion_point(module_scope)
