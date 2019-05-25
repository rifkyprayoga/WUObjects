# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/storyboard_do_step_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wuprotos.data.loot import loot_reward_pb2 as wuprotos_dot_data_dot_loot_dot_loot__reward__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/storyboard_do_step_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n?wuprotos/networking/responses/storyboard_do_step_response.proto\x12\x1dwuprotos.networking.responses\x1a$wuprotos/data/loot/loot_reward.proto\"\xf7\x03\n\x18StoryboardDoStepResponse\x12N\n\x06status\x18\x01 \x01(\x0e\x32>.wuprotos.networking.responses.StoryboardDoStepResponse.Status\x12>\n\x07rewards\x18\x02 \x01(\x0b\x32-.wuprotos.data.loot.LootReward.LootCollection\"\xca\x02\n\x06Status\x12\x1e\n\x1aSTORYBOARD_DO_STEP_UNKNOWN\x10\x00\x12\x1e\n\x1aSTORYBOARD_DO_STEP_SUCCESS\x10\x01\x12&\n\"STORYBOARD_DO_STEP_BAD_STEP_NUMBER\x10\x02\x12\'\n#STORYBOARD_DO_STEP_NO_RESET_ALLOWED\x10\x03\x12\x30\n,STORYBOARD_DO_STEP_RESET_REQUIREMENTS_FAILED\x10\x04\x12\x30\n,STORYBOARD_DO_STEP_START_REQUIREMENTS_FAILED\x10\x05\x12\x1c\n\x18STORYBOARD_DO_STEP_ERROR\x10\x06\x12-\n)STORYBOARD_DO_STEP_SUCCESS_AND_COMPLETION\x10\x07\x62\x06proto3')
  ,
  dependencies=[wuprotos_dot_data_dot_loot_dot_loot__reward__pb2.DESCRIPTOR,])



_STORYBOARDDOSTEPRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='wuprotos.networking.responses.StoryboardDoStepResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STORYBOARD_DO_STEP_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORYBOARD_DO_STEP_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORYBOARD_DO_STEP_BAD_STEP_NUMBER', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORYBOARD_DO_STEP_NO_RESET_ALLOWED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORYBOARD_DO_STEP_RESET_REQUIREMENTS_FAILED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORYBOARD_DO_STEP_START_REQUIREMENTS_FAILED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORYBOARD_DO_STEP_ERROR', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORYBOARD_DO_STEP_SUCCESS_AND_COMPLETION', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=310,
  serialized_end=640,
)
_sym_db.RegisterEnumDescriptor(_STORYBOARDDOSTEPRESPONSE_STATUS)


_STORYBOARDDOSTEPRESPONSE = _descriptor.Descriptor(
  name='StoryboardDoStepResponse',
  full_name='wuprotos.networking.responses.StoryboardDoStepResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wuprotos.networking.responses.StoryboardDoStepResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rewards', full_name='wuprotos.networking.responses.StoryboardDoStepResponse.rewards', index=1,
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
    _STORYBOARDDOSTEPRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=640,
)

_STORYBOARDDOSTEPRESPONSE.fields_by_name['status'].enum_type = _STORYBOARDDOSTEPRESPONSE_STATUS
_STORYBOARDDOSTEPRESPONSE.fields_by_name['rewards'].message_type = wuprotos_dot_data_dot_loot_dot_loot__reward__pb2._LOOTREWARD_LOOTCOLLECTION
_STORYBOARDDOSTEPRESPONSE_STATUS.containing_type = _STORYBOARDDOSTEPRESPONSE
DESCRIPTOR.message_types_by_name['StoryboardDoStepResponse'] = _STORYBOARDDOSTEPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StoryboardDoStepResponse = _reflection.GeneratedProtocolMessageType('StoryboardDoStepResponse', (_message.Message,), dict(
  DESCRIPTOR = _STORYBOARDDOSTEPRESPONSE,
  __module__ = 'wuprotos.networking.responses.storyboard_do_step_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.StoryboardDoStepResponse)
  ))
_sym_db.RegisterMessage(StoryboardDoStepResponse)


# @@protoc_insertion_point(module_scope)