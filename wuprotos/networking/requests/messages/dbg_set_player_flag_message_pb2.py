# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/dbg_set_player_flag_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/dbg_set_player_flag_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nGwuprotos/networking/requests/messages/dbg_set_player_flag_message.proto\x12%wuprotos.networking.requests.messages\"{\n\x17\x44\x62gSetPlayerFlagMessage\x12\x17\n\x0f\x66\x65\x61ture_flag_id\x18\x01 \x01(\t\x12\x0e\n\x04\x62val\x18\x02 \x01(\x08H\x00\x12\x0e\n\x04lval\x18\x03 \x01(\x03H\x00\x12\x0e\n\x04sval\x18\x04 \x01(\tH\x00\x12\x0e\n\x04\x66val\x18\x05 \x01(\x02H\x00\x42\x07\n\x05Valueb\x06proto3')
)




_DBGSETPLAYERFLAGMESSAGE = _descriptor.Descriptor(
  name='DbgSetPlayerFlagMessage',
  full_name='wuprotos.networking.requests.messages.DbgSetPlayerFlagMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_flag_id', full_name='wuprotos.networking.requests.messages.DbgSetPlayerFlagMessage.feature_flag_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bval', full_name='wuprotos.networking.requests.messages.DbgSetPlayerFlagMessage.bval', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lval', full_name='wuprotos.networking.requests.messages.DbgSetPlayerFlagMessage.lval', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sval', full_name='wuprotos.networking.requests.messages.DbgSetPlayerFlagMessage.sval', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fval', full_name='wuprotos.networking.requests.messages.DbgSetPlayerFlagMessage.fval', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
      name='Value', full_name='wuprotos.networking.requests.messages.DbgSetPlayerFlagMessage.Value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=114,
  serialized_end=237,
)

_DBGSETPLAYERFLAGMESSAGE.oneofs_by_name['Value'].fields.append(
  _DBGSETPLAYERFLAGMESSAGE.fields_by_name['bval'])
_DBGSETPLAYERFLAGMESSAGE.fields_by_name['bval'].containing_oneof = _DBGSETPLAYERFLAGMESSAGE.oneofs_by_name['Value']
_DBGSETPLAYERFLAGMESSAGE.oneofs_by_name['Value'].fields.append(
  _DBGSETPLAYERFLAGMESSAGE.fields_by_name['lval'])
_DBGSETPLAYERFLAGMESSAGE.fields_by_name['lval'].containing_oneof = _DBGSETPLAYERFLAGMESSAGE.oneofs_by_name['Value']
_DBGSETPLAYERFLAGMESSAGE.oneofs_by_name['Value'].fields.append(
  _DBGSETPLAYERFLAGMESSAGE.fields_by_name['sval'])
_DBGSETPLAYERFLAGMESSAGE.fields_by_name['sval'].containing_oneof = _DBGSETPLAYERFLAGMESSAGE.oneofs_by_name['Value']
_DBGSETPLAYERFLAGMESSAGE.oneofs_by_name['Value'].fields.append(
  _DBGSETPLAYERFLAGMESSAGE.fields_by_name['fval'])
_DBGSETPLAYERFLAGMESSAGE.fields_by_name['fval'].containing_oneof = _DBGSETPLAYERFLAGMESSAGE.oneofs_by_name['Value']
DESCRIPTOR.message_types_by_name['DbgSetPlayerFlagMessage'] = _DBGSETPLAYERFLAGMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DbgSetPlayerFlagMessage = _reflection.GeneratedProtocolMessageType('DbgSetPlayerFlagMessage', (_message.Message,), dict(
  DESCRIPTOR = _DBGSETPLAYERFLAGMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.dbg_set_player_flag_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.DbgSetPlayerFlagMessage)
  ))
_sym_db.RegisterMessage(DbgSetPlayerFlagMessage)


# @@protoc_insertion_point(module_scope)