from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.endpoint_data import EndpointData


T = TypeVar("T", bound="SourceData")


@attr.s(auto_attribs=True)
class SourceData:
    """
    Attributes:
        source (str):
        total_requests (float):
        total_successes (float):
        total_failures (float):
        endpoint_data (List['EndpointData']):
    """

    source: str
    total_requests: float
    total_successes: float
    total_failures: float
    endpoint_data: List["EndpointData"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source = self.source
        total_requests = self.total_requests
        total_successes = self.total_successes
        total_failures = self.total_failures
        endpoint_data = []
        for endpoint_data_item_data in self.endpoint_data:
            endpoint_data_item = endpoint_data_item_data.to_dict()

            endpoint_data.append(endpoint_data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "totalRequests": total_requests,
                "totalSuccesses": total_successes,
                "totalFailures": total_failures,
                "endpointData": endpoint_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.endpoint_data import EndpointData

        d = src_dict.copy()
        source = d.pop("source")

        total_requests = d.pop("totalRequests")

        total_successes = d.pop("totalSuccesses")

        total_failures = d.pop("totalFailures")

        endpoint_data = []
        _endpoint_data = d.pop("endpointData")
        for endpoint_data_item_data in _endpoint_data:
            endpoint_data_item = EndpointData.from_dict(endpoint_data_item_data)

            endpoint_data.append(endpoint_data_item)

        source_data = cls(
            source=source,
            total_requests=total_requests,
            total_successes=total_successes,
            total_failures=total_failures,
            endpoint_data=endpoint_data,
        )

        source_data.additional_properties = d
        return source_data

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
