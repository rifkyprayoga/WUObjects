# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientWandLength.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientWandLength.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n+WUProtos/Data/Client/ClientWandLength.proto\x12\x14WUProtos.Data.Client\"I\n\x10\x43lientWandLength\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nmodel_path\x18\x02 \x01(\t\x12\x13\n\x0bslidervalue\x18\x03 \x01(\x05\x62\x06proto3')
)




_CLIENTWANDLENGTH = _descriptor.Descriptor(
  name='ClientWandLength',
  full_name='WUProtos.Data.Client.ClientWandLength',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='WUProtos.Data.Client.ClientWandLength.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_path', full_name='WUProtos.Data.Client.ClientWandLength.model_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slidervalue', full_name='WUProtos.Data.Client.ClientWandLength.slidervalue', index=2,
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
  serialized_start=69,
  serialized_end=142,
)

DESCRIPTOR.message_types_by_name['ClientWandLength'] = _CLIENTWANDLENGTH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientWandLength = _reflection.GeneratedProtocolMessageType('ClientWandLength', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTWANDLENGTH,
  __module__ = 'WUProtos.Data.Client.ClientWandLength_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientWandLength)
  ))
_sym_db.RegisterMessage(ClientWandLength)


# @@protoc_insertion_point(module_scope)
