# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/QuestProgress.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import RequirementsQuestProgress_pb2 as WUProtos_dot_Data_dot_RequirementsQuestProgress__pb2
from WUProtos.Data import HookQuestProgress_pb2 as WUProtos_dot_Data_dot_HookQuestProgress__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/QuestProgress.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!WUProtos/Data/QuestProgress.proto\x12\rWUProtos.Data\x1a-WUProtos/Data/RequirementsQuestProgress.proto\x1a%WUProtos/Data/HookQuestProgress.proto\"\x94\x01\n\rQuestProgress\x12@\n\x0creq_progress\x18\x01 \x01(\x0b\x32(.WUProtos.Data.RequirementsQuestProgressH\x00\x12\x39\n\rhook_progress\x18\x02 \x01(\x0b\x32 .WUProtos.Data.HookQuestProgressH\x00\x42\x06\n\x04Typeb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_RequirementsQuestProgress__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_HookQuestProgress__pb2.DESCRIPTOR,])




_QUESTPROGRESS = _descriptor.Descriptor(
  name='QuestProgress',
  full_name='WUProtos.Data.QuestProgress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='req_progress', full_name='WUProtos.Data.QuestProgress.req_progress', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hook_progress', full_name='WUProtos.Data.QuestProgress.hook_progress', index=1,
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
    _descriptor.OneofDescriptor(
      name='Type', full_name='WUProtos.Data.QuestProgress.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=139,
  serialized_end=287,
)

_QUESTPROGRESS.fields_by_name['req_progress'].message_type = WUProtos_dot_Data_dot_RequirementsQuestProgress__pb2._REQUIREMENTSQUESTPROGRESS
_QUESTPROGRESS.fields_by_name['hook_progress'].message_type = WUProtos_dot_Data_dot_HookQuestProgress__pb2._HOOKQUESTPROGRESS
_QUESTPROGRESS.oneofs_by_name['Type'].fields.append(
  _QUESTPROGRESS.fields_by_name['req_progress'])
_QUESTPROGRESS.fields_by_name['req_progress'].containing_oneof = _QUESTPROGRESS.oneofs_by_name['Type']
_QUESTPROGRESS.oneofs_by_name['Type'].fields.append(
  _QUESTPROGRESS.fields_by_name['hook_progress'])
_QUESTPROGRESS.fields_by_name['hook_progress'].containing_oneof = _QUESTPROGRESS.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['QuestProgress'] = _QUESTPROGRESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QuestProgress = _reflection.GeneratedProtocolMessageType('QuestProgress', (_message.Message,), dict(
  DESCRIPTOR = _QUESTPROGRESS,
  __module__ = 'WUProtos.Data.QuestProgress_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.QuestProgress)
  ))
_sym_db.RegisterMessage(QuestProgress)


# @@protoc_insertion_point(module_scope)
