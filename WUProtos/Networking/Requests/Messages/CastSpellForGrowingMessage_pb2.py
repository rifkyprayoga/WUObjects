# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Requests/Messages/CastSpellForGrowingMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Requests/Messages/CastSpellForGrowingMessage.proto',
  package='WUProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nFWUProtos/Networking/Requests/Messages/CastSpellForGrowingMessage.proto\x12%WUProtos.Networking.Requests.Messages\"V\n\x1a\x43\x61stSpellForGrowingMessage\x12\x12\n\noutpost_id\x18\x01 \x01(\t\x12\x0e\n\x06pot_id\x18\x02 \x01(\t\x12\x14\n\x0cspell_energy\x18\x03 \x01(\x05\x62\x06proto3')
)




_CASTSPELLFORGROWINGMESSAGE = _descriptor.Descriptor(
  name='CastSpellForGrowingMessage',
  full_name='WUProtos.Networking.Requests.Messages.CastSpellForGrowingMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outpost_id', full_name='WUProtos.Networking.Requests.Messages.CastSpellForGrowingMessage.outpost_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pot_id', full_name='WUProtos.Networking.Requests.Messages.CastSpellForGrowingMessage.pot_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spell_energy', full_name='WUProtos.Networking.Requests.Messages.CastSpellForGrowingMessage.spell_energy', index=2,
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
  serialized_start=113,
  serialized_end=199,
)

DESCRIPTOR.message_types_by_name['CastSpellForGrowingMessage'] = _CASTSPELLFORGROWINGMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CastSpellForGrowingMessage = _reflection.GeneratedProtocolMessageType('CastSpellForGrowingMessage', (_message.Message,), dict(
  DESCRIPTOR = _CASTSPELLFORGROWINGMESSAGE,
  __module__ = 'WUProtos.Networking.Requests.Messages.CastSpellForGrowingMessage_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Requests.Messages.CastSpellForGrowingMessage)
  ))
_sym_db.RegisterMessage(CastSpellForGrowingMessage)


# @@protoc_insertion_point(module_scope)
