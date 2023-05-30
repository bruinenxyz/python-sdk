from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleEventsEventsItemOriginalStartTime")


@attr.s(auto_attribs=True)
class GoogleEventsEventsItemOriginalStartTime:
    """The originalStartTime of the event

    Attributes:
        date (Union[Unset, str]): The date of the originalStartTime
        date_time (Union[Unset, str]): The dateTime of the originalStartTime
        time_zone (Union[Unset, str]): The timeZone of the originalStartTime
    """

    date: Union[Unset, str] = UNSET
    date_time: Union[Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date
        date_time = self.date_time
        time_zone = self.time_zone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if date_time is not UNSET:
            field_dict["dateTime"] = date_time
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date", UNSET) or UNSET

        date_time = d.pop("dateTime", UNSET) or UNSET

        time_zone = d.pop("timeZone", UNSET) or UNSET

        google_events_events_item_original_start_time = cls(
            date=date,
            date_time=date_time,
            time_zone=time_zone,
        )

        google_events_events_item_original_start_time.additional_properties = d
        return google_events_events_item_original_start_time

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
