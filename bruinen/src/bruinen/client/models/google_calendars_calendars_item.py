from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_calendars_calendars_item_conference_properties import (
        GoogleCalendarsCalendarsItemConferenceProperties,
    )
    from ..models.google_calendars_calendars_item_default_reminders import GoogleCalendarsCalendarsItemDefaultReminders
    from ..models.google_calendars_calendars_item_notification_settings import (
        GoogleCalendarsCalendarsItemNotificationSettings,
    )


T = TypeVar("T", bound="GoogleCalendarsCalendarsItem")


@attr.s(auto_attribs=True)
class GoogleCalendarsCalendarsItem:
    """A google calendar

    Attributes:
        kind (Union[Unset, str]): The kind of the calendar
        etag (Union[Unset, str]): The etag of the calendar
        id (Union[Unset, str]): The id of the calendar
        summary (Union[Unset, str]): The summary of the calendar
        description (Union[Unset, str]): The description of the calendar
        location (Union[Unset, str]): The location of the calendar
        time_zone (Union[Unset, str]): The timeZone of the calendar
        summary_override (Union[Unset, str]): The summaryOverride of the calendar
        color_id (Union[Unset, str]): The colorId of the calendar
        background_color (Union[Unset, str]): The backgroundColor of the calendar
        foreground_color (Union[Unset, str]): The foregroundColor of the calendar
        hidden (Union[Unset, bool]): Whether the calendar is hidden
        selected (Union[Unset, bool]): Whether the calendar is selected
        access_role (Union[Unset, str]): The accessRole of the calendar
        default_reminders (Union[Unset, GoogleCalendarsCalendarsItemDefaultReminders]): The defaultReminders of the
            calendar
        notification_settings (Union[Unset, GoogleCalendarsCalendarsItemNotificationSettings]): The notificationSettings
            of the calendar
        primary (Union[Unset, bool]): Whether the calendar is primary
        deleted (Union[Unset, bool]): Whether the calendar is deleted
        conference_properties (Union[Unset, GoogleCalendarsCalendarsItemConferenceProperties]): The conferenceProperties
            of the calendar
    """

    kind: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    summary_override: Union[Unset, str] = UNSET
    color_id: Union[Unset, str] = UNSET
    background_color: Union[Unset, str] = UNSET
    foreground_color: Union[Unset, str] = UNSET
    hidden: Union[Unset, bool] = UNSET
    selected: Union[Unset, bool] = UNSET
    access_role: Union[Unset, str] = UNSET
    default_reminders: Union[Unset, "GoogleCalendarsCalendarsItemDefaultReminders"] = UNSET
    notification_settings: Union[Unset, "GoogleCalendarsCalendarsItemNotificationSettings"] = UNSET
    primary: Union[Unset, bool] = UNSET
    deleted: Union[Unset, bool] = UNSET
    conference_properties: Union[Unset, "GoogleCalendarsCalendarsItemConferenceProperties"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind = self.kind
        etag = self.etag
        id = self.id
        summary = self.summary
        description = self.description
        location = self.location
        time_zone = self.time_zone
        summary_override = self.summary_override
        color_id = self.color_id
        background_color = self.background_color
        foreground_color = self.foreground_color
        hidden = self.hidden
        selected = self.selected
        access_role = self.access_role
        default_reminders: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_reminders, Unset):
            default_reminders = self.default_reminders.to_dict()

        notification_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notification_settings, Unset):
            notification_settings = self.notification_settings.to_dict()

        primary = self.primary
        deleted = self.deleted
        conference_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conference_properties, Unset):
            conference_properties = self.conference_properties.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if summary_override is not UNSET:
            field_dict["summaryOverride"] = summary_override
        if color_id is not UNSET:
            field_dict["colorId"] = color_id
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if foreground_color is not UNSET:
            field_dict["foregroundColor"] = foreground_color
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if selected is not UNSET:
            field_dict["selected"] = selected
        if access_role is not UNSET:
            field_dict["accessRole"] = access_role
        if default_reminders is not UNSET:
            field_dict["defaultReminders"] = default_reminders
        if notification_settings is not UNSET:
            field_dict["notificationSettings"] = notification_settings
        if primary is not UNSET:
            field_dict["primary"] = primary
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if conference_properties is not UNSET:
            field_dict["conferenceProperties"] = conference_properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_calendars_calendars_item_conference_properties import (
            GoogleCalendarsCalendarsItemConferenceProperties,
        )
        from ..models.google_calendars_calendars_item_default_reminders import (
            GoogleCalendarsCalendarsItemDefaultReminders,
        )
        from ..models.google_calendars_calendars_item_notification_settings import (
            GoogleCalendarsCalendarsItemNotificationSettings,
        )

        d = src_dict.copy()
        kind = d.pop("kind", UNSET) or UNSET

        etag = d.pop("etag", UNSET) or UNSET

        id = d.pop("id", UNSET) or UNSET

        summary = d.pop("summary", UNSET) or UNSET

        description = d.pop("description", UNSET) or UNSET

        location = d.pop("location", UNSET) or UNSET

        time_zone = d.pop("timeZone", UNSET) or UNSET

        summary_override = d.pop("summaryOverride", UNSET) or UNSET

        color_id = d.pop("colorId", UNSET) or UNSET

        background_color = d.pop("backgroundColor", UNSET) or UNSET

        foreground_color = d.pop("foregroundColor", UNSET) or UNSET

        hidden = d.pop("hidden", UNSET) or UNSET

        selected = d.pop("selected", UNSET) or UNSET

        access_role = d.pop("accessRole", UNSET) or UNSET

        _default_reminders = d.pop("defaultReminders", UNSET) or UNSET
        default_reminders: Union[Unset, GoogleCalendarsCalendarsItemDefaultReminders]
        if isinstance(_default_reminders, Unset):
            default_reminders = UNSET
        else:
            default_reminders = GoogleCalendarsCalendarsItemDefaultReminders.from_dict(_default_reminders)

        _notification_settings = d.pop("notificationSettings", UNSET) or UNSET
        notification_settings: Union[Unset, GoogleCalendarsCalendarsItemNotificationSettings]
        if isinstance(_notification_settings, Unset):
            notification_settings = UNSET
        else:
            notification_settings = GoogleCalendarsCalendarsItemNotificationSettings.from_dict(_notification_settings)

        primary = d.pop("primary", UNSET) or UNSET

        deleted = d.pop("deleted", UNSET) or UNSET

        _conference_properties = d.pop("conferenceProperties", UNSET) or UNSET
        conference_properties: Union[Unset, GoogleCalendarsCalendarsItemConferenceProperties]
        if isinstance(_conference_properties, Unset):
            conference_properties = UNSET
        else:
            conference_properties = GoogleCalendarsCalendarsItemConferenceProperties.from_dict(_conference_properties)

        google_calendars_calendars_item = cls(
            kind=kind,
            etag=etag,
            id=id,
            summary=summary,
            description=description,
            location=location,
            time_zone=time_zone,
            summary_override=summary_override,
            color_id=color_id,
            background_color=background_color,
            foreground_color=foreground_color,
            hidden=hidden,
            selected=selected,
            access_role=access_role,
            default_reminders=default_reminders,
            notification_settings=notification_settings,
            primary=primary,
            deleted=deleted,
            conference_properties=conference_properties,
        )

        google_calendars_calendars_item.additional_properties = d
        return google_calendars_calendars_item

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
