# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/LevelRequirement.proto

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
  name='WUProtos/Data/LevelRequirement.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n$WUProtos/Data/LevelRequirement.proto\x12\rWUProtos.Data\x1a\'WUProtos/Enums/ComparisonOperator.proto\"b\n\x10LevelRequirement\x12?\n\x13\x63omparison_operator\x18\x01 \x01(\x0e\x32\".WUProtos.Enums.ComparisonOperator\x12\r\n\x05level\x18\x02 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Enums_dot_ComparisonOperator__pb2.DESCRIPTOR,])




_LEVELREQUIREMENT = _descriptor.Descriptor(
  name='LevelRequirement',
  full_name='WUProtos.Data.LevelRequirement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='comparison_operator', full_name='WUProtos.Data.LevelRequirement.comparison_operator', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='WUProtos.Data.LevelRequirement.level', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=96,
  serialized_end=194,
)

_LEVELREQUIREMENT.fields_by_name['comparison_operator'].enum_type = WUProtos_dot_Enums_dot_ComparisonOperator__pb2._COMPARISONOPERATOR
DESCRIPTOR.message_types_by_name['LevelRequirement'] = _LEVELREQUIREMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LevelRequirement = _reflection.GeneratedProtocolMessageType('LevelRequirement', (_message.Message,), dict(
  DESCRIPTOR = _LEVELREQUIREMENT,
  __module__ = 'WUProtos.Data.LevelRequirement_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.LevelRequirement)
  ))
_sym_db.RegisterMessage(LevelRequirement)


# @@protoc_insertion_point(module_scope)
