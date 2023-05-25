from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.credential_provider import CredentialProvider
from ..models.source_policy_status import SourcePolicyStatus
from ..models.source_type import SourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReturnedSourcePolicyDto")


@attr.s(auto_attribs=True)
class ReturnedSourcePolicyDto:
    """
    Attributes:
        id (str):
        source (SourceType):
        status (SourcePolicyStatus):
        default (bool):
        access_credential_provider (CredentialProvider):
        allowed (List[str]):
        allow_all (bool):
        client_id (str):
        name (Union[Unset, str]):
        auth_credential_provider (Union[Unset, CredentialProvider]):
    """

    id: str
    source: SourceType
    status: SourcePolicyStatus
    default: bool
    access_credential_provider: CredentialProvider
    allowed: List[str]
    allow_all: bool
    client_id: str
    name: Union[Unset, str] = UNSET
    auth_credential_provider: Union[Unset, CredentialProvider] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        source = self.source.value

        status = self.status.value

        default = self.default
        access_credential_provider = self.access_credential_provider.value

        allowed = self.allowed

        allow_all = self.allow_all
        client_id = self.client_id
        name = self.name
        auth_credential_provider: Union[Unset, str] = UNSET
        if not isinstance(self.auth_credential_provider, Unset):
            auth_credential_provider = self.auth_credential_provider.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "source": source,
                "status": status,
                "default": default,
                "accessCredentialProvider": access_credential_provider,
                "allowed": allowed,
                "allowAll": allow_all,
                "clientId": client_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if auth_credential_provider is not UNSET:
            field_dict["authCredentialProvider"] = auth_credential_provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        source = SourceType(d.pop("source"))

        status = SourcePolicyStatus(d.pop("status"))

        default = d.pop("default")

        access_credential_provider = CredentialProvider(d.pop("accessCredentialProvider"))

        allowed = cast(List[str], d.pop("allowed"))

        allow_all = d.pop("allowAll")

        client_id = d.pop("clientId")

        name = d.pop("name", UNSET) or UNSET

        _auth_credential_provider = d.pop("authCredentialProvider", UNSET) or UNSET
        auth_credential_provider: Union[Unset, CredentialProvider]
        if isinstance(_auth_credential_provider, Unset):
            auth_credential_provider = UNSET
        else:
            auth_credential_provider = CredentialProvider(_auth_credential_provider)

        returned_source_policy_dto = cls(
            id=id,
            source=source,
            status=status,
            default=default,
            access_credential_provider=access_credential_provider,
            allowed=allowed,
            allow_all=allow_all,
            client_id=client_id,
            name=name,
            auth_credential_provider=auth_credential_provider,
        )

        returned_source_policy_dto.additional_properties = d
        return returned_source_policy_dto

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
