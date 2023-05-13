from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.returned_account_policy_dto import ReturnedAccountPolicyDto
from ...models.update_account_policy_dto import UpdateAccountPolicyDto
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: UpdateAccountPolicyDto,
) -> Dict[str, Any]:
    url = "{}/account-policies/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ReturnedAccountPolicyDto]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ReturnedAccountPolicyDto.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ReturnedAccountPolicyDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    json_body: UpdateAccountPolicyDto,
) -> Response[ReturnedAccountPolicyDto]:
    """
    Args:
        id (str):
        json_body (UpdateAccountPolicyDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReturnedAccountPolicyDto]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: UpdateAccountPolicyDto,
) -> Optional[ReturnedAccountPolicyDto]:
    """
    Args:
        id (str):
        json_body (UpdateAccountPolicyDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReturnedAccountPolicyDto
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: UpdateAccountPolicyDto,
) -> Response[ReturnedAccountPolicyDto]:
    """
    Args:
        id (str):
        json_body (UpdateAccountPolicyDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReturnedAccountPolicyDto]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: UpdateAccountPolicyDto,
) -> Optional[ReturnedAccountPolicyDto]:
    """
    Args:
        id (str):
        json_body (UpdateAccountPolicyDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReturnedAccountPolicyDto
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed