# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientRecipe.proto

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
  name='WUProtos/Data/Client/ClientRecipe.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\'WUProtos/Data/Client/ClientRecipe.proto\x12\x14WUProtos.Data.Client\x1a\x19WUProtos/Data/Color.proto\"\x81\x02\n\x0c\x43lientRecipe\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04icon\x18\x04 \x01(\t\x12\r\n\x05model\x18\x05 \x01(\t\x12\x12\n\ncollect_fx\x18\x06 \x01(\t\x12\x13\n\x0b\x63rafting_fx\x18\x07 \x01(\t\x12\x11\n\treveal_fx\x18\x08 \x01(\t\x12+\n\rprimary_color\x18\t \x01(\x0b\x32\x14.WUProtos.Data.Color\x12-\n\x0fsecondary_color\x18\n \x01(\x0b\x32\x14.WUProtos.Data.Color\x12\r\n\x05index\x18\x0b \x01(\x05\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Color__pb2.DESCRIPTOR,])




_CLIENTRECIPE = _descriptor.Descriptor(
  name='ClientRecipe',
  full_name='WUProtos.Data.Client.ClientRecipe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.Client.ClientRecipe.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='WUProtos.Data.Client.ClientRecipe.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='WUProtos.Data.Client.ClientRecipe.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='WUProtos.Data.Client.ClientRecipe.icon', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='WUProtos.Data.Client.ClientRecipe.model', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collect_fx', full_name='WUProtos.Data.Client.ClientRecipe.collect_fx', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='crafting_fx', full_name='WUProtos.Data.Client.ClientRecipe.crafting_fx', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reveal_fx', full_name='WUProtos.Data.Client.ClientRecipe.reveal_fx', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primary_color', full_name='WUProtos.Data.Client.ClientRecipe.primary_color', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secondary_color', full_name='WUProtos.Data.Client.ClientRecipe.secondary_color', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='WUProtos.Data.Client.ClientRecipe.index', index=10,
      number=11, type=5, cpp_type=1, label=1,
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
  serialized_start=93,
  serialized_end=350,
)

_CLIENTRECIPE.fields_by_name['primary_color'].message_type = WUProtos_dot_Data_dot_Color__pb2._COLOR
_CLIENTRECIPE.fields_by_name['secondary_color'].message_type = WUProtos_dot_Data_dot_Color__pb2._COLOR
DESCRIPTOR.message_types_by_name['ClientRecipe'] = _CLIENTRECIPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientRecipe = _reflection.GeneratedProtocolMessageType('ClientRecipe', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTRECIPE,
  __module__ = 'WUProtos.Data.Client.ClientRecipe_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientRecipe)
  ))
_sym_db.RegisterMessage(ClientRecipe)


# @@protoc_insertion_point(module_scope)
