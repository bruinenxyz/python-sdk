from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_thread_messages_item_payload_parts_item_body import (
        GoogleThreadMessagesItemPayloadPartsItemBody,
    )
    from ..models.google_thread_messages_item_payload_parts_item_headers_item import (
        GoogleThreadMessagesItemPayloadPartsItemHeadersItem,
    )


T = TypeVar("T", bound="GoogleThreadMessagesItemPayloadPartsItem")


@attr.s(auto_attribs=True)
class GoogleThreadMessagesItemPayloadPartsItem:
    """
    Attributes:
        part_id (Union[Unset, str]): The partId of the part
        mime_type (Union[Unset, str]): The mimeType of the part
        filename (Union[Unset, str]): The filename of the part
        headers (Union[Unset, List['GoogleThreadMessagesItemPayloadPartsItemHeadersItem']]): The headers of the part
        body (Union[Unset, GoogleThreadMessagesItemPayloadPartsItemBody]): The body of the part
    """

    part_id: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    headers: Union[Unset, List["GoogleThreadMessagesItemPayloadPartsItemHeadersItem"]] = UNSET
    body: Union[Unset, "GoogleThreadMessagesItemPayloadPartsItemBody"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        part_id = self.part_id
        mime_type = self.mime_type
        filename = self.filename
        headers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()

                headers.append(headers_item)

        body: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if filename is not UNSET:
            field_dict["filename"] = filename
        if headers is not UNSET:
            field_dict["headers"] = headers
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_thread_messages_item_payload_parts_item_body import (
            GoogleThreadMessagesItemPayloadPartsItemBody,
        )
        from ..models.google_thread_messages_item_payload_parts_item_headers_item import (
            GoogleThreadMessagesItemPayloadPartsItemHeadersItem,
        )

        d = src_dict.copy()
        part_id = d.pop("partId", UNSET) or UNSET

        mime_type = d.pop("mimeType", UNSET) or UNSET

        filename = d.pop("filename", UNSET) or UNSET

        headers = []
        _headers = d.pop("headers", UNSET) or UNSET
        for headers_item_data in _headers or []:
            headers_item = GoogleThreadMessagesItemPayloadPartsItemHeadersItem.from_dict(headers_item_data)

            headers.append(headers_item)

        _body = d.pop("body", UNSET) or UNSET
        body: Union[Unset, GoogleThreadMessagesItemPayloadPartsItemBody]
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = GoogleThreadMessagesItemPayloadPartsItemBody.from_dict(_body)

        google_thread_messages_item_payload_parts_item = cls(
            part_id=part_id,
            mime_type=mime_type,
            filename=filename,
            headers=headers,
            body=body,
        )

        google_thread_messages_item_payload_parts_item.additional_properties = d
        return google_thread_messages_item_payload_parts_item

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
