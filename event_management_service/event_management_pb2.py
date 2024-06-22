# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_management.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x65vent_management.proto\x12\x10\x65vent_management\"\xa1\x01\n\x05\x45vent\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\x04name\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08location\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x15\n\x08\x64\x61tetime\x18\x05 \x01(\tH\x03\x88\x01\x01\x42\x07\n\x05_nameB\x0e\n\x0c_descriptionB\x0b\n\t_locationB\x0b\n\t_datetime\"\x07\n\x05\x45mpty\"\x8a\x01\n\rEventResponse\x12\x14\n\x07success\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x12+\n\x05\x65vent\x18\x03 \x01(\x0b\x32\x17.event_management.EventH\x02\x88\x01\x01\x42\n\n\x08_successB\n\n\x08_messageB\x08\n\x06_event\"n\n\x0eSearchCriteria\x12\x11\n\x04\x64\x61te\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08location\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05topic\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x07\n\x05_dateB\x0b\n\t_locationB\x08\n\x06_topic\"4\n\tEventList\x12\'\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x17.event_management.Event\"y\n\rTicketRequest\x12\x15\n\x08\x65vent_id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07user_id\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x15\n\x08quantity\x18\x03 \x01(\x05H\x02\x88\x01\x01\x42\x0b\n\t_event_idB\n\n\x08_user_idB\x0b\n\t_quantity\"T\n\x0eTicketResponse\x12\x14\n\x07success\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\n\n\x08_successB\n\n\x08_message\"\x14\n\x06UserID\x12\n\n\x02id\x18\x01 \x01(\x05\x32\xd1\x03\n\x0f\x45ventManagement\x12G\n\x0b\x43reateEvent\x12\x17.event_management.Event\x1a\x1f.event_management.EventResponse\x12G\n\x0bUpdateEvent\x12\x17.event_management.Event\x1a\x1f.event_management.EventResponse\x12@\n\x08GetEvent\x12\x17.event_management.Empty\x1a\x1b.event_management.EventList\x12M\n\x0cSearchEvents\x12 .event_management.SearchCriteria\x1a\x1b.event_management.EventList\x12S\n\x0ePurchaseTicket\x12\x1f.event_management.TicketRequest\x1a .event_management.TicketResponse\x12\x46\n\rGetUserEvents\x12\x18.event_management.UserID\x1a\x1b.event_management.EventListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_management_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EVENT']._serialized_start=45
  _globals['_EVENT']._serialized_end=206
  _globals['_EMPTY']._serialized_start=208
  _globals['_EMPTY']._serialized_end=215
  _globals['_EVENTRESPONSE']._serialized_start=218
  _globals['_EVENTRESPONSE']._serialized_end=356
  _globals['_SEARCHCRITERIA']._serialized_start=358
  _globals['_SEARCHCRITERIA']._serialized_end=468
  _globals['_EVENTLIST']._serialized_start=470
  _globals['_EVENTLIST']._serialized_end=522
  _globals['_TICKETREQUEST']._serialized_start=524
  _globals['_TICKETREQUEST']._serialized_end=645
  _globals['_TICKETRESPONSE']._serialized_start=647
  _globals['_TICKETRESPONSE']._serialized_end=731
  _globals['_USERID']._serialized_start=733
  _globals['_USERID']._serialized_end=753
  _globals['_EVENTMANAGEMENT']._serialized_start=756
  _globals['_EVENTMANAGEMENT']._serialized_end=1221
# @@protoc_insertion_point(module_scope)