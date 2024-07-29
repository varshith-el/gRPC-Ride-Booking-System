# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12user_service.proto\x12\x04user\"^\n\x17UserRegistrationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x14\n\x0cphone_number\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\"+\n\x18UserRegistrationResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"3\n\x10UserLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"3\n\x11UserLoginResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\"\x19\n\x06UserId\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"R\n\x0cUserResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x14\n\x0cphone_number\x18\x04 \x01(\t2\xcd\x01\n\x0bUserService\x12O\n\x0cRegisterUser\x12\x1d.user.UserRegistrationRequest\x1a\x1e.user.UserRegistrationResponse\"\x00\x12>\n\tLoginUser\x12\x16.user.UserLoginRequest\x1a\x17.user.UserLoginResponse\"\x00\x12-\n\x07GetUser\x12\x0c.user.UserId\x1a\x12.user.UserResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERREGISTRATIONREQUEST']._serialized_start=28
  _globals['_USERREGISTRATIONREQUEST']._serialized_end=122
  _globals['_USERREGISTRATIONRESPONSE']._serialized_start=124
  _globals['_USERREGISTRATIONRESPONSE']._serialized_end=167
  _globals['_USERLOGINREQUEST']._serialized_start=169
  _globals['_USERLOGINREQUEST']._serialized_end=220
  _globals['_USERLOGINRESPONSE']._serialized_start=222
  _globals['_USERLOGINRESPONSE']._serialized_end=273
  _globals['_USERID']._serialized_start=275
  _globals['_USERID']._serialized_end=300
  _globals['_USERRESPONSE']._serialized_start=302
  _globals['_USERRESPONSE']._serialized_end=384
  _globals['_USERSERVICE']._serialized_start=387
  _globals['_USERSERVICE']._serialized_end=592
# @@protoc_insertion_point(module_scope)
