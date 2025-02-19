# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from typing import TYPE_CHECKING

from .base import AsyncCredentialBase
from .._internal import AadClient
from .._internal.decorators import log_get_token_async
from ..._internal import ClientSecretCredentialBase

if TYPE_CHECKING:
    from typing import Any
    from azure.core.credentials import AccessToken


class ClientSecretCredential(AsyncCredentialBase, ClientSecretCredentialBase):
    """Authenticates as a service principal using a client ID and client secret.

    :param str tenant_id: ID of the service principal's tenant. Also called its 'directory' ID.
    :param str client_id: the service principal's client ID
    :param str client_secret: one of the service principal's client secrets

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example 'login.microsoftonline.com',
          the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
          defines authorities for other clouds.
    :keyword bool enable_persistent_cache: if True, the credential will store tokens in a persistent cache. Defaults to
          False.
    :keyword bool allow_unencrypted_cache: if True, the credential will fall back to a plaintext cache when encryption
          is unavailable. Default to False. Has no effect when `enable_persistent_cache` is False.
    """

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def close(self):
        """Close the credential's transport session."""

        await self._client.__aexit__()

    @log_get_token_async
    async def get_token(self, *scopes: str, **kwargs: "Any") -> "AccessToken":
        """Asynchronously request an access token for `scopes`.

        .. note:: This method is called by Azure SDK clients. It isn't intended for use in application code.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
        :rtype: :class:`azure.core.credentials.AccessToken`
        :raises ~azure.core.exceptions.ClientAuthenticationError: authentication failed. The error's ``message``
          attribute gives a reason. Any error response from Azure Active Directory is available as the error's
          ``response`` attribute.
        """
        if not scopes:
            raise ValueError("'get_token' requires at least one scope")

        token = self._client.get_cached_access_token(scopes, query={"client_id": self._client_id})
        if not token:
            token = await self._client.obtain_token_by_client_secret(scopes, self._secret, **kwargs)
        elif self._client.should_refresh(token):
            try:
                await self._client.obtain_token_by_client_secret(scopes, self._secret, **kwargs)
            except Exception:  # pylint: disable=broad-except
                pass
        return token

    def _get_auth_client(self, tenant_id, client_id, **kwargs):
        return AadClient(tenant_id, client_id, **kwargs)
