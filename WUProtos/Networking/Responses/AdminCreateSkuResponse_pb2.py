# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Responses/AdminCreateSkuResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Responses/AdminCreateSkuResponse.proto',
  package='WUProtos.Networking.Responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n:WUProtos/Networking/Responses/AdminCreateSkuResponse.proto\x12\x1dWUProtos.Networking.Responses\"\x95\x01\n\x16\x41\x64minCreateSkuResponse\x12L\n\x06status\x18\x01 \x01(\x0e\x32<.WUProtos.Networking.Responses.AdminCreateSkuResponse.Status\"-\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x62\x06proto3')
)



_ADMINCREATESKURESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='WUProtos.Networking.Responses.AdminCreateSkuResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=198,
  serialized_end=243,
)
_sym_db.RegisterEnumDescriptor(_ADMINCREATESKURESPONSE_STATUS)


_ADMINCREATESKURESPONSE = _descriptor.Descriptor(
  name='AdminCreateSkuResponse',
  full_name='WUProtos.Networking.Responses.AdminCreateSkuResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='WUProtos.Networking.Responses.AdminCreateSkuResponse.status', index=0,
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
    _ADMINCREATESKURESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=243,
)

_ADMINCREATESKURESPONSE.fields_by_name['status'].enum_type = _ADMINCREATESKURESPONSE_STATUS
_ADMINCREATESKURESPONSE_STATUS.containing_type = _ADMINCREATESKURESPONSE
DESCRIPTOR.message_types_by_name['AdminCreateSkuResponse'] = _ADMINCREATESKURESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdminCreateSkuResponse = _reflection.GeneratedProtocolMessageType('AdminCreateSkuResponse', (_message.Message,), dict(
  DESCRIPTOR = _ADMINCREATESKURESPONSE,
  __module__ = 'WUProtos.Networking.Responses.AdminCreateSkuResponse_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Responses.AdminCreateSkuResponse)
  ))
_sym_db.RegisterMessage(AdminCreateSkuResponse)


# @@protoc_insertion_point(module_scope)
