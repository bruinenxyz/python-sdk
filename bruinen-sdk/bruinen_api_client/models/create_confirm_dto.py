from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_confirm_dto_params import CreateConfirmDtoParams


T = TypeVar("T", bound="CreateConfirmDto")


@attr.s(auto_attribs=True)
class CreateConfirmDto:
    """
    Attributes:
        type (str):
        action (str):
        delivery_channel (str):
        delivery_address (Union[Unset, str]):
        params (Union[Unset, CreateConfirmDtoParams]):
    """

    type: str
    action: str
    delivery_channel: str
    delivery_address: Union[Unset, str] = UNSET
    params: Union[Unset, "CreateConfirmDtoParams"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        action = self.action
        delivery_channel = self.delivery_channel
        delivery_address = self.delivery_address
        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "action": action,
                "deliveryChannel": delivery_channel,
            }
        )
        if delivery_address is not UNSET:
            field_dict["deliveryAddress"] = delivery_address
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_confirm_dto_params import CreateConfirmDtoParams

        d = src_dict.copy()
        type = d.pop("type")

        action = d.pop("action")

        delivery_channel = d.pop("deliveryChannel")

        delivery_address = d.pop("deliveryAddress", UNSET) or UNSET

        _params = d.pop("params", UNSET) or UNSET
        params: Union[Unset, CreateConfirmDtoParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = CreateConfirmDtoParams.from_dict(_params)

        create_confirm_dto = cls(
            type=type,
            action=action,
            delivery_channel=delivery_channel,
            delivery_address=delivery_address,
            params=params,
        )

        create_confirm_dto.additional_properties = d
        return create_confirm_dto

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
