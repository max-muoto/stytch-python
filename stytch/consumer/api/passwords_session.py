# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

from stytch.consumer.models.passwords_session import ResetResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Sessions:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def reset(
        self,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> ResetResponse:
        """Reset the user’s password using their existing session. The endpoint will error if the session does not have a password, email magic link, or email OTP authentication factor that has been issued within the last 5 minutes. This endpoint requires either a `session_jwt` or `session_token` be included in the request.

        Fields:
          - password: The password of the user
          - session_token: The `session_token` associated with a User's existing Session.
          - session_jwt: The `session_jwt` associated with a User's existing Session.
        """  # noqa
        data: Dict[str, Any] = {
            "password": password,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.url_for("/v1/passwords/session/reset", data)
        res = self.sync_client.post(url, data)
        return ResetResponse.from_json(res.response.status_code, res.json)

    async def reset_async(
        self,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> ResetResponse:
        """Reset the user’s password using their existing session. The endpoint will error if the session does not have a password, email magic link, or email OTP authentication factor that has been issued within the last 5 minutes. This endpoint requires either a `session_jwt` or `session_token` be included in the request.

        Fields:
          - password: The password of the user
          - session_token: The `session_token` associated with a User's existing Session.
          - session_jwt: The `session_jwt` associated with a User's existing Session.
        """  # noqa
        data: Dict[str, Any] = {
            "password": password,
        }
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt

        url = self.api_base.url_for("/v1/passwords/session/reset", data)
        res = await self.async_client.post(url, data)
        return ResetResponse.from_json(res.response.status, res.json)
