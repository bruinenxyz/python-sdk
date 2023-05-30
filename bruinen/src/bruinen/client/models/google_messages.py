from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_messages_messages_item import GoogleMessagesMessagesItem


T = TypeVar("T", bound="GoogleMessages")


@attr.s(auto_attribs=True)
class GoogleMessages:
    """Your google messages

    Attributes:
        result_size_estimate (Union[Unset, float]): The result size estimate for your messages
        next_page_token (Union[Unset, str]): The next page token
        messages (Union[Unset, List['GoogleMessagesMessagesItem']]): A list of your google messages
    """

    result_size_estimate: Union[Unset, float] = UNSET
    next_page_token: Union[Unset, str] = UNSET
    messages: Union[Unset, List["GoogleMessagesMessagesItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result_size_estimate = self.result_size_estimate
        next_page_token = self.next_page_token
        messages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()

                messages.append(messages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result_size_estimate is not UNSET:
            field_dict["resultSizeEstimate"] = result_size_estimate
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_messages_messages_item import GoogleMessagesMessagesItem

        d = src_dict.copy()
        result_size_estimate = d.pop("resultSizeEstimate", UNSET) or UNSET

        next_page_token = d.pop("nextPageToken", UNSET) or UNSET

        messages = []
        _messages = d.pop("messages", UNSET) or UNSET
        for messages_item_data in _messages or []:
            messages_item = GoogleMessagesMessagesItem.from_dict(messages_item_data)

            messages.append(messages_item)

        google_messages = cls(
            result_size_estimate=result_size_estimate,
            next_page_token=next_page_token,
            messages=messages,
        )

        google_messages.additional_properties = d
        return google_messages

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
