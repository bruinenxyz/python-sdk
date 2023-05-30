from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_labels_labels_item import GoogleLabelsLabelsItem


T = TypeVar("T", bound="GoogleLabels")


@attr.s(auto_attribs=True)
class GoogleLabels:
    """Your google labels

    Attributes:
        result_size_estimate (Union[Unset, float]): The result size estimate for your labels
        labels (Union[Unset, List['GoogleLabelsLabelsItem']]): A list of your google labels
    """

    result_size_estimate: Union[Unset, float] = UNSET
    labels: Union[Unset, List["GoogleLabelsLabelsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result_size_estimate = self.result_size_estimate
        labels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()

                labels.append(labels_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result_size_estimate is not UNSET:
            field_dict["resultSizeEstimate"] = result_size_estimate
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.google_labels_labels_item import GoogleLabelsLabelsItem

        d = src_dict.copy()
        result_size_estimate = d.pop("resultSizeEstimate", UNSET) or UNSET

        labels = []
        _labels = d.pop("labels", UNSET) or UNSET
        for labels_item_data in _labels or []:
            labels_item = GoogleLabelsLabelsItem.from_dict(labels_item_data)

            labels.append(labels_item)

        google_labels = cls(
            result_size_estimate=result_size_estimate,
            labels=labels,
        )

        google_labels.additional_properties = d
        return google_labels

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
