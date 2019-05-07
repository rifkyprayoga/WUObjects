# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Map/MapAbility.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Enums import MapAbilityTargetType_pb2 as WUProtos_dot_Enums_dot_MapAbilityTargetType__pb2
from WUProtos.Map import MapAbilityLevel_pb2 as WUProtos_dot_Map_dot_MapAbilityLevel__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Map/MapAbility.proto',
  package='WUProtos.Map',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dWUProtos/Map/MapAbility.proto\x12\x0cWUProtos.Map\x1a)WUProtos/Enums/MapAbilityTargetType.proto\x1a\"WUProtos/Map/MapAbilityLevel.proto\"\xe1\x01\n\nMapAbility\x12\n\n\x02id\x18\x01 \x01(\t\x12\x39\n\x0btarget_type\x18\x02 \x01(\x0e\x32$.WUProtos.Enums.MapAbilityTargetType\x12\x18\n\x10\x62\x61se_buff_gmt_id\x18\x03 \x01(\t\x12\x0e\n\x06radius\x18\x04 \x01(\x02\x12\x13\n\x0b\x63ooldown_ms\x18\x05 \x01(\r\x12\x12\n\nfocus_cost\x18\x06 \x01(\x05\x12\x39\n\x12map_ability_levels\x18\x07 \x03(\x0b\x32\x1d.WUProtos.Map.MapAbilityLevelb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Enums_dot_MapAbilityTargetType__pb2.DESCRIPTOR,WUProtos_dot_Map_dot_MapAbilityLevel__pb2.DESCRIPTOR,])




_MAPABILITY = _descriptor.Descriptor(
  name='MapAbility',
  full_name='WUProtos.Map.MapAbility',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Map.MapAbility.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_type', full_name='WUProtos.Map.MapAbility.target_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_buff_gmt_id', full_name='WUProtos.Map.MapAbility.base_buff_gmt_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radius', full_name='WUProtos.Map.MapAbility.radius', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cooldown_ms', full_name='WUProtos.Map.MapAbility.cooldown_ms', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='focus_cost', full_name='WUProtos.Map.MapAbility.focus_cost', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_ability_levels', full_name='WUProtos.Map.MapAbility.map_ability_levels', index=6,
      number=7, type=11, cpp_type=10, label=3,
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
  serialized_start=127,
  serialized_end=352,
)

_MAPABILITY.fields_by_name['target_type'].enum_type = WUProtos_dot_Enums_dot_MapAbilityTargetType__pb2._MAPABILITYTARGETTYPE
_MAPABILITY.fields_by_name['map_ability_levels'].message_type = WUProtos_dot_Map_dot_MapAbilityLevel__pb2._MAPABILITYLEVEL
DESCRIPTOR.message_types_by_name['MapAbility'] = _MAPABILITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MapAbility = _reflection.GeneratedProtocolMessageType('MapAbility', (_message.Message,), dict(
  DESCRIPTOR = _MAPABILITY,
  __module__ = 'WUProtos.Map.MapAbility_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Map.MapAbility)
  ))
_sym_db.RegisterMessage(MapAbility)


# @@protoc_insertion_point(module_scope)
