from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubRepoPermissions")


@attr.s(auto_attribs=True)
class GithubRepoPermissions:
    """The permissions object for the repo

    Attributes:
        admin (Union[Unset, bool]): Whether the repo has admin permissions
        maintain (Union[Unset, bool]): Whether the repo has maintain permissions
        push (Union[Unset, bool]): Whether the repo has push permissions
        triage (Union[Unset, bool]): Whether the repo has triage permissions
        pull (Union[Unset, bool]): Whether the repo has pull permissions
    """

    admin: Union[Unset, bool] = UNSET
    maintain: Union[Unset, bool] = UNSET
    push: Union[Unset, bool] = UNSET
    triage: Union[Unset, bool] = UNSET
    pull: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        admin = self.admin
        maintain = self.maintain
        push = self.push
        triage = self.triage
        pull = self.pull

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin is not UNSET:
            field_dict["admin"] = admin
        if maintain is not UNSET:
            field_dict["maintain"] = maintain
        if push is not UNSET:
            field_dict["push"] = push
        if triage is not UNSET:
            field_dict["triage"] = triage
        if pull is not UNSET:
            field_dict["pull"] = pull

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        admin = d.pop("admin", UNSET) or UNSET

        maintain = d.pop("maintain", UNSET) or UNSET

        push = d.pop("push", UNSET) or UNSET

        triage = d.pop("triage", UNSET) or UNSET

        pull = d.pop("pull", UNSET) or UNSET

        github_repo_permissions = cls(
            admin=admin,
            maintain=maintain,
            push=push,
            triage=triage,
            pull=pull,
        )

        github_repo_permissions.additional_properties = d
        return github_repo_permissions

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
