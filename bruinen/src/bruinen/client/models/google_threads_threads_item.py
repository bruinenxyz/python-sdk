from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleThreadsThreadsItem")


@attr.s(auto_attribs=True)
class GoogleThreadsThreadsItem:
    """
    Attributes:
        id (Union[Unset, str]): The id of the thread
        snippet (Union[Unset, str]): The snippet of the thread
        history_id (Union[Unset, str]): The historyId of the thread
    """

    id: Union[Unset, str] = UNSET
    snippet: Union[Unset, str] = UNSET
    history_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        snippet = self.snippet
        history_id = self.history_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if snippet is not UNSET:
            field_dict["snippet"] = snippet
        if history_id is not UNSET:
            field_dict["historyId"] = history_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET) or UNSET

        snippet = d.pop("snippet", UNSET) or UNSET

        history_id = d.pop("historyId", UNSET) or UNSET

        google_threads_threads_item = cls(
            id=id,
            snippet=snippet,
            history_id=history_id,
        )

        google_threads_threads_item.additional_properties = d
        return google_threads_threads_item

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
