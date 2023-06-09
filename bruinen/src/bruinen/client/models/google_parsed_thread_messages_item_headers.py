from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_parsed_thread_messages_item_headers_bcc_item import (
        GoogleParsedThreadMessagesItemHeadersBccItem,
    )
    from ..models.google_parsed_thread_messages_item_headers_cc_item import GoogleParsedThreadMessagesItemHeadersCcItem
    from ..models.google_parsed_thread_messages_item_headers_from import GoogleParsedThreadMessagesItemHeadersFrom
    from ..models.google_parsed_thread_messages_item_headers_to_item import GoogleParsedThreadMessagesItemHeadersToItem


T = TypeVar("T", bound="GoogleParsedThreadMessagesItemHeaders")


@attr.s(auto_attribs=True)
class GoogleParsedThreadMessagesItemHeaders:
    """The headers of the message

    Attributes:
        date (Union[Unset, str]): The date of the message
        subject (Union[Unset, str]): The subject of the message
        from_ (Union[Unset, GoogleParsedThreadMessagesItemHeadersFrom]): The writer of the message
        to (Union[Unset, List['GoogleParsedThreadMessagesItemHeadersToItem']]): The receivers of the message
        cc (Union[Unset, List['GoogleParsedThreadMessagesItemHeadersCcItem']]): The ccs of the message
        bcc (Union[Unset, List['GoogleParsedThreadMessagesItemHeadersBccItem']]): The bccs of the message
    """

    date: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    from_: Union[Unset, "GoogleParsedThreadMessagesItemHeadersFrom"] = UNSET
    to: Union[Unset, List["GoogleParsedThreadMessagesItemHeadersToItem"]] = UNSET
    cc: Union[Unset, List["GoogleParsedThreadMessagesItemHeadersCcItem"]] = UNSET
    bcc: Union[Unset, List["GoogleParsedThreadMessagesItemHeadersBccItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date
        subject = self.subject
        from_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        to: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.to, Unset):
            to = []
            for to_item_data in self.to:
                to_item = to_item_data.to_dict()

                to.append(to_item)

        cc: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cc, Unset):
            cc = []
            for cc_item_data in self.cc:
                cc_item = cc_item_data.to_dict()

                cc.append(cc_item)

        bcc: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bcc, Unset):
            bcc = []
            for bcc_item_data in self.bcc:
                bcc_item = bcc_item_data.to_dict()

                bcc.append(bcc_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if subject is not UNSET:
            field_dict["subject"] = subject
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if cc is not UNSET:
            field_dict["cc"] = cc
        if bcc is not UNSET:
            field_dict["bcc"] = bcc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_parsed_thread_messages_item_headers_bcc_item import (
            GoogleParsedThreadMessagesItemHeadersBccItem,
        )
        from ..models.google_parsed_thread_messages_item_headers_cc_item import (
            GoogleParsedThreadMessagesItemHeadersCcItem,
        )
        from ..models.google_parsed_thread_messages_item_headers_from import GoogleParsedThreadMessagesItemHeadersFrom
        from ..models.google_parsed_thread_messages_item_headers_to_item import (
            GoogleParsedThreadMessagesItemHeadersToItem,
        )

        d = src_dict.copy()
        date = d.pop("date", UNSET) or UNSET

        subject = d.pop("subject", UNSET) or UNSET

        _from_ = d.pop("from", UNSET) or UNSET
        from_: Union[Unset, GoogleParsedThreadMessagesItemHeadersFrom]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = GoogleParsedThreadMessagesItemHeadersFrom.from_dict(_from_)

        to = []
        _to = d.pop("to", UNSET) or UNSET
        for to_item_data in _to or []:
            to_item = GoogleParsedThreadMessagesItemHeadersToItem.from_dict(to_item_data)

            to.append(to_item)

        cc = []
        _cc = d.pop("cc", UNSET) or UNSET
        for cc_item_data in _cc or []:
            cc_item = GoogleParsedThreadMessagesItemHeadersCcItem.from_dict(cc_item_data)

            cc.append(cc_item)

        bcc = []
        _bcc = d.pop("bcc", UNSET) or UNSET
        for bcc_item_data in _bcc or []:
            bcc_item = GoogleParsedThreadMessagesItemHeadersBccItem.from_dict(bcc_item_data)

            bcc.append(bcc_item)

        google_parsed_thread_messages_item_headers = cls(
            date=date,
            subject=subject,
            from_=from_,
            to=to,
            cc=cc,
            bcc=bcc,
        )

        google_parsed_thread_messages_item_headers.additional_properties = d
        return google_parsed_thread_messages_item_headers

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
