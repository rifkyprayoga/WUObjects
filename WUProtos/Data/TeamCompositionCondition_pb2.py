# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/TeamCompositionCondition.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Enums import ComparisonOperator_pb2 as WUProtos_dot_Enums_dot_ComparisonOperator__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/TeamCompositionCondition.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,WUProtos/Data/TeamCompositionCondition.proto\x12\rWUProtos.Data\x1a\'WUProtos/Enums/ComparisonOperator.proto\"\x93\x01\n\x18TeamCompositionCondition\x12?\n\x13\x63omparison_operator\x18\x01 \x01(\x0e\x32\".WUProtos.Enums.ComparisonOperator\x12\x1f\n\x17target_comparison_value\x18\x02 \x01(\x05\x12\x15\n\rprofession_id\x18\x03 \x01(\tb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Enums_dot_ComparisonOperator__pb2.DESCRIPTOR,])




_TEAMCOMPOSITIONCONDITION = _descriptor.Descriptor(
  name='TeamCompositionCondition',
  full_name='WUProtos.Data.TeamCompositionCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='comparison_operator', full_name='WUProtos.Data.TeamCompositionCondition.comparison_operator', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_comparison_value', full_name='WUProtos.Data.TeamCompositionCondition.target_comparison_value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profession_id', full_name='WUProtos.Data.TeamCompositionCondition.profession_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=105,
  serialized_end=252,
)

_TEAMCOMPOSITIONCONDITION.fields_by_name['comparison_operator'].enum_type = WUProtos_dot_Enums_dot_ComparisonOperator__pb2._COMPARISONOPERATOR
DESCRIPTOR.message_types_by_name['TeamCompositionCondition'] = _TEAMCOMPOSITIONCONDITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TeamCompositionCondition = _reflection.GeneratedProtocolMessageType('TeamCompositionCondition', (_message.Message,), dict(
  DESCRIPTOR = _TEAMCOMPOSITIONCONDITION,
  __module__ = 'WUProtos.Data.TeamCompositionCondition_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.TeamCompositionCondition)
  ))
_sym_db.RegisterMessage(TeamCompositionCondition)


# @@protoc_insertion_point(module_scope)