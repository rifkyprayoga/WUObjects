# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Collection/CollectionPage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Loot import LootCollection_pb2 as WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2
from WUProtos.Data import Requirements_pb2 as WUProtos_dot_Data_dot_Requirements__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Collection/CollectionPage.proto',
  package='WUProtos.Data.Collection',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n-WUProtos/Data/Collection/CollectionPage.proto\x12\x18WUProtos.Data.Collection\x1a\'WUProtos/Data/Loot/LootCollection.proto\x1a WUProtos/Data/Requirements.proto\"\xb8\x01\n\x0e\x43ollectionPage\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfamily_id\x18\x02 \x01(\t\x12\r\n\x05items\x18\x03 \x03(\t\x12>\n\x12\x63ompletion_rewards\x18\x04 \x03(\x0b\x32\".WUProtos.Data.Loot.LootCollection\x12\x38\n\x13unlock_requirements\x18\x05 \x01(\x0b\x32\x1b.WUProtos.Data.Requirementsb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_Requirements__pb2.DESCRIPTOR,])




_COLLECTIONPAGE = _descriptor.Descriptor(
  name='CollectionPage',
  full_name='WUProtos.Data.Collection.CollectionPage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.Collection.CollectionPage.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='family_id', full_name='WUProtos.Data.Collection.CollectionPage.family_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='WUProtos.Data.Collection.CollectionPage.items', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='completion_rewards', full_name='WUProtos.Data.Collection.CollectionPage.completion_rewards', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unlock_requirements', full_name='WUProtos.Data.Collection.CollectionPage.unlock_requirements', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=151,
  serialized_end=335,
)

_COLLECTIONPAGE.fields_by_name['completion_rewards'].message_type = WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2._LOOTCOLLECTION
_COLLECTIONPAGE.fields_by_name['unlock_requirements'].message_type = WUProtos_dot_Data_dot_Requirements__pb2._REQUIREMENTS
DESCRIPTOR.message_types_by_name['CollectionPage'] = _COLLECTIONPAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectionPage = _reflection.GeneratedProtocolMessageType('CollectionPage', (_message.Message,), dict(
  DESCRIPTOR = _COLLECTIONPAGE,
  __module__ = 'WUProtos.Data.Collection.CollectionPage_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Collection.CollectionPage)
  ))
_sym_db.RegisterMessage(CollectionPage)


# @@protoc_insertion_point(module_scope)
