from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_calendars_calendars_item_notification_settings_notifications_item import (
        GoogleCalendarsCalendarsItemNotificationSettingsNotificationsItem,
    )


T = TypeVar("T", bound="GoogleCalendarsCalendarsItemNotificationSettings")


@attr.s(auto_attribs=True)
class GoogleCalendarsCalendarsItemNotificationSettings:
    """The notificationSettings of the calendar

    Attributes:
        notifications (Union[Unset, List['GoogleCalendarsCalendarsItemNotificationSettingsNotificationsItem']]): The
            notifications of the notificationSettings
    """

    notifications: Union[Unset, List["GoogleCalendarsCalendarsItemNotificationSettingsNotificationsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        notifications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = []
            for notifications_item_data in self.notifications:
                notifications_item = notifications_item_data.to_dict()

                notifications.append(notifications_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notifications is not UNSET:
            field_dict["notifications"] = notifications

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_calendars_calendars_item_notification_settings_notifications_item import (
            GoogleCalendarsCalendarsItemNotificationSettingsNotificationsItem,
        )

        d = src_dict.copy()
        notifications = []
        _notifications = d.pop("notifications", UNSET) or UNSET
        for notifications_item_data in _notifications or []:
            notifications_item = GoogleCalendarsCalendarsItemNotificationSettingsNotificationsItem.from_dict(
                notifications_item_data
            )

            notifications.append(notifications_item)

        google_calendars_calendars_item_notification_settings = cls(
            notifications=notifications,
        )

        google_calendars_calendars_item_notification_settings.additional_properties = d
        return google_calendars_calendars_item_notification_settings

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
