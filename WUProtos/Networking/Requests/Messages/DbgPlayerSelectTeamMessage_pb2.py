# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Requests/Messages/DbgPlayerSelectTeamMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Requests/Messages/DbgPlayerSelectTeamMessage.proto',
  package='WUProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nFWUProtos/Networking/Requests/Messages/DbgPlayerSelectTeamMessage.proto\x12%WUProtos.Networking.Requests.Messages\"-\n\x1a\x44\x62gPlayerSelectTeamMessage\x12\x0f\n\x07team_id\x18\x01 \x01(\tb\x06proto3')
)




_DBGPLAYERSELECTTEAMMESSAGE = _descriptor.Descriptor(
  name='DbgPlayerSelectTeamMessage',
  full_name='WUProtos.Networking.Requests.Messages.DbgPlayerSelectTeamMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='team_id', full_name='WUProtos.Networking.Requests.Messages.DbgPlayerSelectTeamMessage.team_id', index=0,
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
  serialized_start=113,
  serialized_end=158,
)

DESCRIPTOR.message_types_by_name['DbgPlayerSelectTeamMessage'] = _DBGPLAYERSELECTTEAMMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DbgPlayerSelectTeamMessage = _reflection.GeneratedProtocolMessageType('DbgPlayerSelectTeamMessage', (_message.Message,), dict(
  DESCRIPTOR = _DBGPLAYERSELECTTEAMMESSAGE,
  __module__ = 'WUProtos.Networking.Requests.Messages.DbgPlayerSelectTeamMessage_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Requests.Messages.DbgPlayerSelectTeamMessage)
  ))
_sym_db.RegisterMessage(DbgPlayerSelectTeamMessage)


# @@protoc_insertion_point(module_scope)
