from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.sources_controller_get_metadata_for_source_response_200 import (
    SourcesControllerGetMetadataForSourceResponse200,
)
from ...types import Response


def _get_kwargs(
    source: Any,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/sources/metadata/{source}".format(client.base_url, source=source)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[SourcesControllerGetMetadataForSourceResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SourcesControllerGetMetadataForSourceResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[SourcesControllerGetMetadataForSourceResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source: Any,
    *,
    client: Client,
) -> Response[SourcesControllerGetMetadataForSourceResponse200]:
    """
    Args:
        source (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SourcesControllerGetMetadataForSourceResponse200]
    """

    kwargs = _get_kwargs(
        source=source,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source: Any,
    *,
    client: Client,
) -> Optional[SourcesControllerGetMetadataForSourceResponse200]:
    """
    Args:
        source (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SourcesControllerGetMetadataForSourceResponse200
    """

    return sync_detailed(
        source=source,
        client=client,
    ).parsed


async def asyncio_detailed(
    source: Any,
    *,
    client: Client,
) -> Response[SourcesControllerGetMetadataForSourceResponse200]:
    """
    Args:
        source (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SourcesControllerGetMetadataForSourceResponse200]
    """

    kwargs = _get_kwargs(
        source=source,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source: Any,
    *,
    client: Client,
) -> Optional[SourcesControllerGetMetadataForSourceResponse200]:
    """
    Args:
        source (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SourcesControllerGetMetadataForSourceResponse200
    """

    return (
        await asyncio_detailed(
            source=source,
            client=client,
        )
    ).parsed
