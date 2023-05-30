from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleProfile")


@attr.s(auto_attribs=True)
class GoogleProfile:
    """A google profile

    Attributes:
        email_address (Union[Unset, str]): The email of the user
        messages_total (Union[Unset, float]): The total messages of the user
        threads_total (Union[Unset, float]): The total email threads of the user
        history_id (Union[Unset, str]): The historyId of the user
    """

    email_address: Union[Unset, str] = UNSET
    messages_total: Union[Unset, float] = UNSET
    threads_total: Union[Unset, float] = UNSET
    history_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email_address = self.email_address
        messages_total = self.messages_total
        threads_total = self.threads_total
        history_id = self.history_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if messages_total is not UNSET:
            field_dict["messagesTotal"] = messages_total
        if threads_total is not UNSET:
            field_dict["threadsTotal"] = threads_total
        if history_id is not UNSET:
            field_dict["historyId"] = history_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email_address = d.pop("emailAddress", UNSET) or UNSET

        messages_total = d.pop("messagesTotal", UNSET) or UNSET

        threads_total = d.pop("threadsTotal", UNSET) or UNSET

        history_id = d.pop("historyId", UNSET) or UNSET

        google_profile = cls(
            email_address=email_address,
            messages_total=messages_total,
            threads_total=threads_total,
            history_id=history_id,
        )

        google_profile.additional_properties = d
        return google_profile

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
