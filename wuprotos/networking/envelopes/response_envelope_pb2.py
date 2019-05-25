# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/envelopes/response_envelope.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wuprotos.networking.envelopes import auth_ticket_pb2 as wuprotos_dot_networking_dot_envelopes_dot_auth__ticket__pb2
from wuprotos.networking.platform import platform_request_type_pb2 as wuprotos_dot_networking_dot_platform_dot_platform__request__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/envelopes/response_envelope.proto',
  package='wuprotos.networking.envelopes',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n5wuprotos/networking/envelopes/response_envelope.proto\x12\x1dwuprotos.networking.envelopes\x1a/wuprotos/networking/envelopes/auth_ticket.proto\x1a\x38wuprotos/networking/platform/platform_request_type.proto\"\xee\x04\n\x10ResponseEnvelope\x12O\n\x0bstatus_code\x18\x01 \x01(\x0e\x32:.wuprotos.networking.envelopes.ResponseEnvelope.StatusCode\x12\x12\n\nrequest_id\x18\x02 \x01(\x04\x12\x0f\n\x07\x61pi_url\x18\x03 \x01(\t\x12Z\n\x10platform_returns\x18\x06 \x03(\x0b\x32@.wuprotos.networking.envelopes.ResponseEnvelope.PlatformResponse\x12>\n\x0b\x61uth_ticket\x18\x07 \x01(\x0b\x32).wuprotos.networking.envelopes.AuthTicket\x12\x0f\n\x07returns\x18\x64 \x03(\x0c\x12\r\n\x05\x65rror\x18\x65 \x01(\t\x1a\x65\n\x10PlatformResponse\x12?\n\x04type\x18\x01 \x01(\x0e\x32\x31.wuprotos.networking.platform.PlatformRequestType\x12\x10\n\x08response\x18\x02 \x01(\x0c\"\xc0\x01\n\nStatusCode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x1a\n\x16OK_RPC_URL_IN_RESPONSE\x10\x02\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\x03\x12\x13\n\x0fINVALID_REQUEST\x10\x33\x12\x1c\n\x18INVALID_PLATFORM_REQUEST\x10\x34\x12\x0c\n\x08REDIRECT\x10\x35\x12\x17\n\x13SESSION_INVALIDATED\x10\x64\x12\x16\n\x12INVALID_AUTH_TOKEN\x10\x66\x62\x06proto3')
  ,
  dependencies=[wuprotos_dot_networking_dot_envelopes_dot_auth__ticket__pb2.DESCRIPTOR,wuprotos_dot_networking_dot_platform_dot_platform__request__type__pb2.DESCRIPTOR,])



_RESPONSEENVELOPE_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='wuprotos.networking.envelopes.ResponseEnvelope.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OK_RPC_URL_IN_RESPONSE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_REQUEST', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_REQUEST', index=4, number=51,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PLATFORM_REQUEST', index=5, number=52,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDIRECT', index=6, number=53,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION_INVALIDATED', index=7, number=100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_AUTH_TOKEN', index=8, number=102,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=626,
  serialized_end=818,
)
_sym_db.RegisterEnumDescriptor(_RESPONSEENVELOPE_STATUSCODE)


_RESPONSEENVELOPE_PLATFORMRESPONSE = _descriptor.Descriptor(
  name='PlatformResponse',
  full_name='wuprotos.networking.envelopes.ResponseEnvelope.PlatformResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='wuprotos.networking.envelopes.ResponseEnvelope.PlatformResponse.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='wuprotos.networking.envelopes.ResponseEnvelope.PlatformResponse.response', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=522,
  serialized_end=623,
)

_RESPONSEENVELOPE = _descriptor.Descriptor(
  name='ResponseEnvelope',
  full_name='wuprotos.networking.envelopes.ResponseEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_code', full_name='wuprotos.networking.envelopes.ResponseEnvelope.status_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='wuprotos.networking.envelopes.ResponseEnvelope.request_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_url', full_name='wuprotos.networking.envelopes.ResponseEnvelope.api_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='platform_returns', full_name='wuprotos.networking.envelopes.ResponseEnvelope.platform_returns', index=3,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_ticket', full_name='wuprotos.networking.envelopes.ResponseEnvelope.auth_ticket', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='returns', full_name='wuprotos.networking.envelopes.ResponseEnvelope.returns', index=5,
      number=100, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='wuprotos.networking.envelopes.ResponseEnvelope.error', index=6,
      number=101, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSEENVELOPE_PLATFORMRESPONSE, ],
  enum_types=[
    _RESPONSEENVELOPE_STATUSCODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=818,
)

_RESPONSEENVELOPE_PLATFORMRESPONSE.fields_by_name['type'].enum_type = wuprotos_dot_networking_dot_platform_dot_platform__request__type__pb2._PLATFORMREQUESTTYPE
_RESPONSEENVELOPE_PLATFORMRESPONSE.containing_type = _RESPONSEENVELOPE
_RESPONSEENVELOPE.fields_by_name['status_code'].enum_type = _RESPONSEENVELOPE_STATUSCODE
_RESPONSEENVELOPE.fields_by_name['platform_returns'].message_type = _RESPONSEENVELOPE_PLATFORMRESPONSE
_RESPONSEENVELOPE.fields_by_name['auth_ticket'].message_type = wuprotos_dot_networking_dot_envelopes_dot_auth__ticket__pb2._AUTHTICKET
_RESPONSEENVELOPE_STATUSCODE.containing_type = _RESPONSEENVELOPE
DESCRIPTOR.message_types_by_name['ResponseEnvelope'] = _RESPONSEENVELOPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseEnvelope = _reflection.GeneratedProtocolMessageType('ResponseEnvelope', (_message.Message,), dict(

  PlatformResponse = _reflection.GeneratedProtocolMessageType('PlatformResponse', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSEENVELOPE_PLATFORMRESPONSE,
    __module__ = 'wuprotos.networking.envelopes.response_envelope_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.networking.envelopes.ResponseEnvelope.PlatformResponse)
    ))
  ,
  DESCRIPTOR = _RESPONSEENVELOPE,
  __module__ = 'wuprotos.networking.envelopes.response_envelope_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.envelopes.ResponseEnvelope)
  ))
_sym_db.RegisterMessage(ResponseEnvelope)
_sym_db.RegisterMessage(ResponseEnvelope.PlatformResponse)


# @@protoc_insertion_point(module_scope)