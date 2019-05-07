# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Requests/Messages/EncounterInteractMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Encounter import EncounterInteractStageOptions_pb2 as WUProtos_dot_Data_dot_Encounter_dot_EncounterInteractStageOptions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Requests/Messages/EncounterInteractMessage.proto',
  package='WUProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nDWUProtos/Networking/Requests/Messages/EncounterInteractMessage.proto\x12%WUProtos.Networking.Requests.Messages\x1a;WUProtos/Data/Encounter/EncounterInteractStageOptions.proto\"\x7f\n\x18\x45ncounterInteractMessage\x12\x14\n\x0c\x65ncounter_id\x18\x01 \x01(\x0c\x12M\n\rstage_options\x18\x02 \x01(\x0b\x32\x36.WUProtos.Data.Encounter.EncounterInteractStageOptionsb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Encounter_dot_EncounterInteractStageOptions__pb2.DESCRIPTOR,])




_ENCOUNTERINTERACTMESSAGE = _descriptor.Descriptor(
  name='EncounterInteractMessage',
  full_name='WUProtos.Networking.Requests.Messages.EncounterInteractMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encounter_id', full_name='WUProtos.Networking.Requests.Messages.EncounterInteractMessage.encounter_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stage_options', full_name='WUProtos.Networking.Requests.Messages.EncounterInteractMessage.stage_options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=172,
  serialized_end=299,
)

_ENCOUNTERINTERACTMESSAGE.fields_by_name['stage_options'].message_type = WUProtos_dot_Data_dot_Encounter_dot_EncounterInteractStageOptions__pb2._ENCOUNTERINTERACTSTAGEOPTIONS
DESCRIPTOR.message_types_by_name['EncounterInteractMessage'] = _ENCOUNTERINTERACTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EncounterInteractMessage = _reflection.GeneratedProtocolMessageType('EncounterInteractMessage', (_message.Message,), dict(
  DESCRIPTOR = _ENCOUNTERINTERACTMESSAGE,
  __module__ = 'WUProtos.Networking.Requests.Messages.EncounterInteractMessage_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Requests.Messages.EncounterInteractMessage)
  ))
_sym_db.RegisterMessage(EncounterInteractMessage)


# @@protoc_insertion_point(module_scope)
