# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientTheme.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientTheme.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&WUProtos/Data/Client/ClientTheme.proto\x12\x14WUProtos.Data.Client\"\x1b\n\x0b\x43lientTheme\x12\x0c\n\x04icon\x18\x01 \x01(\tb\x06proto3')
)




_CLIENTTHEME = _descriptor.Descriptor(
  name='ClientTheme',
  full_name='WUProtos.Data.Client.ClientTheme',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='icon', full_name='WUProtos.Data.Client.ClientTheme.icon', index=0,
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
  serialized_start=64,
  serialized_end=91,
)

DESCRIPTOR.message_types_by_name['ClientTheme'] = _CLIENTTHEME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientTheme = _reflection.GeneratedProtocolMessageType('ClientTheme', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTTHEME,
  __module__ = 'WUProtos.Data.Client.ClientTheme_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientTheme)
  ))
_sym_db.RegisterMessage(ClientTheme)


# @@protoc_insertion_point(module_scope)
