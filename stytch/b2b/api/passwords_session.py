# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from typing import Any, Dict, Optional

from stytch.b2b.models.passwords_session import ResetResponse
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Session:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    @property
    def sub_url(self) -> str:
        return "passwords/session"

    def reset(
        self,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> ResetResponse:
        """Reset the member's password using their existing session. The endpoint will error if the session does not an authentication factor that has been issued within the last 5 minutes.

        Parameters:

        - `password`: The new password for the user.

        - `session_token`: The session token for the user whose password will be reset. This endpoint will error if both session_token and session_jwt are provided.

        - `session_jwt`: The session JWT for the user whose password will be reset. This endpoint will error if both session_token and session_jwt are provided.
        """  # noqa

        payload: Dict[str, Any] = {
            "password": password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "reset")

        res = self.sync_client.post(url, json=payload)
        return ResetResponse.from_json(res.response.status_code, res.json)

    async def reset_async(
        self,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
    ) -> ResetResponse:
        """Reset the member's password using their existing session. The endpoint will error if the session does not an authentication factor that has been issued within the last 5 minutes.

        Parameters:

        - `password`: The new password for the user.

        - `session_token`: The session token for the user whose password will be reset. This endpoint will error if both session_token and session_jwt are provided.

        - `session_jwt`: The session JWT for the user whose password will be reset. This endpoint will error if both session_token and session_jwt are provided.
        """  # noqa

        payload: Dict[str, Any] = {
            "password": password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt

        url = self.api_base.route_with_sub_url(self.sub_url, "reset")

        res = await self.async_client.post(url, json=payload)
        return ResetResponse.from_json(res.response.status, res.json)
