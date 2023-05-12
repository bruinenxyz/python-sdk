from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.client_credential_type import ClientCredentialType

T = TypeVar("T", bound="CreateClientCredentialDto")


@attr.s(auto_attribs=True)
class CreateClientCredentialDto:
    """
    Attributes:
        client_id (str):
        source_policy_id (str):
        type (ClientCredentialType):
        credentials (str):
    """

    client_id: str
    source_policy_id: str
    type: ClientCredentialType
    credentials: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id
        source_policy_id = self.source_policy_id
        type = self.type.value

        credentials = self.credentials

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientId": client_id,
                "sourcePolicyId": source_policy_id,
                "type": type,
                "credentials": credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_id = d.pop("clientId")

        source_policy_id = d.pop("sourcePolicyId")

        type = ClientCredentialType(d.pop("type"))

        credentials = d.pop("credentials")

        create_client_credential_dto = cls(
            client_id=client_id,
            source_policy_id=source_policy_id,
            type=type,
            credentials=credentials,
        )

        create_client_credential_dto.additional_properties = d
        return create_client_credential_dto

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
