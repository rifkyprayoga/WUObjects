# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Mob/MobRewardVictoryPoints.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Mob/MobRewardVictoryPoints.proto',
  package='WUProtos.Data.Mob',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n.WUProtos/Data/Mob/MobRewardVictoryPoints.proto\x12\x11WUProtos.Data.Mob\"*\n\x16MobRewardVictoryPoints\x12\x10\n\x08quantity\x18\x01 \x01(\x05\x62\x06proto3')
)




_MOBREWARDVICTORYPOINTS = _descriptor.Descriptor(
  name='MobRewardVictoryPoints',
  full_name='WUProtos.Data.Mob.MobRewardVictoryPoints',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantity', full_name='WUProtos.Data.Mob.MobRewardVictoryPoints.quantity', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=69,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['MobRewardVictoryPoints'] = _MOBREWARDVICTORYPOINTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MobRewardVictoryPoints = _reflection.GeneratedProtocolMessageType('MobRewardVictoryPoints', (_message.Message,), dict(
  DESCRIPTOR = _MOBREWARDVICTORYPOINTS,
  __module__ = 'WUProtos.Data.Mob.MobRewardVictoryPoints_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Mob.MobRewardVictoryPoints)
  ))
_sym_db.RegisterMessage(MobRewardVictoryPoints)


# @@protoc_insertion_point(module_scope)
