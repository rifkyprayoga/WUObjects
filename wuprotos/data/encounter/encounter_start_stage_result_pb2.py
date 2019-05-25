# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/data/encounter/encounter_start_stage_result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/data/encounter/encounter_start_stage_result.proto',
  package='wuprotos.data.encounter',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n:wuprotos/data/encounter/encounter_start_stage_result.proto\x12\x17wuprotos.data.encounter\"\x9a\x06\n\x19\x45ncounterStartStageResult\x12\x62\n\x05swish\x18\x01 \x01(\x0b\x32Q.wuprotos.data.encounter.EncounterStartStageResult.EncounterStartSwishStageResultH\x00\x12\x64\n\x06\x63ombat\x18\x02 \x01(\x0b\x32R.wuprotos.data.encounter.EncounterStartStageResult.EncounterStartCombatStageResultH\x00\x12\x66\n\x07portkey\x18\x03 \x01(\x0b\x32S.wuprotos.data.encounter.EncounterStartStageResult.EncounterStartPortkeyStageResultH\x00\x1a \n\x1e\x45ncounterStartSwishStageResult\x1a\"\n EncounterStartPortkeyStageResult\x1a\xfc\x02\n\x1f\x45ncounterStartCombatStageResult\x12\x14\n\x0chp_max_enemy\x18\x01 \x01(\x03\x12\x1e\n\x16\x65nemy_damage_unblocked\x18\x02 \x03(\x03\x12\x1c\n\x14\x65nemy_damage_blocked\x18\x03 \x03(\x03\x12\x15\n\rhp_max_player\x18\x04 \x01(\x03\x12\x8f\x01\n\x18player_damage_per_energy\x18\x05 \x03(\x0b\x32m.wuprotos.data.encounter.EncounterStartStageResult.EncounterStartCombatStageResult.PlayerDamagePerEnergyEntry\x12\x1e\n\x16player_crit_multiplier\x18\x06 \x01(\x02\x1a<\n\x1aPlayerDamagePerEnergyEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x42\x06\n\x04Typeb\x06proto3')
)




_ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTSWISHSTAGERESULT = _descriptor.Descriptor(
  name='EncounterStartSwishStageResult',
  full_name='wuprotos.data.encounter.EncounterStartStageResult.EncounterStartSwishStageResult',
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
  serialized_start=423,
  serialized_end=455,
)

_ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTPORTKEYSTAGERESULT = _descriptor.Descriptor(
  name='EncounterStartPortkeyStageResult',
  full_name='wuprotos.data.encounter.EncounterStartStageResult.EncounterStartPortkeyStageResult',
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
  serialized_start=457,
  serialized_end=491,
)

_ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTCOMBATSTAGERESULT_PLAYERDAMAGEPERENERGYENTRY = _descriptor.Descriptor(
  name='PlayerDamagePerEnergyEntry',
  full_name='wuprotos.data.encounter.EncounterStartStageResult.EncounterStartCombatStageResult.PlayerDamagePerEnergyEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='wuprotos.data.encounter.EncounterStartStageResult.EncounterStartCombatStageResult.PlayerDamagePerEnergyEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='wuprotos.data.encounter.EncounterStartStageResult.EncounterStartCombatStageResult.PlayerDamagePerEnergyEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=814,
  serialized_end=874,
)

_ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTCOMBATSTAGERESULT = _descriptor.Descriptor(
  name='EncounterStartCombatStageResult',
  full_name='wuprotos.data.encounter.EncounterStartStageResult.EncounterStartCombatStageResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hp_max_enemy', full_name='wuprotos.data.encounter.EncounterStartStageResult.EncounterStartCombatStageResult.hp_max_enemy', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enemy_damage_unblocked', full_name='wuprotos.data.encounter.EncounterStartStageResult.EncounterStartCombatStageResult.enemy_damage_unblocked', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enemy_damage_blocked', full_name='wuprotos.data.encounter.EncounterStartStageResult.EncounterStartCombatStageResult.enemy_damage_blocked', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hp_max_player', full_name='wuprotos.data.encounter.EncounterStartStageResult.EncounterStartCombatStageResult.hp_max_player', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_damage_per_energy', full_name='wuprotos.data.encounter.EncounterStartStageResult.EncounterStartCombatStageResult.player_damage_per_energy', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_crit_multiplier', full_name='wuprotos.data.encounter.EncounterStartStageResult.EncounterStartCombatStageResult.player_crit_multiplier', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTCOMBATSTAGERESULT_PLAYERDAMAGEPERENERGYENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=494,
  serialized_end=874,
)

_ENCOUNTERSTARTSTAGERESULT = _descriptor.Descriptor(
  name='EncounterStartStageResult',
  full_name='wuprotos.data.encounter.EncounterStartStageResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='swish', full_name='wuprotos.data.encounter.EncounterStartStageResult.swish', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat', full_name='wuprotos.data.encounter.EncounterStartStageResult.combat', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portkey', full_name='wuprotos.data.encounter.EncounterStartStageResult.portkey', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTSWISHSTAGERESULT, _ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTPORTKEYSTAGERESULT, _ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTCOMBATSTAGERESULT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='wuprotos.data.encounter.EncounterStartStageResult.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=88,
  serialized_end=882,
)

_ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTSWISHSTAGERESULT.containing_type = _ENCOUNTERSTARTSTAGERESULT
_ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTPORTKEYSTAGERESULT.containing_type = _ENCOUNTERSTARTSTAGERESULT
_ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTCOMBATSTAGERESULT_PLAYERDAMAGEPERENERGYENTRY.containing_type = _ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTCOMBATSTAGERESULT
_ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTCOMBATSTAGERESULT.fields_by_name['player_damage_per_energy'].message_type = _ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTCOMBATSTAGERESULT_PLAYERDAMAGEPERENERGYENTRY
_ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTCOMBATSTAGERESULT.containing_type = _ENCOUNTERSTARTSTAGERESULT
_ENCOUNTERSTARTSTAGERESULT.fields_by_name['swish'].message_type = _ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTSWISHSTAGERESULT
_ENCOUNTERSTARTSTAGERESULT.fields_by_name['combat'].message_type = _ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTCOMBATSTAGERESULT
_ENCOUNTERSTARTSTAGERESULT.fields_by_name['portkey'].message_type = _ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTPORTKEYSTAGERESULT
_ENCOUNTERSTARTSTAGERESULT.oneofs_by_name['Type'].fields.append(
  _ENCOUNTERSTARTSTAGERESULT.fields_by_name['swish'])
_ENCOUNTERSTARTSTAGERESULT.fields_by_name['swish'].containing_oneof = _ENCOUNTERSTARTSTAGERESULT.oneofs_by_name['Type']
_ENCOUNTERSTARTSTAGERESULT.oneofs_by_name['Type'].fields.append(
  _ENCOUNTERSTARTSTAGERESULT.fields_by_name['combat'])
_ENCOUNTERSTARTSTAGERESULT.fields_by_name['combat'].containing_oneof = _ENCOUNTERSTARTSTAGERESULT.oneofs_by_name['Type']
_ENCOUNTERSTARTSTAGERESULT.oneofs_by_name['Type'].fields.append(
  _ENCOUNTERSTARTSTAGERESULT.fields_by_name['portkey'])
_ENCOUNTERSTARTSTAGERESULT.fields_by_name['portkey'].containing_oneof = _ENCOUNTERSTARTSTAGERESULT.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['EncounterStartStageResult'] = _ENCOUNTERSTARTSTAGERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EncounterStartStageResult = _reflection.GeneratedProtocolMessageType('EncounterStartStageResult', (_message.Message,), dict(

  EncounterStartSwishStageResult = _reflection.GeneratedProtocolMessageType('EncounterStartSwishStageResult', (_message.Message,), dict(
    DESCRIPTOR = _ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTSWISHSTAGERESULT,
    __module__ = 'wuprotos.data.encounter.encounter_start_stage_result_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.data.encounter.EncounterStartStageResult.EncounterStartSwishStageResult)
    ))
  ,

  EncounterStartPortkeyStageResult = _reflection.GeneratedProtocolMessageType('EncounterStartPortkeyStageResult', (_message.Message,), dict(
    DESCRIPTOR = _ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTPORTKEYSTAGERESULT,
    __module__ = 'wuprotos.data.encounter.encounter_start_stage_result_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.data.encounter.EncounterStartStageResult.EncounterStartPortkeyStageResult)
    ))
  ,

  EncounterStartCombatStageResult = _reflection.GeneratedProtocolMessageType('EncounterStartCombatStageResult', (_message.Message,), dict(

    PlayerDamagePerEnergyEntry = _reflection.GeneratedProtocolMessageType('PlayerDamagePerEnergyEntry', (_message.Message,), dict(
      DESCRIPTOR = _ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTCOMBATSTAGERESULT_PLAYERDAMAGEPERENERGYENTRY,
      __module__ = 'wuprotos.data.encounter.encounter_start_stage_result_pb2'
      # @@protoc_insertion_point(class_scope:wuprotos.data.encounter.EncounterStartStageResult.EncounterStartCombatStageResult.PlayerDamagePerEnergyEntry)
      ))
    ,
    DESCRIPTOR = _ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTCOMBATSTAGERESULT,
    __module__ = 'wuprotos.data.encounter.encounter_start_stage_result_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.data.encounter.EncounterStartStageResult.EncounterStartCombatStageResult)
    ))
  ,
  DESCRIPTOR = _ENCOUNTERSTARTSTAGERESULT,
  __module__ = 'wuprotos.data.encounter.encounter_start_stage_result_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.data.encounter.EncounterStartStageResult)
  ))
_sym_db.RegisterMessage(EncounterStartStageResult)
_sym_db.RegisterMessage(EncounterStartStageResult.EncounterStartSwishStageResult)
_sym_db.RegisterMessage(EncounterStartStageResult.EncounterStartPortkeyStageResult)
_sym_db.RegisterMessage(EncounterStartStageResult.EncounterStartCombatStageResult)
_sym_db.RegisterMessage(EncounterStartStageResult.EncounterStartCombatStageResult.PlayerDamagePerEnergyEntry)


_ENCOUNTERSTARTSTAGERESULT_ENCOUNTERSTARTCOMBATSTAGERESULT_PLAYERDAMAGEPERENERGYENTRY._options = None
# @@protoc_insertion_point(module_scope)