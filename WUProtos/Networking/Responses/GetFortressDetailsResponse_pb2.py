# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Responses/GetFortressDetailsResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import PoiDetails_pb2 as WUProtos_dot_Data_dot_PoiDetails__pb2
from WUProtos.Enums import PoiAccessibility_pb2 as WUProtos_dot_Enums_dot_PoiAccessibility__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Responses/GetFortressDetailsResponse.proto',
  package='WUProtos.Networking.Responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n>WUProtos/Networking/Responses/GetFortressDetailsResponse.proto\x12\x1dWUProtos.Networking.Responses\x1a\x1eWUProtos/Data/PoiDetails.proto\x1a%WUProtos/Enums/PoiAccessibility.proto\"\xfb\x02\n\x1aGetFortressDetailsResponse\x12 \n\x18\x66ortress_template_gmt_id\x18\x01 \x01(\t\x12Z\n\x08\x63hambers\x18\x02 \x03(\x0b\x32H.WUProtos.Networking.Responses.GetFortressDetailsResponse.ChamberPreview\x12\x12\n\npartner_id\x18\x04 \x01(\t\x12.\n\x0bpoi_details\x18\x05 \x01(\x0b\x32\x19.WUProtos.Data.PoiDetails\x12;\n\x11poi_accessibility\x18\x06 \x01(\x0e\x32 .WUProtos.Enums.PoiAccessibility\x1a^\n\x0e\x43hamberPreview\x12\x1f\n\x17\x63hamber_template_gmt_id\x18\x01 \x01(\t\x12\x14\n\x0cplayer_count\x18\x02 \x01(\r\x12\x15\n\rstart_time_ms\x18\x03 \x01(\x03\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_PoiDetails__pb2.DESCRIPTOR,WUProtos_dot_Enums_dot_PoiAccessibility__pb2.DESCRIPTOR,])




_GETFORTRESSDETAILSRESPONSE_CHAMBERPREVIEW = _descriptor.Descriptor(
  name='ChamberPreview',
  full_name='WUProtos.Networking.Responses.GetFortressDetailsResponse.ChamberPreview',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chamber_template_gmt_id', full_name='WUProtos.Networking.Responses.GetFortressDetailsResponse.ChamberPreview.chamber_template_gmt_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_count', full_name='WUProtos.Networking.Responses.GetFortressDetailsResponse.ChamberPreview.player_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time_ms', full_name='WUProtos.Networking.Responses.GetFortressDetailsResponse.ChamberPreview.start_time_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=454,
  serialized_end=548,
)

_GETFORTRESSDETAILSRESPONSE = _descriptor.Descriptor(
  name='GetFortressDetailsResponse',
  full_name='WUProtos.Networking.Responses.GetFortressDetailsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fortress_template_gmt_id', full_name='WUProtos.Networking.Responses.GetFortressDetailsResponse.fortress_template_gmt_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chambers', full_name='WUProtos.Networking.Responses.GetFortressDetailsResponse.chambers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner_id', full_name='WUProtos.Networking.Responses.GetFortressDetailsResponse.partner_id', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poi_details', full_name='WUProtos.Networking.Responses.GetFortressDetailsResponse.poi_details', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poi_accessibility', full_name='WUProtos.Networking.Responses.GetFortressDetailsResponse.poi_accessibility', index=4,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETFORTRESSDETAILSRESPONSE_CHAMBERPREVIEW, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=548,
)

_GETFORTRESSDETAILSRESPONSE_CHAMBERPREVIEW.containing_type = _GETFORTRESSDETAILSRESPONSE
_GETFORTRESSDETAILSRESPONSE.fields_by_name['chambers'].message_type = _GETFORTRESSDETAILSRESPONSE_CHAMBERPREVIEW
_GETFORTRESSDETAILSRESPONSE.fields_by_name['poi_details'].message_type = WUProtos_dot_Data_dot_PoiDetails__pb2._POIDETAILS
_GETFORTRESSDETAILSRESPONSE.fields_by_name['poi_accessibility'].enum_type = WUProtos_dot_Enums_dot_PoiAccessibility__pb2._POIACCESSIBILITY
DESCRIPTOR.message_types_by_name['GetFortressDetailsResponse'] = _GETFORTRESSDETAILSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFortressDetailsResponse = _reflection.GeneratedProtocolMessageType('GetFortressDetailsResponse', (_message.Message,), dict(

  ChamberPreview = _reflection.GeneratedProtocolMessageType('ChamberPreview', (_message.Message,), dict(
    DESCRIPTOR = _GETFORTRESSDETAILSRESPONSE_CHAMBERPREVIEW,
    __module__ = 'WUProtos.Networking.Responses.GetFortressDetailsResponse_pb2'
    # @@protoc_insertion_point(class_scope:WUProtos.Networking.Responses.GetFortressDetailsResponse.ChamberPreview)
    ))
  ,
  DESCRIPTOR = _GETFORTRESSDETAILSRESPONSE,
  __module__ = 'WUProtos.Networking.Responses.GetFortressDetailsResponse_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Responses.GetFortressDetailsResponse)
  ))
_sym_db.RegisterMessage(GetFortressDetailsResponse)
_sym_db.RegisterMessage(GetFortressDetailsResponse.ChamberPreview)


# @@protoc_insertion_point(module_scope)
