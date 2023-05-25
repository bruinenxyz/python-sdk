from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReturnedUserDto")


@attr.s(auto_attribs=True)
class ReturnedUserDto:
    """
    Attributes:
        id (str):
        client_id (str):
        external_id (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        email (Union[Unset, str]):
    """

    id: str
    client_id: str
    external_id: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        client_id = self.client_id
        external_id = self.external_id
        first_name = self.first_name
        last_name = self.last_name
        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "clientId": client_id,
            }
        )
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        client_id = d.pop("clientId")

        external_id = d.pop("externalId", UNSET) or UNSET

        first_name = d.pop("firstName", UNSET) or UNSET

        last_name = d.pop("lastName", UNSET) or UNSET

        email = d.pop("email", UNSET) or UNSET

        returned_user_dto = cls(
            id=id,
            client_id=client_id,
            external_id=external_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        returned_user_dto.additional_properties = d
        return returned_user_dto

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
