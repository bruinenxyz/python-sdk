from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleParsedDraftHeadersCcItem")


@attr.s(auto_attribs=True)
class GoogleParsedDraftHeadersCcItem:
    """A cc of the draft

    Attributes:
        name (Union[Unset, str]): The name of the cc
        email (Union[Unset, str]): The email of the cc
    """

    name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET) or UNSET

        email = d.pop("email", UNSET) or UNSET

        google_parsed_draft_headers_cc_item = cls(
            name=name,
            email=email,
        )

        google_parsed_draft_headers_cc_item.additional_properties = d
        return google_parsed_draft_headers_cc_item

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
