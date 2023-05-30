from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_label_color import GoogleLabelColor


T = TypeVar("T", bound="GoogleLabel")


@attr.s(auto_attribs=True)
class GoogleLabel:
    """Your google label

    Attributes:
        id (Union[Unset, str]): The id of the label
        name (Union[Unset, str]): The name of the label
        message_list_visibility (Union[Unset, str]): The messageListVisibility of the label
        label_list_visibility (Union[Unset, str]): The labelListVisibility of the label
        type (Union[Unset, str]): The type of the label
        messages_total (Union[Unset, float]): The total messages for the label
        messages_unread (Union[Unset, float]): The total unread messages for the label
        threads_total (Union[Unset, float]): The total threads for the label
        threads_unread (Union[Unset, float]): The total unread threads for the label
        color (Union[Unset, GoogleLabelColor]): The color of the label
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    message_list_visibility: Union[Unset, str] = UNSET
    label_list_visibility: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    messages_total: Union[Unset, float] = UNSET
    messages_unread: Union[Unset, float] = UNSET
    threads_total: Union[Unset, float] = UNSET
    threads_unread: Union[Unset, float] = UNSET
    color: Union[Unset, "GoogleLabelColor"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        message_list_visibility = self.message_list_visibility
        label_list_visibility = self.label_list_visibility
        type = self.type
        messages_total = self.messages_total
        messages_unread = self.messages_unread
        threads_total = self.threads_total
        threads_unread = self.threads_unread
        color: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if message_list_visibility is not UNSET:
            field_dict["messageListVisibility"] = message_list_visibility
        if label_list_visibility is not UNSET:
            field_dict["labelListVisibility"] = label_list_visibility
        if type is not UNSET:
            field_dict["type"] = type
        if messages_total is not UNSET:
            field_dict["messagesTotal"] = messages_total
        if messages_unread is not UNSET:
            field_dict["messagesUnread"] = messages_unread
        if threads_total is not UNSET:
            field_dict["threadsTotal"] = threads_total
        if threads_unread is not UNSET:
            field_dict["threadsUnread"] = threads_unread
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_label_color import GoogleLabelColor

        d = src_dict.copy()
        id = d.pop("id", UNSET) or UNSET

        name = d.pop("name", UNSET) or UNSET

        message_list_visibility = d.pop("messageListVisibility", UNSET) or UNSET

        label_list_visibility = d.pop("labelListVisibility", UNSET) or UNSET

        type = d.pop("type", UNSET) or UNSET

        messages_total = d.pop("messagesTotal", UNSET) or UNSET

        messages_unread = d.pop("messagesUnread", UNSET) or UNSET

        threads_total = d.pop("threadsTotal", UNSET) or UNSET

        threads_unread = d.pop("threadsUnread", UNSET) or UNSET

        _color = d.pop("color", UNSET) or UNSET
        color: Union[Unset, GoogleLabelColor]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = GoogleLabelColor.from_dict(_color)

        google_label = cls(
            id=id,
            name=name,
            message_list_visibility=message_list_visibility,
            label_list_visibility=label_list_visibility,
            type=type,
            messages_total=messages_total,
            messages_unread=messages_unread,
            threads_total=threads_total,
            threads_unread=threads_unread,
            color=color,
        )

        google_label.additional_properties = d
        return google_label

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
