import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.confirmation_status import ConfirmationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.returned_confirm_dto_params import ReturnedConfirmDtoParams


T = TypeVar("T", bound="ReturnedConfirmDto")


@attr.s(auto_attribs=True)
class ReturnedConfirmDto:
    """
    Attributes:
        id (str):
        type (str):
        action (str):
        status (ConfirmationStatus):
        delivery_channel (str):
        delivery_address (Union[Unset, str]):
        used_at (Union[Unset, datetime.datetime]):
        responded_at (Union[Unset, datetime.datetime]):
        params (Union[Unset, ReturnedConfirmDtoParams]):
    """

    id: str
    type: str
    action: str
    status: ConfirmationStatus
    delivery_channel: str
    delivery_address: Union[Unset, str] = UNSET
    used_at: Union[Unset, datetime.datetime] = UNSET
    responded_at: Union[Unset, datetime.datetime] = UNSET
    params: Union[Unset, "ReturnedConfirmDtoParams"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        action = self.action
        status = self.status.value

        delivery_channel = self.delivery_channel
        delivery_address = self.delivery_address
        used_at: Union[Unset, str] = UNSET
        if not isinstance(self.used_at, Unset):
            used_at = self.used_at.isoformat()

        responded_at: Union[Unset, str] = UNSET
        if not isinstance(self.responded_at, Unset):
            responded_at = self.responded_at.isoformat()

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "action": action,
                "status": status,
                "deliveryChannel": delivery_channel,
            }
        )
        if delivery_address is not UNSET:
            field_dict["deliveryAddress"] = delivery_address
        if used_at is not UNSET:
            field_dict["usedAt"] = used_at
        if responded_at is not UNSET:
            field_dict["respondedAt"] = responded_at
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.returned_confirm_dto_params import ReturnedConfirmDtoParams

        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        action = d.pop("action")

        status = ConfirmationStatus(d.pop("status"))

        delivery_channel = d.pop("deliveryChannel")

        delivery_address = d.pop("deliveryAddress", UNSET) or UNSET

        _used_at = d.pop("usedAt", UNSET) or UNSET
        used_at: Union[Unset, datetime.datetime]
        if isinstance(_used_at, Unset):
            used_at = UNSET
        else:
            used_at = isoparse(_used_at)

        _responded_at = d.pop("respondedAt", UNSET) or UNSET
        responded_at: Union[Unset, datetime.datetime]
        if isinstance(_responded_at, Unset):
            responded_at = UNSET
        else:
            responded_at = isoparse(_responded_at)

        _params = d.pop("params", UNSET) or UNSET
        params: Union[Unset, ReturnedConfirmDtoParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = ReturnedConfirmDtoParams.from_dict(_params)

        returned_confirm_dto = cls(
            id=id,
            type=type,
            action=action,
            status=status,
            delivery_channel=delivery_channel,
            delivery_address=delivery_address,
            used_at=used_at,
            responded_at=responded_at,
            params=params,
        )

        returned_confirm_dto.additional_properties = d
        return returned_confirm_dto

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
