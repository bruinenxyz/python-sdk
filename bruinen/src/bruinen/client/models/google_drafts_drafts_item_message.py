from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleDraftsDraftsItemMessage")


@attr.s(auto_attribs=True)
class GoogleDraftsDraftsItemMessage:
    """The message of the draft

    Attributes:
        id (Union[Unset, str]): The id of the message
        thread_id (Union[Unset, str]): The threadId of the message
    """

    id: Union[Unset, str] = UNSET
    thread_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        thread_id = self.thread_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET) or UNSET

        thread_id = d.pop("threadId", UNSET) or UNSET

        google_drafts_drafts_item_message = cls(
            id=id,
            thread_id=thread_id,
        )

        google_drafts_drafts_item_message.additional_properties = d
        return google_drafts_drafts_item_message

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
