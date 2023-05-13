from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateClientDto")


@attr.s(auto_attribs=True)
class CreateClientDto:
    """
    Attributes:
        name (str):
        clerk_id (Union[Unset, str]):
    """

    name: str
    clerk_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        clerk_id = self.clerk_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if clerk_id is not UNSET:
            field_dict["clerkId"] = clerk_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        clerk_id = d.pop("clerkId", UNSET) or UNSET

        create_client_dto = cls(
            name=name,
            clerk_id=clerk_id,
        )

        create_client_dto.additional_properties = d
        return create_client_dto

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
