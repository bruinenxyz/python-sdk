from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.account_credential_status import AccountCredentialStatus
from ..models.account_credential_type import AccountCredentialType

T = TypeVar("T", bound="ReturnedAccountCredentialDto")


@attr.s(auto_attribs=True)
class ReturnedAccountCredentialDto:
    """
    Attributes:
        id (str):
        status (AccountCredentialStatus):
        type (AccountCredentialType):
        partial_credentials (str):
        account_id (str):
        user_id (str):
    """

    id: str
    status: AccountCredentialStatus
    type: AccountCredentialType
    partial_credentials: str
    account_id: str
    user_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status = self.status.value

        type = self.type.value

        partial_credentials = self.partial_credentials
        account_id = self.account_id
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "type": type,
                "partialCredentials": partial_credentials,
                "accountId": account_id,
                "userId": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        status = AccountCredentialStatus(d.pop("status"))

        type = AccountCredentialType(d.pop("type"))

        partial_credentials = d.pop("partialCredentials")

        account_id = d.pop("accountId")

        user_id = d.pop("userId")

        returned_account_credential_dto = cls(
            id=id,
            status=status,
            type=type,
            partial_credentials=partial_credentials,
            account_id=account_id,
            user_id=user_id,
        )

        returned_account_credential_dto.additional_properties = d
        return returned_account_credential_dto

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
