# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Responses/AcceptTermsOfServiceResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Responses/AcceptTermsOfServiceResponse.proto',
  package='WUProtos.Networking.Responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n@WUProtos/Networking/Responses/AcceptTermsOfServiceResponse.proto\x12\x1dWUProtos.Networking.Responses\"\xa5\x01\n\x1c\x41\x63\x63\x65ptTermsOfServiceResponse\x12R\n\x06status\x18\x01 \x01(\x0e\x32\x42.WUProtos.Networking.Responses.AcceptTermsOfServiceResponse.Status\"1\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\r\n\tCOMPLETED\x10\x02\x62\x06proto3')
)



_ACCEPTTERMSOFSERVICERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='WUProtos.Networking.Responses.AcceptTermsOfServiceResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=216,
  serialized_end=265,
)
_sym_db.RegisterEnumDescriptor(_ACCEPTTERMSOFSERVICERESPONSE_STATUS)


_ACCEPTTERMSOFSERVICERESPONSE = _descriptor.Descriptor(
  name='AcceptTermsOfServiceResponse',
  full_name='WUProtos.Networking.Responses.AcceptTermsOfServiceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='WUProtos.Networking.Responses.AcceptTermsOfServiceResponse.status', index=0,
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
    _ACCEPTTERMSOFSERVICERESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=265,
)

_ACCEPTTERMSOFSERVICERESPONSE.fields_by_name['status'].enum_type = _ACCEPTTERMSOFSERVICERESPONSE_STATUS
_ACCEPTTERMSOFSERVICERESPONSE_STATUS.containing_type = _ACCEPTTERMSOFSERVICERESPONSE
DESCRIPTOR.message_types_by_name['AcceptTermsOfServiceResponse'] = _ACCEPTTERMSOFSERVICERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AcceptTermsOfServiceResponse = _reflection.GeneratedProtocolMessageType('AcceptTermsOfServiceResponse', (_message.Message,), dict(
  DESCRIPTOR = _ACCEPTTERMSOFSERVICERESPONSE,
  __module__ = 'WUProtos.Networking.Responses.AcceptTermsOfServiceResponse_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Responses.AcceptTermsOfServiceResponse)
  ))
_sym_db.RegisterMessage(AcceptTermsOfServiceResponse)


# @@protoc_insertion_point(module_scope)
