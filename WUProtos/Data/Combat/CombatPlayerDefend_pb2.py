# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Combat/CombatPlayerDefend.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Combat/CombatPlayerDefend.proto',
  package='WUProtos.Data.Combat',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n-WUProtos/Data/Combat/CombatPlayerDefend.proto\x12\x14WUProtos.Data.Combat\"\x14\n\x12\x43ombatPlayerDefendb\x06proto3')
)




_COMBATPLAYERDEFEND = _descriptor.Descriptor(
  name='CombatPlayerDefend',
  full_name='WUProtos.Data.Combat.CombatPlayerDefend',
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
  serialized_start=71,
  serialized_end=91,
)

DESCRIPTOR.message_types_by_name['CombatPlayerDefend'] = _COMBATPLAYERDEFEND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatPlayerDefend = _reflection.GeneratedProtocolMessageType('CombatPlayerDefend', (_message.Message,), dict(
  DESCRIPTOR = _COMBATPLAYERDEFEND,
  __module__ = 'WUProtos.Data.Combat.CombatPlayerDefend_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Combat.CombatPlayerDefend)
  ))
_sym_db.RegisterMessage(CombatPlayerDefend)


# @@protoc_insertion_point(module_scope)