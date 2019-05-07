# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Profession/ProfessionRankPointsRequirement.proto

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
  name='WUProtos/Data/Profession/ProfessionRankPointsRequirement.proto',
  package='WUProtos.Data.Profession',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n>WUProtos/Data/Profession/ProfessionRankPointsRequirement.proto\x12\x18WUProtos.Data.Profession\x1a\'WUProtos/Enums/ComparisonOperator.proto\"\x92\x01\n\x1fProfessionRankPointsRequirement\x12\x19\n\x11profession_gmt_id\x18\x01 \x01(\t\x12\x13\n\x0brank_points\x18\x02 \x01(\x05\x12?\n\x13\x63omparison_operator\x18\x03 \x01(\x0e\x32\".WUProtos.Enums.ComparisonOperatorb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Enums_dot_ComparisonOperator__pb2.DESCRIPTOR,])




_PROFESSIONRANKPOINTSREQUIREMENT = _descriptor.Descriptor(
  name='ProfessionRankPointsRequirement',
  full_name='WUProtos.Data.Profession.ProfessionRankPointsRequirement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='profession_gmt_id', full_name='WUProtos.Data.Profession.ProfessionRankPointsRequirement.profession_gmt_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank_points', full_name='WUProtos.Data.Profession.ProfessionRankPointsRequirement.rank_points', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comparison_operator', full_name='WUProtos.Data.Profession.ProfessionRankPointsRequirement.comparison_operator', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=134,
  serialized_end=280,
)

_PROFESSIONRANKPOINTSREQUIREMENT.fields_by_name['comparison_operator'].enum_type = WUProtos_dot_Enums_dot_ComparisonOperator__pb2._COMPARISONOPERATOR
DESCRIPTOR.message_types_by_name['ProfessionRankPointsRequirement'] = _PROFESSIONRANKPOINTSREQUIREMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProfessionRankPointsRequirement = _reflection.GeneratedProtocolMessageType('ProfessionRankPointsRequirement', (_message.Message,), dict(
  DESCRIPTOR = _PROFESSIONRANKPOINTSREQUIREMENT,
  __module__ = 'WUProtos.Data.Profession.ProfessionRankPointsRequirement_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Profession.ProfessionRankPointsRequirement)
  ))
_sym_db.RegisterMessage(ProfessionRankPointsRequirement)


# @@protoc_insertion_point(module_scope)
