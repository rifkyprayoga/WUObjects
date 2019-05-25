# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/data/player/player_profession_progress_v3.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wuprotos.data.loot import loot_reward_pb2 as wuprotos_dot_data_dot_loot_dot_loot__reward__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/data/player/player_profession_progress_v3.proto',
  package='wuprotos.data.player',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n8wuprotos/data/player/player_profession_progress_v3.proto\x12\x14wuprotos.data.player\x1a$wuprotos/data/loot/loot_reward.proto\"\xa8\x06\n\x1aPlayerProfessionProgressV3\x12Y\n\rnode_progress\x18\x01 \x03(\x0b\x32\x42.wuprotos.data.player.PlayerProfessionProgressV3.NodeProgressEntry\x12\x13\n\x0brank_points\x18\x02 \x01(\r\x12`\n\x11rank_progress_map\x18\x03 \x03(\x0b\x32\x45.wuprotos.data.player.PlayerProfessionProgressV3.RankProgressMapEntry\x12\x18\n\x10profession_grade\x18\x04 \x01(\r\x1at\n\x11NodeProgressEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0b\x32?.wuprotos.data.player.PlayerProfessionProgressV3.NodeProgressV3:\x02\x38\x01\x1aw\n\x14RankProgressMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0b\x32?.wuprotos.data.player.PlayerProfessionProgressV3.RankProgressV3:\x02\x38\x01\x1a\x8c\x01\n\x0eNodeProgressV3\x12\r\n\x05level\x18\x01 \x01(\r\x12\x1e\n\x16last_updated_timestamp\x18\x02 \x01(\x03\x12K\n\x14unlocked_levels_cost\x18\x03 \x01(\x0b\x32-.wuprotos.data.loot.LootReward.LootCollection\x1a\x9f\x01\n\x0eRankProgressV3\x1a\x8c\x01\n\x0eNodeProgressV3\x12\r\n\x05level\x18\x01 \x01(\r\x12\x1e\n\x16last_updated_timestamp\x18\x02 \x01(\x03\x12K\n\x14unlocked_levels_cost\x18\x03 \x01(\x0b\x32-.wuprotos.data.loot.LootReward.LootCollectionb\x06proto3')
  ,
  dependencies=[wuprotos_dot_data_dot_loot_dot_loot__reward__pb2.DESCRIPTOR,])




_PLAYERPROFESSIONPROGRESSV3_NODEPROGRESSENTRY = _descriptor.Descriptor(
  name='NodeProgressEntry',
  full_name='wuprotos.data.player.PlayerProfessionProgressV3.NodeProgressEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='wuprotos.data.player.PlayerProfessionProgressV3.NodeProgressEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='wuprotos.data.player.PlayerProfessionProgressV3.NodeProgressEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=387,
  serialized_end=503,
)

_PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSMAPENTRY = _descriptor.Descriptor(
  name='RankProgressMapEntry',
  full_name='wuprotos.data.player.PlayerProfessionProgressV3.RankProgressMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='wuprotos.data.player.PlayerProfessionProgressV3.RankProgressMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='wuprotos.data.player.PlayerProfessionProgressV3.RankProgressMapEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=505,
  serialized_end=624,
)

_PLAYERPROFESSIONPROGRESSV3_NODEPROGRESSV3 = _descriptor.Descriptor(
  name='NodeProgressV3',
  full_name='wuprotos.data.player.PlayerProfessionProgressV3.NodeProgressV3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='wuprotos.data.player.PlayerProfessionProgressV3.NodeProgressV3.level', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_updated_timestamp', full_name='wuprotos.data.player.PlayerProfessionProgressV3.NodeProgressV3.last_updated_timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unlocked_levels_cost', full_name='wuprotos.data.player.PlayerProfessionProgressV3.NodeProgressV3.unlocked_levels_cost', index=2,
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
  ],
  serialized_start=627,
  serialized_end=767,
)

_PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSV3_NODEPROGRESSV3 = _descriptor.Descriptor(
  name='NodeProgressV3',
  full_name='wuprotos.data.player.PlayerProfessionProgressV3.RankProgressV3.NodeProgressV3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='wuprotos.data.player.PlayerProfessionProgressV3.RankProgressV3.NodeProgressV3.level', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_updated_timestamp', full_name='wuprotos.data.player.PlayerProfessionProgressV3.RankProgressV3.NodeProgressV3.last_updated_timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unlocked_levels_cost', full_name='wuprotos.data.player.PlayerProfessionProgressV3.RankProgressV3.NodeProgressV3.unlocked_levels_cost', index=2,
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
  ],
  serialized_start=627,
  serialized_end=767,
)

_PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSV3 = _descriptor.Descriptor(
  name='RankProgressV3',
  full_name='wuprotos.data.player.PlayerProfessionProgressV3.RankProgressV3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSV3_NODEPROGRESSV3, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=770,
  serialized_end=929,
)

_PLAYERPROFESSIONPROGRESSV3 = _descriptor.Descriptor(
  name='PlayerProfessionProgressV3',
  full_name='wuprotos.data.player.PlayerProfessionProgressV3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_progress', full_name='wuprotos.data.player.PlayerProfessionProgressV3.node_progress', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank_points', full_name='wuprotos.data.player.PlayerProfessionProgressV3.rank_points', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank_progress_map', full_name='wuprotos.data.player.PlayerProfessionProgressV3.rank_progress_map', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profession_grade', full_name='wuprotos.data.player.PlayerProfessionProgressV3.profession_grade', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PLAYERPROFESSIONPROGRESSV3_NODEPROGRESSENTRY, _PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSMAPENTRY, _PLAYERPROFESSIONPROGRESSV3_NODEPROGRESSV3, _PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSV3, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=929,
)

