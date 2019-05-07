# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Enums/UpdateType.proto

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
  name='WUProtos/Enums/UpdateType.proto',
  package='WUProtos.Enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1fWUProtos/Enums/UpdateType.proto\x12\x0eWUProtos.Enums*\x89\x01\n\nUpdateType\x12\x07\n\x03\x41\x44\x44\x10\x00\x12\n\n\x06MODIFY\x10\x01\x12\n\n\x06REMOVE\x10\x02\x12\x14\n\x10PREDICTED_MODIFY\x10\x03\x12\x14\n\x10PREDICTED_REMOVE\x10\x04\x12\x16\n\x12ROLLED_BACK_MODIFY\x10\x05\x12\x16\n\x12ROLLED_BACK_REMOVE\x10\x06\x62\x06proto3')
)

_UPDATETYPE = _descriptor.EnumDescriptor(
  name='UpdateType',
  full_name='WUProtos.Enums.UpdateType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODIFY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREDICTED_MODIFY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREDICTED_REMOVE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROLLED_BACK_MODIFY', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROLLED_BACK_REMOVE', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=52,
  serialized_end=189,
)
_sym_db.RegisterEnumDescriptor(_UPDATETYPE)

UpdateType = enum_type_wrapper.EnumTypeWrapper(_UPDATETYPE)
ADD = 0
MODIFY = 1
REMOVE = 2
PREDICTED_MODIFY = 3
PREDICTED_REMOVE = 4
ROLLED_BACK_MODIFY = 5
ROLLED_BACK_REMOVE = 6


DESCRIPTOR.enum_types_by_name['UpdateType'] = _UPDATETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
