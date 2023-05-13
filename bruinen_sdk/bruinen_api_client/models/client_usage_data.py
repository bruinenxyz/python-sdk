from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.source_data import SourceData


T = TypeVar("T", bound="ClientUsageData")


@attr.s(auto_attribs=True)
class ClientUsageData:
    """
    Attributes:
        total_requests (float):
        total_successes (float):
        total_failures (float):
        unique_users (float):
        source_data (List['SourceData']):
    """

    total_requests: float
    total_successes: float
    total_failures: float
    unique_users: float
    source_data: List["SourceData"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_requests = self.total_requests
        total_successes = self.total_successes
        total_failures = self.total_failures
        unique_users = self.unique_users
        source_data = []
        for source_data_item_data in self.source_data:
            source_data_item = source_data_item_data.to_dict()

            source_data.append(source_data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalRequests": total_requests,
                "totalSuccesses": total_successes,
                "totalFailures": total_failures,
                "uniqueUsers": unique_users,
                "sourceData": source_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.source_data import SourceData

        d = src_dict.copy()
        total_requests = d.pop("totalRequests")

        total_successes = d.pop("totalSuccesses")

        total_failures = d.pop("totalFailures")

        unique_users = d.pop("uniqueUsers")

        source_data = []
        _source_data = d.pop("sourceData")
        for source_data_item_data in _source_data:
            source_data_item = SourceData.from_dict(source_data_item_data)

            source_data.append(source_data_item)

        client_usage_data = cls(
            total_requests=total_requests,
            total_successes=total_successes,
            total_failures=total_failures,
            unique_users=unique_users,
            source_data=source_data,
        )

        client_usage_data.additional_properties = d
        return client_usage_data

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
