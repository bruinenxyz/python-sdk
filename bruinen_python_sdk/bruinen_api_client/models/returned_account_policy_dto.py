import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

from ..models.account_policy_status import AccountPolicyStatus
from ..models.source_type import SourceType

T = TypeVar("T", bound="ReturnedAccountPolicyDto")


@attr.s(auto_attribs=True)
class ReturnedAccountPolicyDto:
    """
    Attributes:
        id (str):
        source (SourceType):
        allowed (List[str]):
        allow_all (bool):
        status (AccountPolicyStatus):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        account_id (str):
        user_id (str):
    """

    id: str
    source: SourceType
    allowed: List[str]
    allow_all: bool
    status: AccountPolicyStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    account_id: str
    user_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        source = self.source.value

        allowed = self.allowed

        allow_all = self.allow_all
        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        account_id = self.account_id
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "source": source,
                "allowed": allowed,
                "allowAll": allow_all,
                "status": status,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "accountId": account_id,
                "userId": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        source = SourceType(d.pop("source"))

        allowed = cast(List[str], d.pop("allowed"))

        allow_all = d.pop("allowAll")

        status = AccountPolicyStatus(d.pop("status"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        account_id = d.pop("accountId")

        user_id = d.pop("userId")

        returned_account_policy_dto = cls(
            id=id,
            source=source,
            allowed=allowed,
            allow_all=allow_all,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            account_id=account_id,
            user_id=user_id,
        )

        returned_account_policy_dto.additional_properties = d
        return returned_account_policy_dto

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
