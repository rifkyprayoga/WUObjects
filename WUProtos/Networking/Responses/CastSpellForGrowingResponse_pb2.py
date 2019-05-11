# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Responses/CastSpellForGrowingResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Responses/CastSpellForGrowingResponse.proto',
  package='WUProtos.Networking.Responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n?WUProtos/Networking/Responses/CastSpellForGrowingResponse.proto\x12\x1dWUProtos.Networking.Responses\"\x90\x02\n\x1b\x43\x61stSpellForGrowingResponse\x12Q\n\x06status\x18\x01 \x01(\x0e\x32\x41.WUProtos.Networking.Responses.CastSpellForGrowingResponse.Status\"\x9d\x01\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07TOO_FAR\x10\x02\x12\x0e\n\nPOI_CLOSED\x10\x03\x12\x14\n\x10\x46\x45\x41TURE_DISABLED\x10\x04\x12\x0f\n\x0bINVALID_POT\x10\x05\x12\x1b\n\x17NOT_ENOUGH_SPELL_ENERGY\x10\x06\x12\x1a\n\x16NO_GROWING_IN_PROGRESS\x10\x07\x62\x06proto3')
)



_CASTSPELLFORGROWINGRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='WUProtos.Networking.Responses.CastSpellForGrowingResponse.Status',
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
      name='TOO_FAR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POI_CLOSED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEATURE_DISABLED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_POT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_ENOUGH_SPELL_ENERGY', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_GROWING_IN_PROGRESS', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=214,
  serialized_end=371,
)
_sym_db.RegisterEnumDescriptor(_CASTSPELLFORGROWINGRESPONSE_STATUS)


_CASTSPELLFORGROWINGRESPONSE = _descriptor.Descriptor(
  name='CastSpellForGrowingResponse',
  full_name='WUProtos.Networking.Responses.CastSpellForGrowingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='WUProtos.Networking.Responses.CastSpellForGrowingResponse.status', index=0,
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
    _CASTSPELLFORGROWINGRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=371,
)

_CASTSPELLFORGROWINGRESPONSE.fields_by_name['status'].enum_type = _CASTSPELLFORGROWINGRESPONSE_STATUS
_CASTSPELLFORGROWINGRESPONSE_STATUS.containing_type = _CASTSPELLFORGROWINGRESPONSE
DESCRIPTOR.message_types_by_name['CastSpellForGrowingResponse'] = _CASTSPELLFORGROWINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CastSpellForGrowingResponse = _reflection.GeneratedProtocolMessageType('CastSpellForGrowingResponse', (_message.Message,), dict(
  DESCRIPTOR = _CASTSPELLFORGROWINGRESPONSE,
  __module__ = 'WUProtos.Networking.Responses.CastSpellForGrowingResponse_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Responses.CastSpellForGrowingResponse)
  ))
_sym_db.RegisterMessage(CastSpellForGrowingResponse)


# @@protoc_insertion_point(module_scope)