from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_parsed_thread_messages_item import GoogleParsedThreadMessagesItem


T = TypeVar("T", bound="GoogleParsedThread")


@attr.s(auto_attribs=True)
class GoogleParsedThread:
    """Your google thread

    Attributes:
        id (Union[Unset, str]): The id of the thread
        messages (Union[Unset, List['GoogleParsedThreadMessagesItem']]): A list of the messages in the thread
    """

    id: Union[Unset, str] = UNSET
    messages: Union[Unset, List["GoogleParsedThreadMessagesItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
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
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_parsed_thread_messages_item import GoogleParsedThreadMessagesItem

        d = src_dict.copy()
        id = d.pop("id", UNSET) or UNSET

        messages = []
        _messages = d.pop("messages", UNSET) or UNSET
        for messages_item_data in _messages or []:
            messages_item = GoogleParsedThreadMessagesItem.from_dict(messages_item_data)

            messages.append(messages_item)

        google_parsed_thread = cls(
            id=id,
            messages=messages,
        )

        google_parsed_thread.additional_properties = d
        return google_parsed_thread

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
