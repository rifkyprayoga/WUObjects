# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Responses/DbgResetProfessionResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Responses/DbgResetProfessionResponse.proto',
  package='WUProtos.Networking.Responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n>WUProtos/Networking/Responses/DbgResetProfessionResponse.proto\x12\x1dWUProtos.Networking.Responses\"-\n\x1a\x44\x62gResetProfessionResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x62\x06proto3')
)




_DBGRESETPROFESSIONRESPONSE = _descriptor.Descriptor(
  name='DbgResetProfessionResponse',
  full_name='WUProtos.Networking.Responses.DbgResetProfessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='WUProtos.Networking.Responses.DbgResetProfessionResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=97,
  serialized_end=142,
)

DESCRIPTOR.message_types_by_name['DbgResetProfessionResponse'] = _DBGRESETPROFESSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DbgResetProfessionResponse = _reflection.GeneratedProtocolMessageType('DbgResetProfessionResponse', (_message.Message,), dict(
  DESCRIPTOR = _DBGRESETPROFESSIONRESPONSE,
  __module__ = 'WUProtos.Networking.Responses.DbgResetProfessionResponse_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Responses.DbgResetProfessionResponse)
  ))
_sym_db.RegisterMessage(DbgResetProfessionResponse)


# @@protoc_insertion_point(module_scope)
