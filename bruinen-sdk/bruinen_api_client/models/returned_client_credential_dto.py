from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.client_credential_status import ClientCredentialStatus
from ..models.client_credential_type import ClientCredentialType

T = TypeVar("T", bound="ReturnedClientCredentialDto")


@attr.s(auto_attribs=True)
class ReturnedClientCredentialDto:
    """
    Attributes:
        id (str):
        status (ClientCredentialStatus):
        type (ClientCredentialType):
        partial_credentials (str):
        source_policy_id (str):
        client_id (str):
    """

    id: str
    status: ClientCredentialStatus
    type: ClientCredentialType
    partial_credentials: str
    source_policy_id: str
    client_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status = self.status.value

        type = self.type.value

        partial_credentials = self.partial_credentials
        source_policy_id = self.source_policy_id
        client_id = self.client_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "type": type,
                "partialCredentials": partial_credentials,
                "sourcePolicyId": source_policy_id,
                "clientId": client_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        status = ClientCredentialStatus(d.pop("status"))

        type = ClientCredentialType(d.pop("type"))

        partial_credentials = d.pop("partialCredentials")

        source_policy_id = d.pop("sourcePolicyId")

        client_id = d.pop("clientId")

        returned_client_credential_dto = cls(
            id=id,
            status=status,
            type=type,
            partial_credentials=partial_credentials,
            source_policy_id=source_policy_id,
            client_id=client_id,
        )

        returned_client_credential_dto.additional_properties = d
        return returned_client_credential_dto

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
