# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ProvidersOperations:
    """ProvidersOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.resources.v2019_10_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def unregister(
        self,
        resource_provider_namespace: str,
        **kwargs
    ) -> "models.Provider":
        """Unregisters a subscription from a resource provider.

        :param resource_provider_namespace: The namespace of the resource provider to unregister.
        :type resource_provider_namespace: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Provider, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2019_10_01.models.Provider
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Provider"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01"

        # Construct URL
        url = self.unregister.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceProviderNamespace': self._serialize.url("resource_provider_namespace", resource_provider_namespace, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Provider', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    unregister.metadata = {'url': '/subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}/unregister'}  # type: ignore

    async def register(
        self,
        resource_provider_namespace: str,
        **kwargs
    ) -> "models.Provider":
        """Registers a subscription with a resource provider.

        :param resource_provider_namespace: The namespace of the resource provider to register.
        :type resource_provider_namespace: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Provider, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2019_10_01.models.Provider
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Provider"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01"

        # Construct URL
        url = self.register.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceProviderNamespace': self._serialize.url("resource_provider_namespace", resource_provider_namespace, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Provider', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    register.metadata = {'url': '/subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}/register'}  # type: ignore

    def list(
        self,
        top: Optional[int] = None,
        expand: Optional[str] = None,
        **kwargs
    ) -> AsyncIterable["models.ProviderListResult"]:
        """Gets all resource providers for a subscription.

        :param top: The number of results to return. If null is passed returns all deployments.
        :type top: int
        :param expand: The properties to include in the results. For example, use &$expand=metadata in
     the query string to retrieve resource provider metadata. To include property aliases in
     response, use $expand=resourceTypes/aliases.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProviderListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.resources.v2019_10_01.models.ProviderListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ProviderListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ProviderListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers'}  # type: ignore

    def list_at_tenant_scope(
        self,
        top: Optional[int] = None,
        expand: Optional[str] = None,
        **kwargs
    ) -> AsyncIterable["models.ProviderListResult"]:
        """Gets all resource providers for the tenant.

        :param top: The number of results to return. If null is passed returns all providers.
        :type top: int
        :param expand: The properties to include in the results. For example, use &$expand=metadata in
     the query string to retrieve resource provider metadata. To include property aliases in
     response, use $expand=resourceTypes/aliases.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ProviderListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.resources.v2019_10_01.models.ProviderListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ProviderListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_at_tenant_scope.metadata['url']  # type: ignore
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ProviderListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_at_tenant_scope.metadata = {'url': '/providers'}  # type: ignore

    async def get(
        self,
        resource_provider_namespace: str,
        expand: Optional[str] = None,
        **kwargs
    ) -> "models.Provider":
        """Gets the specified resource provider.

        :param resource_provider_namespace: The namespace of the resource provider.
        :type resource_provider_namespace: str
        :param expand: The $expand query parameter. For example, to include property aliases in
         response, use $expand=resourceTypes/aliases.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Provider, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2019_10_01.models.Provider
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Provider"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceProviderNamespace': self._serialize.url("resource_provider_namespace", resource_provider_namespace, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Provider', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}'}  # type: ignore

    async def get_at_tenant_scope(
        self,
        resource_provider_namespace: str,
        expand: Optional[str] = None,
        **kwargs
    ) -> "models.Provider":
        """Gets the specified resource provider at the tenant level.

        :param resource_provider_namespace: The namespace of the resource provider.
        :type resource_provider_namespace: str
        :param expand: The $expand query parameter. For example, to include property aliases in
         response, use $expand=resourceTypes/aliases.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Provider, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.resources.v2019_10_01.models.Provider
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Provider"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01"

        # Construct URL
        url = self.get_at_tenant_scope.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceProviderNamespace': self._serialize.url("resource_provider_namespace", resource_provider_namespace, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Provider', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_at_tenant_scope.metadata = {'url': '/providers/{resourceProviderNamespace}'}  # type: ignore
