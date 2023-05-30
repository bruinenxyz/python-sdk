from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleEventAttachmentsItem")


@attr.s(auto_attribs=True)
class GoogleEventAttachmentsItem:
    """An attachment

    Attributes:
        file_url (Union[Unset, str]): The fileUrl of the attachment
        title (Union[Unset, str]): The title of the attachment
        mime_type (Union[Unset, str]): The mimeType of the attachment
        icon_link (Union[Unset, str]): The iconLink of the attachment
        file_id (Union[Unset, str]): The fileId of the attachment
    """

    file_url: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    icon_link: Union[Unset, str] = UNSET
    file_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_url = self.file_url
        title = self.title
        mime_type = self.mime_type
        icon_link = self.icon_link
        file_id = self.file_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_url is not UNSET:
            field_dict["fileUrl"] = file_url
        if title is not UNSET:
            field_dict["title"] = title
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if icon_link is not UNSET:
            field_dict["iconLink"] = icon_link
        if file_id is not UNSET:
            field_dict["fileId"] = file_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_url = d.pop("fileUrl", UNSET) or UNSET

        title = d.pop("title", UNSET) or UNSET

        mime_type = d.pop("mimeType", UNSET) or UNSET

        icon_link = d.pop("iconLink", UNSET) or UNSET

        file_id = d.pop("fileId", UNSET) or UNSET

        google_event_attachments_item = cls(
            file_url=file_url,
            title=title,
            mime_type=mime_type,
            icon_link=icon_link,
            file_id=file_id,
        )

        google_event_attachments_item.additional_properties = d
        return google_event_attachments_item

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
