# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/remove_login_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wuprotos.enums import identity_provider_pb2 as wuprotos_dot_enums_dot_identity__provider__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/remove_login_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n@wuprotos/networking/requests/messages/remove_login_message.proto\x12%wuprotos.networking.requests.messages\x1a&wuprotos/enums/identity_provider.proto\"Q\n\x12RemoveLoginMessage\x12;\n\x11identity_provider\x18\x01 \x01(\x0e\x32 .wuprotos.enums.IdentityProviderb\x06proto3')
  ,
  dependencies=[wuprotos_dot_enums_dot_identity__provider__pb2.DESCRIPTOR,])




_REMOVELOGINMESSAGE = _descriptor.Descriptor(
  name='RemoveLoginMessage',
  full_name='wuprotos.networking.requests.messages.RemoveLoginMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identity_provider', full_name='wuprotos.networking.requests.messages.RemoveLoginMessage.identity_provider', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=147,
  serialized_end=228,
)

_REMOVELOGINMESSAGE.fields_by_name['identity_provider'].enum_type = wuprotos_dot_enums_dot_identity__provider__pb2._IDENTITYPROVIDER
DESCRIPTOR.message_types_by_name['RemoveLoginMessage'] = _REMOVELOGINMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemoveLoginMessage = _reflection.GeneratedProtocolMessageType('RemoveLoginMessage', (_message.Message,), dict(
  DESCRIPTOR = _REMOVELOGINMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.remove_login_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.RemoveLoginMessage)
  ))
_sym_db.RegisterMessage(RemoveLoginMessage)


# @@protoc_insertion_point(module_scope)