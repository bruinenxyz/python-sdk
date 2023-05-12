from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.source_type import SourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSourcePolicyDto")


@attr.s(auto_attribs=True)
class CreateSourcePolicyDto:
    """
    Attributes:
        source (SourceType):
        default (Union[Unset, bool]):
    """

    source: SourceType
    default: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source = self.source.value

        default = self.default

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source = SourceType(d.pop("source"))

        default = d.pop("default", UNSET)

        create_source_policy_dto = cls(
            source=source,
            default=default,
        )

        create_source_policy_dto.additional_properties = d
        return create_source_policy_dto

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
