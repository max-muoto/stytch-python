# !!!
# WARNING: This file is autogenerated
# Only modify code within MANUAL() sections
# or your changes may be overwritten later!
# !!!

from __future__ import annotations

from typing import Optional

from stytch.b2b.models.sso import SAMLConnection
from stytch.core.response_base import ResponseBase


class CreateConnectionResponse(ResponseBase):
    """Response type for `SAML.create_connection`.
    Fields:
      - connection: The `SAML Connection` object affected by this API call. See the [SAML Connection Object](https://stytch.com/docs/b2b/api/saml-connection-object) for complete response field details.
    """  # noqa

    connection: Optional[SAMLConnection] = None


class DeleteVerificationCertificateResponse(ResponseBase):
    """Response type for `SAML.delete_verification_certificate`.
    Fields:
      - certificate_id: The ID of the certificate that was deleted.
    """  # noqa

    certificate_id: str


class UpdateConnectionResponse(ResponseBase):
    """Response type for `SAML.update_connection`.
    Fields:
      - connection: The `SAML Connection` object affected by this API call. See the [SAML Connection Object](https://stytch.com/docs/b2b/api/saml-connection-object) for complete response field details.
    """  # noqa

    connection: Optional[SAMLConnection] = None
