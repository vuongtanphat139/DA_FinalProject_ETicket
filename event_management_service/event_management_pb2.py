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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x65vent_management.proto\x12\x10\x65vent_management\"\xb6\x02\n\x05\x45vent\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x10\n\x08\x64\x61tetime\x18\x05 \x01(\t\x12\x11\n\tbannerURL\x18\x06 \x01(\t\x12\x0b\n\x03url\x18\x07 \x01(\t\x12\r\n\x05venue\x18\x08 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\t \x01(\t\x12\r\n\x05orgId\x18\n \x01(\x05\x12\x16\n\x0eminTicketPrice\x18\x0b \x01(\x05\x12\x0e\n\x06status\x18\x0c \x01(\t\x12\x12\n\nstatusName\x18\r \x01(\t\x12\x12\n\norgLogoURL\x18\x0e \x01(\t\x12\x0f\n\x07orgName\x18\x0f \x01(\t\x12\x16\n\x0eorgDescription\x18\x10 \x01(\t\x12\x12\n\ncategories\x18\x11 \x01(\t\".\n\tUserEvent\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\x05\"\x1f\n\x11UserEventResponse\x12\n\n\x02id\x18\x01 \x01(\x05\"l\n\x0cOrganization\x12\n\n\x02id\x18\x01 \x01(\x05\x12\'\n\x06\x65vents\x18\x02 \x01(\x0b\x32\x17.event_management.Event\x12\x0f\n\x07orgName\x18\x03 \x01(\t\x12\x16\n\x0eorgDescription\x18\x04 \x01(\t\"\x90\x01\n\x07Showing\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x12\n\nstatusName\x18\x03 \x01(\t\x12\x11\n\tstartTime\x18\x08 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\t \x01(\t\x12\x31\n\x0bticketTypes\x18\x0c \x03(\x0b\x32\x1c.event_management.TicketType\"\x9c\x02\n\nTicketType\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05\x63olor\x18\x04 \x01(\t\x12\x0e\n\x06isFree\x18\x05 \x01(\x08\x12\r\n\x05price\x18\x06 \x01(\x05\x12\x15\n\roriginalPrice\x18\x07 \x01(\x05\x12\x16\n\x0emaxQtyPerOrder\x18\x08 \x01(\x05\x12\x16\n\x0eminQtyPerOrder\x18\t \x01(\x05\x12\x11\n\tstartTime\x18\n \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x0b \x01(\t\x12\x10\n\x08position\x18\x0c \x01(\x05\x12\x0e\n\x06status\x18\r \x01(\t\x12\x12\n\nstatusName\x18\x0e \x01(\t\x12\x10\n\x08imageUrl\x18\x0f \x01(\t\"\x07\n\x05\x45mpty\"Y\n\rEventResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12&\n\x05\x65vent\x18\x03 \x01(\x0b\x32\x17.event_management.Event\"?\n\x0eSearchCriteria\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t\x12\r\n\x05topic\x18\x03 \x01(\t\"4\n\tEventList\x12\'\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x17.event_management.Event\"D\n\rTicketRequest\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x10\n\x08quantity\x18\x03 \x01(\x05\"2\n\x0eTicketResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x14\n\x06UserID\x12\n\n\x02id\x18\x01 \x01(\x05\"U\n\x0fGetEventRequest\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\ncategories\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_nameB\r\n\x0b_categories\"!\n\x13GetEventByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\'\n\x16GetEventByOrgIdRequest\x12\r\n\x05orgId\x18\x01 \x01(\x05\"q\n\x12\x43reateEventRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tbannerURL\x18\x02 \x01(\t\x12\x10\n\x08\x64\x61tetime\x18\x03 \x01(\t\x12\x16\n\x0eminTicketPrice\x18\x04 \x01(\x05\x12\x10\n\x08location\x18\x05 \x01(\t2\xdf\x05\n\x0f\x45ventManagement\x12L\n\x0b\x43reateEvent\x12$.event_management.CreateEventRequest\x1a\x17.event_management.Event\x12G\n\x0bUpdateEvent\x12\x17.event_management.Event\x1a\x1f.event_management.EventResponse\x12J\n\x08GetEvent\x12!.event_management.GetEventRequest\x1a\x1b.event_management.EventList\x12N\n\x0cGetEventById\x12%.event_management.GetEventByIdRequest\x1a\x17.event_management.Event\x12X\n\x0fGetEventByOrgId\x12(.event_management.GetEventByOrgIdRequest\x1a\x1b.event_management.EventList\x12M\n\x0cSearchEvents\x12 .event_management.SearchCriteria\x1a\x1b.event_management.EventList\x12S\n\x0ePurchaseTicket\x12\x1f.event_management.TicketRequest\x1a .event_management.TicketResponse\x12\x46\n\rGetUserEvents\x12\x18.event_management.UserID\x1a\x1b.event_management.EventList\x12S\n\x0f\x43reateUserEvent\x12\x1b.event_management.UserEvent\x1a#.event_management.UserEventResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event_management_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EVENT']._serialized_start=45
  _globals['_EVENT']._serialized_end=355
  _globals['_USEREVENT']._serialized_start=357
  _globals['_USEREVENT']._serialized_end=403
  _globals['_USEREVENTRESPONSE']._serialized_start=405
  _globals['_USEREVENTRESPONSE']._serialized_end=436
  _globals['_ORGANIZATION']._serialized_start=438
  _globals['_ORGANIZATION']._serialized_end=546
  _globals['_SHOWING']._serialized_start=549
  _globals['_SHOWING']._serialized_end=693
  _globals['_TICKETTYPE']._serialized_start=696
  _globals['_TICKETTYPE']._serialized_end=980
  _globals['_EMPTY']._serialized_start=982
  _globals['_EMPTY']._serialized_end=989
  _globals['_EVENTRESPONSE']._serialized_start=991
  _globals['_EVENTRESPONSE']._serialized_end=1080
  _globals['_SEARCHCRITERIA']._serialized_start=1082
  _globals['_SEARCHCRITERIA']._serialized_end=1145
  _globals['_EVENTLIST']._serialized_start=1147
  _globals['_EVENTLIST']._serialized_end=1199
  _globals['_TICKETREQUEST']._serialized_start=1201
  _globals['_TICKETREQUEST']._serialized_end=1269
  _globals['_TICKETRESPONSE']._serialized_start=1271
  _globals['_TICKETRESPONSE']._serialized_end=1321
  _globals['_USERID']._serialized_start=1323
  _globals['_USERID']._serialized_end=1343
  _globals['_GETEVENTREQUEST']._serialized_start=1345
  _globals['_GETEVENTREQUEST']._serialized_end=1430
  _globals['_GETEVENTBYIDREQUEST']._serialized_start=1432
  _globals['_GETEVENTBYIDREQUEST']._serialized_end=1465
  _globals['_GETEVENTBYORGIDREQUEST']._serialized_start=1467
  _globals['_GETEVENTBYORGIDREQUEST']._serialized_end=1506
  _globals['_CREATEEVENTREQUEST']._serialized_start=1508
  _globals['_CREATEEVENTREQUEST']._serialized_end=1621
  _globals['_EVENTMANAGEMENT']._serialized_start=1624
  _globals['_EVENTMANAGEMENT']._serialized_end=2359
# @@protoc_insertion_point(module_scope)
