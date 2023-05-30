from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GoogleCalendarInput")


@attr.s(auto_attribs=True)
class GoogleCalendarInput:
    """The input for your google calendar

    Attributes:
        calendar_id (str): The id of the calendar
    """

    calendar_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        calendar_id = self.calendar_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "calendarId": calendar_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        calendar_id = d.pop("calendarId")

        google_calendar_input = cls(
            calendar_id=calendar_id,
        )

        google_calendar_input.additional_properties = d
        return google_calendar_input

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
