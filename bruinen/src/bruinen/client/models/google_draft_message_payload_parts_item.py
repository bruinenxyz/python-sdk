from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_draft_message_payload_parts_item_body import GoogleDraftMessagePayloadPartsItemBody
    from ..models.google_draft_message_payload_parts_item_headers_item import (
        GoogleDraftMessagePayloadPartsItemHeadersItem,
    )
    from ..models.google_draft_message_payload_parts_item_parts_item import GoogleDraftMessagePayloadPartsItemPartsItem


T = TypeVar("T", bound="GoogleDraftMessagePayloadPartsItem")


@attr.s(auto_attribs=True)
class GoogleDraftMessagePayloadPartsItem:
    """
    Attributes:
        part_id (Union[Unset, str]): The partId of the part
        mime_type (Union[Unset, str]): The mimeType of the part
        filename (Union[Unset, str]): The filename of the part
        headers (Union[Unset, List['GoogleDraftMessagePayloadPartsItemHeadersItem']]): The headers of the part
        body (Union[Unset, GoogleDraftMessagePayloadPartsItemBody]): The body of the part
        parts (Union[Unset, List['GoogleDraftMessagePayloadPartsItemPartsItem']]): The parts of the part
    """

    part_id: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    headers: Union[Unset, List["GoogleDraftMessagePayloadPartsItemHeadersItem"]] = UNSET
    body: Union[Unset, "GoogleDraftMessagePayloadPartsItemBody"] = UNSET
    parts: Union[Unset, List["GoogleDraftMessagePayloadPartsItemPartsItem"]] = UNSET
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

        parts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parts, Unset):
            parts = []
            for parts_item_data in self.parts:
                parts_item = parts_item_data.to_dict()

                parts.append(parts_item)

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
        if parts is not UNSET:
            field_dict["parts"] = parts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_draft_message_payload_parts_item_body import GoogleDraftMessagePayloadPartsItemBody
        from ..models.google_draft_message_payload_parts_item_headers_item import (
            GoogleDraftMessagePayloadPartsItemHeadersItem,
        )
        from ..models.google_draft_message_payload_parts_item_parts_item import (
            GoogleDraftMessagePayloadPartsItemPartsItem,
        )

        d = src_dict.copy()
        part_id = d.pop("partId", UNSET) or UNSET

        mime_type = d.pop("mimeType", UNSET) or UNSET

        filename = d.pop("filename", UNSET) or UNSET

        headers = []
        _headers = d.pop("headers", UNSET) or UNSET
        for headers_item_data in _headers or []:
            headers_item = GoogleDraftMessagePayloadPartsItemHeadersItem.from_dict(headers_item_data)

            headers.append(headers_item)

        _body = d.pop("body", UNSET) or UNSET
        body: Union[Unset, GoogleDraftMessagePayloadPartsItemBody]
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = GoogleDraftMessagePayloadPartsItemBody.from_dict(_body)

        parts = []
        _parts = d.pop("parts", UNSET) or UNSET
        for parts_item_data in _parts or []:
            parts_item = GoogleDraftMessagePayloadPartsItemPartsItem.from_dict(parts_item_data)

            parts.append(parts_item)

        google_draft_message_payload_parts_item = cls(
            part_id=part_id,
            mime_type=mime_type,
            filename=filename,
            headers=headers,
            body=body,
            parts=parts,
        )

        google_draft_message_payload_parts_item.additional_properties = d
        return google_draft_message_payload_parts_item

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
