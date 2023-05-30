from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleEventInput")


@attr.s(auto_attribs=True)
class GoogleEventInput:
    """The input for your google calendar's event

    Attributes:
        calendar_id (str): The calendarId of the calendar which contains the event
        event_id (str): The id of the event
        time_zone (Union[Unset, str]): The timeZone of the event
    """

    calendar_id: str
    event_id: str
    time_zone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        calendar_id = self.calendar_id
        event_id = self.event_id
        time_zone = self.time_zone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "calendarId": calendar_id,
                "eventId": event_id,
            }
        )
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        calendar_id = d.pop("calendarId")

        event_id = d.pop("eventId")

        time_zone = d.pop("timeZone", UNSET) or UNSET

        google_event_input = cls(
            calendar_id=calendar_id,
            event_id=event_id,
            time_zone=time_zone,
        )

        google_event_input.additional_properties = d
        return google_event_input

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
