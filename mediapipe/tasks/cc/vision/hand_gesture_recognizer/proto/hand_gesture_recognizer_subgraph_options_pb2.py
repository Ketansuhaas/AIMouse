# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/hand_gesture_recognizer/proto/hand_gesture_recognizer_subgraph_options.proto

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
  name='mediapipe/tasks/cc/vision/hand_gesture_recognizer/proto/hand_gesture_recognizer_subgraph_options.proto',
  package='mediapipe.tasks.vision.hand_gesture_recognizer.proto',
  syntax='proto2',
  serialized_pb=_b('\nfmediapipe/tasks/cc/vision/hand_gesture_recognizer/proto/hand_gesture_recognizer_subgraph_options.proto\x12\x34mediapipe.tasks.vision.hand_gesture_recognizer.proto\x1a$mediapipe/framework/calculator.proto\x1a\x36mediapipe/tasks/cc/components/classifier_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\"\xd5\x02\n$HandGestureRecognizerSubgraphOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12>\n\x12\x63lassifier_options\x18\x02 \x01(\x0b\x32\".mediapipe.tasks.ClassifierOptions\x12\"\n\x17min_tracking_confidence\x18\x03 \x01(\x02:\x01\x30\x32\x89\x01\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xd4\xf1\xf9\xdc\x01 \x01(\x0b\x32Z.mediapipe.tasks.vision.hand_gesture_recognizer.proto.HandGestureRecognizerSubgraphOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_components_dot_classifier__options__pb2.DESCRIPTOR,mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HANDGESTURERECOGNIZERSUBGRAPHOPTIONS = _descriptor.Descriptor(
  name='HandGestureRecognizerSubgraphOptions',
  full_name='mediapipe.tasks.vision.hand_gesture_recognizer.proto.HandGestureRecognizerSubgraphOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_options', full_name='mediapipe.tasks.vision.hand_gesture_recognizer.proto.HandGestureRecognizerSubgraphOptions.base_options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='classifier_options', full_name='mediapipe.tasks.vision.hand_gesture_recognizer.proto.HandGestureRecognizerSubgraphOptions.classifier_options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_tracking_confidence', full_name='mediapipe.tasks.vision.hand_gesture_recognizer.proto.HandGestureRecognizerSubgraphOptions.min_tracking_confidence', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.tasks.vision.hand_gesture_recognizer.proto.HandGestureRecognizerSubgraphOptions.ext', index=0,
      number=463370452, type=11, cpp_type=10, label=1,
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
  serialized_start=305,
  serialized_end=646,
)

_HANDGESTURERECOGNIZERSUBGRAPHOPTIONS.fields_by_name['base_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2._BASEOPTIONS
_HANDGESTURERECOGNIZERSUBGRAPHOPTIONS.fields_by_name['classifier_options'].message_type = mediapipe_dot_tasks_dot_cc_dot_components_dot_classifier__options__pb2._CLASSIFIEROPTIONS
DESCRIPTOR.message_types_by_name['HandGestureRecognizerSubgraphOptions'] = _HANDGESTURERECOGNIZERSUBGRAPHOPTIONS

HandGestureRecognizerSubgraphOptions = _reflection.GeneratedProtocolMessageType('HandGestureRecognizerSubgraphOptions', (_message.Message,), dict(
  DESCRIPTOR = _HANDGESTURERECOGNIZERSUBGRAPHOPTIONS,
  __module__ = 'mediapipe.tasks.cc.vision.hand_gesture_recognizer.proto.hand_gesture_recognizer_subgraph_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.vision.hand_gesture_recognizer.proto.HandGestureRecognizerSubgraphOptions)
  ))
_sym_db.RegisterMessage(HandGestureRecognizerSubgraphOptions)

_HANDGESTURERECOGNIZERSUBGRAPHOPTIONS.extensions_by_name['ext'].message_type = _HANDGESTURERECOGNIZERSUBGRAPHOPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_HANDGESTURERECOGNIZERSUBGRAPHOPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
