# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Envelopes/RequestEnvelope.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Networking.Requests import Request_pb2 as WUProtos_dot_Networking_dot_Requests_dot_Request__pb2
from WUProtos.Networking.Envelopes import AuthTicket_pb2 as WUProtos_dot_Networking_dot_Envelopes_dot_AuthTicket__pb2
from WUProtos.Networking.Platform import PlatformRequestType_pb2 as WUProtos_dot_Networking_dot_Platform_dot_PlatformRequestType__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Envelopes/RequestEnvelope.proto',
  package='WUProtos.Networking.Envelopes',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n3WUProtos/Networking/Envelopes/RequestEnvelope.proto\x12\x1dWUProtos.Networking.Envelopes\x1a*WUProtos/Networking/Requests/Request.proto\x1a.WUProtos/Networking/Envelopes/AuthTicket.proto\x1a\x36WUProtos/Networking/Platform/PlatformRequestType.proto\"\xbe\x06\n\x0fRequestEnvelope\x12\x13\n\x0bstatus_code\x18\x01 \x01(\x05\x12\x12\n\nrequest_id\x18\x03 \x01(\x04\x12\x37\n\x08requests\x18\x04 \x03(\x0b\x32%.WUProtos.Networking.Requests.Request\x12Y\n\x11platform_requests\x18\x06 \x03(\x0b\x32>.WUProtos.Networking.Envelopes.RequestEnvelope.PlatformRequest\x12\x10\n\x08latitude\x18\x07 \x01(\x01\x12\x11\n\tlongitude\x18\x08 \x01(\x01\x12\x10\n\x08\x61\x63\x63uracy\x18\t \x01(\x01\x12J\n\tauth_info\x18\n \x01(\x0b\x32\x37.WUProtos.Networking.Envelopes.RequestEnvelope.AuthInfo\x12>\n\x0b\x61uth_ticket\x18\x0b \x01(\x0b\x32).WUProtos.Networking.Envelopes.AuthTicket\x12!\n\x19ms_since_last_locationfix\x18\x0c \x01(\x03\x1a\x9a\x02\n\x08\x41uthInfo\x12\x10\n\x08provider\x18\x01 \x01(\t\x12J\n\x05token\x18\x02 \x01(\x0b\x32;.WUProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.JWT\x12T\n\x07options\x18\x03 \x01(\x0b\x32\x43.WUProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.AuthOptions\x1a)\n\x03JWT\x12\x10\n\x08\x63ontents\x18\x01 \x01(\t\x12\x10\n\x08unknown2\x18\x02 \x01(\x05\x1a/\n\x0b\x41uthOptions\x12 \n\x18prevent_account_creation\x18\x01 \x01(\x08\x1ak\n\x0fPlatformRequest\x12?\n\x04type\x18\x01 \x01(\x0e\x32\x31.WUProtos.Networking.Platform.PlatformRequestType\x12\x17\n\x0frequest_message\x18\x02 \x01(\x0c\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Networking_dot_Requests_dot_Request__pb2.DESCRIPTOR,WUProtos_dot_Networking_dot_Envelopes_dot_AuthTicket__pb2.DESCRIPTOR,WUProtos_dot_Networking_dot_Platform_dot_PlatformRequestType__pb2.DESCRIPTOR,])




_REQUESTENVELOPE_AUTHINFO_JWT = _descriptor.Descriptor(
  name='JWT',
  full_name='WUProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.JWT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contents', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.JWT.contents', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.JWT.unknown2', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=866,
  serialized_end=907,
)

_REQUESTENVELOPE_AUTHINFO_AUTHOPTIONS = _descriptor.Descriptor(
  name='AuthOptions',
  full_name='WUProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.AuthOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prevent_account_creation', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.AuthOptions.prevent_account_creation', index=0,
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
  serialized_start=909,
  serialized_end=956,
)

_REQUESTENVELOPE_AUTHINFO = _descriptor.Descriptor(
  name='AuthInfo',
  full_name='WUProtos.Networking.Envelopes.RequestEnvelope.AuthInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.provider', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.token', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.options', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOPE_AUTHINFO_JWT, _REQUESTENVELOPE_AUTHINFO_AUTHOPTIONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=674,
  serialized_end=956,
)

_REQUESTENVELOPE_PLATFORMREQUEST = _descriptor.Descriptor(
  name='PlatformRequest',
  full_name='WUProtos.Networking.Envelopes.RequestEnvelope.PlatformRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.PlatformRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_message', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.PlatformRequest.request_message', index=1,
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
  serialized_start=958,
  serialized_end=1065,
)

