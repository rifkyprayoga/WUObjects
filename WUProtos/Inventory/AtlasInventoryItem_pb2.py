# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Inventory/AtlasInventoryItem.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Player import PlayerProfile_pb2 as WUProtos_dot_Data_dot_Player_dot_PlayerProfile__pb2
from WUProtos.Data.Player import PlayerProfessionsProgressV3_pb2 as WUProtos_dot_Data_dot_Player_dot_PlayerProfessionsProgressV3__pb2
from WUProtos.Data import LifetimeMetrics_pb2 as WUProtos_dot_Data_dot_LifetimeMetrics__pb2
from WUProtos.Inventory import InventoryVaultItem_pb2 as WUProtos_dot_Inventory_dot_InventoryVaultItem__pb2
from WUProtos.Inventory import InventoryCollectionItem_pb2 as WUProtos_dot_Inventory_dot_InventoryCollectionItem__pb2
from WUProtos.Inventory import InventoryCollectionFamily_pb2 as WUProtos_dot_Inventory_dot_InventoryCollectionFamily__pb2
from WUProtos.Inventory import InventoryWalkboxItem_pb2 as WUProtos_dot_Inventory_dot_InventoryWalkboxItem__pb2
from WUProtos.Inventory import InventoryFeatureFlags_pb2 as WUProtos_dot_Inventory_dot_InventoryFeatureFlags__pb2
from WUProtos.Inventory import InventoryPortkeyItem_pb2 as WUProtos_dot_Inventory_dot_InventoryPortkeyItem__pb2
from WUProtos.Inventory import InventoryCollectionPage_pb2 as WUProtos_dot_Inventory_dot_InventoryCollectionPage__pb2
from WUProtos.Inventory import InventoryVaultCapacity_pb2 as WUProtos_dot_Inventory_dot_InventoryVaultCapacity__pb2
from WUProtos.Inventory import InventoryCauldron_pb2 as WUProtos_dot_Inventory_dot_InventoryCauldron__pb2
from WUProtos.Inventory import InventoryEscrowedRewards_pb2 as WUProtos_dot_Inventory_dot_InventoryEscrowedRewards__pb2
from WUProtos.Inventory import InventoryQuestLog_pb2 as WUProtos_dot_Inventory_dot_InventoryQuestLog__pb2
from WUProtos.Data.Buff import ActiveBuffList_pb2 as WUProtos_dot_Data_dot_Buff_dot_ActiveBuffList__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Inventory/AtlasInventoryItem.proto',
  package='WUProtos.Inventory',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n+WUProtos/Inventory/AtlasInventoryItem.proto\x12\x12WUProtos.Inventory\x1a(WUProtos/Data/Player/PlayerProfile.proto\x1a\x36WUProtos/Data/Player/PlayerProfessionsProgressV3.proto\x1a#WUProtos/Data/LifetimeMetrics.proto\x1a+WUProtos/Inventory/InventoryVaultItem.proto\x1a\x30WUProtos/Inventory/InventoryCollectionItem.proto\x1a\x32WUProtos/Inventory/InventoryCollectionFamily.proto\x1a-WUProtos/Inventory/InventoryWalkboxItem.proto\x1a.WUProtos/Inventory/InventoryFeatureFlags.proto\x1a-WUProtos/Inventory/InventoryPortkeyItem.proto\x1a\x30WUProtos/Inventory/InventoryCollectionPage.proto\x1a/WUProtos/Inventory/InventoryVaultCapacity.proto\x1a*WUProtos/Inventory/InventoryCauldron.proto\x1a\x31WUProtos/Inventory/InventoryEscrowedRewards.proto\x1a*WUProtos/Inventory/InventoryQuestLog.proto\x1a\'WUProtos/Data/Buff/ActiveBuffList.proto\"\x8b\x08\n\x12\x41tlasInventoryItem\x12\x36\n\x07profile\x18\x01 \x01(\x0b\x32#.WUProtos.Data.Player.PlayerProfileH\x00\x12<\n\nvault_item\x18\x02 \x01(\x0b\x32&.WUProtos.Inventory.InventoryVaultItemH\x00\x12\x46\n\x0f\x63ollection_item\x18\x03 \x01(\x0b\x32+.WUProtos.Inventory.InventoryCollectionItemH\x00\x12J\n\x11\x63ollection_family\x18\x04 \x01(\x0b\x32-.WUProtos.Inventory.InventoryCollectionFamilyH\x00\x12;\n\x07walkbox\x18\x05 \x01(\x0b\x32(.WUProtos.Inventory.InventoryWalkboxItemH\x00\x12\x41\n\x0cplayer_flags\x18\x06 \x01(\x0b\x32).WUProtos.Inventory.InventoryFeatureFlagsH\x00\x12;\n\x07portkey\x18\x07 \x01(\x0b\x32(.WUProtos.Inventory.InventoryPortkeyItemH\x00\x12\x45\n\x17player_active_buff_list\x18\x08 \x01(\x0b\x32\".WUProtos.Data.Buff.ActiveBuffListH\x00\x12\x46\n\x0f\x63ollection_page\x18\t \x01(\x0b\x32+.WUProtos.Inventory.InventoryCollectionPageH\x00\x12\x44\n\x0evault_capacity\x18\x0b \x01(\x0b\x32*.WUProtos.Inventory.InventoryVaultCapacityH\x00\x12\x39\n\x08\x63\x61uldron\x18\x0c \x01(\x0b\x32%.WUProtos.Inventory.InventoryCauldronH\x00\x12H\n\x10\x65scrowed_rewards\x18\r \x01(\x0b\x32,.WUProtos.Inventory.InventoryEscrowedRewardsH\x00\x12T\n\x17professions_progress_v3\x18\x0e \x01(\x0b\x32\x31.WUProtos.Data.Player.PlayerProfessionsProgressV3H\x00\x12:\n\tquest_log\x18\x0f \x01(\x0b\x32%.WUProtos.Inventory.InventoryQuestLogH\x00\x12:\n\x10lifetime_metrics\x18\x10 \x01(\x0b\x32\x1e.WUProtos.Data.LifetimeMetricsH\x00\x42\x06\n\x04Typeb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Player_dot_PlayerProfile__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_Player_dot_PlayerProfessionsProgressV3__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_LifetimeMetrics__pb2.DESCRIPTOR,WUProtos_dot_Inventory_dot_InventoryVaultItem__pb2.DESCRIPTOR,WUProtos_dot_Inventory_dot_InventoryCollectionItem__pb2.DESCRIPTOR,WUProtos_dot_Inventory_dot_InventoryCollectionFamily__pb2.DESCRIPTOR,WUProtos_dot_Inventory_dot_InventoryWalkboxItem__pb2.DESCRIPTOR,WUProtos_dot_Inventory_dot_InventoryFeatureFlags__pb2.DESCRIPTOR,WUProtos_dot_Inventory_dot_InventoryPortkeyItem__pb2.DESCRIPTOR,WUProtos_dot_Inventory_dot_InventoryCollectionPage__pb2.DESCRIPTOR,WUProtos_dot_Inventory_dot_InventoryVaultCapacity__pb2.DESCRIPTOR,WUProtos_dot_Inventory_dot_InventoryCauldron__pb2.DESCRIPTOR,WUProtos_dot_Inventory_dot_InventoryEscrowedRewards__pb2.DESCRIPTOR,WUProtos_dot_Inventory_dot_InventoryQuestLog__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_Buff_dot_ActiveBuffList__pb2.DESCRIPTOR,])




_ATLASINVENTORYITEM = _descriptor.Descriptor(
  name='AtlasInventoryItem',
  full_name='WUProtos.Inventory.AtlasInventoryItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='profile', full_name='WUProtos.Inventory.AtlasInventoryItem.profile', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vault_item', full_name='WUProtos.Inventory.AtlasInventoryItem.vault_item', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection_item', full_name='WUProtos.Inventory.AtlasInventoryItem.collection_item', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection_family', full_name='WUProtos.Inventory.AtlasInventoryItem.collection_family', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='walkbox', full_name='WUProtos.Inventory.AtlasInventoryItem.walkbox', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_flags', full_name='WUProtos.Inventory.AtlasInventoryItem.player_flags', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portkey', full_name='WUProtos.Inventory.AtlasInventoryItem.portkey', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_active_buff_list', full_name='WUProtos.Inventory.AtlasInventoryItem.player_active_buff_list', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection_page', full_name='WUProtos.Inventory.AtlasInventoryItem.collection_page', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vault_capacity', full_name='WUProtos.Inventory.AtlasInventoryItem.vault_capacity', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cauldron', full_name='WUProtos.Inventory.AtlasInventoryItem.cauldron', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='escrowed_rewards', full_name='WUProtos.Inventory.AtlasInventoryItem.escrowed_rewards', index=11,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='professions_progress_v3', full_name='WUProtos.Inventory.AtlasInventoryItem.professions_progress_v3', index=12,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quest_log', full_name='WUProtos.Inventory.AtlasInventoryItem.quest_log', index=13,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lifetime_metrics', full_name='WUProtos.Inventory.AtlasInventoryItem.lifetime_metrics', index=14,
      number=16, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='Type', full_name='WUProtos.Inventory.AtlasInventoryItem.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=771,
  serialized_end=1806,
)

_ATLASINVENTORYITEM.fields_by_name['profile'].message_type = WUProtos_dot_Data_dot_Player_dot_PlayerProfile__pb2._PLAYERPROFILE
_ATLASINVENTORYITEM.fields_by_name['vault_item'].message_type = WUProtos_dot_Inventory_dot_InventoryVaultItem__pb2._INVENTORYVAULTITEM
_ATLASINVENTORYITEM.fields_by_name['collection_item'].message_type = WUProtos_dot_Inventory_dot_InventoryCollectionItem__pb2._INVENTORYCOLLECTIONITEM
_ATLASINVENTORYITEM.fields_by_name['collection_family'].message_type = WUProtos_dot_Inventory_dot_InventoryCollectionFamily__pb2._INVENTORYCOLLECTIONFAMILY
_ATLASINVENTORYITEM.fields_by_name['walkbox'].message_type = WUProtos_dot_Inventory_dot_InventoryWalkboxItem__pb2._INVENTORYWALKBOXITEM
_ATLASINVENTORYITEM.fields_by_name['player_flags'].message_type = WUProtos_dot_Inventory_dot_InventoryFeatureFlags__pb2._INVENTORYFEATUREFLAGS
_ATLASINVENTORYITEM.fields_by_name['portkey'].message_type = WUProtos_dot_Inventory_dot_InventoryPortkeyItem__pb2._INVENTORYPORTKEYITEM
_ATLASINVENTORYITEM.fields_by_name['player_active_buff_list'].message_type = WUProtos_dot_Data_dot_Buff_dot_ActiveBuffList__pb2._ACTIVEBUFFLIST
_ATLASINVENTORYITEM.fields_by_name['collection_page'].message_type = WUProtos_dot_Inventory_dot_InventoryCollectionPage__pb2._INVENTORYCOLLECTIONPAGE
_ATLASINVENTORYITEM.fields_by_name['vault_capacity'].message_type = WUProtos_dot_Inventory_dot_InventoryVaultCapacity__pb2._INVENTORYVAULTCAPACITY
_ATLASINVENTORYITEM.fields_by_name['cauldron'].message_type = WUProtos_dot_Inventory_dot_InventoryCauldron__pb2._INVENTORYCAULDRON
_ATLASINVENTORYITEM.fields_by_name['escrowed_rewards'].message_type = WUProtos_dot_Inventory_dot_InventoryEscrowedRewards__pb2._INVENTORYESCROWEDREWARDS
_ATLASINVENTORYITEM.fields_by_name['professions_progress_v3'].message_type = WUProtos_dot_Data_dot_Player_dot_PlayerProfessionsProgressV3__pb2._PLAYERPROFESSIONSPROGRESSV3
_ATLASINVENTORYITEM.fields_by_name['quest_log'].message_type = WUProtos_dot_Inventory_dot_InventoryQuestLog__pb2._INVENTORYQUESTLOG
_ATLASINVENTORYITEM.fields_by_name['lifetime_metrics'].message_type = WUProtos_dot_Data_dot_LifetimeMetrics__pb2._LIFETIMEMETRICS
_ATLASINVENTORYITEM.oneofs_by_name['Type'].fields.append(
  _ATLASINVENTORYITEM.fields_by_name['profile'])
_ATLASINVENTORYITEM.fields_by_name['profile'].containing_oneof = _ATLASINVENTORYITEM.oneofs_by_name['Type']
_ATLASINVENTORYITEM.oneofs_by_name['Type'].fields.append(
  _ATLASINVENTORYITEM.fields_by_name['vault_item'])
_ATLASINVENTORYITEM.fields_by_name['vault_item'].containing_oneof = _ATLASINVENTORYITEM.oneofs_by_name['Type']
_ATLASINVENTORYITEM.oneofs_by_name['Type'].fields.append(
  _ATLASINVENTORYITEM.fields_by_name['collection_item'])
_ATLASINVENTORYITEM.fields_by_name['collection_item'].containing_oneof = _ATLASINVENTORYITEM.oneofs_by_name['Type']
_ATLASINVENTORYITEM.oneofs_by_name['Type'].fields.append(
  _ATLASINVENTORYITEM.fields_by_name['collection_family'])
_ATLASINVENTORYITEM.fields_by_name['collection_family'].containing_oneof = _ATLASINVENTORYITEM.oneofs_by_name['Type']
_ATLASINVENTORYITEM.oneofs_by_name['Type'].fields.append(
  _ATLASINVENTORYITEM.fields_by_name['walkbox'])
_ATLASINVENTORYITEM.fields_by_name['walkbox'].containing_oneof = _ATLASINVENTORYITEM.oneofs_by_name['Type']
_ATLASINVENTORYITEM.oneofs_by_name['Type'].fields.append(
  _ATLASINVENTORYITEM.fields_by_name['player_flags'])
_ATLASINVENTORYITEM.fields_by_name['player_flags'].containing_oneof = _ATLASINVENTORYITEM.oneofs_by_name['Type']
_ATLASINVENTORYITEM.oneofs_by_name['Type'].fields.append(
  _ATLASINVENTORYITEM.fields_by_name['portkey'])
_ATLASINVENTORYITEM.fields_by_name['portkey'].containing_oneof = _ATLASINVENTORYITEM.oneofs_by_name['Type']
_ATLASINVENTORYITEM.oneofs_by_name['Type'].fields.append(
  _ATLASINVENTORYITEM.fields_by_name['player_active_buff_list'])
_ATLASINVENTORYITEM.fields_by_name['player_active_buff_list'].containing_oneof = _ATLASINVENTORYITEM.oneofs_by_name['Type']
_ATLASINVENTORYITEM.oneofs_by_name['Type'].fields.append(
  _ATLASINVENTORYITEM.fields_by_name['collection_page'])
_ATLASINVENTORYITEM.fields_by_name['collection_page'].containing_oneof = _ATLASINVENTORYITEM.oneofs_by_name['Type']
_ATLASINVENTORYITEM.oneofs_by_name['Type'].fields.append(
  _ATLASINVENTORYITEM.fields_by_name['vault_capacity'])
_ATLASINVENTORYITEM.fields_by_name['vault_capacity'].containing_oneof = _ATLASINVENTORYITEM.oneofs_by_name['Type']
_ATLASINVENTORYITEM.oneofs_by_name['Type'].fields.append(
  _ATLASINVENTORYITEM.fields_by_name['cauldron'])
_ATLASINVENTORYITEM.fields_by_name['cauldron'].containing_oneof = _ATLASINVENTORYITEM.oneofs_by_name['Type']
_ATLASINVENTORYITEM.oneofs_by_name['Type'].fields.append(
  _ATLASINVENTORYITEM.fields_by_name['escrowed_rewards'])
_ATLASINVENTORYITEM.fields_by_name['escrowed_rewards'].containing_oneof = _ATLASINVENTORYITEM.oneofs_by_name['Type']
_ATLASINVENTORYITEM.oneofs_by_name['Type'].fields.append(
  _ATLASINVENTORYITEM.fields_by_name['professions_progress_v3'])
_ATLASINVENTORYITEM.fields_by_name['professions_progress_v3'].containing_oneof = _ATLASINVENTORYITEM.oneofs_by_name['Type']
_ATLASINVENTORYITEM.oneofs_by_name['Type'].fields.append(
  _ATLASINVENTORYITEM.fields_by_name['quest_log'])
_ATLASINVENTORYITEM.fields_by_name['quest_log'].containing_oneof = _ATLASINVENTORYITEM.oneofs_by_name['Type']
_ATLASINVENTORYITEM.oneofs_by_name['Type'].fields.append(
  _ATLASINVENTORYITEM.fields_by_name['lifetime_metrics'])
_ATLASINVENTORYITEM.fields_by_name['lifetime_metrics'].containing_oneof = _ATLASINVENTORYITEM.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['AtlasInventoryItem'] = _ATLASINVENTORYITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AtlasInventoryItem = _reflection.GeneratedProtocolMessageType('AtlasInventoryItem', (_message.Message,), dict(
  DESCRIPTOR = _ATLASINVENTORYITEM,
  __module__ = 'WUProtos.Inventory.AtlasInventoryItem_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Inventory.AtlasInventoryItem)
  ))
_sym_db.RegisterMessage(AtlasInventoryItem)


# @@protoc_insertion_point(module_scope)
