# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Requests/Messages/LeaveChamberMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Requests/Messages/LeaveChamberMessage.proto',
  package='WUProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n?WUProtos/Networking/Requests/Messages/LeaveChamberMessage.proto\x12%WUProtos.Networking.Requests.Messages\"\x15\n\x13LeaveChamberMessageb\x06proto3')
)




_LEAVECHAMBERMESSAGE = _descriptor.Descriptor(
  name='LeaveChamberMessage',
  full_name='WUProtos.Networking.Requests.Messages.LeaveChamberMessage',
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
  serialized_start=106,
  serialized_end=127,
)

DESCRIPTOR.message_types_by_name['LeaveChamberMessage'] = _LEAVECHAMBERMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LeaveChamberMessage = _reflection.GeneratedProtocolMessageType('LeaveChamberMessage', (_message.Message,), dict(
  DESCRIPTOR = _LEAVECHAMBERMESSAGE,
  __module__ = 'WUProtos.Networking.Requests.Messages.LeaveChamberMessage_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Requests.Messages.LeaveChamberMessage)
  ))
_sym_db.RegisterMessage(LeaveChamberMessage)


# @@protoc_insertion_point(module_scope)
