# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Inventory/InventoryPortkeyItem.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Inventory/InventoryPortkeyItem.proto',
  package='WUProtos.Inventory',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n-WUProtos/Inventory/InventoryPortkeyItem.proto\x12\x12WUProtos.Inventory\"J\n\x14InventoryPortkeyItem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x13\n\x0btemplate_id\x18\x03 \x01(\tb\x06proto3')
)




_INVENTORYPORTKEYITEM = _descriptor.Descriptor(
  name='InventoryPortkeyItem',
  full_name='WUProtos.Inventory.InventoryPortkeyItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Inventory.InventoryPortkeyItem.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='WUProtos.Inventory.InventoryPortkeyItem.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='template_id', full_name='WUProtos.Inventory.InventoryPortkeyItem.template_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=69,
  serialized_end=143,
)

DESCRIPTOR.message_types_by_name['InventoryPortkeyItem'] = _INVENTORYPORTKEYITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InventoryPortkeyItem = _reflection.GeneratedProtocolMessageType('InventoryPortkeyItem', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYPORTKEYITEM,
  __module__ = 'WUProtos.Inventory.InventoryPortkeyItem_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Inventory.InventoryPortkeyItem)
  ))
_sym_db.RegisterMessage(InventoryPortkeyItem)


# @@protoc_insertion_point(module_scope)