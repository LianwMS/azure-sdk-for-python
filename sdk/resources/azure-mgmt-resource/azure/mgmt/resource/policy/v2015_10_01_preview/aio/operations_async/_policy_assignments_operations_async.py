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

class PolicyAssignmentsOperations:
    """PolicyAssignmentsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.policy.v2015_10_01_preview.models
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

    async def delete(
        self,
        scope: str,
        policy_assignment_name: str,
        **kwargs
    ) -> "models.PolicyAssignment":
        """Deletes a policy assignment.

        :param scope: The scope of the policy assignment.
        :type scope: str
        :param policy_assignment_name: The name of the policy assignment to delete.
        :type policy_assignment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2015_10_01_preview.models.PolicyAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PolicyAssignment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2015-10-01-preview"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'policyAssignmentName': self._serialize.url("policy_assignment_name", policy_assignment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    delete.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/policyassignments/{policyAssignmentName}'}  # type: ignore

    async def create(
        self,
        scope: str,
        policy_assignment_name: str,
        parameters: "models.PolicyAssignment",
        **kwargs
    ) -> "models.PolicyAssignment":
        """Creates a policy assignment.

        Policy assignments are inherited by child resources. For example, when you apply a policy to a
        resource group that policy is assigned to all resources in the group.

        :param scope: The scope of the policy assignment.
        :type scope: str
        :param policy_assignment_name: The name of the policy assignment.
        :type policy_assignment_name: str
        :param parameters: Parameters for the policy assignment.
        :type parameters: ~azure.mgmt.resource.policy.v2015_10_01_preview.models.PolicyAssignment
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2015_10_01_preview.models.PolicyAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PolicyAssignment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2015-10-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create.metadata['url']  # type: ignore
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'policyAssignmentName': self._serialize.url("policy_assignment_name", policy_assignment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'PolicyAssignment')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/policyassignments/{policyAssignmentName}'}  # type: ignore

    async def get(
        self,
        scope: str,
        policy_assignment_name: str,
        **kwargs
    ) -> "models.PolicyAssignment":
        """Gets a policy assignment.

        :param scope: The scope of the policy assignment.
        :type scope: str
        :param policy_assignment_name: The name of the policy assignment to get.
        :type policy_assignment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2015_10_01_preview.models.PolicyAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PolicyAssignment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2015-10-01-preview"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'policyAssignmentName': self._serialize.url("policy_assignment_name", policy_assignment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
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

        deserialized = self._deserialize('PolicyAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/policyassignments/{policyAssignmentName}'}  # type: ignore

    def list_for_resource_group(
        self,
        resource_group_name: str,
        filter: Optional[str] = None,
        **kwargs
    ) -> AsyncIterable["models.PolicyAssignmentListResult"]:
        """Gets policy assignments for the resource group.

        :param resource_group_name: The name of the resource group that contains policy assignments.
        :type resource_group_name: str
        :param filter: The filter to apply on the operation.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyAssignmentListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.policy.v2015_10_01_preview.models.PolicyAssignmentListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PolicyAssignmentListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2015-10-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_for_resource_group.metadata['url']  # type: ignore
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str', skip_quote=True)
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
            deserialized = self._deserialize('PolicyAssignmentListResult', pipeline_response)
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
    list_for_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/policyAssignments'}  # type: ignore

    def list_for_resource(
        self,
        resource_group_name: str,
        resource_provider_namespace: str,
        parent_resource_path: str,
        resource_type: str,
        resource_name: str,
        filter: Optional[str] = None,
        **kwargs
    ) -> AsyncIterable["models.PolicyAssignmentListResult"]:
        """Gets policy assignments for a  resource.

        :param resource_group_name: The name of the resource group containing the resource. The name is
     case insensitive.
        :type resource_group_name: str
        :param resource_provider_namespace: The namespace of the resource provider.
        :type resource_provider_namespace: str
        :param parent_resource_path: The parent resource path.
        :type parent_resource_path: str
        :param resource_type: The resource type.
        :type resource_type: str
        :param resource_name: The name of the resource with policy assignments.
        :type resource_name: str
        :param filter: The filter to apply on the operation.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyAssignmentListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.policy.v2015_10_01_preview.models.PolicyAssignmentListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PolicyAssignmentListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2015-10-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_for_resource.metadata['url']  # type: ignore
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'resourceProviderNamespace': self._serialize.url("resource_provider_namespace", resource_provider_namespace, 'str'),
                    'parentResourcePath': self._serialize.url("parent_resource_path", parent_resource_path, 'str', skip_quote=True),
                    'resourceType': self._serialize.url("resource_type", resource_type, 'str', skip_quote=True),
                    'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
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
            deserialized = self._deserialize('PolicyAssignmentListResult', pipeline_response)
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
    list_for_resource.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/policyassignments'}  # type: ignore

    def list(
        self,
        filter: Optional[str] = None,
        **kwargs
    ) -> AsyncIterable["models.PolicyAssignmentListResult"]:
        """Gets all the policy assignments for a subscription.

        :param filter: The filter to apply on the operation.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyAssignmentListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.policy.v2015_10_01_preview.models.PolicyAssignmentListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PolicyAssignmentListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2015-10-01-preview"

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
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
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
            deserialized = self._deserialize('PolicyAssignmentListResult', pipeline_response)
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
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyassignments'}  # type: ignore

    async def delete_by_id(
        self,
        policy_assignment_id: str,
        **kwargs
    ) -> "models.PolicyAssignment":
        """Deletes a policy assignment by ID.

        When providing a scope for the assignment, use '/subscriptions/{subscription-id}/' for
        subscriptions, '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}' for
        resource groups, and '/subscriptions/{subscription-id}/resourceGroups/{resource-group-
        name}/providers/{resource-provider-namespace}/{resource-type}/{resource-name}' for resources.

        :param policy_assignment_id: The ID of the policy assignment to delete. Use the format
         '/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}'.
        :type policy_assignment_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2015_10_01_preview.models.PolicyAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PolicyAssignment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2015-10-01-preview"

        # Construct URL
        url = self.delete_by_id.metadata['url']  # type: ignore
        path_format_arguments = {
            'policyAssignmentId': self._serialize.url("policy_assignment_id", policy_assignment_id, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    delete_by_id.metadata = {'url': '/{policyAssignmentId}'}  # type: ignore

    async def create_by_id(
        self,
        policy_assignment_id: str,
        parameters: "models.PolicyAssignment",
        **kwargs
    ) -> "models.PolicyAssignment":
        """Creates a policy assignment by ID.

        Policy assignments are inherited by child resources. For example, when you apply a policy to a
        resource group that policy is assigned to all resources in the group. When providing a scope
        for the assignment, use '/subscriptions/{subscription-id}/' for subscriptions,
        '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}' for resource groups,
        and '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-
        provider-namespace}/{resource-type}/{resource-name}' for resources.

        :param policy_assignment_id: The ID of the policy assignment to create. Use the format
         '/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}'.
        :type policy_assignment_id: str
        :param parameters: Parameters for policy assignment.
        :type parameters: ~azure.mgmt.resource.policy.v2015_10_01_preview.models.PolicyAssignment
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2015_10_01_preview.models.PolicyAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PolicyAssignment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2015-10-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_by_id.metadata['url']  # type: ignore
        path_format_arguments = {
            'policyAssignmentId': self._serialize.url("policy_assignment_id", policy_assignment_id, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'PolicyAssignment')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_by_id.metadata = {'url': '/{policyAssignmentId}'}  # type: ignore

    async def get_by_id(
        self,
        policy_assignment_id: str,
        **kwargs
    ) -> "models.PolicyAssignment":
        """Gets a policy assignment by ID.

        When providing a scope for the assignment, use '/subscriptions/{subscription-id}/' for
        subscriptions, '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}' for
        resource groups, and '/subscriptions/{subscription-id}/resourceGroups/{resource-group-
        name}/providers/{resource-provider-namespace}/{resource-type}/{resource-name}' for resources.

        :param policy_assignment_id: The ID of the policy assignment to get. Use the format
         '/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}'.
        :type policy_assignment_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2015_10_01_preview.models.PolicyAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PolicyAssignment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2015-10-01-preview"

        # Construct URL
        url = self.get_by_id.metadata['url']  # type: ignore
        path_format_arguments = {
            'policyAssignmentId': self._serialize.url("policy_assignment_id", policy_assignment_id, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
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

        deserialized = self._deserialize('PolicyAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_by_id.metadata = {'url': '/{policyAssignmentId}'}  # type: ignore
