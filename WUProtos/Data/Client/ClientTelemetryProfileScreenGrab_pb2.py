# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientTelemetryProfileScreenGrab.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Enums import CategoryShareLocation_pb2 as WUProtos_dot_Enums_dot_CategoryShareLocation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientTelemetryProfileScreenGrab.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n;WUProtos/Data/Client/ClientTelemetryProfileScreenGrab.proto\x12\x14WUProtos.Data.Client\x1a*WUProtos/Enums/CategoryShareLocation.proto\"f\n ClientTelemetryProfileScreenGrab\x12\x42\n\x13screengrab_location\x18\x01 \x01(\x0e\x32%.WUProtos.Enums.CategoryShareLocationb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Enums_dot_CategoryShareLocation__pb2.DESCRIPTOR,])




_CLIENTTELEMETRYPROFILESCREENGRAB = _descriptor.Descriptor(
  name='ClientTelemetryProfileScreenGrab',
  full_name='WUProtos.Data.Client.ClientTelemetryProfileScreenGrab',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='screengrab_location', full_name='WUProtos.Data.Client.ClientTelemetryProfileScreenGrab.screengrab_location', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=129,
  serialized_end=231,
)

_CLIENTTELEMETRYPROFILESCREENGRAB.fields_by_name['screengrab_location'].enum_type = WUProtos_dot_Enums_dot_CategoryShareLocation__pb2._CATEGORYSHARELOCATION
DESCRIPTOR.message_types_by_name['ClientTelemetryProfileScreenGrab'] = _CLIENTTELEMETRYPROFILESCREENGRAB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientTelemetryProfileScreenGrab = _reflection.GeneratedProtocolMessageType('ClientTelemetryProfileScreenGrab', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTTELEMETRYPROFILESCREENGRAB,
  __module__ = 'WUProtos.Data.Client.ClientTelemetryProfileScreenGrab_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientTelemetryProfileScreenGrab)
  ))
_sym_db.RegisterMessage(ClientTelemetryProfileScreenGrab)


# @@protoc_insertion_point(module_scope)