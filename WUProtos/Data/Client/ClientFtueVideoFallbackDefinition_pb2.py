# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientFtueVideoFallbackDefinition.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Client import ClientFtueVideoNameDefinition_pb2 as WUProtos_dot_Data_dot_Client_dot_ClientFtueVideoNameDefinition__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientFtueVideoFallbackDefinition.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n<WUProtos/Data/Client/ClientFtueVideoFallbackDefinition.proto\x12\x14WUProtos.Data.Client\x1a\x38WUProtos/Data/Client/ClientFtueVideoNameDefinition.proto\"r\n!ClientFtueVideoFallbackDefinition\x12M\n\x10name_definitions\x18\x01 \x03(\x0b\x32\x33.WUProtos.Data.Client.ClientFtueVideoNameDefinitionb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Client_dot_ClientFtueVideoNameDefinition__pb2.DESCRIPTOR,])




_CLIENTFTUEVIDEOFALLBACKDEFINITION = _descriptor.Descriptor(
  name='ClientFtueVideoFallbackDefinition',
  full_name='WUProtos.Data.Client.ClientFtueVideoFallbackDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name_definitions', full_name='WUProtos.Data.Client.ClientFtueVideoFallbackDefinition.name_definitions', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=144,
  serialized_end=258,
)

_CLIENTFTUEVIDEOFALLBACKDEFINITION.fields_by_name['name_definitions'].message_type = WUProtos_dot_Data_dot_Client_dot_ClientFtueVideoNameDefinition__pb2._CLIENTFTUEVIDEONAMEDEFINITION
DESCRIPTOR.message_types_by_name['ClientFtueVideoFallbackDefinition'] = _CLIENTFTUEVIDEOFALLBACKDEFINITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientFtueVideoFallbackDefinition = _reflection.GeneratedProtocolMessageType('ClientFtueVideoFallbackDefinition', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTFTUEVIDEOFALLBACKDEFINITION,
  __module__ = 'WUProtos.Data.Client.ClientFtueVideoFallbackDefinition_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientFtueVideoFallbackDefinition)
  ))
_sym_db.RegisterMessage(ClientFtueVideoFallbackDefinition)


# @@protoc_insertion_point(module_scope)