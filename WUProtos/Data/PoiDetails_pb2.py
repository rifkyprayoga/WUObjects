# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/PoiDetails.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/PoiDetails.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1eWUProtos/Data/PoiDetails.proto\x12\rWUProtos.Data\"C\n\nPoiDetails\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x12\n\nimage_urls\x18\x03 \x03(\tb\x06proto3')
)




_POIDETAILS = _descriptor.Descriptor(
  name='PoiDetails',
  full_name='WUProtos.Data.PoiDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='WUProtos.Data.PoiDetails.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='WUProtos.Data.PoiDetails.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_urls', full_name='WUProtos.Data.PoiDetails.image_urls', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=49,
  serialized_end=116,
)

DESCRIPTOR.message_types_by_name['PoiDetails'] = _POIDETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PoiDetails = _reflection.GeneratedProtocolMessageType('PoiDetails', (_message.Message,), dict(
  DESCRIPTOR = _POIDETAILS,
  __module__ = 'WUProtos.Data.PoiDetails_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.PoiDetails)
  ))
_sym_db.RegisterMessage(PoiDetails)


# @@protoc_insertion_point(module_scope)
