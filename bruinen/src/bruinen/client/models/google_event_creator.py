from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleEventCreator")


@attr.s(auto_attribs=True)
class GoogleEventCreator:
    """The creator of the event

    Attributes:
        id (Union[Unset, str]): The id of the creator
        email (Union[Unset, str]): The email of the creator
        display_name (Union[Unset, str]): The displayName of the creator
        self_ (Union[Unset, bool]): Whether the creator is self
    """

    id: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    self_: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        email = self.email
        display_name = self.display_name
        self_ = self.self_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET) or UNSET

        email = d.pop("email", UNSET) or UNSET

        display_name = d.pop("displayName", UNSET) or UNSET

        self_ = d.pop("self", UNSET) or UNSET

        google_event_creator = cls(
            id=id,
            email=email,
            display_name=display_name,
            self_=self_,
        )

        google_event_creator.additional_properties = d
        return google_event_creator

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
