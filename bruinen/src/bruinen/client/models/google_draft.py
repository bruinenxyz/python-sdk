from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_draft_message import GoogleDraftMessage


T = TypeVar("T", bound="GoogleDraft")


@attr.s(auto_attribs=True)
class GoogleDraft:
    """Your google draft

    Attributes:
        id (Union[Unset, str]): The id of the draft
        message (Union[Unset, GoogleDraftMessage]): The message of the draft
    """

    id: Union[Unset, str] = UNSET
    message: Union[Unset, "GoogleDraftMessage"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        message: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_draft_message import GoogleDraftMessage

        d = src_dict.copy()
        id = d.pop("id", UNSET) or UNSET

        _message = d.pop("message", UNSET) or UNSET
        message: Union[Unset, GoogleDraftMessage]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = GoogleDraftMessage.from_dict(_message)

        google_draft = cls(
            id=id,
            message=message,
        )

        google_draft.additional_properties = d
        return google_draft

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
