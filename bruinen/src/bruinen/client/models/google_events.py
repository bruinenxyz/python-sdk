from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_events_default_reminders_item import GoogleEventsDefaultRemindersItem
    from ..models.google_events_events_item import GoogleEventsEventsItem


T = TypeVar("T", bound="GoogleEvents")


@attr.s(auto_attribs=True)
class GoogleEvents:
    """Your google calendar's events

    Attributes:
        kind (Union[Unset, str]): The kind of the events
        etag (Union[Unset, str]): The etag of the events
        summary (Union[Unset, str]): The summary of the events
        description (Union[Unset, str]): The description of the events
        updated (Union[Unset, str]): The updated date of the events
        time_zone (Union[Unset, str]): The timeZone of the events
        access_role (Union[Unset, str]): The accessRole of the events
        default_reminders (Union[Unset, List['GoogleEventsDefaultRemindersItem']]): The defaultReminders of the events
        next_page_token (Union[Unset, str]): The nextPageToken of the events
        next_sync_token (Union[Unset, str]): The nextSyncToken of the events
        result_size_estimate (Union[Unset, float]): The resultSizeEstimate of the events
        events (Union[Unset, List['GoogleEventsEventsItem']]): The list of events
    """

    kind: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    updated: Union[Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    access_role: Union[Unset, str] = UNSET
    default_reminders: Union[Unset, List["GoogleEventsDefaultRemindersItem"]] = UNSET
    next_page_token: Union[Unset, str] = UNSET
    next_sync_token: Union[Unset, str] = UNSET
    result_size_estimate: Union[Unset, float] = UNSET
    events: Union[Unset, List["GoogleEventsEventsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind = self.kind
        etag = self.etag
        summary = self.summary
        description = self.description
        updated = self.updated
        time_zone = self.time_zone
        access_role = self.access_role
        default_reminders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.default_reminders, Unset):
            default_reminders = []
            for default_reminders_item_data in self.default_reminders:
                default_reminders_item = default_reminders_item_data.to_dict()

                default_reminders.append(default_reminders_item)

        next_page_token = self.next_page_token
        next_sync_token = self.next_sync_token
        result_size_estimate = self.result_size_estimate
        events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()

                events.append(events_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if etag is not UNSET:
            field_dict["etag"] = etag
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if updated is not UNSET:
            field_dict["updated"] = updated
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if access_role is not UNSET:
            field_dict["accessRole"] = access_role
        if default_reminders is not UNSET:
            field_dict["defaultReminders"] = default_reminders
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if next_sync_token is not UNSET:
            field_dict["nextSyncToken"] = next_sync_token
        if result_size_estimate is not UNSET:
            field_dict["resultSizeEstimate"] = result_size_estimate
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_events_default_reminders_item import GoogleEventsDefaultRemindersItem
        from ..models.google_events_events_item import GoogleEventsEventsItem

        d = src_dict.copy()
        kind = d.pop("kind", UNSET) or UNSET

        etag = d.pop("etag", UNSET) or UNSET

        summary = d.pop("summary", UNSET) or UNSET

        description = d.pop("description", UNSET) or UNSET

        updated = d.pop("updated", UNSET) or UNSET

        time_zone = d.pop("timeZone", UNSET) or UNSET

        access_role = d.pop("accessRole", UNSET) or UNSET

        default_reminders = []
        _default_reminders = d.pop("defaultReminders", UNSET) or UNSET
        for default_reminders_item_data in _default_reminders or []:
            default_reminders_item = GoogleEventsDefaultRemindersItem.from_dict(default_reminders_item_data)

            default_reminders.append(default_reminders_item)

        next_page_token = d.pop("nextPageToken", UNSET) or UNSET

        next_sync_token = d.pop("nextSyncToken", UNSET) or UNSET

        result_size_estimate = d.pop("resultSizeEstimate", UNSET) or UNSET

        events = []
        _events = d.pop("events", UNSET) or UNSET
        for events_item_data in _events or []:
            events_item = GoogleEventsEventsItem.from_dict(events_item_data)

            events.append(events_item)

        google_events = cls(
            kind=kind,
            etag=etag,
            summary=summary,
            description=description,
            updated=updated,
            time_zone=time_zone,
            access_role=access_role,
            default_reminders=default_reminders,
            next_page_token=next_page_token,
            next_sync_token=next_sync_token,
            result_size_estimate=result_size_estimate,
            events=events,
        )

        google_events.additional_properties = d
        return google_events

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
