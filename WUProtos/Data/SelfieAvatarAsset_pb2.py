# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/SelfieAvatarAsset.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import Requirements_pb2 as WUProtos_dot_Data_dot_Requirements__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/SelfieAvatarAsset.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n%WUProtos/Data/SelfieAvatarAsset.proto\x12\rWUProtos.Data\x1a WUProtos/Data/Requirements.proto\"W\n\x11SelfieAvatarAsset\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x11unlock_conditions\x18\x02 \x01(\x0b\x32\x1b.WUProtos.Data.Requirementsb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Requirements__pb2.DESCRIPTOR,])




_SELFIEAVATARASSET = _descriptor.Descriptor(
  name='SelfieAvatarAsset',
  full_name='WUProtos.Data.SelfieAvatarAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.SelfieAvatarAsset.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unlock_conditions', full_name='WUProtos.Data.SelfieAvatarAsset.unlock_conditions', index=1,
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
  ],
  serialized_start=90,
  serialized_end=177,
)

_SELFIEAVATARASSET.fields_by_name['unlock_conditions'].message_type = WUProtos_dot_Data_dot_Requirements__pb2._REQUIREMENTS
DESCRIPTOR.message_types_by_name['SelfieAvatarAsset'] = _SELFIEAVATARASSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SelfieAvatarAsset = _reflection.GeneratedProtocolMessageType('SelfieAvatarAsset', (_message.Message,), dict(
  DESCRIPTOR = _SELFIEAVATARASSET,
  __module__ = 'WUProtos.Data.SelfieAvatarAsset_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.SelfieAvatarAsset)
  ))
_sym_db.RegisterMessage(SelfieAvatarAsset)


# @@protoc_insertion_point(module_scope)