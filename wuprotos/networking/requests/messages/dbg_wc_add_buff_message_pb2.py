# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/dbg_wc_add_buff_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/dbg_wc_add_buff_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nCwuprotos/networking/requests/messages/dbg_wc_add_buff_message.proto\x12%wuprotos.networking.requests.messages\"R\n\x13\x44\x62gWcAddBuffMessage\x12\x13\n\x0b\x62uff_gmt_id\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\r\x12\x14\n\x0c\x65ncounter_id\x18\x03 \x01(\x0c\x62\x06proto3')
)




_DBGWCADDBUFFMESSAGE = _descriptor.Descriptor(
  name='DbgWcAddBuffMessage',
  full_name='wuprotos.networking.requests.messages.DbgWcAddBuffMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buff_gmt_id', full_name='wuprotos.networking.requests.messages.DbgWcAddBuffMessage.buff_gmt_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='wuprotos.networking.requests.messages.DbgWcAddBuffMessage.quantity', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encounter_id', full_name='wuprotos.networking.requests.messages.DbgWcAddBuffMessage.encounter_id', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=110,
  serialized_end=192,
)

DESCRIPTOR.message_types_by_name['DbgWcAddBuffMessage'] = _DBGWCADDBUFFMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DbgWcAddBuffMessage = _reflection.GeneratedProtocolMessageType('DbgWcAddBuffMessage', (_message.Message,), dict(
  DESCRIPTOR = _DBGWCADDBUFFMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.dbg_wc_add_buff_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.DbgWcAddBuffMessage)
  ))
_sym_db.RegisterMessage(DbgWcAddBuffMessage)


# @@protoc_insertion_point(module_scope)