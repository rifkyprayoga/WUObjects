# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/data/client/client_map_poi.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wuprotos.enums import poi_accessibility_pb2 as wuprotos_dot_enums_dot_poi__accessibility__pb2
from wuprotos.data.client import client_dark_detector_amplifier_pb2 as wuprotos_dot_data_dot_client_dot_client__dark__detector__amplifier__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/data/client/client_map_poi.proto',
  package='wuprotos.data.client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n)wuprotos/data/client/client_map_poi.proto\x12\x14wuprotos.data.client\x1a&wuprotos/enums/poi_accessibility.proto\x1a\x39wuprotos/data/client/client_dark_detector_amplifier.proto\"\xa3\x0b\n\x0c\x43lientMapPoi\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08latitude\x18\x03 \x01(\x01\x12\x11\n\tlongitude\x18\x04 \x01(\x01\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x46\n\x07outpost\x18\x06 \x01(\x0b\x32\x33.wuprotos.data.client.ClientMapPoi.ClientMapOutpostH\x00\x12H\n\x08\x66ortress\x18\x07 \x01(\x0b\x32\x34.wuprotos.data.client.ClientMapPoi.ClientMapFortressH\x00\x12L\n\ngreenhouse\x18\x08 \x01(\x0b\x32\x36.wuprotos.data.client.ClientMapPoi.ClientMapGreenhouseH\x00\x12;\n\x11poi_accessibility\x18\t \x01(\x0e\x32 .wuprotos.enums.PoiAccessibility\x12;\n\x07partner\x18\n \x01(\x0b\x32*.wuprotos.data.client.ClientMapPoi.Partner\x12\x1d\n\x15show_passcode_scanner\x18\x0b \x01(\x08\x1a\x9f\x01\n\x10\x43lientMapOutpost\x12\x16\n\x0enext_loot_time\x18\x01 \x01(\x03\x12R\n\x17\x64\x61rk_detector_amplifier\x18\x02 \x01(\x0b\x32\x31.wuprotos.data.client.ClientDarkDetectorAmplifier\x12\x1f\n\x17outpost_template_gmt_id\x18\x03 \x01(\t\x1a\xde\x02\n\x13\x43lientMapGreenhouse\x12\x16\n\x0enext_loot_time\x18\x01 \x01(\x03\x12\"\n\x1agreenhouse_template_gmt_id\x18\x02 \x01(\t\x12[\n\nnormal_pot\x18\x03 \x03(\x0b\x32G.wuprotos.data.client.ClientMapPoi.ClientMapGreenhouse.ClientPotSummary\x12[\n\nrental_pot\x18\x04 \x03(\x0b\x32G.wuprotos.data.client.ClientMapPoi.ClientMapGreenhouse.ClientPotSummary\x1aQ\n\x10\x43lientPotSummary\x12\x19\n\x11ingredient_gmt_id\x18\x01 \x01(\t\x12\"\n\x1agrowing_completion_time_ms\x18\x02 \x01(\x03\x1a\xa8\x01\n\x11\x43lientMapFortress\x12 \n\x18\x66ortress_template_gmt_id\x18\x01 \x01(\t\x12\x16\n\x0eowning_team_id\x18\x02 \x01(\t\x12\x17\n\x0f\x65lectoral_votes\x18\x03 \x01(\x03\x12\x11\n\tseason_id\x18\x04 \x01(\t\x12\x11\n\tregion_id\x18\x05 \x01(\t\x12\x1a\n\x12wc_active_until_ms\x18\x06 \x01(\x03\x1a\x8f\x02\n\x07Partner\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\npopup_desc\x18\x02 \x01(\t\x12\x11\n\thyperlink\x18\x03 \x01(\t\x12L\n\x0cpartner_type\x18\x04 \x01(\x0e\x32\x36.wuprotos.data.client.ClientMapPoi.Partner.PartnerType\"\x82\x01\n\x0bPartnerType\x12\x1c\n\x18PARTNER_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14PARTNER_TYPE_REGULAR\x10\x01\x12\x1a\n\x16PARTNER_TYPE_FRANCHISE\x10\x02\x12\x1f\n\x1bPARTNER_TYPE_PSEUDO_ORGANIC\x10\x03\x42\x06\n\x04Typeb\x06proto3')
  ,
  dependencies=[wuprotos_dot_enums_dot_poi__accessibility__pb2.DESCRIPTOR,wuprotos_dot_data_dot_client_dot_client__dark__detector__amplifier__pb2.DESCRIPTOR,])



