from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateConfirmReturnedDto")


@attr.s(auto_attribs=True)
class CreateConfirmReturnedDto:
    """
    Attributes:
        delivered (bool):
        confirmation_id (str):
        magic_link (Union[Unset, str]):
    """

    delivered: bool
    confirmation_id: str
    magic_link: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delivered = self.delivered
        confirmation_id = self.confirmation_id
        magic_link = self.magic_link

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delivered": delivered,
                "confirmationId": confirmation_id,
            }
        )
        if magic_link is not UNSET:
            field_dict["magicLink"] = magic_link

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        delivered = d.pop("delivered")

        confirmation_id = d.pop("confirmationId")

        magic_link = d.pop("magicLink", UNSET) or UNSET

        create_confirm_returned_dto = cls(
            delivered=delivered,
            confirmation_id=confirmation_id,
            magic_link=magic_link,
        )

        create_confirm_returned_dto.additional_properties = d
        return create_confirm_returned_dto

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
