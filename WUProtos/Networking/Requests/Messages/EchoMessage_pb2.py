# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Requests/Messages/EchoMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Requests/Messages/EchoMessage.proto',
  package='WUProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n7WUProtos/Networking/Requests/Messages/EchoMessage.proto\x12%WUProtos.Networking.Requests.Messages\"\r\n\x0b\x45\x63hoMessageb\x06proto3')
)




_ECHOMESSAGE = _descriptor.Descriptor(
  name='EchoMessage',
  full_name='WUProtos.Networking.Requests.Messages.EchoMessage',
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
  serialized_start=98,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['EchoMessage'] = _ECHOMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EchoMessage = _reflection.GeneratedProtocolMessageType('EchoMessage', (_message.Message,), dict(
  DESCRIPTOR = _ECHOMESSAGE,
  __module__ = 'WUProtos.Networking.Requests.Messages.EchoMessage_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Requests.Messages.EchoMessage)
  ))
_sym_db.RegisterMessage(EchoMessage)


# @@protoc_insertion_point(module_scope)
