from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_events_events_item_conference_data_conference_solution_key import (
        GoogleEventsEventsItemConferenceDataConferenceSolutionKey,
    )


T = TypeVar("T", bound="GoogleEventsEventsItemConferenceDataConferenceSolution")


@attr.s(auto_attribs=True)
class GoogleEventsEventsItemConferenceDataConferenceSolution:
    """The conferenceSolution of the conferenceData

    Attributes:
        key (Union[Unset, GoogleEventsEventsItemConferenceDataConferenceSolutionKey]): The key of the conferenceSolution
        name (Union[Unset, str]): The name of the conferenceSolution
        icon_uri (Union[Unset, str]): The iconUri of the conferenceSolution
    """

    key: Union[Unset, "GoogleEventsEventsItemConferenceDataConferenceSolutionKey"] = UNSET
    name: Union[Unset, str] = UNSET
    icon_uri: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        name = self.name
        icon_uri = self.icon_uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if icon_uri is not UNSET:
            field_dict["iconUri"] = icon_uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_events_events_item_conference_data_conference_solution_key import (
            GoogleEventsEventsItemConferenceDataConferenceSolutionKey,
        )

        d = src_dict.copy()
        _key = d.pop("key", UNSET) or UNSET
        key: Union[Unset, GoogleEventsEventsItemConferenceDataConferenceSolutionKey]
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = GoogleEventsEventsItemConferenceDataConferenceSolutionKey.from_dict(_key)

        name = d.pop("name", UNSET) or UNSET

        icon_uri = d.pop("iconUri", UNSET) or UNSET

        google_events_events_item_conference_data_conference_solution = cls(
            key=key,
            name=name,
            icon_uri=icon_uri,
        )

        google_events_events_item_conference_data_conference_solution.additional_properties = d
        return google_events_events_item_conference_data_conference_solution

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
