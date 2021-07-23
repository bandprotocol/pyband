# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: confio/proofs.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='confio/proofs.proto',
  package='ics23',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x63onfio/proofs.proto\x12\x05ics23\"g\n\x0e\x45xistenceProof\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x1b\n\x04leaf\x18\x03 \x01(\x0b\x32\r.ics23.LeafOp\x12\x1c\n\x04path\x18\x04 \x03(\x0b\x32\x0e.ics23.InnerOp\"k\n\x11NonExistenceProof\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12#\n\x04left\x18\x02 \x01(\x0b\x32\x15.ics23.ExistenceProof\x12$\n\x05right\x18\x03 \x01(\x0b\x32\x15.ics23.ExistenceProof\"\xc7\x01\n\x0f\x43ommitmentProof\x12&\n\x05\x65xist\x18\x01 \x01(\x0b\x32\x15.ics23.ExistenceProofH\x00\x12,\n\x08nonexist\x18\x02 \x01(\x0b\x32\x18.ics23.NonExistenceProofH\x00\x12\"\n\x05\x62\x61tch\x18\x03 \x01(\x0b\x32\x11.ics23.BatchProofH\x00\x12\x31\n\ncompressed\x18\x04 \x01(\x0b\x32\x1b.ics23.CompressedBatchProofH\x00\x42\x07\n\x05proof\"\xa0\x01\n\x06LeafOp\x12\x1b\n\x04hash\x18\x01 \x01(\x0e\x32\r.ics23.HashOp\x12\"\n\x0bprehash_key\x18\x02 \x01(\x0e\x32\r.ics23.HashOp\x12$\n\rprehash_value\x18\x03 \x01(\x0e\x32\r.ics23.HashOp\x12\x1f\n\x06length\x18\x04 \x01(\x0e\x32\x0f.ics23.LengthOp\x12\x0e\n\x06prefix\x18\x05 \x01(\x0c\"F\n\x07InnerOp\x12\x1b\n\x04hash\x18\x01 \x01(\x0e\x32\r.ics23.HashOp\x12\x0e\n\x06prefix\x18\x02 \x01(\x0c\x12\x0e\n\x06suffix\x18\x03 \x01(\x0c\"y\n\tProofSpec\x12 \n\tleaf_spec\x18\x01 \x01(\x0b\x32\r.ics23.LeafOp\x12$\n\ninner_spec\x18\x02 \x01(\x0b\x32\x10.ics23.InnerSpec\x12\x11\n\tmax_depth\x18\x03 \x01(\x05\x12\x11\n\tmin_depth\x18\x04 \x01(\x05\"\x9c\x01\n\tInnerSpec\x12\x13\n\x0b\x63hild_order\x18\x01 \x03(\x05\x12\x12\n\nchild_size\x18\x02 \x01(\x05\x12\x19\n\x11min_prefix_length\x18\x03 \x01(\x05\x12\x19\n\x11max_prefix_length\x18\x04 \x01(\x05\x12\x13\n\x0b\x65mpty_child\x18\x05 \x01(\x0c\x12\x1b\n\x04hash\x18\x06 \x01(\x0e\x32\r.ics23.HashOp\"0\n\nBatchProof\x12\"\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x11.ics23.BatchEntry\"k\n\nBatchEntry\x12&\n\x05\x65xist\x18\x01 \x01(\x0b\x32\x15.ics23.ExistenceProofH\x00\x12,\n\x08nonexist\x18\x02 \x01(\x0b\x32\x18.ics23.NonExistenceProofH\x00\x42\x07\n\x05proof\"k\n\x14\x43ompressedBatchProof\x12,\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1b.ics23.CompressedBatchEntry\x12%\n\rlookup_inners\x18\x02 \x03(\x0b\x32\x0e.ics23.InnerOp\"\x89\x01\n\x14\x43ompressedBatchEntry\x12\x30\n\x05\x65xist\x18\x01 \x01(\x0b\x32\x1f.ics23.CompressedExistenceProofH\x00\x12\x36\n\x08nonexist\x18\x02 \x01(\x0b\x32\".ics23.CompressedNonExistenceProofH\x00\x42\x07\n\x05proof\"a\n\x18\x43ompressedExistenceProof\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x1b\n\x04leaf\x18\x03 \x01(\x0b\x32\r.ics23.LeafOp\x12\x0c\n\x04path\x18\x04 \x03(\x05\"\x89\x01\n\x1b\x43ompressedNonExistenceProof\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12-\n\x04left\x18\x02 \x01(\x0b\x32\x1f.ics23.CompressedExistenceProof\x12.\n\x05right\x18\x03 \x01(\x0b\x32\x1f.ics23.CompressedExistenceProof*U\n\x06HashOp\x12\x0b\n\x07NO_HASH\x10\x00\x12\n\n\x06SHA256\x10\x01\x12\n\n\x06SHA512\x10\x02\x12\n\n\x06KECCAK\x10\x03\x12\r\n\tRIPEMD160\x10\x04\x12\x0b\n\x07\x42ITCOIN\x10\x05*\xab\x01\n\x08LengthOp\x12\r\n\tNO_PREFIX\x10\x00\x12\r\n\tVAR_PROTO\x10\x01\x12\x0b\n\x07VAR_RLP\x10\x02\x12\x0f\n\x0b\x46IXED32_BIG\x10\x03\x12\x12\n\x0e\x46IXED32_LITTLE\x10\x04\x12\x0f\n\x0b\x46IXED64_BIG\x10\x05\x12\x12\n\x0e\x46IXED64_LITTLE\x10\x06\x12\x14\n\x10REQUIRE_32_BYTES\x10\x07\x12\x14\n\x10REQUIRE_64_BYTES\x10\x08\x62\x06proto3'
)

