from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_connection_request_dto_source import CreateConnectionRequestDtoSource


T = TypeVar("T", bound="CreateConnectionRequestDto")


@attr.s(auto_attribs=True)
class CreateConnectionRequestDto:
    """
    Attributes:
        user_id (str):
        client_id (str):
        source (CreateConnectionRequestDtoSource):
        redirect (str):
        source_policy_id (Union[Unset, str]):
        login (Union[Unset, bool]):
    """

    user_id: str
    client_id: str
    source: "CreateConnectionRequestDtoSource"
    redirect: str
    source_policy_id: Union[Unset, str] = UNSET
    login: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        client_id = self.client_id
        source = self.source.to_dict()

        redirect = self.redirect
        source_policy_id = self.source_policy_id
        login = self.login

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "clientId": client_id,
                "source": source,
                "redirect": redirect,
            }
        )
        if source_policy_id is not UNSET:
            field_dict["sourcePolicyId"] = source_policy_id
        if login is not UNSET:
            field_dict["login"] = login

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_connection_request_dto_source import CreateConnectionRequestDtoSource

        d = src_dict.copy()
        user_id = d.pop("userId")

        client_id = d.pop("clientId")

        source = CreateConnectionRequestDtoSource.from_dict(d.pop("source"))

        redirect = d.pop("redirect")

        source_policy_id = d.pop("sourcePolicyId", UNSET) or UNSET

        login = d.pop("login", UNSET) or UNSET

        create_connection_request_dto = cls(
            user_id=user_id,
            client_id=client_id,
            source=source,
            redirect=redirect,
            source_policy_id=source_policy_id,
            login=login,
        )

        create_connection_request_dto.additional_properties = d
        return create_connection_request_dto

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
