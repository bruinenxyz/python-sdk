from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_events_events_item_extended_properties_private import (
        GoogleEventsEventsItemExtendedPropertiesPrivate,
    )
    from ..models.google_events_events_item_extended_properties_shared import (
        GoogleEventsEventsItemExtendedPropertiesShared,
    )


T = TypeVar("T", bound="GoogleEventsEventsItemExtendedProperties")


@attr.s(auto_attribs=True)
class GoogleEventsEventsItemExtendedProperties:
    """The extendedProperties of the event

    Attributes:
        private (Union[Unset, GoogleEventsEventsItemExtendedPropertiesPrivate]): The private extendedProperties of the
            event
        shared (Union[Unset, GoogleEventsEventsItemExtendedPropertiesShared]): The shared extendedProperties of the
            event
    """

    private: Union[Unset, "GoogleEventsEventsItemExtendedPropertiesPrivate"] = UNSET
    shared: Union[Unset, "GoogleEventsEventsItemExtendedPropertiesShared"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        private: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.private, Unset):
            private = self.private.to_dict()

        shared: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shared, Unset):
            shared = self.shared.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if private is not UNSET:
            field_dict["private"] = private
        if shared is not UNSET:
            field_dict["shared"] = shared

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_events_events_item_extended_properties_private import (
            GoogleEventsEventsItemExtendedPropertiesPrivate,
        )
        from ..models.google_events_events_item_extended_properties_shared import (
            GoogleEventsEventsItemExtendedPropertiesShared,
        )

        d = src_dict.copy()
        _private = d.pop("private", UNSET) or UNSET
        private: Union[Unset, GoogleEventsEventsItemExtendedPropertiesPrivate]
        if isinstance(_private, Unset):
            private = UNSET
        else:
            private = GoogleEventsEventsItemExtendedPropertiesPrivate.from_dict(_private)

        _shared = d.pop("shared", UNSET) or UNSET
        shared: Union[Unset, GoogleEventsEventsItemExtendedPropertiesShared]
        if isinstance(_shared, Unset):
            shared = UNSET
        else:
            shared = GoogleEventsEventsItemExtendedPropertiesShared.from_dict(_shared)

        google_events_events_item_extended_properties = cls(
            private=private,
            shared=shared,
        )

        google_events_events_item_extended_properties.additional_properties = d
        return google_events_events_item_extended_properties

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
