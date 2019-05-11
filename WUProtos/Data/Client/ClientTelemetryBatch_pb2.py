# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientTelemetryBatch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Client import ClientTelemetryRecord_pb2 as WUProtos_dot_Data_dot_Client_dot_ClientTelemetryRecord__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientTelemetryBatch.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n/WUProtos/Data/Client/ClientTelemetryBatch.proto\x12\x14WUProtos.Data.Client\x1a\x30WUProtos/Data/Client/ClientTelemetryRecord.proto\"\xcc\x02\n\x14\x43lientTelemetryBatch\x12W\n\x12telemetry_scope_id\x18\x01 \x01(\x0e\x32;.WUProtos.Data.Client.ClientTelemetryBatch.TelemetryScopeId\x12;\n\x06\x65vents\x18\x02 \x03(\x0b\x32+.WUProtos.Data.Client.ClientTelemetryRecord\x12<\n\x07metrics\x18\x03 \x03(\x0b\x32+.WUProtos.Data.Client.ClientTelemetryRecord\x12\x13\n\x0b\x61pi_version\x18\x04 \x01(\t\x12\x17\n\x0fmessage_version\x18\x05 \x01(\t\"2\n\x10TelemetryScopeId\x12\t\n\x05UNSET\x10\x00\x12\t\n\x05\x44ITTO\x10\x01\x12\x08\n\x04GAME\x10\x02\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Client_dot_ClientTelemetryRecord__pb2.DESCRIPTOR,])



_CLIENTTELEMETRYBATCH_TELEMETRYSCOPEID = _descriptor.EnumDescriptor(
  name='TelemetryScopeId',
  full_name='WUProtos.Data.Client.ClientTelemetryBatch.TelemetryScopeId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DITTO', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=406,
  serialized_end=456,
)
_sym_db.RegisterEnumDescriptor(_CLIENTTELEMETRYBATCH_TELEMETRYSCOPEID)


_CLIENTTELEMETRYBATCH = _descriptor.Descriptor(
  name='ClientTelemetryBatch',
  full_name='WUProtos.Data.Client.ClientTelemetryBatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='telemetry_scope_id', full_name='WUProtos.Data.Client.ClientTelemetryBatch.telemetry_scope_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='WUProtos.Data.Client.ClientTelemetryBatch.events', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='WUProtos.Data.Client.ClientTelemetryBatch.metrics', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_version', full_name='WUProtos.Data.Client.ClientTelemetryBatch.api_version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_version', full_name='WUProtos.Data.Client.ClientTelemetryBatch.message_version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLIENTTELEMETRYBATCH_TELEMETRYSCOPEID,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=456,
)

_CLIENTTELEMETRYBATCH.fields_by_name['telemetry_scope_id'].enum_type = _CLIENTTELEMETRYBATCH_TELEMETRYSCOPEID
_CLIENTTELEMETRYBATCH.fields_by_name['events'].message_type = WUProtos_dot_Data_dot_Client_dot_ClientTelemetryRecord__pb2._CLIENTTELEMETRYRECORD
_CLIENTTELEMETRYBATCH.fields_by_name['metrics'].message_type = WUProtos_dot_Data_dot_Client_dot_ClientTelemetryRecord__pb2._CLIENTTELEMETRYRECORD
_CLIENTTELEMETRYBATCH_TELEMETRYSCOPEID.containing_type = _CLIENTTELEMETRYBATCH
DESCRIPTOR.message_types_by_name['ClientTelemetryBatch'] = _CLIENTTELEMETRYBATCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientTelemetryBatch = _reflection.GeneratedProtocolMessageType('ClientTelemetryBatch', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTTELEMETRYBATCH,
  __module__ = 'WUProtos.Data.Client.ClientTelemetryBatch_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientTelemetryBatch)
  ))
_sym_db.RegisterMessage(ClientTelemetryBatch)


# @@protoc_insertion_point(module_scope)