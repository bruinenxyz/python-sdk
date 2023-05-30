from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleEventsInput")


@attr.s(auto_attribs=True)
class GoogleEventsInput:
    """The input for your google calendar's events

    Attributes:
        calendar_id (Union[Unset, str]): The id of the calendar
        max_attendees (Union[Unset, float]): The max attendees
        order_by (Union[Unset, str]): The order by
        page_token (Union[Unset, str]): The page token
        q (Union[Unset, str]): The query
        show_deleted (Union[Unset, bool]): Whether to show deleted
        single_events (Union[Unset, bool]): Whether to show single events
        time_max (Union[Unset, str]): The time max
        time_min (Union[Unset, str]): The time min
        time_zone (Union[Unset, str]): The time zone
        updated_min (Union[Unset, str]): The updated min
        sync_token (Union[Unset, str]): The sync token
        i_cal_uid (Union[Unset, str]): The iCal UID
    """

    calendar_id: Union[Unset, str] = UNSET
    max_attendees: Union[Unset, float] = UNSET
    order_by: Union[Unset, str] = UNSET
    page_token: Union[Unset, str] = UNSET
    q: Union[Unset, str] = UNSET
    show_deleted: Union[Unset, bool] = UNSET
    single_events: Union[Unset, bool] = UNSET
    time_max: Union[Unset, str] = UNSET
    time_min: Union[Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    updated_min: Union[Unset, str] = UNSET
    sync_token: Union[Unset, str] = UNSET
    i_cal_uid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        calendar_id = self.calendar_id
        max_attendees = self.max_attendees
        order_by = self.order_by
        page_token = self.page_token
        q = self.q
        show_deleted = self.show_deleted
        single_events = self.single_events
        time_max = self.time_max
        time_min = self.time_min
        time_zone = self.time_zone
        updated_min = self.updated_min
        sync_token = self.sync_token
        i_cal_uid = self.i_cal_uid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if calendar_id is not UNSET:
            field_dict["calendarId"] = calendar_id
        if max_attendees is not UNSET:
            field_dict["maxAttendees"] = max_attendees
        if order_by is not UNSET:
            field_dict["orderBy"] = order_by
        if page_token is not UNSET:
            field_dict["pageToken"] = page_token
        if q is not UNSET:
            field_dict["q"] = q
        if show_deleted is not UNSET:
            field_dict["showDeleted"] = show_deleted
        if single_events is not UNSET:
            field_dict["singleEvents"] = single_events
        if time_max is not UNSET:
            field_dict["timeMax"] = time_max
        if time_min is not UNSET:
            field_dict["timeMin"] = time_min
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if updated_min is not UNSET:
            field_dict["updatedMin"] = updated_min
        if sync_token is not UNSET:
            field_dict["syncToken"] = sync_token
        if i_cal_uid is not UNSET:
            field_dict["iCalUID"] = i_cal_uid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        calendar_id = d.pop("calendarId", UNSET) or UNSET

        max_attendees = d.pop("maxAttendees", UNSET) or UNSET

        order_by = d.pop("orderBy", UNSET) or UNSET

        page_token = d.pop("pageToken", UNSET) or UNSET

        q = d.pop("q", UNSET) or UNSET

        show_deleted = d.pop("showDeleted", UNSET) or UNSET

        single_events = d.pop("singleEvents", UNSET) or UNSET

        time_max = d.pop("timeMax", UNSET) or UNSET

        time_min = d.pop("timeMin", UNSET) or UNSET

        time_zone = d.pop("timeZone", UNSET) or UNSET

        updated_min = d.pop("updatedMin", UNSET) or UNSET

        sync_token = d.pop("syncToken", UNSET) or UNSET

        i_cal_uid = d.pop("iCalUID", UNSET) or UNSET

        google_events_input = cls(
            calendar_id=calendar_id,
            max_attendees=max_attendees,
            order_by=order_by,
            page_token=page_token,
            q=q,
            show_deleted=show_deleted,
            single_events=single_events,
            time_max=time_max,
            time_min=time_min,
            time_zone=time_zone,
            updated_min=updated_min,
            sync_token=sync_token,
            i_cal_uid=i_cal_uid,
        )

        google_events_input.additional_properties = d
        return google_events_input

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
