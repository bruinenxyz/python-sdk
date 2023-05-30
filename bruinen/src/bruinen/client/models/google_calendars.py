from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_calendars_calendars_item import GoogleCalendarsCalendarsItem


T = TypeVar("T", bound="GoogleCalendars")


@attr.s(auto_attribs=True)
class GoogleCalendars:
    """Your google calendars

    Attributes:
        kind (Union[Unset, str]): The kind of the calendars
        etag (Union[Unset, str]): The etag of the calendars
        next_page_token (Union[Unset, str]): The next page token
        next_sync_token (Union[Unset, str]): The next sync token
        calendars (Union[Unset, List['GoogleCalendarsCalendarsItem']]): A list of your google calendars
    """

    kind: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    next_page_token: Union[Unset, str] = UNSET
    next_sync_token: Union[Unset, str] = UNSET
    calendars: Union[Unset, List["GoogleCalendarsCalendarsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind = self.kind
        etag = self.etag
        next_page_token = self.next_page_token
        next_sync_token = self.next_sync_token
        calendars: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.calendars, Unset):
            calendars = []
            for calendars_item_data in self.calendars:
                calendars_item = calendars_item_data.to_dict()

                calendars.append(calendars_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if etag is not UNSET:
            field_dict["etag"] = etag
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if next_sync_token is not UNSET:
            field_dict["nextSyncToken"] = next_sync_token
        if calendars is not UNSET:
            field_dict["calendars"] = calendars

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_calendars_calendars_item import GoogleCalendarsCalendarsItem

        d = src_dict.copy()
        kind = d.pop("kind", UNSET) or UNSET

        etag = d.pop("etag", UNSET) or UNSET

        next_page_token = d.pop("nextPageToken", UNSET) or UNSET

        next_sync_token = d.pop("nextSyncToken", UNSET) or UNSET

        calendars = []
        _calendars = d.pop("calendars", UNSET) or UNSET
        for calendars_item_data in _calendars or []:
            calendars_item = GoogleCalendarsCalendarsItem.from_dict(calendars_item_data)

            calendars.append(calendars_item)

        google_calendars = cls(
            kind=kind,
            etag=etag,
            next_page_token=next_page_token,
            next_sync_token=next_sync_token,
            calendars=calendars,
        )

        google_calendars.additional_properties = d
        return google_calendars

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
