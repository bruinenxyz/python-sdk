from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.account_credential_type import AccountCredentialType

T = TypeVar("T", bound="CreateAccountCredentialDto")


@attr.s(auto_attribs=True)
class CreateAccountCredentialDto:
    """
    Attributes:
        user_id (str):
        account_id (str):
        type (AccountCredentialType):
        credentials (str):
    """

    user_id: str
    account_id: str
    type: AccountCredentialType
    credentials: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        account_id = self.account_id
        type = self.type.value

        credentials = self.credentials

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "accountId": account_id,
                "type": type,
                "credentials": credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        account_id = d.pop("accountId")

        type = AccountCredentialType(d.pop("type"))

        credentials = d.pop("credentials")

        create_account_credential_dto = cls(
            user_id=user_id,
            account_id=account_id,
            type=type,
            credentials=credentials,
        )

        create_account_credential_dto.additional_properties = d
        return create_account_credential_dto

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
