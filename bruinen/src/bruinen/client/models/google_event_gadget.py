from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_event_gadget_preferences import GoogleEventGadgetPreferences


T = TypeVar("T", bound="GoogleEventGadget")


@attr.s(auto_attribs=True)
class GoogleEventGadget:
    """The gadget of the event

    Attributes:
        type (Union[Unset, str]): The type of the gadget
        title (Union[Unset, str]): The title of the gadget
        link (Union[Unset, str]): The link of the gadget
        icon_link (Union[Unset, str]): The iconLink of the gadget
        width (Union[Unset, float]): The width of the gadget
        height (Union[Unset, float]): The height of the gadget
        display (Union[Unset, str]): The display of the gadget
        preferences (Union[Unset, GoogleEventGadgetPreferences]): The preferences of the gadget
    """

    type: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    icon_link: Union[Unset, str] = UNSET
    width: Union[Unset, float] = UNSET
    height: Union[Unset, float] = UNSET
    display: Union[Unset, str] = UNSET
    preferences: Union[Unset, "GoogleEventGadgetPreferences"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        title = self.title
        link = self.link
        icon_link = self.icon_link
        width = self.width
        height = self.height
        display = self.display
        preferences: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preferences, Unset):
            preferences = self.preferences.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if title is not UNSET:
            field_dict["title"] = title
        if link is not UNSET:
            field_dict["link"] = link
        if icon_link is not UNSET:
            field_dict["iconLink"] = icon_link
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if display is not UNSET:
            field_dict["display"] = display
        if preferences is not UNSET:
            field_dict["preferences"] = preferences

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_event_gadget_preferences import GoogleEventGadgetPreferences

        d = src_dict.copy()
        type = d.pop("type", UNSET) or UNSET

        title = d.pop("title", UNSET) or UNSET

        link = d.pop("link", UNSET) or UNSET

        icon_link = d.pop("iconLink", UNSET) or UNSET

        width = d.pop("width", UNSET) or UNSET

        height = d.pop("height", UNSET) or UNSET

        display = d.pop("display", UNSET) or UNSET

        _preferences = d.pop("preferences", UNSET) or UNSET
        preferences: Union[Unset, GoogleEventGadgetPreferences]
        if isinstance(_preferences, Unset):
            preferences = UNSET
        else:
            preferences = GoogleEventGadgetPreferences.from_dict(_preferences)

        google_event_gadget = cls(
            type=type,
            title=title,
            link=link,
            icon_link=icon_link,
            width=width,
            height=height,
            display=display,
            preferences=preferences,
        )

        google_event_gadget.additional_properties = d
        return google_event_gadget

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
