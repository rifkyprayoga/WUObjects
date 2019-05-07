# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientTelemetryProfileButtonLens.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Enums import CategoryLens_pb2 as WUProtos_dot_Enums_dot_CategoryLens__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientTelemetryProfileButtonLens.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n;WUProtos/Data/Client/ClientTelemetryProfileButtonLens.proto\x12\x14WUProtos.Data.Client\x1a!WUProtos/Enums/CategoryLens.proto\"r\n ClientTelemetryProfileButtonLens\x12\x19\n\x11pressed_button_id\x18\x01 \x01(\t\x12\x33\n\rlens_category\x18\x02 \x01(\x0e\x32\x1c.WUProtos.Enums.CategoryLensb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Enums_dot_CategoryLens__pb2.DESCRIPTOR,])




_CLIENTTELEMETRYPROFILEBUTTONLENS = _descriptor.Descriptor(
  name='ClientTelemetryProfileButtonLens',
  full_name='WUProtos.Data.Client.ClientTelemetryProfileButtonLens',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pressed_button_id', full_name='WUProtos.Data.Client.ClientTelemetryProfileButtonLens.pressed_button_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lens_category', full_name='WUProtos.Data.Client.ClientTelemetryProfileButtonLens.lens_category', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=120,
  serialized_end=234,
)

_CLIENTTELEMETRYPROFILEBUTTONLENS.fields_by_name['lens_category'].enum_type = WUProtos_dot_Enums_dot_CategoryLens__pb2._CATEGORYLENS
DESCRIPTOR.message_types_by_name['ClientTelemetryProfileButtonLens'] = _CLIENTTELEMETRYPROFILEBUTTONLENS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientTelemetryProfileButtonLens = _reflection.GeneratedProtocolMessageType('ClientTelemetryProfileButtonLens', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTTELEMETRYPROFILEBUTTONLENS,
  __module__ = 'WUProtos.Data.Client.ClientTelemetryProfileButtonLens_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientTelemetryProfileButtonLens)
  ))
_sym_db.RegisterMessage(ClientTelemetryProfileButtonLens)


# @@protoc_insertion_point(module_scope)
