# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Collection/CollectionSubfeatureFamilyOrders.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Collection import CollectionFamily_pb2 as WUProtos_dot_Data_dot_Collection_dot_CollectionFamily__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Collection/CollectionSubfeatureFamilyOrders.proto',
  package='WUProtos.Data.Collection',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n?WUProtos/Data/Collection/CollectionSubfeatureFamilyOrders.proto\x12\x18WUProtos.Data.Collection\x1a/WUProtos/Data/Collection/CollectionFamily.proto\"\x85\x01\n CollectionSubfeatureFamilyOrders\x12M\n\nsubfeature\x18\x01 \x01(\x0e\x32\x39.WUProtos.Data.Collection.CollectionFamily.SubfeatureType\x12\x12\n\nfamily_ids\x18\x02 \x03(\tb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Collection_dot_CollectionFamily__pb2.DESCRIPTOR,])




_COLLECTIONSUBFEATUREFAMILYORDERS = _descriptor.Descriptor(
  name='CollectionSubfeatureFamilyOrders',
  full_name='WUProtos.Data.Collection.CollectionSubfeatureFamilyOrders',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subfeature', full_name='WUProtos.Data.Collection.CollectionSubfeatureFamilyOrders.subfeature', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='family_ids', full_name='WUProtos.Data.Collection.CollectionSubfeatureFamilyOrders.family_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=143,
  serialized_end=276,
)

_COLLECTIONSUBFEATUREFAMILYORDERS.fields_by_name['subfeature'].enum_type = WUProtos_dot_Data_dot_Collection_dot_CollectionFamily__pb2._COLLECTIONFAMILY_SUBFEATURETYPE
DESCRIPTOR.message_types_by_name['CollectionSubfeatureFamilyOrders'] = _COLLECTIONSUBFEATUREFAMILYORDERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectionSubfeatureFamilyOrders = _reflection.GeneratedProtocolMessageType('CollectionSubfeatureFamilyOrders', (_message.Message,), dict(
  DESCRIPTOR = _COLLECTIONSUBFEATUREFAMILYORDERS,
  __module__ = 'WUProtos.Data.Collection.CollectionSubfeatureFamilyOrders_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Collection.CollectionSubfeatureFamilyOrders)
  ))
_sym_db.RegisterMessage(CollectionSubfeatureFamilyOrders)


# @@protoc_insertion_point(module_scope)