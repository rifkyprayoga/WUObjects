# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Inventory/InventoryEscrowedRewards.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Loot import LootCollection_pb2 as WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Inventory/InventoryEscrowedRewards.proto',
  package='WUProtos.Inventory',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n1WUProtos/Inventory/InventoryEscrowedRewards.proto\x12\x12WUProtos.Inventory\x1a\'WUProtos/Data/Loot/LootCollection.proto\"O\n\x18InventoryEscrowedRewards\x12\x33\n\x07rewards\x18\x01 \x01(\x0b\x32\".WUProtos.Data.Loot.LootCollectionb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2.DESCRIPTOR,])




_INVENTORYESCROWEDREWARDS = _descriptor.Descriptor(
  name='InventoryEscrowedRewards',
  full_name='WUProtos.Inventory.InventoryEscrowedRewards',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewards', full_name='WUProtos.Inventory.InventoryEscrowedRewards.rewards', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=114,
  serialized_end=193,
)

_INVENTORYESCROWEDREWARDS.fields_by_name['rewards'].message_type = WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2._LOOTCOLLECTION
DESCRIPTOR.message_types_by_name['InventoryEscrowedRewards'] = _INVENTORYESCROWEDREWARDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InventoryEscrowedRewards = _reflection.GeneratedProtocolMessageType('InventoryEscrowedRewards', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYESCROWEDREWARDS,
  __module__ = 'WUProtos.Inventory.InventoryEscrowedRewards_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Inventory.InventoryEscrowedRewards)
  ))
_sym_db.RegisterMessage(InventoryEscrowedRewards)


# @@protoc_insertion_point(module_scope)
