# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/WalkboxTemplate.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/WalkboxTemplate.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#WUProtos/Data/WalkboxTemplate.proto\x12\rWUProtos.Data\";\n\x0fWalkboxTemplate\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1c\n\x14required_distance_km\x18\x02 \x01(\x02\x62\x06proto3')
)




_WALKBOXTEMPLATE = _descriptor.Descriptor(
  name='WalkboxTemplate',
  full_name='WUProtos.Data.WalkboxTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.WalkboxTemplate.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='required_distance_km', full_name='WUProtos.Data.WalkboxTemplate.required_distance_km', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=54,
  serialized_end=113,
)

DESCRIPTOR.message_types_by_name['WalkboxTemplate'] = _WALKBOXTEMPLATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WalkboxTemplate = _reflection.GeneratedProtocolMessageType('WalkboxTemplate', (_message.Message,), dict(
  DESCRIPTOR = _WALKBOXTEMPLATE,
  __module__ = 'WUProtos.Data.WalkboxTemplate_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.WalkboxTemplate)
  ))
_sym_db.RegisterMessage(WalkboxTemplate)


# @@protoc_insertion_point(module_scope)