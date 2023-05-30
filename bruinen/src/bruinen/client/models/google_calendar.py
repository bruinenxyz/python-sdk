from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_calendar_conference_properties import GoogleCalendarConferenceProperties


T = TypeVar("T", bound="GoogleCalendar")


@attr.s(auto_attribs=True)
class GoogleCalendar:
    """Your google calendar

    Attributes:
        kind (Union[Unset, str]): The kind of the calendar
        etag (Union[Unset, str]): The etag of the calendar
        id (Union[Unset, str]): The id of the calendar
        summary (Union[Unset, str]): The summary of the calendar
        description (Union[Unset, str]): The description of the calendar
        location (Union[Unset, str]): The location of the calendar
        time_zone (Union[Unset, str]): The timeZone of the calendar
        conference_properties (Union[Unset, GoogleCalendarConferenceProperties]): The conferenceProperties of the
            calendar
    """

    kind: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    conference_properties: Union[Unset, "GoogleCalendarConferenceProperties"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind = self.kind
        etag = self.etag
        id = self.id
        summary = self.summary
        description = self.description
        location = self.location
        time_zone = self.time_zone
        conference_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conference_properties, Unset):
            conference_properties = self.conference_properties.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if conference_properties is not UNSET:
            field_dict["conferenceProperties"] = conference_properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_calendar_conference_properties import GoogleCalendarConferenceProperties

        d = src_dict.copy()
        kind = d.pop("kind", UNSET) or UNSET

        etag = d.pop("etag", UNSET) or UNSET

        id = d.pop("id", UNSET) or UNSET

        summary = d.pop("summary", UNSET) or UNSET

        description = d.pop("description", UNSET) or UNSET

        location = d.pop("location", UNSET) or UNSET

        time_zone = d.pop("timeZone", UNSET) or UNSET

        _conference_properties = d.pop("conferenceProperties", UNSET) or UNSET
        conference_properties: Union[Unset, GoogleCalendarConferenceProperties]
        if isinstance(_conference_properties, Unset):
            conference_properties = UNSET
        else:
            conference_properties = GoogleCalendarConferenceProperties.from_dict(_conference_properties)

        google_calendar = cls(
            kind=kind,
            etag=etag,
            id=id,
            summary=summary,
            description=description,
            location=location,
            time_zone=time_zone,
            conference_properties=conference_properties,
        )

        google_calendar.additional_properties = d
        return google_calendar

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
