# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/data/client/client_cauldron.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/data/client/client_cauldron.proto',
  package='wuprotos.data.client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n*wuprotos/data/client/client_cauldron.proto\x12\x14wuprotos.data.client\"\x1c\n\x0e\x43lientCauldron\x12\n\n\x02id\x18\x01 \x01(\tb\x06proto3')
)




_CLIENTCAULDRON = _descriptor.Descriptor(
  name='ClientCauldron',
  full_name='wuprotos.data.client.ClientCauldron',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='wuprotos.data.client.ClientCauldron.id', index=0,
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
  serialized_start=68,
  serialized_end=96,
)

DESCRIPTOR.message_types_by_name['ClientCauldron'] = _CLIENTCAULDRON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientCauldron = _reflection.GeneratedProtocolMessageType('ClientCauldron', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTCAULDRON,
  __module__ = 'wuprotos.data.client.client_cauldron_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.data.client.ClientCauldron)
  ))
_sym_db.RegisterMessage(ClientCauldron)


# @@protoc_insertion_point(module_scope)