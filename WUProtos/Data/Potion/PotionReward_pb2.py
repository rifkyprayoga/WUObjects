# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Potion/PotionReward.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Potion/PotionReward.proto',
  package='WUProtos.Data.Potion',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\'WUProtos/Data/Potion/PotionReward.proto\x12\x14WUProtos.Data.Potion\"P\n\x0cPotionReward\x12\x14\n\x0ctime_to_brew\x18\x02 \x01(\x03\x12\x13\n\x0b\x63\x61uldron_id\x18\x03 \x01(\x03\x12\x15\n\rrecipe_gmt_id\x18\x04 \x01(\tb\x06proto3')
)




_POTIONREWARD = _descriptor.Descriptor(
  name='PotionReward',
  full_name='WUProtos.Data.Potion.PotionReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_to_brew', full_name='WUProtos.Data.Potion.PotionReward.time_to_brew', index=0,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cauldron_id', full_name='WUProtos.Data.Potion.PotionReward.cauldron_id', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recipe_gmt_id', full_name='WUProtos.Data.Potion.PotionReward.recipe_gmt_id', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=65,
  serialized_end=145,
)

DESCRIPTOR.message_types_by_name['PotionReward'] = _POTIONREWARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PotionReward = _reflection.GeneratedProtocolMessageType('PotionReward', (_message.Message,), dict(
  DESCRIPTOR = _POTIONREWARD,
  __module__ = 'WUProtos.Data.Potion.PotionReward_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Potion.PotionReward)
  ))
_sym_db.RegisterMessage(PotionReward)


# @@protoc_insertion_point(module_scope)
