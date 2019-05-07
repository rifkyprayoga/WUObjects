# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientSpell.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientSpell.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&WUProtos/Data/Client/ClientSpell.proto\x12\x14WUProtos.Data.Client\"\xcf\x04\n\x0b\x43lientSpell\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x18\n\x10\x63harge_up_effect\x18\x03 \x03(\t\x12\x43\n\ttimelines\x18\x04 \x03(\x0b\x32\x30.WUProtos.Data.Client.ClientSpell.TimelinesEntry\x12J\n\rcritical_hits\x18\x05 \x03(\x0b\x32\x33.WUProtos.Data.Client.ClientSpell.CriticalHitsEntry\x12\x0f\n\x07pattern\x18\x06 \x01(\t\x12\x13\n\x0bglyph_image\x18\x07 \x01(\t\x12!\n\x19protego_player_succeed_tl\x18\x08 \x01(\t\x12 \n\x18protego_player_failed_tl\x18\t \x01(\t\x12\'\n\x1fprotego_player_succeed_intro_tl\x18\n \x01(\t\x12\x18\n\x10\x65nd_burst_effect\x18\x0b \x01(\t\x12\x12\n\nrng_vfx_tl\x18\x0c \x01(\t\x12\x19\n\x11spell_rng_loop_tl\x18\r \x01(\t\x12\x1c\n\x14spell_rng_succeed_tl\x18\x0e \x01(\t\x12\x19\n\x11spell_rng_fail_tl\x18\x0f \x01(\t\x1a\x30\n\x0eTimelinesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x33\n\x11\x43riticalHitsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x62\x06proto3')
)




_CLIENTSPELL_TIMELINESENTRY = _descriptor.Descriptor(
  name='TimelinesEntry',
  full_name='WUProtos.Data.Client.ClientSpell.TimelinesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='WUProtos.Data.Client.ClientSpell.TimelinesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='WUProtos.Data.Client.ClientSpell.TimelinesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=555,
  serialized_end=603,
)

_CLIENTSPELL_CRITICALHITSENTRY = _descriptor.Descriptor(
  name='CriticalHitsEntry',
  full_name='WUProtos.Data.Client.ClientSpell.CriticalHitsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='WUProtos.Data.Client.ClientSpell.CriticalHitsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='WUProtos.Data.Client.ClientSpell.CriticalHitsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=605,
  serialized_end=656,
)

_CLIENTSPELL = _descriptor.Descriptor(
  name='ClientSpell',
  full_name='WUProtos.Data.Client.ClientSpell',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.Client.ClientSpell.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='WUProtos.Data.Client.ClientSpell.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='charge_up_effect', full_name='WUProtos.Data.Client.ClientSpell.charge_up_effect', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timelines', full_name='WUProtos.Data.Client.ClientSpell.timelines', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='critical_hits', full_name='WUProtos.Data.Client.ClientSpell.critical_hits', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pattern', full_name='WUProtos.Data.Client.ClientSpell.pattern', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='glyph_image', full_name='WUProtos.Data.Client.ClientSpell.glyph_image', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protego_player_succeed_tl', full_name='WUProtos.Data.Client.ClientSpell.protego_player_succeed_tl', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protego_player_failed_tl', full_name='WUProtos.Data.Client.ClientSpell.protego_player_failed_tl', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protego_player_succeed_intro_tl', full_name='WUProtos.Data.Client.ClientSpell.protego_player_succeed_intro_tl', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_burst_effect', full_name='WUProtos.Data.Client.ClientSpell.end_burst_effect', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rng_vfx_tl', full_name='WUProtos.Data.Client.ClientSpell.rng_vfx_tl', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spell_rng_loop_tl', full_name='WUProtos.Data.Client.ClientSpell.spell_rng_loop_tl', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spell_rng_succeed_tl', full_name='WUProtos.Data.Client.ClientSpell.spell_rng_succeed_tl', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spell_rng_fail_tl', full_name='WUProtos.Data.Client.ClientSpell.spell_rng_fail_tl', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CLIENTSPELL_TIMELINESENTRY, _CLIENTSPELL_CRITICALHITSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=656,
)

_CLIENTSPELL_TIMELINESENTRY.containing_type = _CLIENTSPELL
_CLIENTSPELL_CRITICALHITSENTRY.containing_type = _CLIENTSPELL
_CLIENTSPELL.fields_by_name['timelines'].message_type = _CLIENTSPELL_TIMELINESENTRY
_CLIENTSPELL.fields_by_name['critical_hits'].message_type = _CLIENTSPELL_CRITICALHITSENTRY
DESCRIPTOR.message_types_by_name['ClientSpell'] = _CLIENTSPELL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientSpell = _reflection.GeneratedProtocolMessageType('ClientSpell', (_message.Message,), dict(

  TimelinesEntry = _reflection.GeneratedProtocolMessageType('TimelinesEntry', (_message.Message,), dict(
    DESCRIPTOR = _CLIENTSPELL_TIMELINESENTRY,
    __module__ = 'WUProtos.Data.Client.ClientSpell_pb2'
    # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientSpell.TimelinesEntry)
    ))
  ,

  CriticalHitsEntry = _reflection.GeneratedProtocolMessageType('CriticalHitsEntry', (_message.Message,), dict(
    DESCRIPTOR = _CLIENTSPELL_CRITICALHITSENTRY,
    __module__ = 'WUProtos.Data.Client.ClientSpell_pb2'
    # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientSpell.CriticalHitsEntry)
    ))
  ,
  DESCRIPTOR = _CLIENTSPELL,
  __module__ = 'WUProtos.Data.Client.ClientSpell_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientSpell)
  ))
_sym_db.RegisterMessage(ClientSpell)
_sym_db.RegisterMessage(ClientSpell.TimelinesEntry)
_sym_db.RegisterMessage(ClientSpell.CriticalHitsEntry)


_CLIENTSPELL_TIMELINESENTRY._options = None
_CLIENTSPELL_CRITICALHITSENTRY._options = None
# @@protoc_insertion_point(module_scope)
