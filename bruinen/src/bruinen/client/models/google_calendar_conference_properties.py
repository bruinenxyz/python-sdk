from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleCalendarConferenceProperties")


@attr.s(auto_attribs=True)
class GoogleCalendarConferenceProperties:
    """The conferenceProperties of the calendar

    Attributes:
        allowed_conference_solution_types (Union[Unset, List[str]]): The allowedConferenceSolutionTypes of the
            conferenceProperties
    """

    allowed_conference_solution_types: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allowed_conference_solution_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed_conference_solution_types, Unset):
            allowed_conference_solution_types = self.allowed_conference_solution_types

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_conference_solution_types is not UNSET:
            field_dict["allowedConferenceSolutionTypes"] = allowed_conference_solution_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allowed_conference_solution_types = cast(List[str], d.pop("allowedConferenceSolutionTypes", UNSET) or UNSET)

        google_calendar_conference_properties = cls(
            allowed_conference_solution_types=allowed_conference_solution_types,
        )

        google_calendar_conference_properties.additional_properties = d
        return google_calendar_conference_properties

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
