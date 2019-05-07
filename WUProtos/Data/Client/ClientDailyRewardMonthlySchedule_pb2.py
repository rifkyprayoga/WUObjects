# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientDailyRewardMonthlySchedule.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Client import ClientDailyReward_pb2 as WUProtos_dot_Data_dot_Client_dot_ClientDailyReward__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientDailyRewardMonthlySchedule.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n;WUProtos/Data/Client/ClientDailyRewardMonthlySchedule.proto\x12\x14WUProtos.Data.Client\x1a,WUProtos/Data/Client/ClientDailyReward.proto\"\xed\x01\n ClientDailyRewardMonthlySchedule\x12\n\n\x02id\x18\x01 \x01(\t\x12_\n\rdaily_rewards\x18\x02 \x03(\x0b\x32H.WUProtos.Data.Client.ClientDailyRewardMonthlySchedule.DailyRewardsEntry\x1a\\\n\x11\x44\x61ilyRewardsEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32\'.WUProtos.Data.Client.ClientDailyReward:\x02\x38\x01\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Client_dot_ClientDailyReward__pb2.DESCRIPTOR,])




_CLIENTDAILYREWARDMONTHLYSCHEDULE_DAILYREWARDSENTRY = _descriptor.Descriptor(
  name='DailyRewardsEntry',
  full_name='WUProtos.Data.Client.ClientDailyRewardMonthlySchedule.DailyRewardsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='WUProtos.Data.Client.ClientDailyRewardMonthlySchedule.DailyRewardsEntry.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='WUProtos.Data.Client.ClientDailyRewardMonthlySchedule.DailyRewardsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=369,
)

_CLIENTDAILYREWARDMONTHLYSCHEDULE = _descriptor.Descriptor(
  name='ClientDailyRewardMonthlySchedule',
  full_name='WUProtos.Data.Client.ClientDailyRewardMonthlySchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.Client.ClientDailyRewardMonthlySchedule.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='daily_rewards', full_name='WUProtos.Data.Client.ClientDailyRewardMonthlySchedule.daily_rewards', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CLIENTDAILYREWARDMONTHLYSCHEDULE_DAILYREWARDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=369,
)

_CLIENTDAILYREWARDMONTHLYSCHEDULE_DAILYREWARDSENTRY.fields_by_name['value'].message_type = WUProtos_dot_Data_dot_Client_dot_ClientDailyReward__pb2._CLIENTDAILYREWARD
_CLIENTDAILYREWARDMONTHLYSCHEDULE_DAILYREWARDSENTRY.containing_type = _CLIENTDAILYREWARDMONTHLYSCHEDULE
_CLIENTDAILYREWARDMONTHLYSCHEDULE.fields_by_name['daily_rewards'].message_type = _CLIENTDAILYREWARDMONTHLYSCHEDULE_DAILYREWARDSENTRY
DESCRIPTOR.message_types_by_name['ClientDailyRewardMonthlySchedule'] = _CLIENTDAILYREWARDMONTHLYSCHEDULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientDailyRewardMonthlySchedule = _reflection.GeneratedProtocolMessageType('ClientDailyRewardMonthlySchedule', (_message.Message,), dict(

  DailyRewardsEntry = _reflection.GeneratedProtocolMessageType('DailyRewardsEntry', (_message.Message,), dict(
    DESCRIPTOR = _CLIENTDAILYREWARDMONTHLYSCHEDULE_DAILYREWARDSENTRY,
    __module__ = 'WUProtos.Data.Client.ClientDailyRewardMonthlySchedule_pb2'
    # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientDailyRewardMonthlySchedule.DailyRewardsEntry)
    ))
  ,
  DESCRIPTOR = _CLIENTDAILYREWARDMONTHLYSCHEDULE,
  __module__ = 'WUProtos.Data.Client.ClientDailyRewardMonthlySchedule_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientDailyRewardMonthlySchedule)
  ))
_sym_db.RegisterMessage(ClientDailyRewardMonthlySchedule)
_sym_db.RegisterMessage(ClientDailyRewardMonthlySchedule.DailyRewardsEntry)


_CLIENTDAILYREWARDMONTHLYSCHEDULE_DAILYREWARDSENTRY._options = None
# @@protoc_insertion_point(module_scope)
