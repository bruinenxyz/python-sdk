from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.client_status import ClientStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReturnedClientDto")


@attr.s(auto_attribs=True)
class ReturnedClientDto:
    """
    Attributes:
        id (str):
        name (str):
        status (ClientStatus):
        clerk_id (Union[Unset, str]):
    """

    id: str
    name: str
    status: ClientStatus
    clerk_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        status = self.status.value

        clerk_id = self.clerk_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
            }
        )
        if clerk_id is not UNSET:
            field_dict["clerkId"] = clerk_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        status = ClientStatus(d.pop("status"))

        clerk_id = d.pop("clerkId", UNSET) or UNSET

        returned_client_dto = cls(
            id=id,
            name=name,
            status=status,
            clerk_id=clerk_id,
        )

        returned_client_dto.additional_properties = d
        return returned_client_dto

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
