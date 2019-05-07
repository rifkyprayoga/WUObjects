# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Player/PlayerProfile.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import EmailOpts_pb2 as WUProtos_dot_Data_dot_EmailOpts__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Player/PlayerProfile.proto',
  package='WUProtos.Data.Player',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(WUProtos/Data/Player/PlayerProfile.proto\x12\x14WUProtos.Data.Player\x1a\x1dWUProtos/Data/EmailOpts.proto\"\xb4\n\n\rPlayerProfile\x12\x10\n\x08nickname\x18\x01 \x01(\t\x12\r\n\x05level\x18\x02 \x01(\x05\x12\x1a\n\x12\x64istance_walked_km\x18\x03 \x01(\x02\x12\x0e\n\x06max_hp\x18\x04 \x01(\x03\x12\x14\n\x0c\x61ttack_power\x18\x05 \x01(\x03\x12\x16\n\x0eplayer_team_id\x18\x06 \x01(\t\x12\x15\n\rprofession_id\x18\x07 \x01(\t\x12\x10\n\x08title_id\x18\x08 \x01(\t\x12\x1a\n\x12unlocked_title_ids\x18\t \x03(\t\x12\x10\n\x08theme_id\x18\n \x01(\t\x12\x1a\n\x12unlocked_theme_ids\x18\x0b \x03(\t\x12\x10\n\x08house_id\x18\x0c \x01(\t\x12=\n\x04wand\x18\r \x01(\x0b\x32/.WUProtos.Data.Player.PlayerProfile.WandOptions\x12\x1a\n\x12\x66\x61vorite_badge_ids\x18\x0e \x03(\t\x12\x1a\n\x12unlocked_badge_ids\x18\x0f \x03(\t\x12\x1a\n\x12\x66\x61vorite_title_ids\x18\x10 \x03(\t\x12\x12\n\nfirst_name\x18\x11 \x01(\t\x12\x11\n\tlast_name\x18\x12 \x01(\t\x12!\n\x19profile_creation_location\x18\x13 \x01(\t\x12!\n\x19unlocked_selfie_asset_ids\x18\x14 \x03(\t\x12!\n\x19total_swish_success_spell\x18\x15 \x01(\x03\x12*\n\"discovered_potions_master_note_ids\x18\x16 \x03(\t\x12h\n\x1cmaster_note_discovery_status\x18\x17 \x03(\x0b\x32\x42.WUProtos.Data.Player.PlayerProfile.MasterNoteDiscoveryStatusEntry\x12R\n\x10swish_spellcasts\x18\x18 \x03(\x0b\x32\x38.WUProtos.Data.Player.PlayerProfile.SwishSpellcastsEntry\x12Y\n\x14store_pack_purchased\x18\x19 \x03(\x0b\x32;.WUProtos.Data.Player.PlayerProfile.StorePackPurchasedEntry\x12,\n\nemail_opts\x18\x1a \x01(\x0b\x32\x18.WUProtos.Data.EmailOpts\x12\x1b\n\x13lifetime_inn_looted\x18\x1b \x01(\x03\x12\"\n\x1alifetime_greenhouse_looted\x18\x1c \x01(\x03\x12\"\n\x1alifetime_map_encounter_won\x18\x1d \x01(\x03\x12\x17\n\x0flifetime_wc_won\x18\x1e \x01(\x03\x1a@\n\x1eMasterNoteDiscoveryStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x36\n\x14SwishSpellcastsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x39\n\x17StorePackPurchasedEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1aZ\n\x0bWandOptions\x12\x0f\n\x07\x63ore_id\x18\x01 \x01(\t\x12\x0f\n\x07wood_id\x18\x02 \x01(\t\x12\x16\n\x0e\x66lexibility_id\x18\x03 \x01(\t\x12\x11\n\tlength_id\x18\x04 \x01(\tb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_EmailOpts__pb2.DESCRIPTOR,])




_PLAYERPROFILE_MASTERNOTEDISCOVERYSTATUSENTRY = _descriptor.Descriptor(
  name='MasterNoteDiscoveryStatusEntry',
  full_name='WUProtos.Data.Player.PlayerProfile.MasterNoteDiscoveryStatusEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='WUProtos.Data.Player.PlayerProfile.MasterNoteDiscoveryStatusEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='WUProtos.Data.Player.PlayerProfile.MasterNoteDiscoveryStatusEntry.value', index=1,
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
  serialized_start=1159,
  serialized_end=1223,
)

_PLAYERPROFILE_SWISHSPELLCASTSENTRY = _descriptor.Descriptor(
  name='SwishSpellcastsEntry',
  full_name='WUProtos.Data.Player.PlayerProfile.SwishSpellcastsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='WUProtos.Data.Player.PlayerProfile.SwishSpellcastsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='WUProtos.Data.Player.PlayerProfile.SwishSpellcastsEntry.value', index=1,
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
  serialized_start=1225,
  serialized_end=1279,
)

_PLAYERPROFILE_STOREPACKPURCHASEDENTRY = _descriptor.Descriptor(
  name='StorePackPurchasedEntry',
  full_name='WUProtos.Data.Player.PlayerProfile.StorePackPurchasedEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='WUProtos.Data.Player.PlayerProfile.StorePackPurchasedEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='WUProtos.Data.Player.PlayerProfile.StorePackPurchasedEntry.value', index=1,
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
  serialized_start=1281,
  serialized_end=1338,
)

_PLAYERPROFILE_WANDOPTIONS = _descriptor.Descriptor(
  name='WandOptions',
  full_name='WUProtos.Data.Player.PlayerProfile.WandOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='core_id', full_name='WUProtos.Data.Player.PlayerProfile.WandOptions.core_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wood_id', full_name='WUProtos.Data.Player.PlayerProfile.WandOptions.wood_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flexibility_id', full_name='WUProtos.Data.Player.PlayerProfile.WandOptions.flexibility_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length_id', full_name='WUProtos.Data.Player.PlayerProfile.WandOptions.length_id', index=3,
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
  serialized_start=1340,
  serialized_end=1430,
)

_PLAYERPROFILE = _descriptor.Descriptor(
  name='PlayerProfile',
  full_name='WUProtos.Data.Player.PlayerProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nickname', full_name='WUProtos.Data.Player.PlayerProfile.nickname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='WUProtos.Data.Player.PlayerProfile.level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance_walked_km', full_name='WUProtos.Data.Player.PlayerProfile.distance_walked_km', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_hp', full_name='WUProtos.Data.Player.PlayerProfile.max_hp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attack_power', full_name='WUProtos.Data.Player.PlayerProfile.attack_power', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_team_id', full_name='WUProtos.Data.Player.PlayerProfile.player_team_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profession_id', full_name='WUProtos.Data.Player.PlayerProfile.profession_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title_id', full_name='WUProtos.Data.Player.PlayerProfile.title_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unlocked_title_ids', full_name='WUProtos.Data.Player.PlayerProfile.unlocked_title_ids', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='theme_id', full_name='WUProtos.Data.Player.PlayerProfile.theme_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unlocked_theme_ids', full_name='WUProtos.Data.Player.PlayerProfile.unlocked_theme_ids', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='house_id', full_name='WUProtos.Data.Player.PlayerProfile.house_id', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wand', full_name='WUProtos.Data.Player.PlayerProfile.wand', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='favorite_badge_ids', full_name='WUProtos.Data.Player.PlayerProfile.favorite_badge_ids', index=13,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unlocked_badge_ids', full_name='WUProtos.Data.Player.PlayerProfile.unlocked_badge_ids', index=14,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='favorite_title_ids', full_name='WUProtos.Data.Player.PlayerProfile.favorite_title_ids', index=15,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='WUProtos.Data.Player.PlayerProfile.first_name', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='WUProtos.Data.Player.PlayerProfile.last_name', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profile_creation_location', full_name='WUProtos.Data.Player.PlayerProfile.profile_creation_location', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unlocked_selfie_asset_ids', full_name='WUProtos.Data.Player.PlayerProfile.unlocked_selfie_asset_ids', index=19,
      number=20, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_swish_success_spell', full_name='WUProtos.Data.Player.PlayerProfile.total_swish_success_spell', index=20,
      number=21, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discovered_potions_master_note_ids', full_name='WUProtos.Data.Player.PlayerProfile.discovered_potions_master_note_ids', index=21,
      number=22, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='master_note_discovery_status', full_name='WUProtos.Data.Player.PlayerProfile.master_note_discovery_status', index=22,
      number=23, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='swish_spellcasts', full_name='WUProtos.Data.Player.PlayerProfile.swish_spellcasts', index=23,
      number=24, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='store_pack_purchased', full_name='WUProtos.Data.Player.PlayerProfile.store_pack_purchased', index=24,
      number=25, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email_opts', full_name='WUProtos.Data.Player.PlayerProfile.email_opts', index=25,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lifetime_inn_looted', full_name='WUProtos.Data.Player.PlayerProfile.lifetime_inn_looted', index=26,
      number=27, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lifetime_greenhouse_looted', full_name='WUProtos.Data.Player.PlayerProfile.lifetime_greenhouse_looted', index=27,
      number=28, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lifetime_map_encounter_won', full_name='WUProtos.Data.Player.PlayerProfile.lifetime_map_encounter_won', index=28,
      number=29, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lifetime_wc_won', full_name='WUProtos.Data.Player.PlayerProfile.lifetime_wc_won', index=29,
      number=30, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PLAYERPROFILE_MASTERNOTEDISCOVERYSTATUSENTRY, _PLAYERPROFILE_SWISHSPELLCASTSENTRY, _PLAYERPROFILE_STOREPACKPURCHASEDENTRY, _PLAYERPROFILE_WANDOPTIONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=1430,
)

_PLAYERPROFILE_MASTERNOTEDISCOVERYSTATUSENTRY.containing_type = _PLAYERPROFILE
_PLAYERPROFILE_SWISHSPELLCASTSENTRY.containing_type = _PLAYERPROFILE
_PLAYERPROFILE_STOREPACKPURCHASEDENTRY.containing_type = _PLAYERPROFILE
_PLAYERPROFILE_WANDOPTIONS.containing_type = _PLAYERPROFILE
_PLAYERPROFILE.fields_by_name['wand'].message_type = _PLAYERPROFILE_WANDOPTIONS
_PLAYERPROFILE.fields_by_name['master_note_discovery_status'].message_type = _PLAYERPROFILE_MASTERNOTEDISCOVERYSTATUSENTRY
_PLAYERPROFILE.fields_by_name['swish_spellcasts'].message_type = _PLAYERPROFILE_SWISHSPELLCASTSENTRY
_PLAYERPROFILE.fields_by_name['store_pack_purchased'].message_type = _PLAYERPROFILE_STOREPACKPURCHASEDENTRY
_PLAYERPROFILE.fields_by_name['email_opts'].message_type = WUProtos_dot_Data_dot_EmailOpts__pb2._EMAILOPTS
DESCRIPTOR.message_types_by_name['PlayerProfile'] = _PLAYERPROFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerProfile = _reflection.GeneratedProtocolMessageType('PlayerProfile', (_message.Message,), dict(

  MasterNoteDiscoveryStatusEntry = _reflection.GeneratedProtocolMessageType('MasterNoteDiscoveryStatusEntry', (_message.Message,), dict(
    DESCRIPTOR = _PLAYERPROFILE_MASTERNOTEDISCOVERYSTATUSENTRY,
    __module__ = 'WUProtos.Data.Player.PlayerProfile_pb2'
    # @@protoc_insertion_point(class_scope:WUProtos.Data.Player.PlayerProfile.MasterNoteDiscoveryStatusEntry)
    ))
  ,

  SwishSpellcastsEntry = _reflection.GeneratedProtocolMessageType('SwishSpellcastsEntry', (_message.Message,), dict(
    DESCRIPTOR = _PLAYERPROFILE_SWISHSPELLCASTSENTRY,
    __module__ = 'WUProtos.Data.Player.PlayerProfile_pb2'
    # @@protoc_insertion_point(class_scope:WUProtos.Data.Player.PlayerProfile.SwishSpellcastsEntry)
    ))
  ,

  StorePackPurchasedEntry = _reflection.GeneratedProtocolMessageType('StorePackPurchasedEntry', (_message.Message,), dict(
    DESCRIPTOR = _PLAYERPROFILE_STOREPACKPURCHASEDENTRY,
    __module__ = 'WUProtos.Data.Player.PlayerProfile_pb2'
    # @@protoc_insertion_point(class_scope:WUProtos.Data.Player.PlayerProfile.StorePackPurchasedEntry)
    ))
  ,

  WandOptions = _reflection.GeneratedProtocolMessageType('WandOptions', (_message.Message,), dict(
    DESCRIPTOR = _PLAYERPROFILE_WANDOPTIONS,
    __module__ = 'WUProtos.Data.Player.PlayerProfile_pb2'
    # @@protoc_insertion_point(class_scope:WUProtos.Data.Player.PlayerProfile.WandOptions)
    ))
  ,
  DESCRIPTOR = _PLAYERPROFILE,
  __module__ = 'WUProtos.Data.Player.PlayerProfile_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Player.PlayerProfile)
  ))
_sym_db.RegisterMessage(PlayerProfile)
_sym_db.RegisterMessage(PlayerProfile.MasterNoteDiscoveryStatusEntry)
_sym_db.RegisterMessage(PlayerProfile.SwishSpellcastsEntry)
_sym_db.RegisterMessage(PlayerProfile.StorePackPurchasedEntry)
_sym_db.RegisterMessage(PlayerProfile.WandOptions)


_PLAYERPROFILE_MASTERNOTEDISCOVERYSTATUSENTRY._options = None
_PLAYERPROFILE_SWISHSPELLCASTSENTRY._options = None
_PLAYERPROFILE_STOREPACKPURCHASEDENTRY._options = None
# @@protoc_insertion_point(module_scope)
