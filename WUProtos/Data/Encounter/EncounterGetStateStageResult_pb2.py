# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Encounter/EncounterGetStateStageResult.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Encounter import EncounterGetStateSwishStageResult_pb2 as WUProtos_dot_Data_dot_Encounter_dot_EncounterGetStateSwishStageResult__pb2
from WUProtos.Data.Encounter import EncounterGetStateCombatStageResult_pb2 as WUProtos_dot_Data_dot_Encounter_dot_EncounterGetStateCombatStageResult__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Encounter/EncounterGetStateStageResult.proto',
  package='WUProtos.Data.Encounter',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n:WUProtos/Data/Encounter/EncounterGetStateStageResult.proto\x12\x17WUProtos.Data.Encounter\x1a?WUProtos/Data/Encounter/EncounterGetStateSwishStageResult.proto\x1a@WUProtos/Data/Encounter/EncounterGetStateCombatStageResult.proto\"\xc2\x01\n\x1c\x45ncounterGetStateStageResult\x12K\n\x05swish\x18\x01 \x01(\x0b\x32:.WUProtos.Data.Encounter.EncounterGetStateSwishStageResultH\x00\x12M\n\x06\x63ombat\x18\x02 \x01(\x0b\x32;.WUProtos.Data.Encounter.EncounterGetStateCombatStageResultH\x00\x42\x06\n\x04Typeb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Encounter_dot_EncounterGetStateSwishStageResult__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_Encounter_dot_EncounterGetStateCombatStageResult__pb2.DESCRIPTOR,])




_ENCOUNTERGETSTATESTAGERESULT = _descriptor.Descriptor(
  name='EncounterGetStateStageResult',
  full_name='WUProtos.Data.Encounter.EncounterGetStateStageResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='swish', full_name='WUProtos.Data.Encounter.EncounterGetStateStageResult.swish', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat', full_name='WUProtos.Data.Encounter.EncounterGetStateStageResult.combat', index=1,
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
    _descriptor.OneofDescriptor(
      name='Type', full_name='WUProtos.Data.Encounter.EncounterGetStateStageResult.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=219,
  serialized_end=413,
)

_ENCOUNTERGETSTATESTAGERESULT.fields_by_name['swish'].message_type = WUProtos_dot_Data_dot_Encounter_dot_EncounterGetStateSwishStageResult__pb2._ENCOUNTERGETSTATESWISHSTAGERESULT
_ENCOUNTERGETSTATESTAGERESULT.fields_by_name['combat'].message_type = WUProtos_dot_Data_dot_Encounter_dot_EncounterGetStateCombatStageResult__pb2._ENCOUNTERGETSTATECOMBATSTAGERESULT
_ENCOUNTERGETSTATESTAGERESULT.oneofs_by_name['Type'].fields.append(
  _ENCOUNTERGETSTATESTAGERESULT.fields_by_name['swish'])
_ENCOUNTERGETSTATESTAGERESULT.fields_by_name['swish'].containing_oneof = _ENCOUNTERGETSTATESTAGERESULT.oneofs_by_name['Type']
_ENCOUNTERGETSTATESTAGERESULT.oneofs_by_name['Type'].fields.append(
  _ENCOUNTERGETSTATESTAGERESULT.fields_by_name['combat'])
_ENCOUNTERGETSTATESTAGERESULT.fields_by_name['combat'].containing_oneof = _ENCOUNTERGETSTATESTAGERESULT.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['EncounterGetStateStageResult'] = _ENCOUNTERGETSTATESTAGERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EncounterGetStateStageResult = _reflection.GeneratedProtocolMessageType('EncounterGetStateStageResult', (_message.Message,), dict(
  DESCRIPTOR = _ENCOUNTERGETSTATESTAGERESULT,
  __module__ = 'WUProtos.Data.Encounter.EncounterGetStateStageResult_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Encounter.EncounterGetStateStageResult)
  ))
_sym_db.RegisterMessage(EncounterGetStateStageResult)


# @@protoc_insertion_point(module_scope)
