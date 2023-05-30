from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_threads_threads_item import GoogleThreadsThreadsItem


T = TypeVar("T", bound="GoogleThreads")


@attr.s(auto_attribs=True)
class GoogleThreads:
    """Your google threads

    Attributes:
        result_size_estimate (Union[Unset, float]): The result size estimate for your threads
        next_page_token (Union[Unset, str]): The next page token
        threads (Union[Unset, List['GoogleThreadsThreadsItem']]): A list of your google threads
    """

    result_size_estimate: Union[Unset, float] = UNSET
    next_page_token: Union[Unset, str] = UNSET
    threads: Union[Unset, List["GoogleThreadsThreadsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result_size_estimate = self.result_size_estimate
        next_page_token = self.next_page_token
        threads: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.threads, Unset):
            threads = []
            for threads_item_data in self.threads:
                threads_item = threads_item_data.to_dict()

                threads.append(threads_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result_size_estimate is not UNSET:
            field_dict["resultSizeEstimate"] = result_size_estimate
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if threads is not UNSET:
            field_dict["threads"] = threads

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_threads_threads_item import GoogleThreadsThreadsItem

        d = src_dict.copy()
        result_size_estimate = d.pop("resultSizeEstimate", UNSET) or UNSET

        next_page_token = d.pop("nextPageToken", UNSET) or UNSET

        threads = []
        _threads = d.pop("threads", UNSET) or UNSET
        for threads_item_data in _threads or []:
            threads_item = GoogleThreadsThreadsItem.from_dict(threads_item_data)

            threads.append(threads_item)

        google_threads = cls(
            result_size_estimate=result_size_estimate,
            next_page_token=next_page_token,
            threads=threads,
        )

        google_threads.additional_properties = d
        return google_threads

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
