# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: echo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='echo.proto',
  package='echo',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\necho.proto\x12\x04\x65\x63ho\"2\n\x0b\x45\x63hoRequest\x12\x11\n\tfirstname\x18\x01 \x01(\t\x12\x10\n\x08lastname\x18\x02 \x01(\t\"\x1c\n\tEchoReply\x12\x0f\n\x07message\x18\x01 \x01(\t2x\n\nEchoServer\x12\x30\n\x08SayHello\x12\x11.echo.EchoRequest\x1a\x0f.echo.EchoReply\"\x00\x12\x38\n\x0eSayHelloStream\x12\x11.echo.EchoRequest\x1a\x0f.echo.EchoReply\"\x00\x30\x01\x62\x06proto3'
)




_ECHOREQUEST = _descriptor.Descriptor(
  name='EchoRequest',
  full_name='echo.EchoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='firstname', full_name='echo.EchoRequest.firstname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lastname', full_name='echo.EchoRequest.lastname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=20,
  serialized_end=70,
)


_ECHOREPLY = _descriptor.Descriptor(
  name='EchoReply',
  full_name='echo.EchoReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='echo.EchoReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=72,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['EchoRequest'] = _ECHOREQUEST
DESCRIPTOR.message_types_by_name['EchoReply'] = _ECHOREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EchoRequest = _reflection.GeneratedProtocolMessageType('EchoRequest', (_message.Message,), {
  'DESCRIPTOR' : _ECHOREQUEST,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:echo.EchoRequest)
  })
_sym_db.RegisterMessage(EchoRequest)

EchoReply = _reflection.GeneratedProtocolMessageType('EchoReply', (_message.Message,), {
  'DESCRIPTOR' : _ECHOREPLY,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:echo.EchoReply)
  })
_sym_db.RegisterMessage(EchoReply)



_ECHOSERVER = _descriptor.ServiceDescriptor(
  name='EchoServer',
  full_name='echo.EchoServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=102,
  serialized_end=222,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='echo.EchoServer.SayHello',
    index=0,
    containing_service=None,
    input_type=_ECHOREQUEST,
    output_type=_ECHOREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SayHelloStream',
    full_name='echo.EchoServer.SayHelloStream',
    index=1,
    containing_service=None,
    input_type=_ECHOREQUEST,
    output_type=_ECHOREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ECHOSERVER)

DESCRIPTOR.services_by_name['EchoServer'] = _ECHOSERVER

# @@protoc_insertion_point(module_scope)
