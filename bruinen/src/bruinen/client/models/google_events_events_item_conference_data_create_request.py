from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_events_events_item_conference_data_create_request_conference_solution_key import (
        GoogleEventsEventsItemConferenceDataCreateRequestConferenceSolutionKey,
    )
    from ..models.google_events_events_item_conference_data_create_request_status import (
        GoogleEventsEventsItemConferenceDataCreateRequestStatus,
    )


T = TypeVar("T", bound="GoogleEventsEventsItemConferenceDataCreateRequest")


@attr.s(auto_attribs=True)
class GoogleEventsEventsItemConferenceDataCreateRequest:
    """The createRequest of the conferenceData

    Attributes:
        request_id (Union[Unset, str]): The requestId of the createRequest
        conference_solution_key (Union[Unset, GoogleEventsEventsItemConferenceDataCreateRequestConferenceSolutionKey]):
            The conferenceSolutionKey of the createRequest
        status (Union[Unset, GoogleEventsEventsItemConferenceDataCreateRequestStatus]): The status of the createRequest
    """

    request_id: Union[Unset, str] = UNSET
    conference_solution_key: Union[
        Unset, "GoogleEventsEventsItemConferenceDataCreateRequestConferenceSolutionKey"
    ] = UNSET
    status: Union[Unset, "GoogleEventsEventsItemConferenceDataCreateRequestStatus"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id
        conference_solution_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conference_solution_key, Unset):
            conference_solution_key = self.conference_solution_key.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if conference_solution_key is not UNSET:
            field_dict["conferenceSolutionKey"] = conference_solution_key
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_events_events_item_conference_data_create_request_conference_solution_key import (
            GoogleEventsEventsItemConferenceDataCreateRequestConferenceSolutionKey,
        )
        from ..models.google_events_events_item_conference_data_create_request_status import (
            GoogleEventsEventsItemConferenceDataCreateRequestStatus,
        )

        d = src_dict.copy()
        request_id = d.pop("requestId", UNSET) or UNSET

        _conference_solution_key = d.pop("conferenceSolutionKey", UNSET) or UNSET
        conference_solution_key: Union[Unset, GoogleEventsEventsItemConferenceDataCreateRequestConferenceSolutionKey]
        if isinstance(_conference_solution_key, Unset):
            conference_solution_key = UNSET
        else:
            conference_solution_key = GoogleEventsEventsItemConferenceDataCreateRequestConferenceSolutionKey.from_dict(
                _conference_solution_key
            )

        _status = d.pop("status", UNSET) or UNSET
        status: Union[Unset, GoogleEventsEventsItemConferenceDataCreateRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GoogleEventsEventsItemConferenceDataCreateRequestStatus.from_dict(_status)

        google_events_events_item_conference_data_create_request = cls(
            request_id=request_id,
            conference_solution_key=conference_solution_key,
            status=status,
        )

        google_events_events_item_conference_data_create_request.additional_properties = d
        return google_events_events_item_conference_data_create_request

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
