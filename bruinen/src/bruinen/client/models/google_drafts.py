from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_drafts_drafts_item import GoogleDraftsDraftsItem


T = TypeVar("T", bound="GoogleDrafts")


@attr.s(auto_attribs=True)
class GoogleDrafts:
    """Your google drafts

    Attributes:
        drafts (Union[Unset, List['GoogleDraftsDraftsItem']]): A list of your google drafts
        next_page_token (Union[Unset, str]): The next page token for your drafts
        result_size_estimate (Union[Unset, float]): The result size estimate for your drafts
    """

    drafts: Union[Unset, List["GoogleDraftsDraftsItem"]] = UNSET
    next_page_token: Union[Unset, str] = UNSET
    result_size_estimate: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        drafts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.drafts, Unset):
            drafts = []
            for drafts_item_data in self.drafts:
                drafts_item = drafts_item_data.to_dict()

                drafts.append(drafts_item)

        next_page_token = self.next_page_token
        result_size_estimate = self.result_size_estimate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if drafts is not UNSET:
            field_dict["drafts"] = drafts
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if result_size_estimate is not UNSET:
            field_dict["resultSizeEstimate"] = result_size_estimate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_drafts_drafts_item import GoogleDraftsDraftsItem

        d = src_dict.copy()
        drafts = []
        _drafts = d.pop("drafts", UNSET) or UNSET
        for drafts_item_data in _drafts or []:
            drafts_item = GoogleDraftsDraftsItem.from_dict(drafts_item_data)

            drafts.append(drafts_item)

        next_page_token = d.pop("nextPageToken", UNSET) or UNSET

        result_size_estimate = d.pop("resultSizeEstimate", UNSET) or UNSET

        google_drafts = cls(
            drafts=drafts,
            next_page_token=next_page_token,
            result_size_estimate=result_size_estimate,
        )

        google_drafts.additional_properties = d
        return google_drafts

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
