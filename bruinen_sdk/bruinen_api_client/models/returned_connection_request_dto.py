from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.returned_connection_request_dto_source import ReturnedConnectionRequestDtoSource


T = TypeVar("T", bound="ReturnedConnectionRequestDto")


@attr.s(auto_attribs=True)
class ReturnedConnectionRequestDto:
    """
    Attributes:
        id (str):
        source (ReturnedConnectionRequestDtoSource):
        status (str):
        client_id (str):
        user_id (str):
        source_policy_id (str):
        redirect (Union[Unset, str]):
        auth_url (Union[Unset, str]):
        account_id (Union[Unset, str]):
    """

    id: str
    source: "ReturnedConnectionRequestDtoSource"
    status: str
    client_id: str
    user_id: str
    source_policy_id: str
    redirect: Union[Unset, str] = UNSET
    auth_url: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        source = self.source.to_dict()

        status = self.status
        client_id = self.client_id
        user_id = self.user_id
        source_policy_id = self.source_policy_id
        redirect = self.redirect
        auth_url = self.auth_url
        account_id = self.account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "source": source,
                "status": status,
                "clientId": client_id,
                "userId": user_id,
                "sourcePolicyId": source_policy_id,
            }
        )
        if redirect is not UNSET:
            field_dict["redirect"] = redirect
        if auth_url is not UNSET:
            field_dict["authUrl"] = auth_url
        if account_id is not UNSET:
            field_dict["accountId"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.returned_connection_request_dto_source import ReturnedConnectionRequestDtoSource

        d = src_dict.copy()
        id = d.pop("id")

        source = ReturnedConnectionRequestDtoSource.from_dict(d.pop("source"))

        status = d.pop("status")

        client_id = d.pop("clientId")

        user_id = d.pop("userId")

        source_policy_id = d.pop("sourcePolicyId")

        redirect = d.pop("redirect", UNSET) or UNSET

        auth_url = d.pop("authUrl", UNSET) or UNSET

        account_id = d.pop("accountId", UNSET) or UNSET

        returned_connection_request_dto = cls(
            id=id,
            source=source,
            status=status,
            client_id=client_id,
            user_id=user_id,
            source_policy_id=source_policy_id,
            redirect=redirect,
            auth_url=auth_url,
            account_id=account_id,
        )

        returned_connection_request_dto.additional_properties = d
        return returned_connection_request_dto

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
