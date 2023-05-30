from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleEventsEventsItemConferenceDataConferenceSolutionKey")


@attr.s(auto_attribs=True)
class GoogleEventsEventsItemConferenceDataConferenceSolutionKey:
    """The key of the conferenceSolution

    Attributes:
        type (Union[Unset, str]): The type of the key
    """

    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET) or UNSET

        google_events_events_item_conference_data_conference_solution_key = cls(
            type=type,
        )

        google_events_events_item_conference_data_conference_solution_key.additional_properties = d
        return google_events_events_item_conference_data_conference_solution_key

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