_HASHOP = _descriptor.EnumDescriptor(
  name='HashOp',
  full_name='ics23.HashOp',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_HASH', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHA256', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHA512', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KECCAK', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RIPEMD160', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BITCOIN', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1610,
  serialized_end=1695,
)
_sym_db.RegisterEnumDescriptor(_HASHOP)

HashOp = enum_type_wrapper.EnumTypeWrapper(_HASHOP)
_LENGTHOP = _descriptor.EnumDescriptor(
  name='LengthOp',
  full_name='ics23.LengthOp',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_PREFIX', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VAR_PROTO', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VAR_RLP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIXED32_BIG', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIXED32_LITTLE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIXED64_BIG', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIXED64_LITTLE', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REQUIRE_32_BYTES', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REQUIRE_64_BYTES', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1698,
  serialized_end=1869,
)
_sym_db.RegisterEnumDescriptor(_LENGTHOP)

LengthOp = enum_type_wrapper.EnumTypeWrapper(_LENGTHOP)
NO_HASH = 0
SHA256 = 1
SHA512 = 2
KECCAK = 3
RIPEMD160 = 4
BITCOIN = 5
NO_PREFIX = 0
VAR_PROTO = 1
VAR_RLP = 2
FIXED32_BIG = 3
FIXED32_LITTLE = 4
FIXED64_BIG = 5
FIXED64_LITTLE = 6
REQUIRE_32_BYTES = 7
REQUIRE_64_BYTES = 8



_EXISTENCEPROOF = _descriptor.Descriptor(
  name='ExistenceProof',
  full_name='ics23.ExistenceProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ics23.ExistenceProof.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='ics23.ExistenceProof.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='leaf', full_name='ics23.ExistenceProof.leaf', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='ics23.ExistenceProof.path', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=30,
  serialized_end=133,
)


_NONEXISTENCEPROOF = _descriptor.Descriptor(
  name='NonExistenceProof',
  full_name='ics23.NonExistenceProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ics23.NonExistenceProof.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='left', full_name='ics23.NonExistenceProof.left', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='right', full_name='ics23.NonExistenceProof.right', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=135,
  serialized_end=242,
)


_COMMITMENTPROOF = _descriptor.Descriptor(
  name='CommitmentProof',
  full_name='ics23.CommitmentProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='exist', full_name='ics23.CommitmentProof.exist', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nonexist', full_name='ics23.CommitmentProof.nonexist', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch', full_name='ics23.CommitmentProof.batch', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compressed', full_name='ics23.CommitmentProof.compressed', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='proof', full_name='ics23.CommitmentProof.proof',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=245,
  serialized_end=444,
)


_LEAFOP = _descriptor.Descriptor(
  name='LeafOp',
  full_name='ics23.LeafOp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='ics23.LeafOp.hash', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prehash_key', full_name='ics23.LeafOp.prehash_key', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prehash_value', full_name='ics23.LeafOp.prehash_value', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='ics23.LeafOp.length', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='ics23.LeafOp.prefix', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=447,
  serialized_end=607,
)


_INNEROP = _descriptor.Descriptor(
  name='InnerOp',
  full_name='ics23.InnerOp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='ics23.InnerOp.hash', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='ics23.InnerOp.prefix', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='suffix', full_name='ics23.InnerOp.suffix', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=609,
  serialized_end=679,
)


