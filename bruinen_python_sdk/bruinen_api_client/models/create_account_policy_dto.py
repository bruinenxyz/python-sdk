from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.create_account_policy_dto_source import CreateAccountPolicyDtoSource


T = TypeVar("T", bound="CreateAccountPolicyDto")


@attr.s(auto_attribs=True)
class CreateAccountPolicyDto:
    """
    Attributes:
        user_id (str):
        account_id (str):
        source (CreateAccountPolicyDtoSource):
    """

    user_id: str
    account_id: str
    source: "CreateAccountPolicyDtoSource"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        account_id = self.account_id
        source = self.source.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "accountId": account_id,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_account_policy_dto_source import CreateAccountPolicyDtoSource

        d = src_dict.copy()
        user_id = d.pop("userId")

        account_id = d.pop("accountId")

        source = CreateAccountPolicyDtoSource.from_dict(d.pop("source"))

        create_account_policy_dto = cls(
            user_id=user_id,
            account_id=account_id,
            source=source,
        )

        create_account_policy_dto.additional_properties = d
        return create_account_policy_dto

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
