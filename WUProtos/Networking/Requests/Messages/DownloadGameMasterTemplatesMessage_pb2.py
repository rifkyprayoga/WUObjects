# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Requests/Messages/DownloadGameMasterTemplatesMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Requests/Messages/DownloadGameMasterTemplatesMessage.proto',
  package='WUProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nNWUProtos/Networking/Requests/Messages/DownloadGameMasterTemplatesMessage.proto\x12%WUProtos.Networking.Requests.Messages\"c\n\"DownloadGameMasterTemplatesMessage\x12\x16\n\x0e\x62\x61sis_batch_id\x18\x01 \x01(\x03\x12\x10\n\x08\x62\x61tch_id\x18\x02 \x01(\x03\x12\x13\n\x0bpage_offset\x18\x03 \x01(\x05\x62\x06proto3')
)




_DOWNLOADGAMEMASTERTEMPLATESMESSAGE = _descriptor.Descriptor(
  name='DownloadGameMasterTemplatesMessage',
  full_name='WUProtos.Networking.Requests.Messages.DownloadGameMasterTemplatesMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='basis_batch_id', full_name='WUProtos.Networking.Requests.Messages.DownloadGameMasterTemplatesMessage.basis_batch_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_id', full_name='WUProtos.Networking.Requests.Messages.DownloadGameMasterTemplatesMessage.batch_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_offset', full_name='WUProtos.Networking.Requests.Messages.DownloadGameMasterTemplatesMessage.page_offset', index=2,
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
  serialized_start=121,
  serialized_end=220,
)

DESCRIPTOR.message_types_by_name['DownloadGameMasterTemplatesMessage'] = _DOWNLOADGAMEMASTERTEMPLATESMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DownloadGameMasterTemplatesMessage = _reflection.GeneratedProtocolMessageType('DownloadGameMasterTemplatesMessage', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADGAMEMASTERTEMPLATESMESSAGE,
  __module__ = 'WUProtos.Networking.Requests.Messages.DownloadGameMasterTemplatesMessage_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Requests.Messages.DownloadGameMasterTemplatesMessage)
  ))
_sym_db.RegisterMessage(DownloadGameMasterTemplatesMessage)


# @@protoc_insertion_point(module_scope)
