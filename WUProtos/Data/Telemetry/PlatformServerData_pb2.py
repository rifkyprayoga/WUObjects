# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Telemetry/PlatformServerData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Telemetry/PlatformServerData.proto',
  package='WUProtos.Data.Telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n0WUProtos/Data/Telemetry/PlatformServerData.proto\x12\x17WUProtos.Data.Telemetry\"g\n\x12PlatformServerData\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x14\n\x0ctelemetry_id\x18\x02 \x01(\t\x12\x12\n\nsession_id\x18\x03 \x01(\t\x12\x16\n\x0e\x65xperiment_ids\x18\x04 \x03(\x05\x62\x06proto3')
)




_PLATFORMSERVERDATA = _descriptor.Descriptor(
  name='PlatformServerData',
  full_name='WUProtos.Data.Telemetry.PlatformServerData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='WUProtos.Data.Telemetry.PlatformServerData.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='telemetry_id', full_name='WUProtos.Data.Telemetry.PlatformServerData.telemetry_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='WUProtos.Data.Telemetry.PlatformServerData.session_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experiment_ids', full_name='WUProtos.Data.Telemetry.PlatformServerData.experiment_ids', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=77,
  serialized_end=180,
)

DESCRIPTOR.message_types_by_name['PlatformServerData'] = _PLATFORMSERVERDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlatformServerData = _reflection.GeneratedProtocolMessageType('PlatformServerData', (_message.Message,), dict(
  DESCRIPTOR = _PLATFORMSERVERDATA,
  __module__ = 'WUProtos.Data.Telemetry.PlatformServerData_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Telemetry.PlatformServerData)
  ))
_sym_db.RegisterMessage(PlatformServerData)


# @@protoc_insertion_point(module_scope)