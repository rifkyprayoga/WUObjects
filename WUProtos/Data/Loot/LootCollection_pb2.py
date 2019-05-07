# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Loot/LootCollection.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Loot import LootReward_pb2 as WUProtos_dot_Data_dot_Loot_dot_LootReward__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Loot/LootCollection.proto',
  package='WUProtos.Data.Loot',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\'WUProtos/Data/Loot/LootCollection.proto\x12\x12WUProtos.Data.Loot\x1a#WUProtos/Data/Loot/LootReward.proto\"{\n\x0eLootCollection\x12/\n\x07rewards\x18\x01 \x03(\x0b\x32\x1e.WUProtos.Data.Loot.LootReward\x12\x38\n\x10\x65scrowed_rewards\x18\x02 \x03(\x0b\x32\x1e.WUProtos.Data.Loot.LootRewardb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Loot_dot_LootReward__pb2.DESCRIPTOR,])




_LOOTCOLLECTION = _descriptor.Descriptor(
  name='LootCollection',
  full_name='WUProtos.Data.Loot.LootCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewards', full_name='WUProtos.Data.Loot.LootCollection.rewards', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='escrowed_rewards', full_name='WUProtos.Data.Loot.LootCollection.escrowed_rewards', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=100,
  serialized_end=223,
)

_LOOTCOLLECTION.fields_by_name['rewards'].message_type = WUProtos_dot_Data_dot_Loot_dot_LootReward__pb2._LOOTREWARD
_LOOTCOLLECTION.fields_by_name['escrowed_rewards'].message_type = WUProtos_dot_Data_dot_Loot_dot_LootReward__pb2._LOOTREWARD
DESCRIPTOR.message_types_by_name['LootCollection'] = _LOOTCOLLECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LootCollection = _reflection.GeneratedProtocolMessageType('LootCollection', (_message.Message,), dict(
  DESCRIPTOR = _LOOTCOLLECTION,
  __module__ = 'WUProtos.Data.Loot.LootCollection_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Loot.LootCollection)
  ))
_sym_db.RegisterMessage(LootCollection)


# @@protoc_insertion_point(module_scope)
