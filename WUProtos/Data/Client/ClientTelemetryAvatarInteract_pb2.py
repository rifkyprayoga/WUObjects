# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientTelemetryAvatarInteract.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientTelemetryAvatarInteract.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n8WUProtos/Data/Client/ClientTelemetryAvatarInteract.proto\x12\x14WUProtos.Data.Client\"5\n\x1d\x43lientTelemetryAvatarInteract\x12\x14\n\x0cplayer_level\x18\x01 \x01(\x03\x62\x06proto3')
)




_CLIENTTELEMETRYAVATARINTERACT = _descriptor.Descriptor(
  name='ClientTelemetryAvatarInteract',
  full_name='WUProtos.Data.Client.ClientTelemetryAvatarInteract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_level', full_name='WUProtos.Data.Client.ClientTelemetryAvatarInteract.player_level', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=82,
  serialized_end=135,
)

DESCRIPTOR.message_types_by_name['ClientTelemetryAvatarInteract'] = _CLIENTTELEMETRYAVATARINTERACT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientTelemetryAvatarInteract = _reflection.GeneratedProtocolMessageType('ClientTelemetryAvatarInteract', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTTELEMETRYAVATARINTERACT,
  __module__ = 'WUProtos.Data.Client.ClientTelemetryAvatarInteract_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientTelemetryAvatarInteract)
  ))
_sym_db.RegisterMessage(ClientTelemetryAvatarInteract)


# @@protoc_insertion_point(module_scope)
