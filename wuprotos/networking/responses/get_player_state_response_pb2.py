# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/get_player_state_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wuprotos.data.client import client_map_poi_pb2 as wuprotos_dot_data_dot_client_dot_client__map__poi__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/get_player_state_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n=wuprotos/networking/responses/get_player_state_response.proto\x12\x1dwuprotos.networking.responses\x1a)wuprotos/data/client/client_map_poi.proto\"\xe7\x03\n\x16GetPlayerStateResponse\x12R\n\x06player\x18\x01 \x01(\x0b\x32\x42.wuprotos.networking.responses.GetPlayerStateResponse.ClientPlayer\x1a\xf3\x01\n\x0c\x43lientPlayer\x12\x18\n\x10\x63reation_time_ms\x18\x01 \x01(\x03\x12Y\n\x03map\x18\x02 \x01(\x0b\x32J.wuprotos.networking.responses.GetPlayerStateResponse.ClientPlayerMapStateH\x00\x12\x65\n\tchallenge\x18\x03 \x01(\x0b\x32P.wuprotos.networking.responses.GetPlayerStateResponse.ClientPlayerChallengeStateH\x00\x42\x07\n\x05State\x1a\x16\n\x14\x43lientPlayerMapState\x1ak\n\x1a\x43lientPlayerChallengeState\x12\x13\n\x0b\x66ortress_id\x18\x01 \x01(\t\x12\x38\n\x0c\x66ortress_poi\x18\x02 \x01(\x0b\x32\".wuprotos.data.client.ClientMapPoib\x06proto3')
  ,
  dependencies=[wuprotos_dot_data_dot_client_dot_client__map__poi__pb2.DESCRIPTOR,])




_GETPLAYERSTATERESPONSE_CLIENTPLAYER = _descriptor.Descriptor(
  name='ClientPlayer',
  full_name='wuprotos.networking.responses.GetPlayerStateResponse.ClientPlayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creation_time_ms', full_name='wuprotos.networking.responses.GetPlayerStateResponse.ClientPlayer.creation_time_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map', full_name='wuprotos.networking.responses.GetPlayerStateResponse.ClientPlayer.map', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='challenge', full_name='wuprotos.networking.responses.GetPlayerStateResponse.ClientPlayer.challenge', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='State', full_name='wuprotos.networking.responses.GetPlayerStateResponse.ClientPlayer.State',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=251,
  serialized_end=494,
)

_GETPLAYERSTATERESPONSE_CLIENTPLAYERMAPSTATE = _descriptor.Descriptor(
  name='ClientPlayerMapState',
  full_name='wuprotos.networking.responses.GetPlayerStateResponse.ClientPlayerMapState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=496,
  serialized_end=518,
)

_GETPLAYERSTATERESPONSE_CLIENTPLAYERCHALLENGESTATE = _descriptor.Descriptor(
  name='ClientPlayerChallengeState',
  full_name='wuprotos.networking.responses.GetPlayerStateResponse.ClientPlayerChallengeState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fortress_id', full_name='wuprotos.networking.responses.GetPlayerStateResponse.ClientPlayerChallengeState.fortress_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fortress_poi', full_name='wuprotos.networking.responses.GetPlayerStateResponse.ClientPlayerChallengeState.fortress_poi', index=1,
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
  serialized_start=520,
  serialized_end=627,
)

_GETPLAYERSTATERESPONSE = _descriptor.Descriptor(
  name='GetPlayerStateResponse',
  full_name='wuprotos.networking.responses.GetPlayerStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player', full_name='wuprotos.networking.responses.GetPlayerStateResponse.player', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETPLAYERSTATERESPONSE_CLIENTPLAYER, _GETPLAYERSTATERESPONSE_CLIENTPLAYERMAPSTATE, _GETPLAYERSTATERESPONSE_CLIENTPLAYERCHALLENGESTATE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=140,
  serialized_end=627,
)

