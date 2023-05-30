from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_message_payload import GoogleMessagePayload


T = TypeVar("T", bound="GoogleMessage")


@attr.s(auto_attribs=True)
class GoogleMessage:
    """Your google message

    Attributes:
        id (Union[Unset, str]): The id of the message
        thread_id (Union[Unset, str]): The threadId of the message
        label_ids (Union[Unset, List[str]]): The labelIds of the message
        snippet (Union[Unset, str]): The snippet of the message
        history_id (Union[Unset, str]): The historyId of the message
        internal_date (Union[Unset, str]): The internalDate of the message
        payload (Union[Unset, GoogleMessagePayload]): The payload of the message
        size_estimate (Union[Unset, float]): The sizeEstimate of the message
    """

    id: Union[Unset, str] = UNSET
    thread_id: Union[Unset, str] = UNSET
    label_ids: Union[Unset, List[str]] = UNSET
    snippet: Union[Unset, str] = UNSET
    history_id: Union[Unset, str] = UNSET
    internal_date: Union[Unset, str] = UNSET
    payload: Union[Unset, "GoogleMessagePayload"] = UNSET
    size_estimate: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        thread_id = self.thread_id
        label_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.label_ids, Unset):
            label_ids = self.label_ids

        snippet = self.snippet
        history_id = self.history_id
        internal_date = self.internal_date
        payload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        size_estimate = self.size_estimate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if label_ids is not UNSET:
            field_dict["labelIds"] = label_ids
        if snippet is not UNSET:
            field_dict["snippet"] = snippet
        if history_id is not UNSET:
            field_dict["historyId"] = history_id
        if internal_date is not UNSET:
            field_dict["internalDate"] = internal_date
        if payload is not UNSET:
            field_dict["payload"] = payload
        if size_estimate is not UNSET:
            field_dict["sizeEstimate"] = size_estimate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_message_payload import GoogleMessagePayload

        d = src_dict.copy()
        id = d.pop("id", UNSET) or UNSET

        thread_id = d.pop("threadId", UNSET) or UNSET

        label_ids = cast(List[str], d.pop("labelIds", UNSET) or UNSET)

        snippet = d.pop("snippet", UNSET) or UNSET

        history_id = d.pop("historyId", UNSET) or UNSET

        internal_date = d.pop("internalDate", UNSET) or UNSET

        _payload = d.pop("payload", UNSET) or UNSET
        payload: Union[Unset, GoogleMessagePayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = GoogleMessagePayload.from_dict(_payload)

        size_estimate = d.pop("sizeEstimate", UNSET) or UNSET

        google_message = cls(
            id=id,
            thread_id=thread_id,
            label_ids=label_ids,
            snippet=snippet,
            history_id=history_id,
            internal_date=internal_date,
            payload=payload,
            size_estimate=size_estimate,
        )

        google_message.additional_properties = d
        return google_message

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
