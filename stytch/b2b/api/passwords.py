# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from typing import Any, Dict, Optional, Union

from stytch.b2b.api.passwords_email import Email
from stytch.b2b.api.passwords_existing_password import ExistingPassword
from stytch.b2b.api.passwords_session import Session
from stytch.b2b.models.passwords import (
    AuthenticateResponse,
    MigrateResponse,
    StrengthCheckResponse,
)
from stytch.core.api_base import ApiBase
from stytch.core.http.client import AsyncClient, SyncClient
from stytch.core.models import Name


class Passwords:
    def __init__(
        self,
        api_base: ApiBase,
        sync_client: SyncClient,
        async_client: AsyncClient,
    ) -> None:
        self.api_base = api_base
        self.sync_client = sync_client
        self.async_client = async_client
        self.email = Email(api_base, sync_client, async_client)
        self.existing_password = ExistingPassword(api_base, sync_client, async_client)
        self.session = Session(api_base, sync_client, async_client)

    @property
    def sub_url(self) -> str:
        return "passwords"

    def authenticate(
        self,
        organization_id: str,
        email_address: str,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        """[Stytch docs](https://stytch.com/docs/b2b/api/passwords-authenticate)

        Authenticate a member with their email address and password. This endpoint verifies that the member has a password currently set, and that the entered password is correct. There are two instances where the endpoint will return a reset_password error even if they enter their previous password:

        - The member’s credentials appeared in the HaveIBeenPwned dataset.

          - We force a password reset to ensure that the member is the legitimate owner of the email address, and not a malicious actor abusing the compromised credentials.

        - A member that has previously authenticated with email/password uses a passwordless authentication method tied to the same email address (e.g. Magic Links, Google OAuth) for the first time. Any subsequent email/password authentication attempt will result in this error.

          - We force a password reset in this instance in order to safely deduplicate the account by email address, without introducing the risk of a pre-hijack account takeover attack. Imagine a bad actor creates many accounts using passwords and the known email addresses of their victims. If a victim comes to the site and logs in for the first time with an email-based passwordless authentication method then both the victim and the bad actor have credentials to access to the same account. To prevent this, any further email/password login attempts first require a password reset which can only be accomplished by someone with access to the underlying email address.

        Parameters:

        - `organization_id`: Globally unique UUID that identifies a specific Organization. The organization_id is critical to perform operations on an Organization, so be sure to preserve this value.

        - `email_address`: The email of the Member

        - `password`: The password to authenticate

        - `session_token`: A secret token for a given Stytch Session. Read more about session_token in our Session Management guide.

        - `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session. Read more about session_token in our Session Management guide.

        - `session_duration_minutes`: The Session lifetime of this many minutes from now; minimum of 5 and a maximum of 129600 minutes (90 days). Note that a successful authentication will continue to extend the Session this many minutes.

        - `session_custom_claims`: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in Session duration minutes. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.
          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes
        """  # noqa

        payload: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
            "password": password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate")

        res = self.sync_client.post(url, json=payload)
        return AuthenticateResponse.from_json(res.response.status_code, res.json)

    async def authenticate_async(
        self,
        organization_id: str,
        email_address: str,
        password: str,
        session_token: Optional[str] = None,
        session_jwt: Optional[str] = None,
        session_duration_minutes: Optional[int] = None,
        session_custom_claims: Optional[Dict[str, Any]] = None,
    ) -> AuthenticateResponse:
        """[Stytch docs](https://stytch.com/docs/b2b/api/passwords-authenticate)

        Authenticate a member with their email address and password. This endpoint verifies that the member has a password currently set, and that the entered password is correct. There are two instances where the endpoint will return a reset_password error even if they enter their previous password:

        - The member’s credentials appeared in the HaveIBeenPwned dataset.

          - We force a password reset to ensure that the member is the legitimate owner of the email address, and not a malicious actor abusing the compromised credentials.

        - A member that has previously authenticated with email/password uses a passwordless authentication method tied to the same email address (e.g. Magic Links, Google OAuth) for the first time. Any subsequent email/password authentication attempt will result in this error.

          - We force a password reset in this instance in order to safely deduplicate the account by email address, without introducing the risk of a pre-hijack account takeover attack. Imagine a bad actor creates many accounts using passwords and the known email addresses of their victims. If a victim comes to the site and logs in for the first time with an email-based passwordless authentication method then both the victim and the bad actor have credentials to access to the same account. To prevent this, any further email/password login attempts first require a password reset which can only be accomplished by someone with access to the underlying email address.

        Parameters:

        - `organization_id`: Globally unique UUID that identifies a specific Organization. The organization_id is critical to perform operations on an Organization, so be sure to preserve this value.

        - `email_address`: The email of the Member

        - `password`: The password to authenticate

        - `session_token`: A secret token for a given Stytch Session. Read more about session_token in our Session Management guide.

        - `session_jwt`: The JSON Web Token (JWT) for a given Stytch Session. Read more about session_token in our Session Management guide.

        - `session_duration_minutes`: The Session lifetime of this many minutes from now; minimum of 5 and a maximum of 129600 minutes (90 days). Note that a successful authentication will continue to extend the Session this many minutes.

        - `session_custom_claims`: Add a custom claims map to the Session being authenticated. Claims are only created if a Session is initialized by providing a value in Session duration minutes. Claims will be included on the Session object and in the JWT. To update a key in an existing Session, supply a new value. To delete a key, supply a null value.
          Custom claims made with reserved claims ("iss", "sub", "aud", "exp", "nbf", "iat", "jti") will be ignored. Total custom claims size cannot exceed four kilobytes
        """  # noqa

        payload: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
            "password": password,
        }

        if session_token is not None:
            payload["session_token"] = session_token
        if session_jwt is not None:
            payload["session_jwt"] = session_jwt
        if session_duration_minutes is not None:
            payload["session_duration_minutes"] = session_duration_minutes
        if session_custom_claims is not None:
            payload["session_custom_claims"] = session_custom_claims

        url = self.api_base.route_with_sub_url(self.sub_url, "authenticate")

        res = await self.async_client.post(url, json=payload)
        return AuthenticateResponse.from_json(res.response.status, res.json)

    def strength_check(
        self,
        password: str,
        email_address: Optional[str] = None,
    ) -> StrengthCheckResponse:

        payload: Dict[str, Any] = {
            "password": password,
        }

        if email_address is not None:
            payload["email_address"] = email_address

        url = self.api_base.route_with_sub_url(self.sub_url, "strength_check")

        res = self.sync_client.post(url, json=payload)
        return StrengthCheckResponse.from_json(res.response.status_code, res.json)

    async def strength_check_async(
        self,
        password: str,
        email_address: Optional[str] = None,
    ) -> StrengthCheckResponse:

        payload: Dict[str, Any] = {
            "password": password,
        }

        if email_address is not None:
            payload["email_address"] = email_address

        url = self.api_base.route_with_sub_url(self.sub_url, "strength_check")

        res = await self.async_client.post(url, json=payload)
        return StrengthCheckResponse.from_json(res.response.status, res.json)

    def migrate(
        self,
        organization_id: str,
        email_address: str,
        hash: str,
        hash_type: str,
        md_5_config: Optional[Dict[str, Any]] = None,
        argon_2_config: Optional[Dict[str, Any]] = None,
        sha_1_config: Optional[Dict[str, Any]] = None,
        scrypt_config: Optional[Dict[str, Any]] = None,
        name: Optional[Union[Name, Dict[str, str]]] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> MigrateResponse:
        """Adds an existing password to a member's email that doesn't have a password yet. We support migrating members from passwords stored with bcrypt, scrypt, argon2, MD-5, and SHA-1. This endpoint has a rate limit of 10 requests per second.

        Parameters:

        - `organization_id`: Globally unique UUID that identifies a specific Organization. The organization_id is critical to perform operations on an Organization, so be sure to preserve this value.

        - `email_address`: The email of the Member

        - `hash`: The password hash. For a Scrypt hash, the hash needs to be a base64 encoded string.

        - `hash_type`: The password hash used. Currently bcrypt, scrypt, argon2i, argon2id, md_5, and sha_1 are supported.

        - `scrypt_config`: Required parameters if the scrypt is not provided in a PHC encoded form.

        - `argon_2_config`: Required parameters if the argon2 hex form, as opposed to the encoded form, is supplied.

        - `md_5_config`: Optional parameters for MD-5 hash types.

        - `sha_1_config`: Optional parameters for SHA-1 hash types.

        - `name`: The name of the user. Each field in the name object is optional.

        - `trusted_metadata`: An arbitrary JSON object for storing application-specific or identity-provider-specific data.

        - `untrusted_metadata`: The untrusted_metadata field contains an arbitrary JSON object of application-specific data. Untrusted metadata can be edited by end Members directly via the SDK, and cannot be used to store critical information. See the Metadata reference for complete field behavior details.
        """  # noqa

        payload: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
            "hash": hash,
            "hash_type": hash_type,
        }

        if md_5_config is not None:
            payload["md_5_config"] = md_5_config
        if argon_2_config is not None:
            payload["argon_2_config"] = argon_2_config
        if sha_1_config is not None:
            payload["sha_1_config"] = sha_1_config
        if scrypt_config is not None:
            payload["scrypt_config"] = scrypt_config
        if name is not None:
            payload["name"] = name
        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            payload["untrusted_metadata"] = untrusted_metadata

        url = self.api_base.route_with_sub_url(self.sub_url, "migrate")

        res = self.sync_client.post(url, json=payload)
        return MigrateResponse.from_json(res.response.status_code, res.json)

    async def migrate_async(
        self,
        organization_id: str,
        email_address: str,
        hash: str,
        hash_type: str,
        md_5_config: Optional[Dict[str, Any]] = None,
        argon_2_config: Optional[Dict[str, Any]] = None,
        sha_1_config: Optional[Dict[str, Any]] = None,
        scrypt_config: Optional[Dict[str, Any]] = None,
        name: Optional[Union[Name, Dict[str, str]]] = None,
        trusted_metadata: Optional[Dict[str, Any]] = None,
        untrusted_metadata: Optional[Dict[str, Any]] = None,
    ) -> MigrateResponse:
        """Adds an existing password to a member's email that doesn't have a password yet. We support migrating members from passwords stored with bcrypt, scrypt, argon2, MD-5, and SHA-1. This endpoint has a rate limit of 10 requests per second.

        Parameters:

        - `organization_id`: Globally unique UUID that identifies a specific Organization. The organization_id is critical to perform operations on an Organization, so be sure to preserve this value.

        - `email_address`: The email of the Member

        - `hash`: The password hash. For a Scrypt hash, the hash needs to be a base64 encoded string.

        - `hash_type`: The password hash used. Currently bcrypt, scrypt, argon2i, argon2id, md_5, and sha_1 are supported.

        - `scrypt_config`: Required parameters if the scrypt is not provided in a PHC encoded form.

        - `argon_2_config`: Required parameters if the argon2 hex form, as opposed to the encoded form, is supplied.

        - `md_5_config`: Optional parameters for MD-5 hash types.

        - `sha_1_config`: Optional parameters for SHA-1 hash types.

        - `name`: The name of the user. Each field in the name object is optional.

        - `trusted_metadata`: An arbitrary JSON object for storing application-specific or identity-provider-specific data.

        - `untrusted_metadata`: The untrusted_metadata field contains an arbitrary JSON object of application-specific data. Untrusted metadata can be edited by end Members directly via the SDK, and cannot be used to store critical information. See the Metadata reference for complete field behavior details.
        """  # noqa

        payload: Dict[str, Any] = {
            "organization_id": organization_id,
            "email_address": email_address,
            "hash": hash,
            "hash_type": hash_type,
        }

        if md_5_config is not None:
            payload["md_5_config"] = md_5_config
        if argon_2_config is not None:
            payload["argon_2_config"] = argon_2_config
        if sha_1_config is not None:
            payload["sha_1_config"] = sha_1_config
        if scrypt_config is not None:
            payload["scrypt_config"] = scrypt_config
        if name is not None:
            payload["name"] = name
        if trusted_metadata is not None:
            payload["trusted_metadata"] = trusted_metadata
        if untrusted_metadata is not None:
            payload["untrusted_metadata"] = untrusted_metadata

        url = self.api_base.route_with_sub_url(self.sub_url, "migrate")

        res = await self.async_client.post(url, json=payload)
        return MigrateResponse.from_json(res.response.status, res.json)
