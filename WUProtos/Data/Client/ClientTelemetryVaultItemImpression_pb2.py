# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientTelemetryVaultItemImpression.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientTelemetryVaultItemImpression.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n=WUProtos/Data/Client/ClientTelemetryVaultItemImpression.proto\x12\x14WUProtos.Data.Client\";\n\"ClientTelemetryVaultItemImpression\x12\x15\n\rvault_item_id\x18\x01 \x01(\tb\x06proto3')
)




_CLIENTTELEMETRYVAULTITEMIMPRESSION = _descriptor.Descriptor(
  name='ClientTelemetryVaultItemImpression',
  full_name='WUProtos.Data.Client.ClientTelemetryVaultItemImpression',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vault_item_id', full_name='WUProtos.Data.Client.ClientTelemetryVaultItemImpression.vault_item_id', index=0,
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
  serialized_start=87,
  serialized_end=146,
)

DESCRIPTOR.message_types_by_name['ClientTelemetryVaultItemImpression'] = _CLIENTTELEMETRYVAULTITEMIMPRESSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientTelemetryVaultItemImpression = _reflection.GeneratedProtocolMessageType('ClientTelemetryVaultItemImpression', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTTELEMETRYVAULTITEMIMPRESSION,
  __module__ = 'WUProtos.Data.Client.ClientTelemetryVaultItemImpression_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientTelemetryVaultItemImpression)
  ))
_sym_db.RegisterMessage(ClientTelemetryVaultItemImpression)


# @@protoc_insertion_point(module_scope)
