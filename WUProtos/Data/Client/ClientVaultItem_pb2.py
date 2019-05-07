# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientVaultItem.proto

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
  name='WUProtos/Data/Client/ClientVaultItem.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n*WUProtos/Data/Client/ClientVaultItem.proto\x12\x14WUProtos.Data.Client\x1a\x19WUProtos/Data/Color.proto\x1a\x1fWUProtos/Data/SoundConfig.proto\"\xf9\x02\n\x0f\x43lientVaultItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12\x0e\n\x06prefab\x18\x04 \x01(\t\x12\x0e\n\x06rarity\x18\x05 \x01(\x03\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x1f\n\x17show_in_vault_item_menu\x18\x08 \x01(\x08\x12\x11\n\tdeletable\x18\t \x01(\x08\x12\x1c\n\x14show_in_rewards_flow\x18\n \x01(\x08\x12#\n\x05\x63olor\x18\x0b \x01(\x0b\x32\x14.WUProtos.Data.Color\x12\x12\n\nbackground\x18\x0c \x01(\t\x12\x10\n\x08ordering\x18\r \x01(\x05\x12\x30\n\x0creward_sound\x18\x0e \x01(\x0b\x32\x1a.WUProtos.Data.SoundConfig\x12\x1d\n\x15reward_sound_priority\x18\x0f \x01(\x05\x12\x1b\n\x13spine_animated_icon\x18\x10 \x01(\tb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Color__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_SoundConfig__pb2.DESCRIPTOR,])




_CLIENTVAULTITEM = _descriptor.Descriptor(
  name='ClientVaultItem',
  full_name='WUProtos.Data.Client.ClientVaultItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.Client.ClientVaultItem.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='WUProtos.Data.Client.ClientVaultItem.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='WUProtos.Data.Client.ClientVaultItem.icon', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefab', full_name='WUProtos.Data.Client.ClientVaultItem.prefab', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rarity', full_name='WUProtos.Data.Client.ClientVaultItem.rarity', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='WUProtos.Data.Client.ClientVaultItem.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_in_vault_item_menu', full_name='WUProtos.Data.Client.ClientVaultItem.show_in_vault_item_menu', index=6,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deletable', full_name='WUProtos.Data.Client.ClientVaultItem.deletable', index=7,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_in_rewards_flow', full_name='WUProtos.Data.Client.ClientVaultItem.show_in_rewards_flow', index=8,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='WUProtos.Data.Client.ClientVaultItem.color', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='background', full_name='WUProtos.Data.Client.ClientVaultItem.background', index=10,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ordering', full_name='WUProtos.Data.Client.ClientVaultItem.ordering', index=11,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward_sound', full_name='WUProtos.Data.Client.ClientVaultItem.reward_sound', index=12,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward_sound_priority', full_name='WUProtos.Data.Client.ClientVaultItem.reward_sound_priority', index=13,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spine_animated_icon', full_name='WUProtos.Data.Client.ClientVaultItem.spine_animated_icon', index=14,
      number=16, type=9, cpp_type=9, label=1,
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
  serialized_start=129,
  serialized_end=506,
)

_CLIENTVAULTITEM.fields_by_name['color'].message_type = WUProtos_dot_Data_dot_Color__pb2._COLOR
_CLIENTVAULTITEM.fields_by_name['reward_sound'].message_type = WUProtos_dot_Data_dot_SoundConfig__pb2._SOUNDCONFIG
DESCRIPTOR.message_types_by_name['ClientVaultItem'] = _CLIENTVAULTITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientVaultItem = _reflection.GeneratedProtocolMessageType('ClientVaultItem', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTVAULTITEM,
  __module__ = 'WUProtos.Data.Client.ClientVaultItem_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientVaultItem)
  ))
_sym_db.RegisterMessage(ClientVaultItem)


# @@protoc_insertion_point(module_scope)