_REQUESTENVELOPE = _descriptor.Descriptor(
  name='RequestEnvelope',
  full_name='WUProtos.Networking.Envelopes.RequestEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_code', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.status_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.request_id', index=1,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requests', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.requests', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='platform_requests', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.platform_requests', index=3,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.latitude', index=4,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.longitude', index=5,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accuracy', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.accuracy', index=6,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_info', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.auth_info', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_ticket', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.auth_ticket', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ms_since_last_locationfix', full_name='WUProtos.Networking.Envelopes.RequestEnvelope.ms_since_last_locationfix', index=9,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOPE_AUTHINFO, _REQUESTENVELOPE_PLATFORMREQUEST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=235,
  serialized_end=1065,
)

_REQUESTENVELOPE_AUTHINFO_JWT.containing_type = _REQUESTENVELOPE_AUTHINFO
_REQUESTENVELOPE_AUTHINFO_AUTHOPTIONS.containing_type = _REQUESTENVELOPE_AUTHINFO
_REQUESTENVELOPE_AUTHINFO.fields_by_name['token'].message_type = _REQUESTENVELOPE_AUTHINFO_JWT
_REQUESTENVELOPE_AUTHINFO.fields_by_name['options'].message_type = _REQUESTENVELOPE_AUTHINFO_AUTHOPTIONS
_REQUESTENVELOPE_AUTHINFO.containing_type = _REQUESTENVELOPE
_REQUESTENVELOPE_PLATFORMREQUEST.fields_by_name['type'].enum_type = WUProtos_dot_Networking_dot_Platform_dot_PlatformRequestType__pb2._PLATFORMREQUESTTYPE
_REQUESTENVELOPE_PLATFORMREQUEST.containing_type = _REQUESTENVELOPE
_REQUESTENVELOPE.fields_by_name['requests'].message_type = WUProtos_dot_Networking_dot_Requests_dot_Request__pb2._REQUEST
_REQUESTENVELOPE.fields_by_name['platform_requests'].message_type = _REQUESTENVELOPE_PLATFORMREQUEST
_REQUESTENVELOPE.fields_by_name['auth_info'].message_type = _REQUESTENVELOPE_AUTHINFO
_REQUESTENVELOPE.fields_by_name['auth_ticket'].message_type = WUProtos_dot_Networking_dot_Envelopes_dot_AuthTicket__pb2._AUTHTICKET
DESCRIPTOR.message_types_by_name['RequestEnvelope'] = _REQUESTENVELOPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestEnvelope = _reflection.GeneratedProtocolMessageType('RequestEnvelope', (_message.Message,), dict(

  AuthInfo = _reflection.GeneratedProtocolMessageType('AuthInfo', (_message.Message,), dict(

    JWT = _reflection.GeneratedProtocolMessageType('JWT', (_message.Message,), dict(
      DESCRIPTOR = _REQUESTENVELOPE_AUTHINFO_JWT,
      __module__ = 'WUProtos.Networking.Envelopes.RequestEnvelope_pb2'
      # @@protoc_insertion_point(class_scope:WUProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.JWT)
      ))
    ,

    AuthOptions = _reflection.GeneratedProtocolMessageType('AuthOptions', (_message.Message,), dict(
      DESCRIPTOR = _REQUESTENVELOPE_AUTHINFO_AUTHOPTIONS,
      __module__ = 'WUProtos.Networking.Envelopes.RequestEnvelope_pb2'
      # @@protoc_insertion_point(class_scope:WUProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.AuthOptions)
      ))
    ,
    DESCRIPTOR = _REQUESTENVELOPE_AUTHINFO,
    __module__ = 'WUProtos.Networking.Envelopes.RequestEnvelope_pb2'
    # @@protoc_insertion_point(class_scope:WUProtos.Networking.Envelopes.RequestEnvelope.AuthInfo)
    ))
  ,

  PlatformRequest = _reflection.GeneratedProtocolMessageType('PlatformRequest', (_message.Message,), dict(
    DESCRIPTOR = _REQUESTENVELOPE_PLATFORMREQUEST,
    __module__ = 'WUProtos.Networking.Envelopes.RequestEnvelope_pb2'
    # @@protoc_insertion_point(class_scope:WUProtos.Networking.Envelopes.RequestEnvelope.PlatformRequest)
    ))
  ,
  DESCRIPTOR = _REQUESTENVELOPE,
  __module__ = 'WUProtos.Networking.Envelopes.RequestEnvelope_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Envelopes.RequestEnvelope)
  ))
_sym_db.RegisterMessage(RequestEnvelope)
_sym_db.RegisterMessage(RequestEnvelope.AuthInfo)
_sym_db.RegisterMessage(RequestEnvelope.AuthInfo.JWT)
_sym_db.RegisterMessage(RequestEnvelope.AuthInfo.AuthOptions)
_sym_db.RegisterMessage(RequestEnvelope.PlatformRequest)


# @@protoc_insertion_point(module_scope)