from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.account_status import AccountStatus
from ..models.source_type import SourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReturnedAccountDto")


@attr.s(auto_attribs=True)
class ReturnedAccountDto:
    """
    Attributes:
        id (str):
        connection_request_id (str):
        source (SourceType):
        status (AccountStatus):
        user_id (str):
        source_policy_id (str):
        client_id (str):
        external_account_id (Union[Unset, str]):
        auth_url (Union[Unset, str]):
    """

    id: str
    connection_request_id: str
    source: SourceType
    status: AccountStatus
    user_id: str
    source_policy_id: str
    client_id: str
    external_account_id: Union[Unset, str] = UNSET
    auth_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        connection_request_id = self.connection_request_id
        source = self.source.value

        status = self.status.value

        user_id = self.user_id
        source_policy_id = self.source_policy_id
        client_id = self.client_id
        external_account_id = self.external_account_id
        auth_url = self.auth_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "connectionRequestId": connection_request_id,
                "source": source,
                "status": status,
                "userId": user_id,
                "sourcePolicyId": source_policy_id,
                "clientId": client_id,
            }
        )
        if external_account_id is not UNSET:
            field_dict["externalAccountId"] = external_account_id
        if auth_url is not UNSET:
            field_dict["authUrl"] = auth_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        connection_request_id = d.pop("connectionRequestId")

        source = SourceType(d.pop("source"))

        status = AccountStatus(d.pop("status"))

        user_id = d.pop("userId")

        source_policy_id = d.pop("sourcePolicyId")

        client_id = d.pop("clientId")

        external_account_id = d.pop("externalAccountId", UNSET) or UNSET

        auth_url = d.pop("authUrl", UNSET) or UNSET

        returned_account_dto = cls(
            id=id,
            connection_request_id=connection_request_id,
            source=source,
            status=status,
            user_id=user_id,
            source_policy_id=source_policy_id,
            client_id=client_id,
            external_account_id=external_account_id,
            auth_url=auth_url,
        )

        returned_account_dto.additional_properties = d
        return returned_account_dto

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