_CLIENTMAPPOI_PARTNER_PARTNERTYPE = _descriptor.EnumDescriptor(
  name='PartnerType',
  full_name='wuprotos.data.client.ClientMapPoi.Partner.PartnerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PARTNER_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARTNER_TYPE_REGULAR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARTNER_TYPE_FRANCHISE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARTNER_TYPE_PSEUDO_ORGANIC', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1472,
  serialized_end=1602,
)
_sym_db.RegisterEnumDescriptor(_CLIENTMAPPOI_PARTNER_PARTNERTYPE)


_CLIENTMAPPOI_CLIENTMAPOUTPOST = _descriptor.Descriptor(
  name='ClientMapOutpost',
  full_name='wuprotos.data.client.ClientMapPoi.ClientMapOutpost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_loot_time', full_name='wuprotos.data.client.ClientMapPoi.ClientMapOutpost.next_loot_time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dark_detector_amplifier', full_name='wuprotos.data.client.ClientMapPoi.ClientMapOutpost.dark_detector_amplifier', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outpost_template_gmt_id', full_name='wuprotos.data.client.ClientMapPoi.ClientMapOutpost.outpost_template_gmt_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=645,
  serialized_end=804,
)

_CLIENTMAPPOI_CLIENTMAPGREENHOUSE_CLIENTPOTSUMMARY = _descriptor.Descriptor(
  name='ClientPotSummary',
  full_name='wuprotos.data.client.ClientMapPoi.ClientMapGreenhouse.ClientPotSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ingredient_gmt_id', full_name='wuprotos.data.client.ClientMapPoi.ClientMapGreenhouse.ClientPotSummary.ingredient_gmt_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='growing_completion_time_ms', full_name='wuprotos.data.client.ClientMapPoi.ClientMapGreenhouse.ClientPotSummary.growing_completion_time_ms', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1076,
  serialized_end=1157,
)

_CLIENTMAPPOI_CLIENTMAPGREENHOUSE = _descriptor.Descriptor(
  name='ClientMapGreenhouse',
  full_name='wuprotos.data.client.ClientMapPoi.ClientMapGreenhouse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_loot_time', full_name='wuprotos.data.client.ClientMapPoi.ClientMapGreenhouse.next_loot_time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='greenhouse_template_gmt_id', full_name='wuprotos.data.client.ClientMapPoi.ClientMapGreenhouse.greenhouse_template_gmt_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='normal_pot', full_name='wuprotos.data.client.ClientMapPoi.ClientMapGreenhouse.normal_pot', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rental_pot', full_name='wuprotos.data.client.ClientMapPoi.ClientMapGreenhouse.rental_pot', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CLIENTMAPPOI_CLIENTMAPGREENHOUSE_CLIENTPOTSUMMARY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=807,
  serialized_end=1157,
)

_CLIENTMAPPOI_CLIENTMAPFORTRESS = _descriptor.Descriptor(
  name='ClientMapFortress',
  full_name='wuprotos.data.client.ClientMapPoi.ClientMapFortress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fortress_template_gmt_id', full_name='wuprotos.data.client.ClientMapPoi.ClientMapFortress.fortress_template_gmt_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owning_team_id', full_name='wuprotos.data.client.ClientMapPoi.ClientMapFortress.owning_team_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='electoral_votes', full_name='wuprotos.data.client.ClientMapPoi.ClientMapFortress.electoral_votes', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='season_id', full_name='wuprotos.data.client.ClientMapPoi.ClientMapFortress.season_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='region_id', full_name='wuprotos.data.client.ClientMapPoi.ClientMapFortress.region_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wc_active_until_ms', full_name='wuprotos.data.client.ClientMapPoi.ClientMapFortress.wc_active_until_ms', index=5,
      number=6, type=3, cpp_type=2, label=1,
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
  serialized_start=1160,
  serialized_end=1328,
)

