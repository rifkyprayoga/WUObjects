# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Enums/AppBackgroundResult.proto

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
  name='WUProtos/Enums/AppBackgroundResult.proto',
  package='WUProtos.Enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(WUProtos/Enums/AppBackgroundResult.proto\x12\x0eWUProtos.Enums*Z\n\x13\x41ppBackgroundResult\x12\x08\n\x04NONE\x10\x00\x12\r\n\tMAP_STATE\x10\x01\x12\x0e\n\nFULL_RESET\x10\x02\x12\x1a\n\x16\x44\x45\x46\x41ULT_APP_BACKGROUND\x10\x03\x62\x06proto3')
)

_APPBACKGROUNDRESULT = _descriptor.EnumDescriptor(
  name='AppBackgroundResult',
  full_name='WUProtos.Enums.AppBackgroundResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAP_STATE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL_RESET', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEFAULT_APP_BACKGROUND', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=60,
  serialized_end=150,
)
_sym_db.RegisterEnumDescriptor(_APPBACKGROUNDRESULT)

AppBackgroundResult = enum_type_wrapper.EnumTypeWrapper(_APPBACKGROUNDRESULT)
NONE = 0
MAP_STATE = 1
FULL_RESET = 2
DEFAULT_APP_BACKGROUND = 3


DESCRIPTOR.enum_types_by_name['AppBackgroundResult'] = _APPBACKGROUNDRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)