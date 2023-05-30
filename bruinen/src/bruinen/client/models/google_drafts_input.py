from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleDraftsInput")


@attr.s(auto_attribs=True)
class GoogleDraftsInput:
    """The input for your google drafts

    Attributes:
        page_token (Union[Unset, str]): The page token for your drafts
        q (Union[Unset, str]): The query for your drafts
    """

    page_token: Union[Unset, str] = UNSET
    q: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page_token = self.page_token
        q = self.q

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_token is not UNSET:
            field_dict["pageToken"] = page_token
        if q is not UNSET:
            field_dict["q"] = q

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page_token = d.pop("pageToken", UNSET) or UNSET

        q = d.pop("q", UNSET) or UNSET

        google_drafts_input = cls(
            page_token=page_token,
            q=q,
        )

        google_drafts_input.additional_properties = d
        return google_drafts_input

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
