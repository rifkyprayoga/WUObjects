# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientMapLandmark.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientMapLandmark.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,WUProtos/Data/Client/ClientMapLandmark.proto\x12\x14WUProtos.Data.Client\"\x91\x01\n\x11\x43lientMapLandmark\x12\x1c\n\x14\x63ollection_family_id\x18\x01 \x01(\t\x12\x14\n\x0cpoi_latitude\x18\x02 \x01(\x01\x12\x15\n\rpoi_longitude\x18\x03 \x01(\x01\x12\x17\n\x0f\x62order_latitude\x18\x04 \x03(\x01\x12\x18\n\x10\x62order_longitude\x18\x05 \x03(\x01\x62\x06proto3')
)




_CLIENTMAPLANDMARK = _descriptor.Descriptor(
  name='ClientMapLandmark',
  full_name='WUProtos.Data.Client.ClientMapLandmark',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection_family_id', full_name='WUProtos.Data.Client.ClientMapLandmark.collection_family_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poi_latitude', full_name='WUProtos.Data.Client.ClientMapLandmark.poi_latitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poi_longitude', full_name='WUProtos.Data.Client.ClientMapLandmark.poi_longitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='border_latitude', full_name='WUProtos.Data.Client.ClientMapLandmark.border_latitude', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='border_longitude', full_name='WUProtos.Data.Client.ClientMapLandmark.border_longitude', index=4,
      number=5, type=1, cpp_type=5, label=3,
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
  serialized_start=71,
  serialized_end=216,
)

DESCRIPTOR.message_types_by_name['ClientMapLandmark'] = _CLIENTMAPLANDMARK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientMapLandmark = _reflection.GeneratedProtocolMessageType('ClientMapLandmark', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTMAPLANDMARK,
  __module__ = 'WUProtos.Data.Client.ClientMapLandmark_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientMapLandmark)
  ))
_sym_db.RegisterMessage(ClientMapLandmark)


# @@protoc_insertion_point(module_scope)
