from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.google_events import GoogleEvents
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    i_cal_uid: Union[Unset, None, str] = UNSET,
    sync_token: Union[Unset, None, str] = UNSET,
    updated_min: Union[Unset, None, str] = UNSET,
    time_zone: Union[Unset, None, str] = UNSET,
    time_min: Union[Unset, None, str] = UNSET,
    time_max: Union[Unset, None, str] = UNSET,
    single_events: Union[Unset, None, bool] = UNSET,
    show_deleted: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
    max_attendees: Union[Unset, None, float] = UNSET,
    calendar_id: Union[Unset, None, str] = UNSET,
    account_id: str,
) -> Dict[str, Any]:
    url = "{}/sources/google/events".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["iCalUID"] = i_cal_uid

    params["syncToken"] = sync_token

    params["updatedMin"] = updated_min

    params["timeZone"] = time_zone

    params["timeMin"] = time_min

    params["timeMax"] = time_max

    params["singleEvents"] = single_events

    params["showDeleted"] = show_deleted

    params["q"] = q

    params["pageToken"] = page_token

    params["orderBy"] = order_by

    params["maxAttendees"] = max_attendees

    params["calendarId"] = calendar_id

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GoogleEvents]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GoogleEvents.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GoogleEvents]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    i_cal_uid: Union[Unset, None, str] = UNSET,
    sync_token: Union[Unset, None, str] = UNSET,
    updated_min: Union[Unset, None, str] = UNSET,
    time_zone: Union[Unset, None, str] = UNSET,
    time_min: Union[Unset, None, str] = UNSET,
    time_max: Union[Unset, None, str] = UNSET,
    single_events: Union[Unset, None, bool] = UNSET,
    show_deleted: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
    max_attendees: Union[Unset, None, float] = UNSET,
    calendar_id: Union[Unset, None, str] = UNSET,
    account_id: str,
) -> Response[GoogleEvents]:
    """
    Args:
        i_cal_uid (Union[Unset, None, str]):
        sync_token (Union[Unset, None, str]):
        updated_min (Union[Unset, None, str]):
        time_zone (Union[Unset, None, str]):
        time_min (Union[Unset, None, str]):
        time_max (Union[Unset, None, str]):
        single_events (Union[Unset, None, bool]):
        show_deleted (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        page_token (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):
        max_attendees (Union[Unset, None, float]):
        calendar_id (Union[Unset, None, str]):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoogleEvents]
    """

    kwargs = _get_kwargs(
        client=client,
        i_cal_uid=i_cal_uid,
        sync_token=sync_token,
        updated_min=updated_min,
        time_zone=time_zone,
        time_min=time_min,
        time_max=time_max,
        single_events=single_events,
        show_deleted=show_deleted,
        q=q,
        page_token=page_token,
        order_by=order_by,
        max_attendees=max_attendees,
        calendar_id=calendar_id,
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
    i_cal_uid: Union[Unset, None, str] = UNSET,
    sync_token: Union[Unset, None, str] = UNSET,
    updated_min: Union[Unset, None, str] = UNSET,
    time_zone: Union[Unset, None, str] = UNSET,
    time_min: Union[Unset, None, str] = UNSET,
    time_max: Union[Unset, None, str] = UNSET,
    single_events: Union[Unset, None, bool] = UNSET,
    show_deleted: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
    max_attendees: Union[Unset, None, float] = UNSET,
    calendar_id: Union[Unset, None, str] = UNSET,
    account_id: str,
) -> Optional[GoogleEvents]:
    """
    Args:
        i_cal_uid (Union[Unset, None, str]):
        sync_token (Union[Unset, None, str]):
        updated_min (Union[Unset, None, str]):
        time_zone (Union[Unset, None, str]):
        time_min (Union[Unset, None, str]):
        time_max (Union[Unset, None, str]):
        single_events (Union[Unset, None, bool]):
        show_deleted (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        page_token (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):
        max_attendees (Union[Unset, None, float]):
        calendar_id (Union[Unset, None, str]):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoogleEvents
    """

    return sync_detailed(
        client=client,
        i_cal_uid=i_cal_uid,
        sync_token=sync_token,
        updated_min=updated_min,
        time_zone=time_zone,
        time_min=time_min,
        time_max=time_max,
        single_events=single_events,
        show_deleted=show_deleted,
        q=q,
        page_token=page_token,
        order_by=order_by,
        max_attendees=max_attendees,
        calendar_id=calendar_id,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    i_cal_uid: Union[Unset, None, str] = UNSET,
    sync_token: Union[Unset, None, str] = UNSET,
    updated_min: Union[Unset, None, str] = UNSET,
    time_zone: Union[Unset, None, str] = UNSET,
    time_min: Union[Unset, None, str] = UNSET,
    time_max: Union[Unset, None, str] = UNSET,
    single_events: Union[Unset, None, bool] = UNSET,
    show_deleted: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
    max_attendees: Union[Unset, None, float] = UNSET,
    calendar_id: Union[Unset, None, str] = UNSET,
    account_id: str,
) -> Response[GoogleEvents]:
    """
    Args:
        i_cal_uid (Union[Unset, None, str]):
        sync_token (Union[Unset, None, str]):
        updated_min (Union[Unset, None, str]):
        time_zone (Union[Unset, None, str]):
        time_min (Union[Unset, None, str]):
        time_max (Union[Unset, None, str]):
        single_events (Union[Unset, None, bool]):
        show_deleted (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        page_token (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):
        max_attendees (Union[Unset, None, float]):
        calendar_id (Union[Unset, None, str]):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoogleEvents]
    """

    kwargs = _get_kwargs(
        client=client,
        i_cal_uid=i_cal_uid,
        sync_token=sync_token,
        updated_min=updated_min,
        time_zone=time_zone,
        time_min=time_min,
        time_max=time_max,
        single_events=single_events,
        show_deleted=show_deleted,
        q=q,
        page_token=page_token,
        order_by=order_by,
        max_attendees=max_attendees,
        calendar_id=calendar_id,
        account_id=account_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    i_cal_uid: Union[Unset, None, str] = UNSET,
    sync_token: Union[Unset, None, str] = UNSET,
    updated_min: Union[Unset, None, str] = UNSET,
    time_zone: Union[Unset, None, str] = UNSET,
    time_min: Union[Unset, None, str] = UNSET,
    time_max: Union[Unset, None, str] = UNSET,
    single_events: Union[Unset, None, bool] = UNSET,
    show_deleted: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
    max_attendees: Union[Unset, None, float] = UNSET,
    calendar_id: Union[Unset, None, str] = UNSET,
    account_id: str,
) -> Optional[GoogleEvents]:
    """
    Args:
        i_cal_uid (Union[Unset, None, str]):
        sync_token (Union[Unset, None, str]):
        updated_min (Union[Unset, None, str]):
        time_zone (Union[Unset, None, str]):
        time_min (Union[Unset, None, str]):
        time_max (Union[Unset, None, str]):
        single_events (Union[Unset, None, bool]):
        show_deleted (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        page_token (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):
        max_attendees (Union[Unset, None, float]):
        calendar_id (Union[Unset, None, str]):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoogleEvents
    """

    return (
        await asyncio_detailed(
            client=client,
            i_cal_uid=i_cal_uid,
            sync_token=sync_token,
            updated_min=updated_min,
            time_zone=time_zone,
            time_min=time_min,
            time_max=time_max,
            single_events=single_events,
            show_deleted=show_deleted,
            q=q,
            page_token=page_token,
            order_by=order_by,
            max_attendees=max_attendees,
            calendar_id=calendar_id,
            account_id=account_id,
        )
    ).parsed
