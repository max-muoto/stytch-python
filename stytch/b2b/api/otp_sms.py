# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Any, Dict, Optional

from stytch.b2b.models.otp_sms import (
    AuthenticateResponse,
    SendRequestLocale,
    SendResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient


class Sms:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client

    def send(
        self,
        organization_id: str,
        member_id: str,
        phone_number: Optional[str] = None,
        locale: Optional[SendRequestLocale] = None,
    ) -> SendResponse:
        """Send a one-time passcode (OTP) to a Member's phone number. If the Member already has a phone number, this will send an OTP to the number associated with their `member_id`. If not, then this will send an OTP to the `phone_number` provided and link the `phone_number` with the Member.
        An error will be thrown if the Member already has a phone number and the provided `phone_number` does not match the existing one.

        Note that sending another OTP code before the first has expired will invalidate the first code.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
          - phone_number: The phone number to send the OTP to. If the Member already has a phone number, this argument is not needed.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
        }
        if phone_number is not None:
            data["phone_number"] = phone_number
        if locale is not None:
            data["locale"] = locale.value

        url = self.api_base.url_for("/v1/b2b/otps/sms/send", data)
        res = self.sync_client.post(url, data)
        return SendResponse.from_json(res.response.status_code, res.json)

    async def send_async(
        self,
        organization_id: str,
        member_id: str,
        phone_number: Optional[str] = None,
        locale: Optional[SendRequestLocale] = None,
    ) -> SendResponse:
        """Send a one-time passcode (OTP) to a Member's phone number. If the Member already has a phone number, this will send an OTP to the number associated with their `member_id`. If not, then this will send an OTP to the `phone_number` provided and link the `phone_number` with the Member.
        An error will be thrown if the Member already has a phone number and the provided `phone_number` does not match the existing one.

        Note that sending another OTP code before the first has expired will invalidate the first code.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
          - phone_number: The phone number to send the OTP to. If the Member already has a phone number, this argument is not needed.
          - locale: Used to determine which language to use when sending the user this delivery method. Parameter is a [IETF BCP 47 language tag](https://www.w3.org/International/articles/language-tags/), e.g. `"en"`.

        Currently supported languages are English (`"en"`), Spanish (`"es"`), and Brazilian Portuguese (`"pt-br"`); if no value is provided, the copy defaults to English.

        Request support for additional languages [here](https://docs.google.com/forms/d/e/1FAIpQLScZSpAu_m2AmLXRT3F3kap-s_mcV6UTBitYn6CdyWP0-o7YjQ/viewform?usp=sf_link")!

        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
        }
        if phone_number is not None:
            data["phone_number"] = phone_number
        if locale is not None:
            data["locale"] = locale.value

        url = self.api_base.url_for("/v1/b2b/otps/sms/send", data)
        res = await self.async_client.post(url, data)
        return SendResponse.from_json(res.response.status, res.json)

    def authenticate(
        self,
        organization_id: str,
        member_id: str,
        code: str,
        intermediate_session_token: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        set_mfa_enrollment: Optional[str] = None,
    ) -> AuthenticateResponse:
        """Authenticates a Member's OTP code. This endpoint verifies that the code is valid and hasn't expired or been previously used. A given Member may only have a single active OTP code at any given time. If a Member requests another OTP code before the first one has expired, the first one will be invalidated.

        Exactly one of `intermediate_session_token`, `session_token`, or `session_jwt` must be provided in the request.
        If an intermediate session token is provided, this operation will consume it.

        If the Organization's MFA policy is `REQUIRED_FOR_ALL`, a successful OTP authentication will change the Member's `mfa_enrolled` status to `true` if it is not already `true`.
        If the Organization's MFA policy is `OPTIONAL`, the Member's MFA enrollment can be toggled by passing in a value for the `set_mfa_enrollment` field.

        Provide the `session_duration_minutes` parameter to set the lifetime of the session. If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a duration of 60 minutes.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
          - code: The code to authenticate.
          - intermediate_session_token: The Intermediate Session Token. This token does not necessarily belong to a specific instance of a Member, but represents a bag of factors that may be converted to a member session.
            The token can be used with the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms) to complete an MFA flow;
            the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) to join a specific Organization that allows the factors represented by the intermediate session token;
            or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to create a new Organization and Member.
          - session_token: A secret token for a given Stytch Session.
          - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want
          to use the Stytch session product, you can ignore the session fields in the response.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in
          `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To
          delete a key, supply a null value. Custom claims made with reserved claims (`iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`) will be ignored.
          Total custom claims size cannot exceed four kilobytes.
          - set_mfa_enrollment: Optionally sets the Member’s MFA enrollment status upon a successful authentication. If the Organization’s MFA policy is `REQUIRED_FOR_ALL`, this field will be ignored. If this field is not passed in, the Member’s `mfa_enrolled` boolean will not be affected. The options are:

          `enroll` – sets the Member's `mfa_enrolled` boolean to `true`. The Member will be required to complete an MFA step upon subsequent logins to the Organization.

          `unenroll` –  sets the Member's `mfa_enrolled` boolean to `false`. The Member will no longer be required to complete MFA steps when logging in to the Organization.

        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
            "code": code,
        }
        if intermediate_session_token is not None:
            data["intermediate_session_token"] = intermediate_session_token
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims
        if set_mfa_enrollment is not None:
            data["set_mfa_enrollment"] = set_mfa_enrollment

        url = self.api_base.url_for("/v1/b2b/otps/sms/authenticate", data)
        res = self.sync_client.post(url, data)
        return AuthenticateResponse.from_json(res.response.status_code, res.json)

    async def authenticate_async(
        self,
        organization_id: str,
        member_id: str,
        code: str,
        intermediate_session_token: Optional[str] = None,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
        set_mfa_enrollment: Optional[str] = None,
    ) -> AuthenticateResponse:
        """Authenticates a Member's OTP code. This endpoint verifies that the code is valid and hasn't expired or been previously used. A given Member may only have a single active OTP code at any given time. If a Member requests another OTP code before the first one has expired, the first one will be invalidated.

        Exactly one of `intermediate_session_token`, `session_token`, or `session_jwt` must be provided in the request.
        If an intermediate session token is provided, this operation will consume it.

        If the Organization's MFA policy is `REQUIRED_FOR_ALL`, a successful OTP authentication will change the Member's `mfa_enrolled` status to `true` if it is not already `true`.
        If the Organization's MFA policy is `OPTIONAL`, the Member's MFA enrollment can be toggled by passing in a value for the `set_mfa_enrollment` field.

        Provide the `session_duration_minutes` parameter to set the lifetime of the session. If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a duration of 60 minutes.

        Fields:
          - organization_id: Globally unique UUID that identifies a specific Organization. The `organization_id` is critical to perform operations on an Organization, so be sure to preserve this value.
          - member_id: Globally unique UUID that identifies a specific Member. The `member_id` is critical to perform operations on a Member, so be sure to preserve this value.
          - code: The code to authenticate.
          - intermediate_session_token: The Intermediate Session Token. This token does not necessarily belong to a specific instance of a Member, but represents a bag of factors that may be converted to a member session.
            The token can be used with the [OTP SMS Authenticate endpoint](https://stytch.com/docs/b2b/api/authenticate-otp-sms) to complete an MFA flow;
            the [Exchange Intermediate Session endpoint](https://stytch.com/docs/b2b/api/exchange-intermediate-session) to join a specific Organization that allows the factors represented by the intermediate session token;
            or the [Create Organization via Discovery endpoint](https://stytch.com/docs/b2b/api/create-organization-via-discovery) to create a new Organization and Member.
          - session_token: A secret token for a given Stytch Session.
          - session_jwt: The JSON Web Token (JWT) for a given Stytch Session.
          - session_duration_minutes: Set the session lifetime to be this many minutes from now. This will start a new session if one doesn't already exist,
          returning both an opaque `session_token` and `session_jwt` for this session. Remember that the `session_jwt` will have a fixed lifetime of
          five minutes regardless of the underlying session duration, and will need to be refreshed over time.

          This value must be a minimum of 5 and a maximum of 527040 minutes (366 days).

          If a `session_token` or `session_jwt` is provided then a successful authentication will continue to extend the session this many minutes.

          If the `session_duration_minutes` parameter is not specified, a Stytch session will be created with a 60 minute duration. If you don't want
          to use the Stytch session product, you can ignore the session fields in the response.
          - session_custom_claims: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in
          `session_duration_minutes`. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To
          delete a key, supply a null value. Custom claims made with reserved claims (`iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`) will be ignored.
          Total custom claims size cannot exceed four kilobytes.
          - set_mfa_enrollment: Optionally sets the Member’s MFA enrollment status upon a successful authentication. If the Organization’s MFA policy is `REQUIRED_FOR_ALL`, this field will be ignored. If this field is not passed in, the Member’s `mfa_enrolled` boolean will not be affected. The options are:

          `enroll` – sets the Member's `mfa_enrolled` boolean to `true`. The Member will be required to complete an MFA step upon subsequent logins to the Organization.

          `unenroll` –  sets the Member's `mfa_enrolled` boolean to `false`. The Member will no longer be required to complete MFA steps when logging in to the Organization.

        """  # noqa
        data: Dict[str, Any] = {
            "organization_id": organization_id,
            "member_id": member_id,
            "code": code,
        }
        if intermediate_session_token is not None:
            data["intermediate_session_token"] = intermediate_session_token
        if session_token is not None:
            data["session_token"] = session_token
        if session_jwt is not None:
            data["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            data["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            data["session_custom_claims"] = session_custom_claims
        if set_mfa_enrollment is not None:
            data["set_mfa_enrollment"] = set_mfa_enrollment

        url = self.api_base.url_for("/v1/b2b/otps/sms/authenticate", data)
        res = await self.async_client.post(url, data)
        return AuthenticateResponse.from_json(res.response.status, res.json)
