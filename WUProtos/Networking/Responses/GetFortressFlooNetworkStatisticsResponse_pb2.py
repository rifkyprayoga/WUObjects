# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Responses/GetFortressFlooNetworkStatisticsResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import FlooNetworkFortressStatistics_pb2 as WUProtos_dot_Data_dot_FlooNetworkFortressStatistics__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Responses/GetFortressFlooNetworkStatisticsResponse.proto',
  package='WUProtos.Networking.Responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nLWUProtos/Networking/Responses/GetFortressFlooNetworkStatisticsResponse.proto\x12\x1dWUProtos.Networking.Responses\x1a\x31WUProtos/Data/FlooNetworkFortressStatistics.proto\"\x9d\x01\n(GetFortressFlooNetworkStatisticsResponse\x12I\n\x13\x66ortress_statistics\x18\x01 \x01(\x0b\x32,.WUProtos.Data.FlooNetworkFortressStatistics\x12&\n\x1etemp_next_add_pts_timestamp_ms\x18\x02 \x01(\x03\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_FlooNetworkFortressStatistics__pb2.DESCRIPTOR,])




_GETFORTRESSFLOONETWORKSTATISTICSRESPONSE = _descriptor.Descriptor(
  name='GetFortressFlooNetworkStatisticsResponse',
  full_name='WUProtos.Networking.Responses.GetFortressFlooNetworkStatisticsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fortress_statistics', full_name='WUProtos.Networking.Responses.GetFortressFlooNetworkStatisticsResponse.fortress_statistics', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temp_next_add_pts_timestamp_ms', full_name='WUProtos.Networking.Responses.GetFortressFlooNetworkStatisticsResponse.temp_next_add_pts_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=163,
  serialized_end=320,
)

_GETFORTRESSFLOONETWORKSTATISTICSRESPONSE.fields_by_name['fortress_statistics'].message_type = WUProtos_dot_Data_dot_FlooNetworkFortressStatistics__pb2._FLOONETWORKFORTRESSSTATISTICS
DESCRIPTOR.message_types_by_name['GetFortressFlooNetworkStatisticsResponse'] = _GETFORTRESSFLOONETWORKSTATISTICSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFortressFlooNetworkStatisticsResponse = _reflection.GeneratedProtocolMessageType('GetFortressFlooNetworkStatisticsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETFORTRESSFLOONETWORKSTATISTICSRESPONSE,
  __module__ = 'WUProtos.Networking.Responses.GetFortressFlooNetworkStatisticsResponse_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Responses.GetFortressFlooNetworkStatisticsResponse)
  ))
_sym_db.RegisterMessage(GetFortressFlooNetworkStatisticsResponse)


# @@protoc_insertion_point(module_scope)