_PROOFSPEC = _descriptor.Descriptor(
  name='ProofSpec',
  full_name='ics23.ProofSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='leaf_spec', full_name='ics23.ProofSpec.leaf_spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inner_spec', full_name='ics23.ProofSpec.inner_spec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_depth', full_name='ics23.ProofSpec.max_depth', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_depth', full_name='ics23.ProofSpec.min_depth', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=681,
  serialized_end=802,
)


_INNERSPEC = _descriptor.Descriptor(
  name='InnerSpec',
  full_name='ics23.InnerSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='child_order', full_name='ics23.InnerSpec.child_order', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='child_size', full_name='ics23.InnerSpec.child_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_prefix_length', full_name='ics23.InnerSpec.min_prefix_length', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_prefix_length', full_name='ics23.InnerSpec.max_prefix_length', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='empty_child', full_name='ics23.InnerSpec.empty_child', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash', full_name='ics23.InnerSpec.hash', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=805,
  serialized_end=961,
)


_BATCHPROOF = _descriptor.Descriptor(
  name='BatchProof',
  full_name='ics23.BatchProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='ics23.BatchProof.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=963,
  serialized_end=1011,
)


_BATCHENTRY = _descriptor.Descriptor(
  name='BatchEntry',
  full_name='ics23.BatchEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='exist', full_name='ics23.BatchEntry.exist', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nonexist', full_name='ics23.BatchEntry.nonexist', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='proof', full_name='ics23.BatchEntry.proof',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1013,
  serialized_end=1120,
)


_COMPRESSEDBATCHPROOF = _descriptor.Descriptor(
  name='CompressedBatchProof',
  full_name='ics23.CompressedBatchProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='ics23.CompressedBatchProof.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lookup_inners', full_name='ics23.CompressedBatchProof.lookup_inners', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1122,
  serialized_end=1229,
)


_COMPRESSEDBATCHENTRY = _descriptor.Descriptor(
  name='CompressedBatchEntry',
  full_name='ics23.CompressedBatchEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='exist', full_name='ics23.CompressedBatchEntry.exist', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nonexist', full_name='ics23.CompressedBatchEntry.nonexist', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='proof', full_name='ics23.CompressedBatchEntry.proof',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1232,
  serialized_end=1369,
)


_COMPRESSEDEXISTENCEPROOF = _descriptor.Descriptor(
  name='CompressedExistenceProof',
  full_name='ics23.CompressedExistenceProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ics23.CompressedExistenceProof.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='ics23.CompressedExistenceProof.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='leaf', full_name='ics23.CompressedExistenceProof.leaf', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='ics23.CompressedExistenceProof.path', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1371,
  serialized_end=1468,
)


_COMPRESSEDNONEXISTENCEPROOF = _descriptor.Descriptor(
  name='CompressedNonExistenceProof',
  full_name='ics23.CompressedNonExistenceProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ics23.CompressedNonExistenceProof.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='left', full_name='ics23.CompressedNonExistenceProof.left', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='right', full_name='ics23.CompressedNonExistenceProof.right', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1471,
  serialized_end=1608,
)

_EXISTENCEPROOF.fields_by_name['leaf'].message_type = _LEAFOP
_EXISTENCEPROOF.fields_by_name['path'].message_type = _INNEROP
_NONEXISTENCEPROOF.fields_by_name['left'].message_type = _EXISTENCEPROOF
_NONEXISTENCEPROOF.fields_by_name['right'].message_type = _EXISTENCEPROOF
_COMMITMENTPROOF.fields_by_name['exist'].message_type = _EXISTENCEPROOF
_COMMITMENTPROOF.fields_by_name['nonexist'].message_type = _NONEXISTENCEPROOF
_COMMITMENTPROOF.fields_by_name['batch'].message_type = _BATCHPROOF
_COMMITMENTPROOF.fields_by_name['compressed'].message_type = _COMPRESSEDBATCHPROOF
_COMMITMENTPROOF.oneofs_by_name['proof'].fields.append(
  _COMMITMENTPROOF.fields_by_name['exist'])
_COMMITMENTPROOF.fields_by_name['exist'].containing_oneof = _COMMITMENTPROOF.oneofs_by_name['proof']
_COMMITMENTPROOF.oneofs_by_name['proof'].fields.append(
  _COMMITMENTPROOF.fields_by_name['nonexist'])
