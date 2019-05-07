# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Encounter/EncounterInteractCombatStageResult.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Combat import CombatResults_pb2 as WUProtos_dot_Data_dot_Combat_dot_CombatResults__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Encounter/EncounterInteractCombatStageResult.proto',
  package='WUProtos.Data.Encounter',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n@WUProtos/Data/Encounter/EncounterInteractCombatStageResult.proto\x12\x17WUProtos.Data.Encounter\x1a(WUProtos/Data/Combat/CombatResults.proto\"\xa5\x03\n\"EncounterInteractCombatStageResult\x12R\n\x06status\x18\x01 \x01(\x0e\x32\x42.WUProtos.Data.Encounter.EncounterInteractCombatStageResult.Status\x12\x34\n\x07results\x18\x02 \x01(\x0b\x32#.WUProtos.Data.Combat.CombatResults\"\xf4\x01\n\x06Status\x12\"\n\x1e\x43OMBAT_INTERACT_RESULT_UNKNOWN\x10\x00\x12)\n%COMBAT_INTERACT_RESULT_ENEMY_DEFEATED\x10\x01\x12#\n\x1f\x43OMBAT_INTERACT_RESULT_CONTINUE\x10\x02\x12*\n&COMBAT_INTERACT_RESULT_PLAYER_DEFEATED\x10\x03\x12(\n$COMBAT_INTERACT_RESULT_OUT_OF_ENERGY\x10\x04\x12 \n\x1c\x43OMBAT_INTERACT_RESULT_ERROR\x10\x05\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Combat_dot_CombatResults__pb2.DESCRIPTOR,])



_ENCOUNTERINTERACTCOMBATSTAGERESULT_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='WUProtos.Data.Encounter.EncounterInteractCombatStageResult.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMBAT_INTERACT_RESULT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMBAT_INTERACT_RESULT_ENEMY_DEFEATED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMBAT_INTERACT_RESULT_CONTINUE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMBAT_INTERACT_RESULT_PLAYER_DEFEATED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMBAT_INTERACT_RESULT_OUT_OF_ENERGY', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMBAT_INTERACT_RESULT_ERROR', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=313,
  serialized_end=557,
)
_sym_db.RegisterEnumDescriptor(_ENCOUNTERINTERACTCOMBATSTAGERESULT_STATUS)


_ENCOUNTERINTERACTCOMBATSTAGERESULT = _descriptor.Descriptor(
  name='EncounterInteractCombatStageResult',
  full_name='WUProtos.Data.Encounter.EncounterInteractCombatStageResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='WUProtos.Data.Encounter.EncounterInteractCombatStageResult.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='WUProtos.Data.Encounter.EncounterInteractCombatStageResult.results', index=1,
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
    _ENCOUNTERINTERACTCOMBATSTAGERESULT_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=557,
)

_ENCOUNTERINTERACTCOMBATSTAGERESULT.fields_by_name['status'].enum_type = _ENCOUNTERINTERACTCOMBATSTAGERESULT_STATUS
_ENCOUNTERINTERACTCOMBATSTAGERESULT.fields_by_name['results'].message_type = WUProtos_dot_Data_dot_Combat_dot_CombatResults__pb2._COMBATRESULTS
_ENCOUNTERINTERACTCOMBATSTAGERESULT_STATUS.containing_type = _ENCOUNTERINTERACTCOMBATSTAGERESULT
DESCRIPTOR.message_types_by_name['EncounterInteractCombatStageResult'] = _ENCOUNTERINTERACTCOMBATSTAGERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EncounterInteractCombatStageResult = _reflection.GeneratedProtocolMessageType('EncounterInteractCombatStageResult', (_message.Message,), dict(
  DESCRIPTOR = _ENCOUNTERINTERACTCOMBATSTAGERESULT,
  __module__ = 'WUProtos.Data.Encounter.EncounterInteractCombatStageResult_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Encounter.EncounterInteractCombatStageResult)
  ))
_sym_db.RegisterMessage(EncounterInteractCombatStageResult)


# @@protoc_insertion_point(module_scope)
