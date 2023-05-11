from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindOrCreateUserDto")


@attr.s(auto_attribs=True)
class FindOrCreateUserDto:
    """
    Attributes:
        client_id (str):
        email (Union[Unset, str]):
        external_id (Union[Unset, str]):
    """

    client_id: str
    email: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id
        email = self.email
        external_id = self.external_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientId": client_id,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_id = d.pop("clientId")

        email = d.pop("email", UNSET) or UNSET

        external_id = d.pop("externalId", UNSET) or UNSET

        find_or_create_user_dto = cls(
            client_id=client_id,
            email=email,
            external_id=external_id,
        )

        find_or_create_user_dto.additional_properties = d
        return find_or_create_user_dto

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
