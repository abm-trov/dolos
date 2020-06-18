# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FakerModel.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='FakerModel.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x46\x61kerModel.proto\"Z\n\x14GenerationParameters\x12%\n\x08mod_conf\x18\x01 \x01(\x0b\x32\x13.ModelConfiguration\x12\x1b\n\x06schema\x18\x02 \x01(\x0b\x32\x0b.DataSchema\"R\n\x12ModelConfiguration\x12\x11\n\tclassname\x18\x01 \x01(\t\x12\x14\n\x0cprovidername\x18\x02 \x01(\t\x12\x13\n\x0bgeneratable\x18\x03 \x03(\t\"\x1b\n\nDataSchema\x12\r\n\x05\x66ield\x18\x01 \x03(\tb\x06proto3')
)




_GENERATIONPARAMETERS = _descriptor.Descriptor(
  name='GenerationParameters',
  full_name='GenerationParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mod_conf', full_name='GenerationParameters.mod_conf', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schema', full_name='GenerationParameters.schema', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=20,
  serialized_end=110,
)


_MODELCONFIGURATION = _descriptor.Descriptor(
  name='ModelConfiguration',
  full_name='ModelConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='classname', full_name='ModelConfiguration.classname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='providername', full_name='ModelConfiguration.providername', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generatable', full_name='ModelConfiguration.generatable', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=112,
  serialized_end=194,
)


_DATASCHEMA = _descriptor.Descriptor(
  name='DataSchema',
  full_name='DataSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='DataSchema.field', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=196,
  serialized_end=223,
)

_GENERATIONPARAMETERS.fields_by_name['mod_conf'].message_type = _MODELCONFIGURATION
_GENERATIONPARAMETERS.fields_by_name['schema'].message_type = _DATASCHEMA
DESCRIPTOR.message_types_by_name['GenerationParameters'] = _GENERATIONPARAMETERS
DESCRIPTOR.message_types_by_name['ModelConfiguration'] = _MODELCONFIGURATION
DESCRIPTOR.message_types_by_name['DataSchema'] = _DATASCHEMA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenerationParameters = _reflection.GeneratedProtocolMessageType('GenerationParameters', (_message.Message,), dict(
  DESCRIPTOR = _GENERATIONPARAMETERS,
  __module__ = 'FakerModel_pb2'
  # @@protoc_insertion_point(class_scope:GenerationParameters)
  ))
_sym_db.RegisterMessage(GenerationParameters)

ModelConfiguration = _reflection.GeneratedProtocolMessageType('ModelConfiguration', (_message.Message,), dict(
  DESCRIPTOR = _MODELCONFIGURATION,
  __module__ = 'FakerModel_pb2'
  # @@protoc_insertion_point(class_scope:ModelConfiguration)
  ))
_sym_db.RegisterMessage(ModelConfiguration)

DataSchema = _reflection.GeneratedProtocolMessageType('DataSchema', (_message.Message,), dict(
  DESCRIPTOR = _DATASCHEMA,
  __module__ = 'FakerModel_pb2'
  # @@protoc_insertion_point(class_scope:DataSchema)
  ))
_sym_db.RegisterMessage(DataSchema)


# @@protoc_insertion_point(module_scope)
