# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/collect_ingredient_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/collect_ingredient_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nFwuprotos/networking/requests/messages/collect_ingredient_message.proto\x12%wuprotos.networking.requests.messages\"*\n\x18\x43ollectIngredientMessage\x12\x0e\n\x06ticket\x18\x01 \x01(\x0c\x62\x06proto3')
)




_COLLECTINGREDIENTMESSAGE = _descriptor.Descriptor(
  name='CollectIngredientMessage',
  full_name='wuprotos.networking.requests.messages.CollectIngredientMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ticket', full_name='wuprotos.networking.requests.messages.CollectIngredientMessage.ticket', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  serialized_start=113,
  serialized_end=155,
)

DESCRIPTOR.message_types_by_name['CollectIngredientMessage'] = _COLLECTINGREDIENTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectIngredientMessage = _reflection.GeneratedProtocolMessageType('CollectIngredientMessage', (_message.Message,), dict(
  DESCRIPTOR = _COLLECTINGREDIENTMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.collect_ingredient_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.CollectIngredientMessage)
  ))
_sym_db.RegisterMessage(CollectIngredientMessage)


# @@protoc_insertion_point(module_scope)