_GETPLAYERSTATERESPONSE_CLIENTPLAYER.fields_by_name['map'].message_type = _GETPLAYERSTATERESPONSE_CLIENTPLAYERMAPSTATE
_GETPLAYERSTATERESPONSE_CLIENTPLAYER.fields_by_name['challenge'].message_type = _GETPLAYERSTATERESPONSE_CLIENTPLAYERCHALLENGESTATE
_GETPLAYERSTATERESPONSE_CLIENTPLAYER.containing_type = _GETPLAYERSTATERESPONSE
_GETPLAYERSTATERESPONSE_CLIENTPLAYER.oneofs_by_name['State'].fields.append(
  _GETPLAYERSTATERESPONSE_CLIENTPLAYER.fields_by_name['map'])
_GETPLAYERSTATERESPONSE_CLIENTPLAYER.fields_by_name['map'].containing_oneof = _GETPLAYERSTATERESPONSE_CLIENTPLAYER.oneofs_by_name['State']
_GETPLAYERSTATERESPONSE_CLIENTPLAYER.oneofs_by_name['State'].fields.append(
  _GETPLAYERSTATERESPONSE_CLIENTPLAYER.fields_by_name['challenge'])
_GETPLAYERSTATERESPONSE_CLIENTPLAYER.fields_by_name['challenge'].containing_oneof = _GETPLAYERSTATERESPONSE_CLIENTPLAYER.oneofs_by_name['State']
_GETPLAYERSTATERESPONSE_CLIENTPLAYERMAPSTATE.containing_type = _GETPLAYERSTATERESPONSE
_GETPLAYERSTATERESPONSE_CLIENTPLAYERCHALLENGESTATE.fields_by_name['fortress_poi'].message_type = wuprotos_dot_data_dot_client_dot_client__map__poi__pb2._CLIENTMAPPOI
_GETPLAYERSTATERESPONSE_CLIENTPLAYERCHALLENGESTATE.containing_type = _GETPLAYERSTATERESPONSE
_GETPLAYERSTATERESPONSE.fields_by_name['player'].message_type = _GETPLAYERSTATERESPONSE_CLIENTPLAYER
DESCRIPTOR.message_types_by_name['GetPlayerStateResponse'] = _GETPLAYERSTATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetPlayerStateResponse = _reflection.GeneratedProtocolMessageType('GetPlayerStateResponse', (_message.Message,), dict(

  ClientPlayer = _reflection.GeneratedProtocolMessageType('ClientPlayer', (_message.Message,), dict(
    DESCRIPTOR = _GETPLAYERSTATERESPONSE_CLIENTPLAYER,
    __module__ = 'wuprotos.networking.responses.get_player_state_response_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.GetPlayerStateResponse.ClientPlayer)
    ))
  ,

  ClientPlayerMapState = _reflection.GeneratedProtocolMessageType('ClientPlayerMapState', (_message.Message,), dict(
    DESCRIPTOR = _GETPLAYERSTATERESPONSE_CLIENTPLAYERMAPSTATE,
    __module__ = 'wuprotos.networking.responses.get_player_state_response_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.GetPlayerStateResponse.ClientPlayerMapState)
    ))
  ,

  ClientPlayerChallengeState = _reflection.GeneratedProtocolMessageType('ClientPlayerChallengeState', (_message.Message,), dict(
    DESCRIPTOR = _GETPLAYERSTATERESPONSE_CLIENTPLAYERCHALLENGESTATE,
    __module__ = 'wuprotos.networking.responses.get_player_state_response_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.GetPlayerStateResponse.ClientPlayerChallengeState)
    ))
  ,
  DESCRIPTOR = _GETPLAYERSTATERESPONSE,
  __module__ = 'wuprotos.networking.responses.get_player_state_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.GetPlayerStateResponse)
  ))
_sym_db.RegisterMessage(GetPlayerStateResponse)
_sym_db.RegisterMessage(GetPlayerStateResponse.ClientPlayer)
_sym_db.RegisterMessage(GetPlayerStateResponse.ClientPlayerMapState)
_sym_db.RegisterMessage(GetPlayerStateResponse.ClientPlayerChallengeState)


# @@protoc_insertion_point(module_scope)