from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleLabelColor")


@attr.s(auto_attribs=True)
class GoogleLabelColor:
    """The color of the label

    Attributes:
        text_color (Union[Unset, str]):
        background_color (Union[Unset, str]):
    """

    text_color: Union[Unset, str] = UNSET
    background_color: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text_color = self.text_color
        background_color = self.background_color

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text_color is not UNSET:
            field_dict["textColor"] = text_color
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text_color = d.pop("textColor", UNSET) or UNSET

        background_color = d.pop("backgroundColor", UNSET) or UNSET

        google_label_color = cls(
            text_color=text_color,
            background_color=background_color,
        )

        google_label_color.additional_properties = d
        return google_label_color

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
