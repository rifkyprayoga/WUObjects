# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/data/player/player_achievement.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/data/player/player_achievement.proto',
  package='wuprotos.data.player',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n-wuprotos/data/player/player_achievement.proto\x12\x14wuprotos.data.player\"\x13\n\x11PlayerAchievementb\x06proto3')
)




_PLAYERACHIEVEMENT = _descriptor.Descriptor(
  name='PlayerAchievement',
  full_name='wuprotos.data.player.PlayerAchievement',
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
  serialized_start=71,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['PlayerAchievement'] = _PLAYERACHIEVEMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerAchievement = _reflection.GeneratedProtocolMessageType('PlayerAchievement', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERACHIEVEMENT,
  __module__ = 'wuprotos.data.player.player_achievement_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.data.player.PlayerAchievement)
  ))
_sym_db.RegisterMessage(PlayerAchievement)


# @@protoc_insertion_point(module_scope)