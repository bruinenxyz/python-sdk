from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleDraftMessagePayloadPartsItemPartsItemBody")


@attr.s(auto_attribs=True)
class GoogleDraftMessagePayloadPartsItemPartsItemBody:
    """The body of the part

    Attributes:
        size (Union[Unset, float]):
        data (Union[Unset, str]):
    """

    size: Union[Unset, float] = UNSET
    data: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        size = self.size
        data = self.data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if size is not UNSET:
            field_dict["size"] = size
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        size = d.pop("size", UNSET) or UNSET

        data = d.pop("data", UNSET) or UNSET

        google_draft_message_payload_parts_item_parts_item_body = cls(
            size=size,
            data=data,
        )

        google_draft_message_payload_parts_item_parts_item_body.additional_properties = d
        return google_draft_message_payload_parts_item_parts_item_body

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
