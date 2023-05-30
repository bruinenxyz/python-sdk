from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleEventAttendeesItem")


@attr.s(auto_attribs=True)
class GoogleEventAttendeesItem:
    """An attendee

    Attributes:
        id (Union[Unset, str]): The id of the attendee
        email (Union[Unset, str]): The email of the attendee
        display_name (Union[Unset, str]): The displayName of the attendee
        organizer (Union[Unset, bool]): Whether the attendee is the organizer
        self_ (Union[Unset, bool]): Whether the attendee is self
        resource (Union[Unset, bool]): Whether the attendee is a resource
        optional (Union[Unset, bool]): Whether the attendee is optional
        response_status (Union[Unset, str]): The responseStatus of the attendee
        comment (Union[Unset, str]): The comment of the attendee
        additional_guests (Union[Unset, float]): The additionalGuests of the attendee
    """

    id: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    organizer: Union[Unset, bool] = UNSET
    self_: Union[Unset, bool] = UNSET
    resource: Union[Unset, bool] = UNSET
    optional: Union[Unset, bool] = UNSET
    response_status: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_guests: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        email = self.email
        display_name = self.display_name
        organizer = self.organizer
        self_ = self.self_
        resource = self.resource
        optional = self.optional
        response_status = self.response_status
        comment = self.comment
        additional_guests = self.additional_guests

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if organizer is not UNSET:
            field_dict["organizer"] = organizer
        if self_ is not UNSET:
            field_dict["self"] = self_
        if resource is not UNSET:
            field_dict["resource"] = resource
        if optional is not UNSET:
            field_dict["optional"] = optional
        if response_status is not UNSET:
            field_dict["responseStatus"] = response_status
        if comment is not UNSET:
            field_dict["comment"] = comment
        if additional_guests is not UNSET:
            field_dict["additionalGuests"] = additional_guests

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET) or UNSET

        email = d.pop("email", UNSET) or UNSET

        display_name = d.pop("displayName", UNSET) or UNSET

        organizer = d.pop("organizer", UNSET) or UNSET

        self_ = d.pop("self", UNSET) or UNSET

        resource = d.pop("resource", UNSET) or UNSET

        optional = d.pop("optional", UNSET) or UNSET

        response_status = d.pop("responseStatus", UNSET) or UNSET

        comment = d.pop("comment", UNSET) or UNSET

        additional_guests = d.pop("additionalGuests", UNSET) or UNSET

        google_event_attendees_item = cls(
            id=id,
            email=email,
            display_name=display_name,
            organizer=organizer,
            self_=self_,
            resource=resource,
            optional=optional,
            response_status=response_status,
            comment=comment,
            additional_guests=additional_guests,
        )

        google_event_attendees_item.additional_properties = d
        return google_event_attendees_item

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
