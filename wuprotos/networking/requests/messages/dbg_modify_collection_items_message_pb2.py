# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/dbg_modify_collection_items_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/dbg_modify_collection_items_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nOwuprotos/networking/requests/messages/dbg_modify_collection_items_message.proto\x12%wuprotos.networking.requests.messages\"\x93\x02\n\x1f\x44\x62gModifyCollectionItemsMessage\x12z\n\x10\x63ollection_items\x18\x01 \x03(\x0b\x32`.wuprotos.networking.requests.messages.DbgModifyCollectionItemsMessage.DebugModifyCollectionItem\x1at\n\x19\x44\x65\x62ugModifyCollectionItem\x12\n\n\x02id\x18\x01 \x01(\t\x12&\n\x1eincrement_times_encountered_by\x18\x02 \x01(\x05\x12#\n\x1bincrement_times_returned_by\x18\x03 \x01(\x05\x62\x06proto3')
)




_DBGMODIFYCOLLECTIONITEMSMESSAGE_DEBUGMODIFYCOLLECTIONITEM = _descriptor.Descriptor(
  name='DebugModifyCollectionItem',
  full_name='wuprotos.networking.requests.messages.DbgModifyCollectionItemsMessage.DebugModifyCollectionItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='wuprotos.networking.requests.messages.DbgModifyCollectionItemsMessage.DebugModifyCollectionItem.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='increment_times_encountered_by', full_name='wuprotos.networking.requests.messages.DbgModifyCollectionItemsMessage.DebugModifyCollectionItem.increment_times_encountered_by', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='increment_times_returned_by', full_name='wuprotos.networking.requests.messages.DbgModifyCollectionItemsMessage.DebugModifyCollectionItem.increment_times_returned_by', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=282,
  serialized_end=398,
)

_DBGMODIFYCOLLECTIONITEMSMESSAGE = _descriptor.Descriptor(
  name='DbgModifyCollectionItemsMessage',
  full_name='wuprotos.networking.requests.messages.DbgModifyCollectionItemsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection_items', full_name='wuprotos.networking.requests.messages.DbgModifyCollectionItemsMessage.collection_items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DBGMODIFYCOLLECTIONITEMSMESSAGE_DEBUGMODIFYCOLLECTIONITEM, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=398,
)

_DBGMODIFYCOLLECTIONITEMSMESSAGE_DEBUGMODIFYCOLLECTIONITEM.containing_type = _DBGMODIFYCOLLECTIONITEMSMESSAGE
_DBGMODIFYCOLLECTIONITEMSMESSAGE.fields_by_name['collection_items'].message_type = _DBGMODIFYCOLLECTIONITEMSMESSAGE_DEBUGMODIFYCOLLECTIONITEM
DESCRIPTOR.message_types_by_name['DbgModifyCollectionItemsMessage'] = _DBGMODIFYCOLLECTIONITEMSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DbgModifyCollectionItemsMessage = _reflection.GeneratedProtocolMessageType('DbgModifyCollectionItemsMessage', (_message.Message,), dict(

  DebugModifyCollectionItem = _reflection.GeneratedProtocolMessageType('DebugModifyCollectionItem', (_message.Message,), dict(
    DESCRIPTOR = _DBGMODIFYCOLLECTIONITEMSMESSAGE_DEBUGMODIFYCOLLECTIONITEM,
    __module__ = 'wuprotos.networking.requests.messages.dbg_modify_collection_items_message_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.DbgModifyCollectionItemsMessage.DebugModifyCollectionItem)
    ))
  ,
  DESCRIPTOR = _DBGMODIFYCOLLECTIONITEMSMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.dbg_modify_collection_items_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.DbgModifyCollectionItemsMessage)
  ))
_sym_db.RegisterMessage(DbgModifyCollectionItemsMessage)
_sym_db.RegisterMessage(DbgModifyCollectionItemsMessage.DebugModifyCollectionItem)


# @@protoc_insertion_point(module_scope)