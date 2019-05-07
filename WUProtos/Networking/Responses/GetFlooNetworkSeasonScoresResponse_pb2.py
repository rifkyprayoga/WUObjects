# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Responses/GetFlooNetworkSeasonScoresResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import FlooNetworkSeasonScores_pb2 as WUProtos_dot_Data_dot_FlooNetworkSeasonScores__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Responses/GetFlooNetworkSeasonScoresResponse.proto',
  package='WUProtos.Networking.Responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nFWUProtos/Networking/Responses/GetFlooNetworkSeasonScoresResponse.proto\x12\x1dWUProtos.Networking.Responses\x1a+WUProtos/Data/FlooNetworkSeasonScores.proto\"o\n\"GetFlooNetworkSeasonScoresResponse\x12\x11\n\tseason_id\x18\x01 \x01(\t\x12\x36\n\x06scores\x18\x02 \x01(\x0b\x32&.WUProtos.Data.FlooNetworkSeasonScoresb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_FlooNetworkSeasonScores__pb2.DESCRIPTOR,])




_GETFLOONETWORKSEASONSCORESRESPONSE = _descriptor.Descriptor(
  name='GetFlooNetworkSeasonScoresResponse',
  full_name='WUProtos.Networking.Responses.GetFlooNetworkSeasonScoresResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='season_id', full_name='WUProtos.Networking.Responses.GetFlooNetworkSeasonScoresResponse.season_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scores', full_name='WUProtos.Networking.Responses.GetFlooNetworkSeasonScoresResponse.scores', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=150,
  serialized_end=261,
)

_GETFLOONETWORKSEASONSCORESRESPONSE.fields_by_name['scores'].message_type = WUProtos_dot_Data_dot_FlooNetworkSeasonScores__pb2._FLOONETWORKSEASONSCORES
DESCRIPTOR.message_types_by_name['GetFlooNetworkSeasonScoresResponse'] = _GETFLOONETWORKSEASONSCORESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFlooNetworkSeasonScoresResponse = _reflection.GeneratedProtocolMessageType('GetFlooNetworkSeasonScoresResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETFLOONETWORKSEASONSCORESRESPONSE,
  __module__ = 'WUProtos.Networking.Responses.GetFlooNetworkSeasonScoresResponse_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Responses.GetFlooNetworkSeasonScoresResponse)
  ))
_sym_db.RegisterMessage(GetFlooNetworkSeasonScoresResponse)


# @@protoc_insertion_point(module_scope)
