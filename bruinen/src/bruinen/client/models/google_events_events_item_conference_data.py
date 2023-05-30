from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_events_events_item_conference_data_conference_solution import (
        GoogleEventsEventsItemConferenceDataConferenceSolution,
    )
    from ..models.google_events_events_item_conference_data_create_request import (
        GoogleEventsEventsItemConferenceDataCreateRequest,
    )
    from ..models.google_events_events_item_conference_data_entry_points_item import (
        GoogleEventsEventsItemConferenceDataEntryPointsItem,
    )


T = TypeVar("T", bound="GoogleEventsEventsItemConferenceData")


@attr.s(auto_attribs=True)
class GoogleEventsEventsItemConferenceData:
    """The conferenceData of the event

    Attributes:
        create_request (Union[Unset, GoogleEventsEventsItemConferenceDataCreateRequest]): The createRequest of the
            conferenceData
        entry_points (Union[Unset, List['GoogleEventsEventsItemConferenceDataEntryPointsItem']]): The entryPoints of the
            conferenceData
        conference_solution (Union[Unset, GoogleEventsEventsItemConferenceDataConferenceSolution]): The
            conferenceSolution of the conferenceData
        conference_id (Union[Unset, str]): The conferenceId of the conferenceData
        signature (Union[Unset, str]): The signature of the conferenceData
        notes (Union[Unset, str]): The notes of the conferenceData
    """

    create_request: Union[Unset, "GoogleEventsEventsItemConferenceDataCreateRequest"] = UNSET
    entry_points: Union[Unset, List["GoogleEventsEventsItemConferenceDataEntryPointsItem"]] = UNSET
    conference_solution: Union[Unset, "GoogleEventsEventsItemConferenceDataConferenceSolution"] = UNSET
    conference_id: Union[Unset, str] = UNSET
    signature: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        create_request: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.create_request, Unset):
            create_request = self.create_request.to_dict()

        entry_points: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entry_points, Unset):
            entry_points = []
            for entry_points_item_data in self.entry_points:
                entry_points_item = entry_points_item_data.to_dict()

                entry_points.append(entry_points_item)

        conference_solution: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conference_solution, Unset):
            conference_solution = self.conference_solution.to_dict()

        conference_id = self.conference_id
        signature = self.signature
        notes = self.notes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_request is not UNSET:
            field_dict["createRequest"] = create_request
        if entry_points is not UNSET:
            field_dict["entryPoints"] = entry_points
        if conference_solution is not UNSET:
            field_dict["conferenceSolution"] = conference_solution
        if conference_id is not UNSET:
            field_dict["conferenceId"] = conference_id
        if signature is not UNSET:
            field_dict["signature"] = signature
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_events_events_item_conference_data_conference_solution import (
            GoogleEventsEventsItemConferenceDataConferenceSolution,
        )
        from ..models.google_events_events_item_conference_data_create_request import (
            GoogleEventsEventsItemConferenceDataCreateRequest,
        )
        from ..models.google_events_events_item_conference_data_entry_points_item import (
            GoogleEventsEventsItemConferenceDataEntryPointsItem,
        )

        d = src_dict.copy()
        _create_request = d.pop("createRequest", UNSET) or UNSET
        create_request: Union[Unset, GoogleEventsEventsItemConferenceDataCreateRequest]
        if isinstance(_create_request, Unset):
            create_request = UNSET
        else:
            create_request = GoogleEventsEventsItemConferenceDataCreateRequest.from_dict(_create_request)

        entry_points = []
        _entry_points = d.pop("entryPoints", UNSET) or UNSET
        for entry_points_item_data in _entry_points or []:
            entry_points_item = GoogleEventsEventsItemConferenceDataEntryPointsItem.from_dict(entry_points_item_data)

            entry_points.append(entry_points_item)

        _conference_solution = d.pop("conferenceSolution", UNSET) or UNSET
        conference_solution: Union[Unset, GoogleEventsEventsItemConferenceDataConferenceSolution]
        if isinstance(_conference_solution, Unset):
            conference_solution = UNSET
        else:
            conference_solution = GoogleEventsEventsItemConferenceDataConferenceSolution.from_dict(_conference_solution)

        conference_id = d.pop("conferenceId", UNSET) or UNSET

        signature = d.pop("signature", UNSET) or UNSET

        notes = d.pop("notes", UNSET) or UNSET

        google_events_events_item_conference_data = cls(
            create_request=create_request,
            entry_points=entry_points,
            conference_solution=conference_solution,
            conference_id=conference_id,
            signature=signature,
            notes=notes,
        )

        google_events_events_item_conference_data.additional_properties = d
        return google_events_events_item_conference_data

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
