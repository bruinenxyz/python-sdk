from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_events_events_item_reminders_overrides_item import GoogleEventsEventsItemRemindersOverridesItem


T = TypeVar("T", bound="GoogleEventsEventsItemReminders")


@attr.s(auto_attribs=True)
class GoogleEventsEventsItemReminders:
    """The reminders of the event

    Attributes:
        use_default (Union[Unset, bool]): Whether the reminders use default
        overrides (Union[Unset, List['GoogleEventsEventsItemRemindersOverridesItem']]): The overrides of the reminders
    """

    use_default: Union[Unset, bool] = UNSET
    overrides: Union[Unset, List["GoogleEventsEventsItemRemindersOverridesItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        use_default = self.use_default
        overrides: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.overrides, Unset):
            overrides = []
            for overrides_item_data in self.overrides:
                overrides_item = overrides_item_data.to_dict()

                overrides.append(overrides_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if use_default is not UNSET:
            field_dict["useDefault"] = use_default
        if overrides is not UNSET:
            field_dict["overrides"] = overrides

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_events_events_item_reminders_overrides_item import (
            GoogleEventsEventsItemRemindersOverridesItem,
        )

        d = src_dict.copy()
        use_default = d.pop("useDefault", UNSET) or UNSET

        overrides = []
        _overrides = d.pop("overrides", UNSET) or UNSET
        for overrides_item_data in _overrides or []:
            overrides_item = GoogleEventsEventsItemRemindersOverridesItem.from_dict(overrides_item_data)

            overrides.append(overrides_item)

        google_events_events_item_reminders = cls(
            use_default=use_default,
            overrides=overrides,
        )

        google_events_events_item_reminders.additional_properties = d
        return google_events_events_item_reminders

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