_CLIENTMAPPOI_PARTNER = _descriptor.Descriptor(
  name='Partner',
  full_name='wuprotos.data.client.ClientMapPoi.Partner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='wuprotos.data.client.ClientMapPoi.Partner.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='popup_desc', full_name='wuprotos.data.client.ClientMapPoi.Partner.popup_desc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hyperlink', full_name='wuprotos.data.client.ClientMapPoi.Partner.hyperlink', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner_type', full_name='wuprotos.data.client.ClientMapPoi.Partner.partner_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLIENTMAPPOI_PARTNER_PARTNERTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1331,
  serialized_end=1602,
)

_CLIENTMAPPOI = _descriptor.Descriptor(
  name='ClientMapPoi',
  full_name='wuprotos.data.client.ClientMapPoi',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='wuprotos.data.client.ClientMapPoi.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='wuprotos.data.client.ClientMapPoi.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='wuprotos.data.client.ClientMapPoi.latitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='wuprotos.data.client.ClientMapPoi.longitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='wuprotos.data.client.ClientMapPoi.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outpost', full_name='wuprotos.data.client.ClientMapPoi.outpost', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fortress', full_name='wuprotos.data.client.ClientMapPoi.fortress', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='greenhouse', full_name='wuprotos.data.client.ClientMapPoi.greenhouse', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poi_accessibility', full_name='wuprotos.data.client.ClientMapPoi.poi_accessibility', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner', full_name='wuprotos.data.client.ClientMapPoi.partner', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_passcode_scanner', full_name='wuprotos.data.client.ClientMapPoi.show_passcode_scanner', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CLIENTMAPPOI_CLIENTMAPOUTPOST, _CLIENTMAPPOI_CLIENTMAPGREENHOUSE, _CLIENTMAPPOI_CLIENTMAPFORTRESS, _CLIENTMAPPOI_PARTNER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='wuprotos.data.client.ClientMapPoi.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=167,
  serialized_end=1610,
)

_CLIENTMAPPOI_CLIENTMAPOUTPOST.fields_by_name['dark_detector_amplifier'].message_type = wuprotos_dot_data_dot_client_dot_client__dark__detector__amplifier__pb2._CLIENTDARKDETECTORAMPLIFIER
_CLIENTMAPPOI_CLIENTMAPOUTPOST.containing_type = _CLIENTMAPPOI
_CLIENTMAPPOI_CLIENTMAPGREENHOUSE_CLIENTPOTSUMMARY.containing_type = _CLIENTMAPPOI_CLIENTMAPGREENHOUSE
_CLIENTMAPPOI_CLIENTMAPGREENHOUSE.fields_by_name['normal_pot'].message_type = _CLIENTMAPPOI_CLIENTMAPGREENHOUSE_CLIENTPOTSUMMARY
_CLIENTMAPPOI_CLIENTMAPGREENHOUSE.fields_by_name['rental_pot'].message_type = _CLIENTMAPPOI_CLIENTMAPGREENHOUSE_CLIENTPOTSUMMARY
_CLIENTMAPPOI_CLIENTMAPGREENHOUSE.containing_type = _CLIENTMAPPOI
_CLIENTMAPPOI_CLIENTMAPFORTRESS.containing_type = _CLIENTMAPPOI
_CLIENTMAPPOI_PARTNER.fields_by_name['partner_type'].enum_type = _CLIENTMAPPOI_PARTNER_PARTNERTYPE
_CLIENTMAPPOI_PARTNER.containing_type = _CLIENTMAPPOI
_CLIENTMAPPOI_PARTNER_PARTNERTYPE.containing_type = _CLIENTMAPPOI_PARTNER
_CLIENTMAPPOI.fields_by_name['outpost'].message_type = _CLIENTMAPPOI_CLIENTMAPOUTPOST
_CLIENTMAPPOI.fields_by_name['fortress'].message_type = _CLIENTMAPPOI_CLIENTMAPFORTRESS
_CLIENTMAPPOI.fields_by_name['greenhouse'].message_type = _CLIENTMAPPOI_CLIENTMAPGREENHOUSE
_CLIENTMAPPOI.fields_by_name['poi_accessibility'].enum_type = wuprotos_dot_enums_dot_poi__accessibility__pb2._POIACCESSIBILITY
_CLIENTMAPPOI.fields_by_name['partner'].message_type = _CLIENTMAPPOI_PARTNER
_CLIENTMAPPOI.oneofs_by_name['Type'].fields.append(
  _CLIENTMAPPOI.fields_by_name['outpost'])
