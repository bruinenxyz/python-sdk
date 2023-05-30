from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_event_attachments_item import GoogleEventAttachmentsItem
    from ..models.google_event_attendees_item import GoogleEventAttendeesItem
    from ..models.google_event_conference_data import GoogleEventConferenceData
    from ..models.google_event_creator import GoogleEventCreator
    from ..models.google_event_end import GoogleEventEnd
    from ..models.google_event_extended_properties import GoogleEventExtendedProperties
    from ..models.google_event_gadget import GoogleEventGadget
    from ..models.google_event_organizer import GoogleEventOrganizer
    from ..models.google_event_original_start_time import GoogleEventOriginalStartTime
    from ..models.google_event_reminders import GoogleEventReminders
    from ..models.google_event_source import GoogleEventSource
    from ..models.google_event_start import GoogleEventStart


T = TypeVar("T", bound="GoogleEvent")


@attr.s(auto_attribs=True)
class GoogleEvent:
    """Your google calendar's event

    Attributes:
        kind (Union[Unset, str]): The kind of the event
        etag (Union[Unset, str]): The etag of the event
        id (Union[Unset, str]): The id of the event
        status (Union[Unset, str]): The status of the event
        html_link (Union[Unset, str]): The htmlLink of the event
        created (Union[Unset, str]): The created date of the event
        updated (Union[Unset, str]): The updated date of the event
        summary (Union[Unset, str]): The summary of the event
        description (Union[Unset, str]): The description of the event
        location (Union[Unset, str]): The location of the event
        color_id (Union[Unset, str]): The colorId of the event
        creator (Union[Unset, GoogleEventCreator]): The creator of the event
        organizer (Union[Unset, GoogleEventOrganizer]): The organizer of the event
        start (Union[Unset, GoogleEventStart]): The start of the event
        end (Union[Unset, GoogleEventEnd]): The end of the event
        end_time_unspecified (Union[Unset, bool]): Whether the endTime is unspecified
        recurrence (Union[Unset, List[str]]): The recurrence of the event
        recurring_event_id (Union[Unset, str]): The recurringEventId of the event
        original_start_time (Union[Unset, GoogleEventOriginalStartTime]): The originalStartTime of the event
        transparency (Union[Unset, str]): The transparency of the event
        visibility (Union[Unset, str]): The visibility of the event
        i_cal_uid (Union[Unset, str]): The iCalUID of the event
        sequence (Union[Unset, float]): The sequence of the event
        attendees (Union[Unset, List['GoogleEventAttendeesItem']]): The attendees of the event
        attendees_omitted (Union[Unset, bool]): Whether attendees are omitted
        extended_properties (Union[Unset, GoogleEventExtendedProperties]): The extendedProperties of the event
        hangout_link (Union[Unset, str]): The hangoutLink of the event
        conference_data (Union[Unset, GoogleEventConferenceData]): The conferenceData of the event
        gadget (Union[Unset, GoogleEventGadget]): The gadget of the event
        anyone_can_add_self (Union[Unset, bool]): Whether anyone can add self
        guests_can_invite_others (Union[Unset, bool]): Whether guests can invite others
        guests_can_modify (Union[Unset, bool]): Whether guests can modify
        guests_can_see_other_guests (Union[Unset, bool]): Whether guests can see other guests
        private_copy (Union[Unset, bool]): Whether the event is a private copy
        locked (Union[Unset, bool]): Whether the event is locked
        reminders (Union[Unset, GoogleEventReminders]): The reminders of the event
        source (Union[Unset, GoogleEventSource]): The source of the event
        attachments (Union[Unset, List['GoogleEventAttachmentsItem']]): The attachments of the event
        event_type (Union[Unset, str]): The eventType of the event
    """

    kind: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    html_link: Union[Unset, str] = UNSET
    created: Union[Unset, str] = UNSET
    updated: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    color_id: Union[Unset, str] = UNSET
    creator: Union[Unset, "GoogleEventCreator"] = UNSET
    organizer: Union[Unset, "GoogleEventOrganizer"] = UNSET
    start: Union[Unset, "GoogleEventStart"] = UNSET
    end: Union[Unset, "GoogleEventEnd"] = UNSET
    end_time_unspecified: Union[Unset, bool] = UNSET
    recurrence: Union[Unset, List[str]] = UNSET
    recurring_event_id: Union[Unset, str] = UNSET
    original_start_time: Union[Unset, "GoogleEventOriginalStartTime"] = UNSET
    transparency: Union[Unset, str] = UNSET
    visibility: Union[Unset, str] = UNSET
    i_cal_uid: Union[Unset, str] = UNSET
    sequence: Union[Unset, float] = UNSET
    attendees: Union[Unset, List["GoogleEventAttendeesItem"]] = UNSET
    attendees_omitted: Union[Unset, bool] = UNSET
    extended_properties: Union[Unset, "GoogleEventExtendedProperties"] = UNSET
    hangout_link: Union[Unset, str] = UNSET
    conference_data: Union[Unset, "GoogleEventConferenceData"] = UNSET
    gadget: Union[Unset, "GoogleEventGadget"] = UNSET
    anyone_can_add_self: Union[Unset, bool] = UNSET
    guests_can_invite_others: Union[Unset, bool] = UNSET
    guests_can_modify: Union[Unset, bool] = UNSET
    guests_can_see_other_guests: Union[Unset, bool] = UNSET
    private_copy: Union[Unset, bool] = UNSET
    locked: Union[Unset, bool] = UNSET
    reminders: Union[Unset, "GoogleEventReminders"] = UNSET
    source: Union[Unset, "GoogleEventSource"] = UNSET
    attachments: Union[Unset, List["GoogleEventAttachmentsItem"]] = UNSET
    event_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind = self.kind
        etag = self.etag
        id = self.id
        status = self.status
        html_link = self.html_link
        created = self.created
        updated = self.updated
        summary = self.summary
        description = self.description
        location = self.location
        color_id = self.color_id
        creator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        organizer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organizer, Unset):
            organizer = self.organizer.to_dict()

        start: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        end: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        end_time_unspecified = self.end_time_unspecified
        recurrence: Union[Unset, List[str]] = UNSET
        if not isinstance(self.recurrence, Unset):
            recurrence = self.recurrence

        recurring_event_id = self.recurring_event_id
        original_start_time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.original_start_time, Unset):
            original_start_time = self.original_start_time.to_dict()

        transparency = self.transparency
        visibility = self.visibility
        i_cal_uid = self.i_cal_uid
        sequence = self.sequence
        attendees: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attendees, Unset):
            attendees = []
            for attendees_item_data in self.attendees:
                attendees_item = attendees_item_data.to_dict()

                attendees.append(attendees_item)

        attendees_omitted = self.attendees_omitted
        extended_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extended_properties, Unset):
            extended_properties = self.extended_properties.to_dict()

        hangout_link = self.hangout_link
        conference_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conference_data, Unset):
            conference_data = self.conference_data.to_dict()

        gadget: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gadget, Unset):
            gadget = self.gadget.to_dict()

        anyone_can_add_self = self.anyone_can_add_self
        guests_can_invite_others = self.guests_can_invite_others
        guests_can_modify = self.guests_can_modify
        guests_can_see_other_guests = self.guests_can_see_other_guests
        private_copy = self.private_copy
        locked = self.locked
        reminders: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reminders, Unset):
            reminders = self.reminders.to_dict()

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        attachments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()

                attachments.append(attachments_item)

        event_type = self.event_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if html_link is not UNSET:
            field_dict["htmlLink"] = html_link
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location
        if color_id is not UNSET:
            field_dict["colorId"] = color_id
        if creator is not UNSET:
            field_dict["creator"] = creator
        if organizer is not UNSET:
            field_dict["organizer"] = organizer
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if end_time_unspecified is not UNSET:
            field_dict["endTimeUnspecified"] = end_time_unspecified
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if recurring_event_id is not UNSET:
            field_dict["recurringEventId"] = recurring_event_id
        if original_start_time is not UNSET:
            field_dict["originalStartTime"] = original_start_time
        if transparency is not UNSET:
            field_dict["transparency"] = transparency
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if i_cal_uid is not UNSET:
            field_dict["iCalUID"] = i_cal_uid
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if attendees is not UNSET:
            field_dict["attendees"] = attendees
        if attendees_omitted is not UNSET:
            field_dict["attendeesOmitted"] = attendees_omitted
        if extended_properties is not UNSET:
            field_dict["extendedProperties"] = extended_properties
        if hangout_link is not UNSET:
            field_dict["hangoutLink"] = hangout_link
        if conference_data is not UNSET:
            field_dict["conferenceData"] = conference_data
        if gadget is not UNSET:
            field_dict["gadget"] = gadget
        if anyone_can_add_self is not UNSET:
            field_dict["anyoneCanAddSelf"] = anyone_can_add_self
        if guests_can_invite_others is not UNSET:
            field_dict["guestsCanInviteOthers"] = guests_can_invite_others
        if guests_can_modify is not UNSET:
            field_dict["guestsCanModify"] = guests_can_modify
        if guests_can_see_other_guests is not UNSET:
            field_dict["guestsCanSeeOtherGuests"] = guests_can_see_other_guests
        if private_copy is not UNSET:
            field_dict["privateCopy"] = private_copy
        if locked is not UNSET:
            field_dict["locked"] = locked
        if reminders is not UNSET:
            field_dict["reminders"] = reminders
        if source is not UNSET:
            field_dict["source"] = source
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if event_type is not UNSET:
            field_dict["eventType"] = event_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_event_attachments_item import GoogleEventAttachmentsItem
        from ..models.google_event_attendees_item import GoogleEventAttendeesItem
        from ..models.google_event_conference_data import GoogleEventConferenceData
        from ..models.google_event_creator import GoogleEventCreator
        from ..models.google_event_end import GoogleEventEnd
        from ..models.google_event_extended_properties import GoogleEventExtendedProperties
        from ..models.google_event_gadget import GoogleEventGadget
        from ..models.google_event_organizer import GoogleEventOrganizer
        from ..models.google_event_original_start_time import GoogleEventOriginalStartTime
        from ..models.google_event_reminders import GoogleEventReminders
        from ..models.google_event_source import GoogleEventSource
        from ..models.google_event_start import GoogleEventStart

        d = src_dict.copy()
        kind = d.pop("kind", UNSET) or UNSET

        etag = d.pop("etag", UNSET) or UNSET

        id = d.pop("id", UNSET) or UNSET

        status = d.pop("status", UNSET) or UNSET

        html_link = d.pop("htmlLink", UNSET) or UNSET

        created = d.pop("created", UNSET) or UNSET

        updated = d.pop("updated", UNSET) or UNSET

        summary = d.pop("summary", UNSET) or UNSET

        description = d.pop("description", UNSET) or UNSET

        location = d.pop("location", UNSET) or UNSET

        color_id = d.pop("colorId", UNSET) or UNSET

        _creator = d.pop("creator", UNSET) or UNSET
        creator: Union[Unset, GoogleEventCreator]
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = GoogleEventCreator.from_dict(_creator)

        _organizer = d.pop("organizer", UNSET) or UNSET
        organizer: Union[Unset, GoogleEventOrganizer]
        if isinstance(_organizer, Unset):
            organizer = UNSET
        else:
            organizer = GoogleEventOrganizer.from_dict(_organizer)

        _start = d.pop("start", UNSET) or UNSET
        start: Union[Unset, GoogleEventStart]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = GoogleEventStart.from_dict(_start)

        _end = d.pop("end", UNSET) or UNSET
        end: Union[Unset, GoogleEventEnd]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = GoogleEventEnd.from_dict(_end)

        end_time_unspecified = d.pop("endTimeUnspecified", UNSET) or UNSET

        recurrence = cast(List[str], d.pop("recurrence", UNSET) or UNSET)

        recurring_event_id = d.pop("recurringEventId", UNSET) or UNSET

        _original_start_time = d.pop("originalStartTime", UNSET) or UNSET
        original_start_time: Union[Unset, GoogleEventOriginalStartTime]
        if isinstance(_original_start_time, Unset):
            original_start_time = UNSET
        else:
            original_start_time = GoogleEventOriginalStartTime.from_dict(_original_start_time)

        transparency = d.pop("transparency", UNSET) or UNSET

        visibility = d.pop("visibility", UNSET) or UNSET

        i_cal_uid = d.pop("iCalUID", UNSET) or UNSET

        sequence = d.pop("sequence", UNSET) or UNSET

        attendees = []
        _attendees = d.pop("attendees", UNSET) or UNSET
        for attendees_item_data in _attendees or []:
            attendees_item = GoogleEventAttendeesItem.from_dict(attendees_item_data)

            attendees.append(attendees_item)

        attendees_omitted = d.pop("attendeesOmitted", UNSET) or UNSET

        _extended_properties = d.pop("extendedProperties", UNSET) or UNSET
        extended_properties: Union[Unset, GoogleEventExtendedProperties]
        if isinstance(_extended_properties, Unset):
            extended_properties = UNSET
        else:
            extended_properties = GoogleEventExtendedProperties.from_dict(_extended_properties)

        hangout_link = d.pop("hangoutLink", UNSET) or UNSET

        _conference_data = d.pop("conferenceData", UNSET) or UNSET
        conference_data: Union[Unset, GoogleEventConferenceData]
        if isinstance(_conference_data, Unset):
            conference_data = UNSET
        else:
            conference_data = GoogleEventConferenceData.from_dict(_conference_data)

        _gadget = d.pop("gadget", UNSET) or UNSET
        gadget: Union[Unset, GoogleEventGadget]
        if isinstance(_gadget, Unset):
            gadget = UNSET
        else:
            gadget = GoogleEventGadget.from_dict(_gadget)

        anyone_can_add_self = d.pop("anyoneCanAddSelf", UNSET) or UNSET

        guests_can_invite_others = d.pop("guestsCanInviteOthers", UNSET) or UNSET

        guests_can_modify = d.pop("guestsCanModify", UNSET) or UNSET

        guests_can_see_other_guests = d.pop("guestsCanSeeOtherGuests", UNSET) or UNSET

        private_copy = d.pop("privateCopy", UNSET) or UNSET

        locked = d.pop("locked", UNSET) or UNSET

        _reminders = d.pop("reminders", UNSET) or UNSET
        reminders: Union[Unset, GoogleEventReminders]
        if isinstance(_reminders, Unset):
            reminders = UNSET
        else:
            reminders = GoogleEventReminders.from_dict(_reminders)

        _source = d.pop("source", UNSET) or UNSET
        source: Union[Unset, GoogleEventSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = GoogleEventSource.from_dict(_source)

        attachments = []
        _attachments = d.pop("attachments", UNSET) or UNSET
        for attachments_item_data in _attachments or []:
            attachments_item = GoogleEventAttachmentsItem.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        event_type = d.pop("eventType", UNSET) or UNSET

        google_event = cls(
            kind=kind,
            etag=etag,
            id=id,
            status=status,
            html_link=html_link,
            created=created,
            updated=updated,
            summary=summary,
            description=description,
            location=location,
            color_id=color_id,
            creator=creator,
            organizer=organizer,
            start=start,
            end=end,
            end_time_unspecified=end_time_unspecified,
            recurrence=recurrence,
            recurring_event_id=recurring_event_id,
            original_start_time=original_start_time,
            transparency=transparency,
            visibility=visibility,
            i_cal_uid=i_cal_uid,
            sequence=sequence,
            attendees=attendees,
            attendees_omitted=attendees_omitted,
            extended_properties=extended_properties,
            hangout_link=hangout_link,
            conference_data=conference_data,
            gadget=gadget,
            anyone_can_add_self=anyone_can_add_self,
            guests_can_invite_others=guests_can_invite_others,
            guests_can_modify=guests_can_modify,
            guests_can_see_other_guests=guests_can_see_other_guests,
            private_copy=private_copy,
            locked=locked,
            reminders=reminders,
            source=source,
            attachments=attachments,
            event_type=event_type,
        )

        google_event.additional_properties = d
        return google_event

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
