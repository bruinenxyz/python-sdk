from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.google_drafts import GoogleDrafts
from ...models.google_drafts_input import GoogleDraftsInput
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    field_: "GoogleDraftsInput",
    account_id: str,
) -> Dict[str, Any]:
    url = "{}/sources/google/drafts".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_field_ = field_.to_dict()

    params.update(json_field_)

    params["accountId"] = account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GoogleDrafts]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GoogleDrafts.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GoogleDrafts]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    field_: "GoogleDraftsInput",
    account_id: str,
) -> Response[GoogleDrafts]:
    """
    Args:
        field_ (GoogleDraftsInput): The input for your google drafts
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoogleDrafts]
    """

    kwargs = _get_kwargs(
        client=client,
        field_=field_,
        account_id=account_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    field_: "GoogleDraftsInput",
    account_id: str,
) -> Optional[GoogleDrafts]:
    """
    Args:
        field_ (GoogleDraftsInput): The input for your google drafts
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoogleDrafts
    """

    return sync_detailed(
        client=client,
        field_=field_,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    field_: "GoogleDraftsInput",
    account_id: str,
) -> Response[GoogleDrafts]:
    """
    Args:
        field_ (GoogleDraftsInput): The input for your google drafts
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoogleDrafts]
    """

    kwargs = _get_kwargs(
        client=client,
        field_=field_,
        account_id=account_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    field_: "GoogleDraftsInput",
    account_id: str,
) -> Optional[GoogleDrafts]:
    """
    Args:
        field_ (GoogleDraftsInput): The input for your google drafts
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoogleDrafts
    """

    return (
        await asyncio_detailed(
            client=client,
            field_=field_,
            account_id=account_id,
        )
    ).parsed
