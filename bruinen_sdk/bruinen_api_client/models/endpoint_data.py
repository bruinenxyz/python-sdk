from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="EndpointData")


@attr.s(auto_attribs=True)
class EndpointData:
    """
    Attributes:
        endpoint (str):
        total_requests (float):
        total_successes (float):
        total_failures (float):
    """

    endpoint: str
    total_requests: float
    total_successes: float
    total_failures: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoint = self.endpoint
        total_requests = self.total_requests
        total_successes = self.total_successes
        total_failures = self.total_failures

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint": endpoint,
                "totalRequests": total_requests,
                "totalSuccesses": total_successes,
                "totalFailures": total_failures,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        endpoint = d.pop("endpoint")

        total_requests = d.pop("totalRequests")

        total_successes = d.pop("totalSuccesses")

        total_failures = d.pop("totalFailures")

        endpoint_data = cls(
            endpoint=endpoint,
            total_requests=total_requests,
            total_successes=total_successes,
            total_failures=total_failures,
        )

        endpoint_data.additional_properties = d
        return endpoint_data

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
