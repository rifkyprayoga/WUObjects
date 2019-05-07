# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/AvailableSku.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import CurrencyQuantity_pb2 as WUProtos_dot_Data_dot_CurrencyQuantity__pb2
from WUProtos.Data import GameItemContent_pb2 as WUProtos_dot_Data_dot_GameItemContent__pb2
from WUProtos.Data import SkuPresentation_pb2 as WUProtos_dot_Data_dot_SkuPresentation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/AvailableSku.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n WUProtos/Data/AvailableSku.proto\x12\rWUProtos.Data\x1a$WUProtos/Data/CurrencyQuantity.proto\x1a#WUProtos/Data/GameItemContent.proto\x1a#WUProtos/Data/SkuPresentation.proto\"\xb9\x02\n\x0c\x41vailableSku\x12\n\n\x02id\x18\x01 \x01(\t\x12\"\n\x1ais_third_party_vendor_item\x18\x02 \x01(\x08\x12.\n\x05price\x18\x03 \x03(\x0b\x32\x1f.WUProtos.Data.CurrencyQuantity\x12\x39\n\x10\x63urrency_granted\x18\x04 \x03(\x0b\x32\x1f.WUProtos.Data.CurrencyQuantity\x12\x39\n\x11game_item_content\x18\x05 \x03(\x0b\x32\x1e.WUProtos.Data.GameItemContent\x12\x39\n\x11presentation_data\x18\x06 \x03(\x0b\x32\x1e.WUProtos.Data.SkuPresentation\x12\x18\n\x10\x63\x61n_be_purchased\x18\x07 \x01(\x08\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_CurrencyQuantity__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_GameItemContent__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_SkuPresentation__pb2.DESCRIPTOR,])




_AVAILABLESKU = _descriptor.Descriptor(
  name='AvailableSku',
  full_name='WUProtos.Data.AvailableSku',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.AvailableSku.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_third_party_vendor_item', full_name='WUProtos.Data.AvailableSku.is_third_party_vendor_item', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='WUProtos.Data.AvailableSku.price', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency_granted', full_name='WUProtos.Data.AvailableSku.currency_granted', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_item_content', full_name='WUProtos.Data.AvailableSku.game_item_content', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='presentation_data', full_name='WUProtos.Data.AvailableSku.presentation_data', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='can_be_purchased', full_name='WUProtos.Data.AvailableSku.can_be_purchased', index=6,
      number=7, type=8, cpp_type=7, label=1,
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
  serialized_start=164,
  serialized_end=477,
)

_AVAILABLESKU.fields_by_name['price'].message_type = WUProtos_dot_Data_dot_CurrencyQuantity__pb2._CURRENCYQUANTITY
_AVAILABLESKU.fields_by_name['currency_granted'].message_type = WUProtos_dot_Data_dot_CurrencyQuantity__pb2._CURRENCYQUANTITY
_AVAILABLESKU.fields_by_name['game_item_content'].message_type = WUProtos_dot_Data_dot_GameItemContent__pb2._GAMEITEMCONTENT
_AVAILABLESKU.fields_by_name['presentation_data'].message_type = WUProtos_dot_Data_dot_SkuPresentation__pb2._SKUPRESENTATION
DESCRIPTOR.message_types_by_name['AvailableSku'] = _AVAILABLESKU
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AvailableSku = _reflection.GeneratedProtocolMessageType('AvailableSku', (_message.Message,), dict(
  DESCRIPTOR = _AVAILABLESKU,
  __module__ = 'WUProtos.Data.AvailableSku_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.AvailableSku)
  ))
_sym_db.RegisterMessage(AvailableSku)


# @@protoc_insertion_point(module_scope)
