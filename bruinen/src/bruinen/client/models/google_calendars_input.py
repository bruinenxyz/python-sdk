from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleCalendarsInput")


@attr.s(auto_attribs=True)
class GoogleCalendarsInput:
    """The input for your google calendars

    Attributes:
        page_token (Union[Unset, str]): The pageToken of the calendars
        show_deleted (Union[Unset, bool]): Whether to show deleted calendars
        show_hidden (Union[Unset, bool]): Whether to show hidden calendars
        sync_token (Union[Unset, str]): The syncToken of the calendars
    """

    page_token: Union[Unset, str] = UNSET
    show_deleted: Union[Unset, bool] = UNSET
    show_hidden: Union[Unset, bool] = UNSET
    sync_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page_token = self.page_token
        show_deleted = self.show_deleted
        show_hidden = self.show_hidden
        sync_token = self.sync_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_token is not UNSET:
            field_dict["pageToken"] = page_token
        if show_deleted is not UNSET:
            field_dict["showDeleted"] = show_deleted
        if show_hidden is not UNSET:
            field_dict["showHidden"] = show_hidden
        if sync_token is not UNSET:
            field_dict["syncToken"] = sync_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page_token = d.pop("pageToken", UNSET) or UNSET

        show_deleted = d.pop("showDeleted", UNSET) or UNSET

        show_hidden = d.pop("showHidden", UNSET) or UNSET

        sync_token = d.pop("syncToken", UNSET) or UNSET

        google_calendars_input = cls(
            page_token=page_token,
            show_deleted=show_deleted,
            show_hidden=show_hidden,
            sync_token=sync_token,
        )

        google_calendars_input.additional_properties = d
        return google_calendars_input

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
