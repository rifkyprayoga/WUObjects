# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientBonusCategory.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import Color_pb2 as WUProtos_dot_Data_dot_Color__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientBonusCategory.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n.WUProtos/Data/Client/ClientBonusCategory.proto\x12\x14WUProtos.Data.Client\x1a\x19WUProtos/Data/Color.proto\"v\n\x13\x43lientBonusCategory\x12\n\n\x02id\x18\x01 \x01(\t\x12#\n\x05\x63olor\x18\x02 \x01(\x0b\x32\x14.WUProtos.Data.Color\x12\x14\n\x0cname_loc_key\x18\x03 \x01(\t\x12\x18\n\x10\x62\x61\x63kground_image\x18\x04 \x01(\tb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Color__pb2.DESCRIPTOR,])




_CLIENTBONUSCATEGORY = _descriptor.Descriptor(
  name='ClientBonusCategory',
  full_name='WUProtos.Data.Client.ClientBonusCategory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.Client.ClientBonusCategory.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='WUProtos.Data.Client.ClientBonusCategory.color', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name_loc_key', full_name='WUProtos.Data.Client.ClientBonusCategory.name_loc_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='background_image', full_name='WUProtos.Data.Client.ClientBonusCategory.background_image', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=99,
  serialized_end=217,
)

_CLIENTBONUSCATEGORY.fields_by_name['color'].message_type = WUProtos_dot_Data_dot_Color__pb2._COLOR
DESCRIPTOR.message_types_by_name['ClientBonusCategory'] = _CLIENTBONUSCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientBonusCategory = _reflection.GeneratedProtocolMessageType('ClientBonusCategory', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTBONUSCATEGORY,
  __module__ = 'WUProtos.Data.Client.ClientBonusCategory_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientBonusCategory)
  ))
_sym_db.RegisterMessage(ClientBonusCategory)


# @@protoc_insertion_point(module_scope)
