# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientGameDataWrapper.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Client import ClientGmTemplate_pb2 as WUProtos_dot_Data_dot_Client_dot_ClientGmTemplate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientGameDataWrapper.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n0WUProtos/Data/Client/ClientGameDataWrapper.proto\x12\x14WUProtos.Data.Client\x1a+WUProtos/Data/Client/ClientGmTemplate.proto\"Q\n\x15\x43lientGameDataWrapper\x12\x38\n\x08messages\x18\x01 \x03(\x0b\x32&.WUProtos.Data.Client.ClientGmTemplateb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Client_dot_ClientGmTemplate__pb2.DESCRIPTOR,])




_CLIENTGAMEDATAWRAPPER = _descriptor.Descriptor(
  name='ClientGameDataWrapper',
  full_name='WUProtos.Data.Client.ClientGameDataWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='WUProtos.Data.Client.ClientGameDataWrapper.messages', index=0,
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
  serialized_start=119,
  serialized_end=200,
)

_CLIENTGAMEDATAWRAPPER.fields_by_name['messages'].message_type = WUProtos_dot_Data_dot_Client_dot_ClientGmTemplate__pb2._CLIENTGMTEMPLATE
DESCRIPTOR.message_types_by_name['ClientGameDataWrapper'] = _CLIENTGAMEDATAWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientGameDataWrapper = _reflection.GeneratedProtocolMessageType('ClientGameDataWrapper', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTGAMEDATAWRAPPER,
  __module__ = 'WUProtos.Data.Client.ClientGameDataWrapper_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientGameDataWrapper)
  ))
_sym_db.RegisterMessage(ClientGameDataWrapper)


# @@protoc_insertion_point(module_scope)