from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GoogleEventsEventsItemExtendedPropertiesPrivate")


@attr.s(auto_attribs=True)
class GoogleEventsEventsItemExtendedPropertiesPrivate:
    """The private extendedProperties of the event"""

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        google_events_events_item_extended_properties_private = cls()

        google_events_events_item_extended_properties_private.additional_properties = d
        return google_events_events_item_extended_properties_private

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
