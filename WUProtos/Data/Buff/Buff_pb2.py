# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Buff/Buff.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Buff import BuffDuration_pb2 as WUProtos_dot_Data_dot_Buff_dot_BuffDuration__pb2
from WUProtos.Data.Buff import BuffExclusivityGroup_pb2 as WUProtos_dot_Data_dot_Buff_dot_BuffExclusivityGroup__pb2
from WUProtos.Data import ConditionalModifiers_pb2 as WUProtos_dot_Data_dot_ConditionalModifiers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Buff/Buff.proto',
  package='WUProtos.Data.Buff',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dWUProtos/Data/Buff/Buff.proto\x12\x12WUProtos.Data.Buff\x1a%WUProtos/Data/Buff/BuffDuration.proto\x1a-WUProtos/Data/Buff/BuffExclusivityGroup.proto\x1a(WUProtos/Data/ConditionalModifiers.proto\"\x9f\x03\n\x04\x42uff\x12\n\n\x02id\x18\x01 \x01(\t\x12\x32\n\x08\x64uration\x18\x03 \x01(\x0b\x32 .WUProtos.Data.Buff.BuffDuration\x12\x43\n\x11\x65xclusivity_group\x18\x04 \x01(\x0b\x32(.WUProtos.Data.Buff.BuffExclusivityGroup\x12\x34\n\tbuff_type\x18\x05 \x01(\x0e\x32!.WUProtos.Data.Buff.Buff.BuffType\x12:\n\tmodifiers\x18\x06 \x03(\x0b\x32\'.WUProtos.Data.Buff.Buff.ModifiersEntry\x12\x42\n\x15\x63onditional_modifiers\x18\x07 \x03(\x0b\x32#.WUProtos.Data.ConditionalModifiers\x1a\x30\n\x0eModifiersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"*\n\x08\x42uffType\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04\x42UFF\x10\x01\x12\n\n\x06\x44\x45\x42UFF\x10\x02\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Buff_dot_BuffDuration__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_Buff_dot_BuffExclusivityGroup__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_ConditionalModifiers__pb2.DESCRIPTOR,])



_BUFF_BUFFTYPE = _descriptor.EnumDescriptor(
  name='BuffType',
  full_name='WUProtos.Data.Buff.Buff.BuffType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUFF', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEBUFF', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=555,
  serialized_end=597,
)
_sym_db.RegisterEnumDescriptor(_BUFF_BUFFTYPE)


_BUFF_MODIFIERSENTRY = _descriptor.Descriptor(
  name='ModifiersEntry',
  full_name='WUProtos.Data.Buff.Buff.ModifiersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='WUProtos.Data.Buff.Buff.ModifiersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='WUProtos.Data.Buff.Buff.ModifiersEntry.value', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=505,
  serialized_end=553,
)

_BUFF = _descriptor.Descriptor(
  name='Buff',
  full_name='WUProtos.Data.Buff.Buff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.Buff.Buff.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='WUProtos.Data.Buff.Buff.duration', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exclusivity_group', full_name='WUProtos.Data.Buff.Buff.exclusivity_group', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buff_type', full_name='WUProtos.Data.Buff.Buff.buff_type', index=3,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modifiers', full_name='WUProtos.Data.Buff.Buff.modifiers', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conditional_modifiers', full_name='WUProtos.Data.Buff.Buff.conditional_modifiers', index=5,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BUFF_MODIFIERSENTRY, ],
  enum_types=[
    _BUFF_BUFFTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=597,
)

_BUFF_MODIFIERSENTRY.containing_type = _BUFF
_BUFF.fields_by_name['duration'].message_type = WUProtos_dot_Data_dot_Buff_dot_BuffDuration__pb2._BUFFDURATION
_BUFF.fields_by_name['exclusivity_group'].message_type = WUProtos_dot_Data_dot_Buff_dot_BuffExclusivityGroup__pb2._BUFFEXCLUSIVITYGROUP
_BUFF.fields_by_name['buff_type'].enum_type = _BUFF_BUFFTYPE
_BUFF.fields_by_name['modifiers'].message_type = _BUFF_MODIFIERSENTRY
_BUFF.fields_by_name['conditional_modifiers'].message_type = WUProtos_dot_Data_dot_ConditionalModifiers__pb2._CONDITIONALMODIFIERS
_BUFF_BUFFTYPE.containing_type = _BUFF
DESCRIPTOR.message_types_by_name['Buff'] = _BUFF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Buff = _reflection.GeneratedProtocolMessageType('Buff', (_message.Message,), dict(

  ModifiersEntry = _reflection.GeneratedProtocolMessageType('ModifiersEntry', (_message.Message,), dict(
    DESCRIPTOR = _BUFF_MODIFIERSENTRY,
    __module__ = 'WUProtos.Data.Buff.Buff_pb2'
    # @@protoc_insertion_point(class_scope:WUProtos.Data.Buff.Buff.ModifiersEntry)
    ))
  ,
  DESCRIPTOR = _BUFF,
  __module__ = 'WUProtos.Data.Buff.Buff_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Buff.Buff)
  ))
_sym_db.RegisterMessage(Buff)
_sym_db.RegisterMessage(Buff.ModifiersEntry)


_BUFF_MODIFIERSENTRY._options = None
# @@protoc_insertion_point(module_scope)
