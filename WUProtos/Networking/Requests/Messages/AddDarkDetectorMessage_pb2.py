# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Requests/Messages/AddDarkDetectorMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Requests/Messages/AddDarkDetectorMessage.proto',
  package='WUProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nBWUProtos/Networking/Requests/Messages/AddDarkDetectorMessage.proto\x12%WUProtos.Networking.Requests.Messages\"a\n\x16\x41\x64\x64\x44\x61rkDetectorMessage\x12\x18\n\x10\x64\x61rk_detector_id\x18\x01 \x01(\t\x12\x19\n\x11target_outpost_id\x18\x02 \x01(\t\x12\x12\n\nslot_index\x18\x03 \x01(\x05\x62\x06proto3')
)




_ADDDARKDETECTORMESSAGE = _descriptor.Descriptor(
  name='AddDarkDetectorMessage',
  full_name='WUProtos.Networking.Requests.Messages.AddDarkDetectorMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dark_detector_id', full_name='WUProtos.Networking.Requests.Messages.AddDarkDetectorMessage.dark_detector_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_outpost_id', full_name='WUProtos.Networking.Requests.Messages.AddDarkDetectorMessage.target_outpost_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot_index', full_name='WUProtos.Networking.Requests.Messages.AddDarkDetectorMessage.slot_index', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=109,
  serialized_end=206,
)

DESCRIPTOR.message_types_by_name['AddDarkDetectorMessage'] = _ADDDARKDETECTORMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddDarkDetectorMessage = _reflection.GeneratedProtocolMessageType('AddDarkDetectorMessage', (_message.Message,), dict(
  DESCRIPTOR = _ADDDARKDETECTORMESSAGE,
  __module__ = 'WUProtos.Networking.Requests.Messages.AddDarkDetectorMessage_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Requests.Messages.AddDarkDetectorMessage)
  ))
_sym_db.RegisterMessage(AddDarkDetectorMessage)


# @@protoc_insertion_point(module_scope)
