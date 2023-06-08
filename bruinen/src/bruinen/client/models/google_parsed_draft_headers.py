from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_parsed_draft_headers_bcc_item import GoogleParsedDraftHeadersBccItem
    from ..models.google_parsed_draft_headers_cc_item import GoogleParsedDraftHeadersCcItem
    from ..models.google_parsed_draft_headers_from import GoogleParsedDraftHeadersFrom
    from ..models.google_parsed_draft_headers_to_item import GoogleParsedDraftHeadersToItem


T = TypeVar("T", bound="GoogleParsedDraftHeaders")


@attr.s(auto_attribs=True)
class GoogleParsedDraftHeaders:
    """The headers of the draft

    Attributes:
        date (Union[Unset, str]): The date of the draft
        subject (Union[Unset, str]): The subject of the draft
        from_ (Union[Unset, GoogleParsedDraftHeadersFrom]): The writer of the draft
        to (Union[Unset, List['GoogleParsedDraftHeadersToItem']]): The receivers of the draft
        cc (Union[Unset, List['GoogleParsedDraftHeadersCcItem']]): The ccs of the draft
        bcc (Union[Unset, List['GoogleParsedDraftHeadersBccItem']]): The bccs of the draft
    """

    date: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    from_: Union[Unset, "GoogleParsedDraftHeadersFrom"] = UNSET
    to: Union[Unset, List["GoogleParsedDraftHeadersToItem"]] = UNSET
    cc: Union[Unset, List["GoogleParsedDraftHeadersCcItem"]] = UNSET
    bcc: Union[Unset, List["GoogleParsedDraftHeadersBccItem"]] = UNSET
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
        from ..models.google_parsed_draft_headers_bcc_item import GoogleParsedDraftHeadersBccItem
        from ..models.google_parsed_draft_headers_cc_item import GoogleParsedDraftHeadersCcItem
        from ..models.google_parsed_draft_headers_from import GoogleParsedDraftHeadersFrom
        from ..models.google_parsed_draft_headers_to_item import GoogleParsedDraftHeadersToItem

        d = src_dict.copy()
        date = d.pop("date", UNSET) or UNSET

        subject = d.pop("subject", UNSET) or UNSET

        _from_ = d.pop("from", UNSET) or UNSET
        from_: Union[Unset, GoogleParsedDraftHeadersFrom]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = GoogleParsedDraftHeadersFrom.from_dict(_from_)

        to = []
        _to = d.pop("to", UNSET) or UNSET
        for to_item_data in _to or []:
            to_item = GoogleParsedDraftHeadersToItem.from_dict(to_item_data)

            to.append(to_item)

        cc = []
        _cc = d.pop("cc", UNSET) or UNSET
        for cc_item_data in _cc or []:
            cc_item = GoogleParsedDraftHeadersCcItem.from_dict(cc_item_data)

            cc.append(cc_item)

        bcc = []
        _bcc = d.pop("bcc", UNSET) or UNSET
        for bcc_item_data in _bcc or []:
            bcc_item = GoogleParsedDraftHeadersBccItem.from_dict(bcc_item_data)

            bcc.append(bcc_item)

        google_parsed_draft_headers = cls(
            date=date,
            subject=subject,
            from_=from_,
            to=to,
            cc=cc,
            bcc=bcc,
        )

        google_parsed_draft_headers.additional_properties = d
        return google_parsed_draft_headers

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