_CLIENTMAPPOI.fields_by_name['outpost'].containing_oneof = _CLIENTMAPPOI.oneofs_by_name['Type']
_CLIENTMAPPOI.oneofs_by_name['Type'].fields.append(
  _CLIENTMAPPOI.fields_by_name['fortress'])
_CLIENTMAPPOI.fields_by_name['fortress'].containing_oneof = _CLIENTMAPPOI.oneofs_by_name['Type']
_CLIENTMAPPOI.oneofs_by_name['Type'].fields.append(
  _CLIENTMAPPOI.fields_by_name['greenhouse'])
_CLIENTMAPPOI.fields_by_name['greenhouse'].containing_oneof = _CLIENTMAPPOI.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['ClientMapPoi'] = _CLIENTMAPPOI
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientMapPoi = _reflection.GeneratedProtocolMessageType('ClientMapPoi', (_message.Message,), dict(

  ClientMapOutpost = _reflection.GeneratedProtocolMessageType('ClientMapOutpost', (_message.Message,), dict(
    DESCRIPTOR = _CLIENTMAPPOI_CLIENTMAPOUTPOST,
    __module__ = 'wuprotos.data.client.client_map_poi_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.data.client.ClientMapPoi.ClientMapOutpost)
    ))
  ,

  ClientMapGreenhouse = _reflection.GeneratedProtocolMessageType('ClientMapGreenhouse', (_message.Message,), dict(

    ClientPotSummary = _reflection.GeneratedProtocolMessageType('ClientPotSummary', (_message.Message,), dict(
      DESCRIPTOR = _CLIENTMAPPOI_CLIENTMAPGREENHOUSE_CLIENTPOTSUMMARY,
      __module__ = 'wuprotos.data.client.client_map_poi_pb2'
      # @@protoc_insertion_point(class_scope:wuprotos.data.client.ClientMapPoi.ClientMapGreenhouse.ClientPotSummary)
      ))
    ,
    DESCRIPTOR = _CLIENTMAPPOI_CLIENTMAPGREENHOUSE,
    __module__ = 'wuprotos.data.client.client_map_poi_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.data.client.ClientMapPoi.ClientMapGreenhouse)
    ))
  ,

  ClientMapFortress = _reflection.GeneratedProtocolMessageType('ClientMapFortress', (_message.Message,), dict(
    DESCRIPTOR = _CLIENTMAPPOI_CLIENTMAPFORTRESS,
    __module__ = 'wuprotos.data.client.client_map_poi_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.data.client.ClientMapPoi.ClientMapFortress)
    ))
  ,

  Partner = _reflection.GeneratedProtocolMessageType('Partner', (_message.Message,), dict(
    DESCRIPTOR = _CLIENTMAPPOI_PARTNER,
    __module__ = 'wuprotos.data.client.client_map_poi_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.data.client.ClientMapPoi.Partner)
    ))
  ,
  DESCRIPTOR = _CLIENTMAPPOI,
  __module__ = 'wuprotos.data.client.client_map_poi_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.data.client.ClientMapPoi)
  ))
_sym_db.RegisterMessage(ClientMapPoi)
_sym_db.RegisterMessage(ClientMapPoi.ClientMapOutpost)
_sym_db.RegisterMessage(ClientMapPoi.ClientMapGreenhouse)
_sym_db.RegisterMessage(ClientMapPoi.ClientMapGreenhouse.ClientPotSummary)
_sym_db.RegisterMessage(ClientMapPoi.ClientMapFortress)
_sym_db.RegisterMessage(ClientMapPoi.Partner)


# @@protoc_insertion_point(module_scope)