from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_parsed_thread_messages_item_attachments_item import (
        GoogleParsedThreadMessagesItemAttachmentsItem,
    )
    from ..models.google_parsed_thread_messages_item_headers import GoogleParsedThreadMessagesItemHeaders


T = TypeVar("T", bound="GoogleParsedThreadMessagesItem")


@attr.s(auto_attribs=True)
class GoogleParsedThreadMessagesItem:
    """A message in the thread

    Attributes:
        id (Union[Unset, str]): The id of the message
        thread_id (Union[Unset, str]): The threadId of the message
        label_ids (Union[Unset, List[str]]): The labelIds of the message
        headers (Union[Unset, GoogleParsedThreadMessagesItemHeaders]): The headers of the message
        body (Union[Unset, str]): The body of the message
        attachments (Union[Unset, List['GoogleParsedThreadMessagesItemAttachmentsItem']]): The attachments of the
            message
    """

    id: Union[Unset, str] = UNSET
    thread_id: Union[Unset, str] = UNSET
    label_ids: Union[Unset, List[str]] = UNSET
    headers: Union[Unset, "GoogleParsedThreadMessagesItemHeaders"] = UNSET
    body: Union[Unset, str] = UNSET
    attachments: Union[Unset, List["GoogleParsedThreadMessagesItemAttachmentsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        thread_id = self.thread_id
        label_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.label_ids, Unset):
            label_ids = self.label_ids

        headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        body = self.body
        attachments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()

                attachments.append(attachments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if label_ids is not UNSET:
            field_dict["labelIds"] = label_ids
        if headers is not UNSET:
            field_dict["headers"] = headers
        if body is not UNSET:
            field_dict["body"] = body
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_parsed_thread_messages_item_attachments_item import (
            GoogleParsedThreadMessagesItemAttachmentsItem,
        )
        from ..models.google_parsed_thread_messages_item_headers import GoogleParsedThreadMessagesItemHeaders

        d = src_dict.copy()
        id = d.pop("id", UNSET) or UNSET

        thread_id = d.pop("threadId", UNSET) or UNSET

        label_ids = cast(List[str], d.pop("labelIds", UNSET) or UNSET)

        _headers = d.pop("headers", UNSET) or UNSET
        headers: Union[Unset, GoogleParsedThreadMessagesItemHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = GoogleParsedThreadMessagesItemHeaders.from_dict(_headers)

        body = d.pop("body", UNSET) or UNSET

        attachments = []
        _attachments = d.pop("attachments", UNSET) or UNSET
        for attachments_item_data in _attachments or []:
            attachments_item = GoogleParsedThreadMessagesItemAttachmentsItem.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        google_parsed_thread_messages_item = cls(
            id=id,
            thread_id=thread_id,
            label_ids=label_ids,
            headers=headers,
            body=body,
            attachments=attachments,
        )

        google_parsed_thread_messages_item.additional_properties = d
        return google_parsed_thread_messages_item

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
