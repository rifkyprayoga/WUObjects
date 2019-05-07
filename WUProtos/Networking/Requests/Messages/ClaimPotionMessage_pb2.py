# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Requests/Messages/ClaimPotionMessage.proto

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
  name='WUProtos/Networking/Requests/Messages/ClaimPotionMessage.proto',
  package='WUProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n>WUProtos/Networking/Requests/Messages/ClaimPotionMessage.proto\x12%WUProtos.Networking.Requests.Messages\x1a\'WUProtos/Data/Loot/LootCollection.proto\"\x7f\n\x12\x43laimPotionMessage\x12\x13\n\x0b\x63\x61uldron_id\x18\x01 \x01(\x03\x12\x15\n\rcauldron_slot\x18\x02 \x01(\x05\x12=\n\x11requested_rewards\x18\x03 \x01(\x0b\x32\".WUProtos.Data.Loot.LootCollectionb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2.DESCRIPTOR,])




_CLAIMPOTIONMESSAGE = _descriptor.Descriptor(
  name='ClaimPotionMessage',
  full_name='WUProtos.Networking.Requests.Messages.ClaimPotionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cauldron_id', full_name='WUProtos.Networking.Requests.Messages.ClaimPotionMessage.cauldron_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cauldron_slot', full_name='WUProtos.Networking.Requests.Messages.ClaimPotionMessage.cauldron_slot', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requested_rewards', full_name='WUProtos.Networking.Requests.Messages.ClaimPotionMessage.requested_rewards', index=2,
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
  serialized_start=146,
  serialized_end=273,
)

_CLAIMPOTIONMESSAGE.fields_by_name['requested_rewards'].message_type = WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2._LOOTCOLLECTION
DESCRIPTOR.message_types_by_name['ClaimPotionMessage'] = _CLAIMPOTIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClaimPotionMessage = _reflection.GeneratedProtocolMessageType('ClaimPotionMessage', (_message.Message,), dict(
  DESCRIPTOR = _CLAIMPOTIONMESSAGE,
  __module__ = 'WUProtos.Networking.Requests.Messages.ClaimPotionMessage_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Requests.Messages.ClaimPotionMessage)
  ))
_sym_db.RegisterMessage(ClaimPotionMessage)


# @@protoc_insertion_point(module_scope)
