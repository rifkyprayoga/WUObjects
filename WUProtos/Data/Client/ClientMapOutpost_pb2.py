# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientMapOutpost.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Client import ClientDarkDetectorAmplifier_pb2 as WUProtos_dot_Data_dot_Client_dot_ClientDarkDetectorAmplifier__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientMapOutpost.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n+WUProtos/Data/Client/ClientMapOutpost.proto\x12\x14WUProtos.Data.Client\x1a\x36WUProtos/Data/Client/ClientDarkDetectorAmplifier.proto\"\x9f\x01\n\x10\x43lientMapOutpost\x12\x16\n\x0enext_loot_time\x18\x01 \x01(\x03\x12R\n\x17\x64\x61rk_detector_amplifier\x18\x02 \x01(\x0b\x32\x31.WUProtos.Data.Client.ClientDarkDetectorAmplifier\x12\x1f\n\x17outpost_template_gmt_id\x18\x03 \x01(\tb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Client_dot_ClientDarkDetectorAmplifier__pb2.DESCRIPTOR,])




_CLIENTMAPOUTPOST = _descriptor.Descriptor(
  name='ClientMapOutpost',
  full_name='WUProtos.Data.Client.ClientMapOutpost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_loot_time', full_name='WUProtos.Data.Client.ClientMapOutpost.next_loot_time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dark_detector_amplifier', full_name='WUProtos.Data.Client.ClientMapOutpost.dark_detector_amplifier', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outpost_template_gmt_id', full_name='WUProtos.Data.Client.ClientMapOutpost.outpost_template_gmt_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=126,
  serialized_end=285,
)

_CLIENTMAPOUTPOST.fields_by_name['dark_detector_amplifier'].message_type = WUProtos_dot_Data_dot_Client_dot_ClientDarkDetectorAmplifier__pb2._CLIENTDARKDETECTORAMPLIFIER
DESCRIPTOR.message_types_by_name['ClientMapOutpost'] = _CLIENTMAPOUTPOST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientMapOutpost = _reflection.GeneratedProtocolMessageType('ClientMapOutpost', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTMAPOUTPOST,
  __module__ = 'WUProtos.Data.Client.ClientMapOutpost_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientMapOutpost)
  ))
_sym_db.RegisterMessage(ClientMapOutpost)


# @@protoc_insertion_point(module_scope)
