# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/encounter_spellcat_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/encounter_spellcat_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nFwuprotos/networking/requests/messages/encounter_spellcat_message.proto\x12%wuprotos.networking.requests.messages\"\x1a\n\x18\x45ncounterSpellcatMessageb\x06proto3')
)




_ENCOUNTERSPELLCATMESSAGE = _descriptor.Descriptor(
  name='EncounterSpellcatMessage',
  full_name='wuprotos.networking.requests.messages.EncounterSpellcatMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_end=139,
)

DESCRIPTOR.message_types_by_name['EncounterSpellcatMessage'] = _ENCOUNTERSPELLCATMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EncounterSpellcatMessage = _reflection.GeneratedProtocolMessageType('EncounterSpellcatMessage', (_message.Message,), dict(
  DESCRIPTOR = _ENCOUNTERSPELLCATMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.encounter_spellcat_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.EncounterSpellcatMessage)
  ))
_sym_db.RegisterMessage(EncounterSpellcatMessage)


# @@protoc_insertion_point(module_scope)