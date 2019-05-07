# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/StorePackConfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Enums import StorePackConfigSize_pb2 as WUProtos_dot_Enums_dot_StorePackConfigSize__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/StorePackConfig.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#WUProtos/Data/StorePackConfig.proto\x12\rWUProtos.Data\x1a(WUProtos/Enums/StorePackConfigSize.proto\"\xd5\x03\n\x0fStorePackConfig\x12\x10\n\x08priority\x18\x01 \x01(\x05\x12\x16\n\x0esubcategory_id\x18\x02 \x01(\t\x12\x11\n\ticon_path\x18\x03 \x01(\t\x12\x1c\n\x14show_quantity_banner\x18\x04 \x01(\x08\x12\x19\n\x11quantity_override\x18\x05 \x01(\t\x12\x13\n\x0bprefab_path\x18\x06 \x01(\t\x12\x16\n\x0emarketing_text\x18\x07 \x01(\t\x12\x18\n\x10\x64\x65scription_text\x18\x08 \x01(\t\x12\x12\n\nshow_badge\x18\t \x01(\x08\x12\x13\n\x0b\x62onus_value\x18\n \x01(\x05\x12\x11\n\trarity_id\x18\x0b \x01(\t\x12\x36\n\tpack_size\x18\x0c \x01(\x0e\x32#.WUProtos.Enums.StorePackConfigSize\x12\x13\n\x0bshow_in_hud\x18\r \x01(\x08\x12\x14\n\x0chud_priority\x18\x0e \x01(\x05\x12\x15\n\rhud_icon_path\x18\x0f \x01(\t\x12\x12\n\nicon2_path\x18\x10 \x01(\t\x12\x1c\n\x14popup_image_override\x18\x11 \x01(\t\x12\x1d\n\x15hide_pack_on_sold_out\x18\x12 \x01(\x08\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Enums_dot_StorePackConfigSize__pb2.DESCRIPTOR,])




_STOREPACKCONFIG = _descriptor.Descriptor(
  name='StorePackConfig',
  full_name='WUProtos.Data.StorePackConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='priority', full_name='WUProtos.Data.StorePackConfig.priority', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subcategory_id', full_name='WUProtos.Data.StorePackConfig.subcategory_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_path', full_name='WUProtos.Data.StorePackConfig.icon_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_quantity_banner', full_name='WUProtos.Data.StorePackConfig.show_quantity_banner', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity_override', full_name='WUProtos.Data.StorePackConfig.quantity_override', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefab_path', full_name='WUProtos.Data.StorePackConfig.prefab_path', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='marketing_text', full_name='WUProtos.Data.StorePackConfig.marketing_text', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description_text', full_name='WUProtos.Data.StorePackConfig.description_text', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_badge', full_name='WUProtos.Data.StorePackConfig.show_badge', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bonus_value', full_name='WUProtos.Data.StorePackConfig.bonus_value', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rarity_id', full_name='WUProtos.Data.StorePackConfig.rarity_id', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pack_size', full_name='WUProtos.Data.StorePackConfig.pack_size', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_in_hud', full_name='WUProtos.Data.StorePackConfig.show_in_hud', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hud_priority', full_name='WUProtos.Data.StorePackConfig.hud_priority', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hud_icon_path', full_name='WUProtos.Data.StorePackConfig.hud_icon_path', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon2_path', full_name='WUProtos.Data.StorePackConfig.icon2_path', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='popup_image_override', full_name='WUProtos.Data.StorePackConfig.popup_image_override', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hide_pack_on_sold_out', full_name='WUProtos.Data.StorePackConfig.hide_pack_on_sold_out', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=97,
  serialized_end=566,
)

_STOREPACKCONFIG.fields_by_name['pack_size'].enum_type = WUProtos_dot_Enums_dot_StorePackConfigSize__pb2._STOREPACKCONFIGSIZE
DESCRIPTOR.message_types_by_name['StorePackConfig'] = _STOREPACKCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StorePackConfig = _reflection.GeneratedProtocolMessageType('StorePackConfig', (_message.Message,), dict(
  DESCRIPTOR = _STOREPACKCONFIG,
  __module__ = 'WUProtos.Data.StorePackConfig_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.StorePackConfig)
  ))
_sym_db.RegisterMessage(StorePackConfig)


# @@protoc_insertion_point(module_scope)
