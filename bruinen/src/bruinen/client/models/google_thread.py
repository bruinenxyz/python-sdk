from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_thread_messages_item import GoogleThreadMessagesItem


T = TypeVar("T", bound="GoogleThread")


@attr.s(auto_attribs=True)
class GoogleThread:
    """Your google thread

    Attributes:
        id (Union[Unset, str]): The id of the thread
        snippet (Union[Unset, str]): The snippet of the thread
        history_id (Union[Unset, str]): The historyId of the thread
        messages (Union[Unset, List['GoogleThreadMessagesItem']]): A list of the messages in the thread
    """

    id: Union[Unset, str] = UNSET
    snippet: Union[Unset, str] = UNSET
    history_id: Union[Unset, str] = UNSET
    messages: Union[Unset, List["GoogleThreadMessagesItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        snippet = self.snippet
        history_id = self.history_id
        messages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()

                messages.append(messages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if snippet is not UNSET:
            field_dict["snippet"] = snippet
        if history_id is not UNSET:
            field_dict["historyId"] = history_id
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_thread_messages_item import GoogleThreadMessagesItem

        d = src_dict.copy()
        id = d.pop("id", UNSET) or UNSET

        snippet = d.pop("snippet", UNSET) or UNSET

        history_id = d.pop("historyId", UNSET) or UNSET

        messages = []
        _messages = d.pop("messages", UNSET) or UNSET
        for messages_item_data in _messages or []:
            messages_item = GoogleThreadMessagesItem.from_dict(messages_item_data)

            messages.append(messages_item)

        google_thread = cls(
            id=id,
            snippet=snippet,
            history_id=history_id,
            messages=messages,
        )

        google_thread.additional_properties = d
        return google_thread

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
