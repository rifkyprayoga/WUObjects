# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientPortkey.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientPortkey.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(WUProtos/Data/Client/ClientPortkey.proto\x12\x14WUProtos.Data.Client\"X\n\rClientPortkey\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12\x1f\n\x17localized_complete_text\x18\x04 \x01(\tb\x06proto3')
)




_CLIENTPORTKEY = _descriptor.Descriptor(
  name='ClientPortkey',
  full_name='WUProtos.Data.Client.ClientPortkey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.Client.ClientPortkey.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='WUProtos.Data.Client.ClientPortkey.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='WUProtos.Data.Client.ClientPortkey.icon', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='localized_complete_text', full_name='WUProtos.Data.Client.ClientPortkey.localized_complete_text', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=66,
  serialized_end=154,
)

DESCRIPTOR.message_types_by_name['ClientPortkey'] = _CLIENTPORTKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientPortkey = _reflection.GeneratedProtocolMessageType('ClientPortkey', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTPORTKEY,
  __module__ = 'WUProtos.Data.Client.ClientPortkey_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientPortkey)
  ))
_sym_db.RegisterMessage(ClientPortkey)


# @@protoc_insertion_point(module_scope)