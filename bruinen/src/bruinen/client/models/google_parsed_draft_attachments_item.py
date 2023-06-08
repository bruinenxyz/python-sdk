from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleParsedDraftAttachmentsItem")


@attr.s(auto_attribs=True)
class GoogleParsedDraftAttachmentsItem:
    """An attachment of the draft

    Attributes:
        attachment_id (Union[Unset, str]): The attachmentId of the attachment
        mime_type (Union[Unset, str]): The mimeType of the attachment
        filename (Union[Unset, str]): The filename of the attachment
        content_type (Union[Unset, str]): The contentType of the attachment
        content_disposition (Union[Unset, str]): The contentDisposition of the attachment
        content_transfer_encoding (Union[Unset, str]): The contentTransferEncoding of the attachment
        size (Union[Unset, float]): The size of the attachment
    """

    attachment_id: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    content_disposition: Union[Unset, str] = UNSET
    content_transfer_encoding: Union[Unset, str] = UNSET
    size: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attachment_id = self.attachment_id
        mime_type = self.mime_type
        filename = self.filename
        content_type = self.content_type
        content_disposition = self.content_disposition
        content_transfer_encoding = self.content_transfer_encoding
        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachment_id is not UNSET:
            field_dict["attachmentId"] = attachment_id
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if filename is not UNSET:
            field_dict["filename"] = filename
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if content_disposition is not UNSET:
            field_dict["contentDisposition"] = content_disposition
        if content_transfer_encoding is not UNSET:
            field_dict["contentTransferEncoding"] = content_transfer_encoding
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attachment_id = d.pop("attachmentId", UNSET) or UNSET

        mime_type = d.pop("mimeType", UNSET) or UNSET

        filename = d.pop("filename", UNSET) or UNSET

        content_type = d.pop("contentType", UNSET) or UNSET

        content_disposition = d.pop("contentDisposition", UNSET) or UNSET

        content_transfer_encoding = d.pop("contentTransferEncoding", UNSET) or UNSET

        size = d.pop("size", UNSET) or UNSET

        google_parsed_draft_attachments_item = cls(
            attachment_id=attachment_id,
            mime_type=mime_type,
            filename=filename,
            content_type=content_type,
            content_disposition=content_disposition,
            content_transfer_encoding=content_transfer_encoding,
            size=size,
        )

        google_parsed_draft_attachments_item.additional_properties = d
        return google_parsed_draft_attachments_item

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
