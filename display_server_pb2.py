# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: display_server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='display_server.proto',
  package='LED_display',
  syntax='proto3',
  serialized_pb=_b('\n\x14\x64isplay_server.proto\x12\x0bLED_display\"]\n\x0b\x44ISPLAY_MSG\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x0b\n\x03typ\x18\x02 \x01(\x05\x12\r\n\x05\x64im_x\x18\x03 \x01(\x05\x12\r\n\x05\x64im_y\x18\x04 \x01(\x05\x12\x12\n\npixel_list\x18\x05 \x01(\t\"#\n\x10\x44ISPLAY_RESPONSE\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32]\n\x0eWS2801_Display\x12K\n\x0e\x44ISPLAY_CHANGE\x12\x18.LED_display.DISPLAY_MSG\x1a\x1d.LED_display.DISPLAY_RESPONSE\"\x00\x62\x06proto3')
)




_DISPLAY_MSG = _descriptor.Descriptor(
  name='DISPLAY_MSG',
  full_name='LED_display.DISPLAY_MSG',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='LED_display.DISPLAY_MSG.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='typ', full_name='LED_display.DISPLAY_MSG.typ', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dim_x', full_name='LED_display.DISPLAY_MSG.dim_x', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dim_y', full_name='LED_display.DISPLAY_MSG.dim_y', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pixel_list', full_name='LED_display.DISPLAY_MSG.pixel_list', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=130,
)


_DISPLAY_RESPONSE = _descriptor.Descriptor(
  name='DISPLAY_RESPONSE',
  full_name='LED_display.DISPLAY_RESPONSE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='LED_display.DISPLAY_RESPONSE.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=167,
)

DESCRIPTOR.message_types_by_name['DISPLAY_MSG'] = _DISPLAY_MSG
DESCRIPTOR.message_types_by_name['DISPLAY_RESPONSE'] = _DISPLAY_RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DISPLAY_MSG = _reflection.GeneratedProtocolMessageType('DISPLAY_MSG', (_message.Message,), dict(
  DESCRIPTOR = _DISPLAY_MSG,
  __module__ = 'display_server_pb2'
  # @@protoc_insertion_point(class_scope:LED_display.DISPLAY_MSG)
  ))
_sym_db.RegisterMessage(DISPLAY_MSG)

DISPLAY_RESPONSE = _reflection.GeneratedProtocolMessageType('DISPLAY_RESPONSE', (_message.Message,), dict(
  DESCRIPTOR = _DISPLAY_RESPONSE,
  __module__ = 'display_server_pb2'
  # @@protoc_insertion_point(class_scope:LED_display.DISPLAY_RESPONSE)
  ))
_sym_db.RegisterMessage(DISPLAY_RESPONSE)



_WS2801_DISPLAY = _descriptor.ServiceDescriptor(
  name='WS2801_Display',
  full_name='LED_display.WS2801_Display',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=169,
  serialized_end=262,
  methods=[
  _descriptor.MethodDescriptor(
    name='DISPLAY_CHANGE',
    full_name='LED_display.WS2801_Display.DISPLAY_CHANGE',
    index=0,
    containing_service=None,
    input_type=_DISPLAY_MSG,
    output_type=_DISPLAY_RESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_WS2801_DISPLAY)

DESCRIPTOR.services_by_name['WS2801_Display'] = _WS2801_DISPLAY

# @@protoc_insertion_point(module_scope)
