# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientTelemetryDescriptionClickthrough.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientTelemetryDescriptionClickthrough.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nAWUProtos/Data/Client/ClientTelemetryDescriptionClickthrough.proto\x12\x14WUProtos.Data.Client\"P\n&ClientTelemetryDescriptionClickthrough\x12\x12\n\noutpost_id\x18\x01 \x01(\t\x12\x12\n\npartner_id\x18\x02 \x01(\tb\x06proto3')
)




_CLIENTTELEMETRYDESCRIPTIONCLICKTHROUGH = _descriptor.Descriptor(
  name='ClientTelemetryDescriptionClickthrough',
  full_name='WUProtos.Data.Client.ClientTelemetryDescriptionClickthrough',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outpost_id', full_name='WUProtos.Data.Client.ClientTelemetryDescriptionClickthrough.outpost_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner_id', full_name='WUProtos.Data.Client.ClientTelemetryDescriptionClickthrough.partner_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=91,
  serialized_end=171,
)

DESCRIPTOR.message_types_by_name['ClientTelemetryDescriptionClickthrough'] = _CLIENTTELEMETRYDESCRIPTIONCLICKTHROUGH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientTelemetryDescriptionClickthrough = _reflection.GeneratedProtocolMessageType('ClientTelemetryDescriptionClickthrough', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTTELEMETRYDESCRIPTIONCLICKTHROUGH,
  __module__ = 'WUProtos.Data.Client.ClientTelemetryDescriptionClickthrough_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientTelemetryDescriptionClickthrough)
  ))
_sym_db.RegisterMessage(ClientTelemetryDescriptionClickthrough)


# @@protoc_insertion_point(module_scope)
