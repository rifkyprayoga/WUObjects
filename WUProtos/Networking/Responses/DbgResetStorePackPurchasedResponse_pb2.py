# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Responses/DbgResetStorePackPurchasedResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Responses/DbgResetStorePackPurchasedResponse.proto',
  package='WUProtos.Networking.Responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nFWUProtos/Networking/Responses/DbgResetStorePackPurchasedResponse.proto\x12\x1dWUProtos.Networking.Responses\"8\n\"DbgResetStorePackPurchasedResponse\x12\x12\n\nsuccessful\x18\x01 \x01(\x08\x62\x06proto3')
)




_DBGRESETSTOREPACKPURCHASEDRESPONSE = _descriptor.Descriptor(
  name='DbgResetStorePackPurchasedResponse',
  full_name='WUProtos.Networking.Responses.DbgResetStorePackPurchasedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='successful', full_name='WUProtos.Networking.Responses.DbgResetStorePackPurchasedResponse.successful', index=0,
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
  serialized_start=105,
  serialized_end=161,
)

DESCRIPTOR.message_types_by_name['DbgResetStorePackPurchasedResponse'] = _DBGRESETSTOREPACKPURCHASEDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DbgResetStorePackPurchasedResponse = _reflection.GeneratedProtocolMessageType('DbgResetStorePackPurchasedResponse', (_message.Message,), dict(
  DESCRIPTOR = _DBGRESETSTOREPACKPURCHASEDRESPONSE,
  __module__ = 'WUProtos.Networking.Responses.DbgResetStorePackPurchasedResponse_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Responses.DbgResetStorePackPurchasedResponse)
  ))
_sym_db.RegisterMessage(DbgResetStorePackPurchasedResponse)


# @@protoc_insertion_point(module_scope)
