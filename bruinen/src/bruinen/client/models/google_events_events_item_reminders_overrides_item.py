from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleEventsEventsItemRemindersOverridesItem")


@attr.s(auto_attribs=True)
class GoogleEventsEventsItemRemindersOverridesItem:
    """A reminder override

    Attributes:
        method (Union[Unset, str]): The method of the reminder override
        minutes (Union[Unset, float]): The minutes of the reminder override
    """

    method: Union[Unset, str] = UNSET
    minutes: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method = self.method
        minutes = self.minutes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if minutes is not UNSET:
            field_dict["minutes"] = minutes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        method = d.pop("method", UNSET) or UNSET

        minutes = d.pop("minutes", UNSET) or UNSET

        google_events_events_item_reminders_overrides_item = cls(
            method=method,
            minutes=minutes,
        )

        google_events_events_item_reminders_overrides_item.additional_properties = d
        return google_events_events_item_reminders_overrides_item

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
