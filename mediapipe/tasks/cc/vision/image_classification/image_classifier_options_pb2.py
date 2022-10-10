# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/image_classification/image_classifier_options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
from mediapipe.tasks.cc.components import classifier_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_components_dot_classifier__options__pb2
from mediapipe.tasks.cc.core.proto import base_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/tasks/cc/vision/image_classification/image_classifier_options.proto',
  package='mediapipe.tasks',
  syntax='proto2',
  serialized_pb=_b('\nMmediapipe/tasks/cc/vision/image_classification/image_classifier_options.proto\x12\x0fmediapipe.tasks\x1a$mediapipe/framework/calculator.proto\x1a\x36mediapipe/tasks/cc/components/classifier_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\"\xef\x01\n\x16ImageClassifierOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12>\n\x12\x63lassifier_options\x18\x02 \x01(\x0b\x32\".mediapipe.tasks.ClassifierOptions2V\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x97\xb7\xcf\xd9\x01 \x01(\x0b\x32\'.mediapipe.tasks.ImageClassifierOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_components_dot_classifier__options__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_IMAGECLASSIFIEROPTIONS = _descriptor.Descriptor(
  name='ImageClassifierOptions',
  full_name='mediapipe.tasks.ImageClassifierOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_options', full_name='mediapipe.tasks.ImageClassifierOptions.base_options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='classifier_options', full_name='mediapipe.tasks.ImageClassifierOptions.classifier_options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.tasks.ImageClassifierOptions.ext', index=0,
      number=456383383, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=243,
  serialized_end=482,
)

_IMAGECLASSIFIEROPTIONS.fields_by_name['base_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2._BASEOPTIONS
_IMAGECLASSIFIEROPTIONS.fields_by_name['classifier_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_components_dot_classifier__options__pb2._CLASSIFIEROPTIONS
DESCRIPTOR.message_types_by_name['ImageClassifierOptions'] = _IMAGECLASSIFIEROPTIONS

ImageClassifierOptions = _reflection.GeneratedProtocolMessageType('ImageClassifierOptions', (_message.Message,), dict(
  DESCRIPTOR = _IMAGECLASSIFIEROPTIONS,
  __module__ = 'mediapipe.tasks.cc.vision.image_classification.image_classifier_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.ImageClassifierOptions)
  ))
_sym_db.RegisterMessage(ImageClassifierOptions)

_IMAGECLASSIFIEROPTIONS.extensions_by_name['ext'].message_type = _IMAGECLASSIFIEROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_IMAGECLASSIFIEROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)