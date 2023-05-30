from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleEventsEventsItemConferenceDataEntryPointsItem")


@attr.s(auto_attribs=True)
class GoogleEventsEventsItemConferenceDataEntryPointsItem:
    """An entryPoint

    Attributes:
        entry_point_type (Union[Unset, str]): The entryPointType of the entryPoint
        uri (Union[Unset, str]): The uri of the entryPoint
        label (Union[Unset, str]): The label of the entryPoint
        pin (Union[Unset, str]): The pin of the entryPoint
        access_code (Union[Unset, str]): The accessCode of the entryPoint
        meeting_code (Union[Unset, str]): The meetingCode of the entryPoint
        passcode (Union[Unset, str]): The passcode of the entryPoint
        password (Union[Unset, str]): The password of the entryPoint
    """

    entry_point_type: Union[Unset, str] = UNSET
    uri: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    pin: Union[Unset, str] = UNSET
    access_code: Union[Unset, str] = UNSET
    meeting_code: Union[Unset, str] = UNSET
    passcode: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry_point_type = self.entry_point_type
        uri = self.uri
        label = self.label
        pin = self.pin
        access_code = self.access_code
        meeting_code = self.meeting_code
        passcode = self.passcode
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry_point_type is not UNSET:
            field_dict["entryPointType"] = entry_point_type
        if uri is not UNSET:
            field_dict["uri"] = uri
        if label is not UNSET:
            field_dict["label"] = label
        if pin is not UNSET:
            field_dict["pin"] = pin
        if access_code is not UNSET:
            field_dict["accessCode"] = access_code
        if meeting_code is not UNSET:
            field_dict["meetingCode"] = meeting_code
        if passcode is not UNSET:
            field_dict["passcode"] = passcode
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entry_point_type = d.pop("entryPointType", UNSET) or UNSET

        uri = d.pop("uri", UNSET) or UNSET

        label = d.pop("label", UNSET) or UNSET

        pin = d.pop("pin", UNSET) or UNSET

        access_code = d.pop("accessCode", UNSET) or UNSET

        meeting_code = d.pop("meetingCode", UNSET) or UNSET

        passcode = d.pop("passcode", UNSET) or UNSET

        password = d.pop("password", UNSET) or UNSET

        google_events_events_item_conference_data_entry_points_item = cls(
            entry_point_type=entry_point_type,
            uri=uri,
            label=label,
            pin=pin,
            access_code=access_code,
            meeting_code=meeting_code,
            passcode=passcode,
            password=password,
        )

        google_events_events_item_conference_data_entry_points_item.additional_properties = d
        return google_events_events_item_conference_data_entry_points_item

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
