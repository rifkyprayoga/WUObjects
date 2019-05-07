# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Requests/Messages/MapAbilityStartMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Map import MapCoordinate_pb2 as WUProtos_dot_Map_dot_MapCoordinate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Requests/Messages/MapAbilityStartMessage.proto',
  package='WUProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nBWUProtos/Networking/Requests/Messages/MapAbilityStartMessage.proto\x12%WUProtos.Networking.Requests.Messages\x1a WUProtos/Map/MapCoordinate.proto\"\xa2\x01\n\x16MapAbilityStartMessage\x12\x1a\n\x12map_ability_gmt_id\x18\x01 \x01(\t\x12\x19\n\x0fplayer_nickname\x18\x02 \x01(\tH\x00\x12\x35\n\x0emap_coordinate\x18\x03 \x01(\x0b\x32\x1b.WUProtos.Map.MapCoordinateH\x00\x12\x10\n\x06mob_id\x18\x04 \x01(\x0cH\x00\x42\x08\n\x06Targetb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Map_dot_MapCoordinate__pb2.DESCRIPTOR,])




_MAPABILITYSTARTMESSAGE = _descriptor.Descriptor(
  name='MapAbilityStartMessage',
  full_name='WUProtos.Networking.Requests.Messages.MapAbilityStartMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='map_ability_gmt_id', full_name='WUProtos.Networking.Requests.Messages.MapAbilityStartMessage.map_ability_gmt_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_nickname', full_name='WUProtos.Networking.Requests.Messages.MapAbilityStartMessage.player_nickname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_coordinate', full_name='WUProtos.Networking.Requests.Messages.MapAbilityStartMessage.map_coordinate', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mob_id', full_name='WUProtos.Networking.Requests.Messages.MapAbilityStartMessage.mob_id', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
      name='Target', full_name='WUProtos.Networking.Requests.Messages.MapAbilityStartMessage.Target',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=144,
  serialized_end=306,
)

_MAPABILITYSTARTMESSAGE.fields_by_name['map_coordinate'].message_type = WUProtos_dot_Map_dot_MapCoordinate__pb2._MAPCOORDINATE
_MAPABILITYSTARTMESSAGE.oneofs_by_name['Target'].fields.append(
  _MAPABILITYSTARTMESSAGE.fields_by_name['player_nickname'])
_MAPABILITYSTARTMESSAGE.fields_by_name['player_nickname'].containing_oneof = _MAPABILITYSTARTMESSAGE.oneofs_by_name['Target']
_MAPABILITYSTARTMESSAGE.oneofs_by_name['Target'].fields.append(
  _MAPABILITYSTARTMESSAGE.fields_by_name['map_coordinate'])
_MAPABILITYSTARTMESSAGE.fields_by_name['map_coordinate'].containing_oneof = _MAPABILITYSTARTMESSAGE.oneofs_by_name['Target']
_MAPABILITYSTARTMESSAGE.oneofs_by_name['Target'].fields.append(
  _MAPABILITYSTARTMESSAGE.fields_by_name['mob_id'])
_MAPABILITYSTARTMESSAGE.fields_by_name['mob_id'].containing_oneof = _MAPABILITYSTARTMESSAGE.oneofs_by_name['Target']
DESCRIPTOR.message_types_by_name['MapAbilityStartMessage'] = _MAPABILITYSTARTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MapAbilityStartMessage = _reflection.GeneratedProtocolMessageType('MapAbilityStartMessage', (_message.Message,), dict(
  DESCRIPTOR = _MAPABILITYSTARTMESSAGE,
  __module__ = 'WUProtos.Networking.Requests.Messages.MapAbilityStartMessage_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Requests.Messages.MapAbilityStartMessage)
  ))
_sym_db.RegisterMessage(MapAbilityStartMessage)


# @@protoc_insertion_point(module_scope)
