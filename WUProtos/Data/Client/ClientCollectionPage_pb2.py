# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientCollectionPage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientCollectionPage.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n/WUProtos/Data/Client/ClientCollectionPage.proto\x12\x14WUProtos.Data.Client\"j\n\x14\x43lientCollectionPage\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bpage_prefab\x18\x03 \x01(\t\x12\x0f\n\x07icon_bg\x18\x04 \x01(\t\x12\x12\n\nshow_in_ui\x18\x05 \x01(\x08\x62\x06proto3')
)




_CLIENTCOLLECTIONPAGE = _descriptor.Descriptor(
  name='ClientCollectionPage',
  full_name='WUProtos.Data.Client.ClientCollectionPage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.Client.ClientCollectionPage.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='WUProtos.Data.Client.ClientCollectionPage.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_prefab', full_name='WUProtos.Data.Client.ClientCollectionPage.page_prefab', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_bg', full_name='WUProtos.Data.Client.ClientCollectionPage.icon_bg', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_in_ui', full_name='WUProtos.Data.Client.ClientCollectionPage.show_in_ui', index=4,
      number=5, type=8, cpp_type=7, label=1,
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
  serialized_start=73,
  serialized_end=179,
)

DESCRIPTOR.message_types_by_name['ClientCollectionPage'] = _CLIENTCOLLECTIONPAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientCollectionPage = _reflection.GeneratedProtocolMessageType('ClientCollectionPage', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTCOLLECTIONPAGE,
  __module__ = 'WUProtos.Data.Client.ClientCollectionPage_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientCollectionPage)
  ))
_sym_db.RegisterMessage(ClientCollectionPage)


# @@protoc_insertion_point(module_scope)