_COMMITMENTPROOF.fields_by_name['nonexist'].containing_oneof = _COMMITMENTPROOF.oneofs_by_name['proof']
_COMMITMENTPROOF.oneofs_by_name['proof'].fields.append(
  _COMMITMENTPROOF.fields_by_name['batch'])
_COMMITMENTPROOF.fields_by_name['batch'].containing_oneof = _COMMITMENTPROOF.oneofs_by_name['proof']
_COMMITMENTPROOF.oneofs_by_name['proof'].fields.append(
  _COMMITMENTPROOF.fields_by_name['compressed'])
_COMMITMENTPROOF.fields_by_name['compressed'].containing_oneof = _COMMITMENTPROOF.oneofs_by_name['proof']
_LEAFOP.fields_by_name['hash'].enum_type = _HASHOP
_LEAFOP.fields_by_name['prehash_key'].enum_type = _HASHOP
_LEAFOP.fields_by_name['prehash_value'].enum_type = _HASHOP
_LEAFOP.fields_by_name['length'].enum_type = _LENGTHOP
_INNEROP.fields_by_name['hash'].enum_type = _HASHOP
_PROOFSPEC.fields_by_name['leaf_spec'].message_type = _LEAFOP
_PROOFSPEC.fields_by_name['inner_spec'].message_type = _INNERSPEC
_INNERSPEC.fields_by_name['hash'].enum_type = _HASHOP
_BATCHPROOF.fields_by_name['entries'].message_type = _BATCHENTRY
_BATCHENTRY.fields_by_name['exist'].message_type = _EXISTENCEPROOF
_BATCHENTRY.fields_by_name['nonexist'].message_type = _NONEXISTENCEPROOF
_BATCHENTRY.oneofs_by_name['proof'].fields.append(
  _BATCHENTRY.fields_by_name['exist'])
_BATCHENTRY.fields_by_name['exist'].containing_oneof = _BATCHENTRY.oneofs_by_name['proof']
_BATCHENTRY.oneofs_by_name['proof'].fields.append(
  _BATCHENTRY.fields_by_name['nonexist'])
_BATCHENTRY.fields_by_name['nonexist'].containing_oneof = _BATCHENTRY.oneofs_by_name['proof']
_COMPRESSEDBATCHPROOF.fields_by_name['entries'].message_type = _COMPRESSEDBATCHENTRY
_COMPRESSEDBATCHPROOF.fields_by_name['lookup_inners'].message_type = _INNEROP
_COMPRESSEDBATCHENTRY.fields_by_name['exist'].message_type = _COMPRESSEDEXISTENCEPROOF
_COMPRESSEDBATCHENTRY.fields_by_name['nonexist'].message_type = _COMPRESSEDNONEXISTENCEPROOF
_COMPRESSEDBATCHENTRY.oneofs_by_name['proof'].fields.append(
  _COMPRESSEDBATCHENTRY.fields_by_name['exist'])
_COMPRESSEDBATCHENTRY.fields_by_name['exist'].containing_oneof = _COMPRESSEDBATCHENTRY.oneofs_by_name['proof']
_COMPRESSEDBATCHENTRY.oneofs_by_name['proof'].fields.append(
  _COMPRESSEDBATCHENTRY.fields_by_name['nonexist'])
_COMPRESSEDBATCHENTRY.fields_by_name['nonexist'].containing_oneof = _COMPRESSEDBATCHENTRY.oneofs_by_name['proof']
_COMPRESSEDEXISTENCEPROOF.fields_by_name['leaf'].message_type = _LEAFOP
_COMPRESSEDNONEXISTENCEPROOF.fields_by_name['left'].message_type = _COMPRESSEDEXISTENCEPROOF
_COMPRESSEDNONEXISTENCEPROOF.fields_by_name['right'].message_type = _COMPRESSEDEXISTENCEPROOF
DESCRIPTOR.message_types_by_name['ExistenceProof'] = _EXISTENCEPROOF
DESCRIPTOR.message_types_by_name['NonExistenceProof'] = _NONEXISTENCEPROOF
DESCRIPTOR.message_types_by_name['CommitmentProof'] = _COMMITMENTPROOF
DESCRIPTOR.message_types_by_name['LeafOp'] = _LEAFOP
DESCRIPTOR.message_types_by_name['InnerOp'] = _INNEROP
DESCRIPTOR.message_types_by_name['ProofSpec'] = _PROOFSPEC
DESCRIPTOR.message_types_by_name['InnerSpec'] = _INNERSPEC
DESCRIPTOR.message_types_by_name['BatchProof'] = _BATCHPROOF
DESCRIPTOR.message_types_by_name['BatchEntry'] = _BATCHENTRY
DESCRIPTOR.message_types_by_name['CompressedBatchProof'] = _COMPRESSEDBATCHPROOF
DESCRIPTOR.message_types_by_name['CompressedBatchEntry'] = _COMPRESSEDBATCHENTRY
DESCRIPTOR.message_types_by_name['CompressedExistenceProof'] = _COMPRESSEDEXISTENCEPROOF
DESCRIPTOR.message_types_by_name['CompressedNonExistenceProof'] = _COMPRESSEDNONEXISTENCEPROOF
DESCRIPTOR.enum_types_by_name['HashOp'] = _HASHOP
DESCRIPTOR.enum_types_by_name['LengthOp'] = _LENGTHOP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExistenceProof = _reflection.GeneratedProtocolMessageType('ExistenceProof', (_message.Message,), {
  'DESCRIPTOR' : _EXISTENCEPROOF,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.ExistenceProof)
  })
