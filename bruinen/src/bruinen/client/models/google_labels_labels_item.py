from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleLabelsLabelsItem")


@attr.s(auto_attribs=True)
class GoogleLabelsLabelsItem:
    """
    Attributes:
        id (Union[Unset, str]): The id of the label
        name (Union[Unset, str]): The name of the label
        message_list_visibility (Union[Unset, str]): The messageListVisibility of the label
        label_list_visibility (Union[Unset, str]): The labelListVisibility of the label
        type (Union[Unset, str]): The type of the label
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    message_list_visibility: Union[Unset, str] = UNSET
    label_list_visibility: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        message_list_visibility = self.message_list_visibility
        label_list_visibility = self.label_list_visibility
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if message_list_visibility is not UNSET:
            field_dict["messageListVisibility"] = message_list_visibility
        if label_list_visibility is not UNSET:
            field_dict["labelListVisibility"] = label_list_visibility
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET) or UNSET

        name = d.pop("name", UNSET) or UNSET

        message_list_visibility = d.pop("messageListVisibility", UNSET) or UNSET

        label_list_visibility = d.pop("labelListVisibility", UNSET) or UNSET

        type = d.pop("type", UNSET) or UNSET

        google_labels_labels_item = cls(
            id=id,
            name=name,
            message_list_visibility=message_list_visibility,
            label_list_visibility=label_list_visibility,
            type=type,
        )

        google_labels_labels_item.additional_properties = d
        return google_labels_labels_item

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
