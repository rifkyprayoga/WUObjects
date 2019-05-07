# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/MasterNote.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Enums import MasterNoteGesture_pb2 as WUProtos_dot_Enums_dot_MasterNoteGesture__pb2
from WUProtos.Data import MasterNoteEffect_pb2 as WUProtos_dot_Data_dot_MasterNoteEffect__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/MasterNote.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1eWUProtos/Data/MasterNote.proto\x12\rWUProtos.Data\x1a&WUProtos/Enums/MasterNoteGesture.proto\x1a$WUProtos/Data/MasterNoteEffect.proto\"~\n\nMasterNote\x12\n\n\x02id\x18\x01 \x01(\t\x12\x33\n\x08gestures\x18\x02 \x03(\x0e\x32!.WUProtos.Enums.MasterNoteGesture\x12/\n\x06\x65\x66\x66\x65\x63t\x18\x03 \x01(\x0b\x32\x1f.WUProtos.Data.MasterNoteEffectb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Enums_dot_MasterNoteGesture__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_MasterNoteEffect__pb2.DESCRIPTOR,])




_MASTERNOTE = _descriptor.Descriptor(
  name='MasterNote',
  full_name='WUProtos.Data.MasterNote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.MasterNote.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gestures', full_name='WUProtos.Data.MasterNote.gestures', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='effect', full_name='WUProtos.Data.MasterNote.effect', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=127,
  serialized_end=253,
)

_MASTERNOTE.fields_by_name['gestures'].enum_type = WUProtos_dot_Enums_dot_MasterNoteGesture__pb2._MASTERNOTEGESTURE
_MASTERNOTE.fields_by_name['effect'].message_type = WUProtos_dot_Data_dot_MasterNoteEffect__pb2._MASTERNOTEEFFECT
DESCRIPTOR.message_types_by_name['MasterNote'] = _MASTERNOTE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MasterNote = _reflection.GeneratedProtocolMessageType('MasterNote', (_message.Message,), dict(
  DESCRIPTOR = _MASTERNOTE,
  __module__ = 'WUProtos.Data.MasterNote_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.MasterNote)
  ))
_sym_db.RegisterMessage(MasterNote)


# @@protoc_insertion_point(module_scope)
