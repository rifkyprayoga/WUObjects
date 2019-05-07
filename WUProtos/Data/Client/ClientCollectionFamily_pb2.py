# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientCollectionFamily.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import Color_pb2 as WUProtos_dot_Data_dot_Color__pb2
from WUProtos.Data import SoundConfig_pb2 as WUProtos_dot_Data_dot_SoundConfig__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientCollectionFamily.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n1WUProtos/Data/Client/ClientCollectionFamily.proto\x12\x14WUProtos.Data.Client\x1a\x19WUProtos/Data/Color.proto\x1a\x1fWUProtos/Data/SoundConfig.proto\"\x9c\x03\n\x16\x43lientCollectionFamily\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x18\n\x10landmark_texture\x18\x06 \x01(\t\x12\x17\n\x0flandmark_prefab\x18\x07 \x01(\t\x12\x1c\n\x14landmark_description\x18\x08 \x01(\t\x12\x12\n\nshow_in_ui\x18\t \x01(\x08\x12\x15\n\rlandmark_icon\x18\x0b \x01(\t\x12#\n\x05\x63olor\x18\x0c \x01(\x0b\x32\x14.WUProtos.Data.Color\x12-\n\x0f\x63olor_highlight\x18\r \x01(\x0b\x32\x14.WUProtos.Data.Color\x12\x14\n\x0ctrace_prefab\x18\x0e \x01(\t\x12\x15\n\rborder_images\x18\x0f \x03(\t\x12\x1d\n\x15\x66\x61mily_runestone_icon\x18\x10 \x01(\t\x12)\n\x05sound\x18\x11 \x01(\x0b\x32\x1a.WUProtos.Data.SoundConfigb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Color__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_SoundConfig__pb2.DESCRIPTOR,])




_CLIENTCOLLECTIONFAMILY = _descriptor.Descriptor(
  name='ClientCollectionFamily',
  full_name='WUProtos.Data.Client.ClientCollectionFamily',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.Client.ClientCollectionFamily.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='WUProtos.Data.Client.ClientCollectionFamily.name', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='WUProtos.Data.Client.ClientCollectionFamily.description', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='WUProtos.Data.Client.ClientCollectionFamily.icon', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='landmark_texture', full_name='WUProtos.Data.Client.ClientCollectionFamily.landmark_texture', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='landmark_prefab', full_name='WUProtos.Data.Client.ClientCollectionFamily.landmark_prefab', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='landmark_description', full_name='WUProtos.Data.Client.ClientCollectionFamily.landmark_description', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_in_ui', full_name='WUProtos.Data.Client.ClientCollectionFamily.show_in_ui', index=7,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='landmark_icon', full_name='WUProtos.Data.Client.ClientCollectionFamily.landmark_icon', index=8,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='WUProtos.Data.Client.ClientCollectionFamily.color', index=9,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color_highlight', full_name='WUProtos.Data.Client.ClientCollectionFamily.color_highlight', index=10,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_prefab', full_name='WUProtos.Data.Client.ClientCollectionFamily.trace_prefab', index=11,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='border_images', full_name='WUProtos.Data.Client.ClientCollectionFamily.border_images', index=12,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='family_runestone_icon', full_name='WUProtos.Data.Client.ClientCollectionFamily.family_runestone_icon', index=13,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sound', full_name='WUProtos.Data.Client.ClientCollectionFamily.sound', index=14,
      number=17, type=11, cpp_type=10, label=1,
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
  serialized_start=136,
  serialized_end=548,
)

_CLIENTCOLLECTIONFAMILY.fields_by_name['color'].message_type = WUProtos_dot_Data_dot_Color__pb2._COLOR
_CLIENTCOLLECTIONFAMILY.fields_by_name['color_highlight'].message_type = WUProtos_dot_Data_dot_Color__pb2._COLOR
_CLIENTCOLLECTIONFAMILY.fields_by_name['sound'].message_type = WUProtos_dot_Data_dot_SoundConfig__pb2._SOUNDCONFIG
DESCRIPTOR.message_types_by_name['ClientCollectionFamily'] = _CLIENTCOLLECTIONFAMILY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientCollectionFamily = _reflection.GeneratedProtocolMessageType('ClientCollectionFamily', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTCOLLECTIONFAMILY,
  __module__ = 'WUProtos.Data.Client.ClientCollectionFamily_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientCollectionFamily)
  ))
_sym_db.RegisterMessage(ClientCollectionFamily)


# @@protoc_insertion_point(module_scope)