_PLAYERPROFESSIONPROGRESSV3_NODEPROGRESSENTRY.fields_by_name['value'].message_type = _PLAYERPROFESSIONPROGRESSV3_NODEPROGRESSV3
_PLAYERPROFESSIONPROGRESSV3_NODEPROGRESSENTRY.containing_type = _PLAYERPROFESSIONPROGRESSV3
_PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSMAPENTRY.fields_by_name['value'].message_type = _PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSV3
_PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSMAPENTRY.containing_type = _PLAYERPROFESSIONPROGRESSV3
_PLAYERPROFESSIONPROGRESSV3_NODEPROGRESSV3.fields_by_name['unlocked_levels_cost'].message_type = wuprotos_dot_data_dot_loot_dot_loot__reward__pb2._LOOTREWARD_LOOTCOLLECTION
_PLAYERPROFESSIONPROGRESSV3_NODEPROGRESSV3.containing_type = _PLAYERPROFESSIONPROGRESSV3
_PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSV3_NODEPROGRESSV3.fields_by_name['unlocked_levels_cost'].message_type = wuprotos_dot_data_dot_loot_dot_loot__reward__pb2._LOOTREWARD_LOOTCOLLECTION
_PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSV3_NODEPROGRESSV3.containing_type = _PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSV3
_PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSV3.containing_type = _PLAYERPROFESSIONPROGRESSV3
_PLAYERPROFESSIONPROGRESSV3.fields_by_name['node_progress'].message_type = _PLAYERPROFESSIONPROGRESSV3_NODEPROGRESSENTRY
_PLAYERPROFESSIONPROGRESSV3.fields_by_name['rank_progress_map'].message_type = _PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSMAPENTRY
DESCRIPTOR.message_types_by_name['PlayerProfessionProgressV3'] = _PLAYERPROFESSIONPROGRESSV3
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerProfessionProgressV3 = _reflection.GeneratedProtocolMessageType('PlayerProfessionProgressV3', (_message.Message,), dict(

  NodeProgressEntry = _reflection.GeneratedProtocolMessageType('NodeProgressEntry', (_message.Message,), dict(
    DESCRIPTOR = _PLAYERPROFESSIONPROGRESSV3_NODEPROGRESSENTRY,
    __module__ = 'wuprotos.data.player.player_profession_progress_v3_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.data.player.PlayerProfessionProgressV3.NodeProgressEntry)
    ))
  ,

  RankProgressMapEntry = _reflection.GeneratedProtocolMessageType('RankProgressMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSMAPENTRY,
    __module__ = 'wuprotos.data.player.player_profession_progress_v3_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.data.player.PlayerProfessionProgressV3.RankProgressMapEntry)
    ))
  ,

  NodeProgressV3 = _reflection.GeneratedProtocolMessageType('NodeProgressV3', (_message.Message,), dict(
    DESCRIPTOR = _PLAYERPROFESSIONPROGRESSV3_NODEPROGRESSV3,
    __module__ = 'wuprotos.data.player.player_profession_progress_v3_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.data.player.PlayerProfessionProgressV3.NodeProgressV3)
    ))
  ,

  RankProgressV3 = _reflection.GeneratedProtocolMessageType('RankProgressV3', (_message.Message,), dict(

    NodeProgressV3 = _reflection.GeneratedProtocolMessageType('NodeProgressV3', (_message.Message,), dict(
      DESCRIPTOR = _PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSV3_NODEPROGRESSV3,
      __module__ = 'wuprotos.data.player.player_profession_progress_v3_pb2'
      # @@protoc_insertion_point(class_scope:wuprotos.data.player.PlayerProfessionProgressV3.RankProgressV3.NodeProgressV3)
      ))
    ,
    DESCRIPTOR = _PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSV3,
    __module__ = 'wuprotos.data.player.player_profession_progress_v3_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.data.player.PlayerProfessionProgressV3.RankProgressV3)
    ))
  ,
  DESCRIPTOR = _PLAYERPROFESSIONPROGRESSV3,
  __module__ = 'wuprotos.data.player.player_profession_progress_v3_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.data.player.PlayerProfessionProgressV3)
  ))
_sym_db.RegisterMessage(PlayerProfessionProgressV3)
_sym_db.RegisterMessage(PlayerProfessionProgressV3.NodeProgressEntry)
_sym_db.RegisterMessage(PlayerProfessionProgressV3.RankProgressMapEntry)
_sym_db.RegisterMessage(PlayerProfessionProgressV3.NodeProgressV3)
_sym_db.RegisterMessage(PlayerProfessionProgressV3.RankProgressV3)
_sym_db.RegisterMessage(PlayerProfessionProgressV3.RankProgressV3.NodeProgressV3)


_PLAYERPROFESSIONPROGRESSV3_NODEPROGRESSENTRY._options = None
_PLAYERPROFESSIONPROGRESSV3_RANKPROGRESSMAPENTRY._options = None
# @@protoc_insertion_point(module_scope)