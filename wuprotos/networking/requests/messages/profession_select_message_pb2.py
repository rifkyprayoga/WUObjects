# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/profession_select_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/profession_select_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nEwuprotos/networking/requests/messages/profession_select_message.proto\x12%wuprotos.networking.requests.messages\"4\n\x17ProfessionSelectMessage\x12\x19\n\x11profession_gmt_id\x18\x01 \x01(\tb\x06proto3')
)




_PROFESSIONSELECTMESSAGE = _descriptor.Descriptor(
  name='ProfessionSelectMessage',
  full_name='wuprotos.networking.requests.messages.ProfessionSelectMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='profession_gmt_id', full_name='wuprotos.networking.requests.messages.ProfessionSelectMessage.profession_gmt_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=112,
  serialized_end=164,
)

DESCRIPTOR.message_types_by_name['ProfessionSelectMessage'] = _PROFESSIONSELECTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProfessionSelectMessage = _reflection.GeneratedProtocolMessageType('ProfessionSelectMessage', (_message.Message,), dict(
  DESCRIPTOR = _PROFESSIONSELECTMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.profession_select_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.ProfessionSelectMessage)
  ))
_sym_db.RegisterMessage(ProfessionSelectMessage)


# @@protoc_insertion_point(module_scope)