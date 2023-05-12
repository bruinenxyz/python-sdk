from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_account_policy_dto_source import UpdateAccountPolicyDtoSource


T = TypeVar("T", bound="UpdateAccountPolicyDto")


@attr.s(auto_attribs=True)
class UpdateAccountPolicyDto:
    """
    Attributes:
        user_id (Union[Unset, str]):
        account_id (Union[Unset, str]):
        source (Union[Unset, UpdateAccountPolicyDtoSource]):
    """

    user_id: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    source: Union[Unset, "UpdateAccountPolicyDtoSource"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        account_id = self.account_id
        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_account_policy_dto_source import UpdateAccountPolicyDtoSource

        d = src_dict.copy()
        user_id = d.pop("userId", UNSET)

        account_id = d.pop("accountId", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, UpdateAccountPolicyDtoSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = UpdateAccountPolicyDtoSource.from_dict(_source)

        update_account_policy_dto = cls(
            user_id=user_id,
            account_id=account_id,
            source=source,
        )

        update_account_policy_dto.additional_properties = d
        return update_account_policy_dto

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
