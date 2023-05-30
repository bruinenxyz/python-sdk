from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GoogleLabelInput")


@attr.s(auto_attribs=True)
class GoogleLabelInput:
    """The input for your google label

    Attributes:
        label_id (str): The id of the label
    """

    label_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label_id = self.label_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "labelId": label_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label_id = d.pop("labelId")

        google_label_input = cls(
            label_id=label_id,
        )

        google_label_input.additional_properties = d
        return google_label_input

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