_sym_db.RegisterMessage(ExistenceProof)

NonExistenceProof = _reflection.GeneratedProtocolMessageType('NonExistenceProof', (_message.Message,), {
  'DESCRIPTOR' : _NONEXISTENCEPROOF,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.NonExistenceProof)
  })
_sym_db.RegisterMessage(NonExistenceProof)

CommitmentProof = _reflection.GeneratedProtocolMessageType('CommitmentProof', (_message.Message,), {
  'DESCRIPTOR' : _COMMITMENTPROOF,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.CommitmentProof)
  })
_sym_db.RegisterMessage(CommitmentProof)

LeafOp = _reflection.GeneratedProtocolMessageType('LeafOp', (_message.Message,), {
  'DESCRIPTOR' : _LEAFOP,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.LeafOp)
  })
_sym_db.RegisterMessage(LeafOp)

InnerOp = _reflection.GeneratedProtocolMessageType('InnerOp', (_message.Message,), {
  'DESCRIPTOR' : _INNEROP,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.InnerOp)
  })
_sym_db.RegisterMessage(InnerOp)

ProofSpec = _reflection.GeneratedProtocolMessageType('ProofSpec', (_message.Message,), {
  'DESCRIPTOR' : _PROOFSPEC,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.ProofSpec)
  })
_sym_db.RegisterMessage(ProofSpec)

InnerSpec = _reflection.GeneratedProtocolMessageType('InnerSpec', (_message.Message,), {
  'DESCRIPTOR' : _INNERSPEC,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.InnerSpec)
  })
_sym_db.RegisterMessage(InnerSpec)

BatchProof = _reflection.GeneratedProtocolMessageType('BatchProof', (_message.Message,), {
  'DESCRIPTOR' : _BATCHPROOF,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.BatchProof)
  })
_sym_db.RegisterMessage(BatchProof)

BatchEntry = _reflection.GeneratedProtocolMessageType('BatchEntry', (_message.Message,), {
  'DESCRIPTOR' : _BATCHENTRY,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.BatchEntry)
  })
_sym_db.RegisterMessage(BatchEntry)

CompressedBatchProof = _reflection.GeneratedProtocolMessageType('CompressedBatchProof', (_message.Message,), {
  'DESCRIPTOR' : _COMPRESSEDBATCHPROOF,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.CompressedBatchProof)
  })
_sym_db.RegisterMessage(CompressedBatchProof)

CompressedBatchEntry = _reflection.GeneratedProtocolMessageType('CompressedBatchEntry', (_message.Message,), {
  'DESCRIPTOR' : _COMPRESSEDBATCHENTRY,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.CompressedBatchEntry)
  })
_sym_db.RegisterMessage(CompressedBatchEntry)

CompressedExistenceProof = _reflection.GeneratedProtocolMessageType('CompressedExistenceProof', (_message.Message,), {
  'DESCRIPTOR' : _COMPRESSEDEXISTENCEPROOF,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.CompressedExistenceProof)
  })
_sym_db.RegisterMessage(CompressedExistenceProof)

CompressedNonExistenceProof = _reflection.GeneratedProtocolMessageType('CompressedNonExistenceProof', (_message.Message,), {
  'DESCRIPTOR' : _COMPRESSEDNONEXISTENCEPROOF,
  '__module__' : 'confio.proofs_pb2'
  # @@protoc_insertion_point(class_scope:ics23.CompressedNonExistenceProof)
  })
_sym_db.RegisterMessage(CompressedNonExistenceProof)


# @@protoc_insertion_point(module_scope)
