# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Enums/CombatPhaseOutcome.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Enums/CombatPhaseOutcome.proto',
  package='WUProtos.Enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\'WUProtos/Enums/CombatPhaseOutcome.proto\x12\x0eWUProtos.Enums*g\n\x12\x43ombatPhaseOutcome\x12 \n\x1c\x43OMBAT_PHASE_OUTCOME_UNKNOWN\x10\x00\x12\x0b\n\x07SUCCEED\x10\x01\x12\x13\n\x0f\x46\x41IL_CHECKPOINT\x10\x02\x12\r\n\tFAIL_TIME\x10\x03\x62\x06proto3')
)

_COMBATPHASEOUTCOME = _descriptor.EnumDescriptor(
  name='CombatPhaseOutcome',
  full_name='WUProtos.Enums.CombatPhaseOutcome',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMBAT_PHASE_OUTCOME_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCEED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL_CHECKPOINT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL_TIME', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=59,
  serialized_end=162,
)
_sym_db.RegisterEnumDescriptor(_COMBATPHASEOUTCOME)

CombatPhaseOutcome = enum_type_wrapper.EnumTypeWrapper(_COMBATPHASEOUTCOME)
COMBAT_PHASE_OUTCOME_UNKNOWN = 0
SUCCEED = 1
FAIL_CHECKPOINT = 2
FAIL_TIME = 3


DESCRIPTOR.enum_types_by_name['CombatPhaseOutcome'] = _COMBATPHASEOUTCOME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
