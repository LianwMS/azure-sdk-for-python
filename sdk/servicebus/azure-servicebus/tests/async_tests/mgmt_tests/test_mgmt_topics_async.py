#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------
import logging
import pytest
import datetime

import msrest
from azure.servicebus.aio.management import ServiceBusManagementClient
from azure.servicebus.management import TopicDescription
from utilities import get_logger
from azure.core.exceptions import HttpResponseError, ResourceExistsError

from devtools_testutils import AzureMgmtTestCase, CachedResourceGroupPreparer
from servicebus_preparer import (
    CachedServiceBusNamespacePreparer,
    ServiceBusNamespacePreparer
)

from mgmt_test_utilities_async import async_pageable_to_list, clear_topics

_logger = get_logger(logging.DEBUG)


class ServiceBusManagementClientTopicAsyncTests(AzureMgmtTestCase):
    @CachedResourceGroupPreparer(name_prefix='servicebustest')
    @CachedServiceBusNamespacePreparer(name_prefix='servicebustest')
    async def test_async_mgmt_topic_create_by_name(self, servicebus_namespace_connection_string, **kwargs):
        mgmt_service = ServiceBusManagementClient.from_connection_string(servicebus_namespace_connection_string)
        await clear_topics(mgmt_service)
        topic_name = "topic_testaddf"

        try:
            await mgmt_service.create_topic(topic_name)
            topic = await mgmt_service.get_topic(topic_name)
            assert topic.name == topic_name
            assert topic.entity_availability_status == 'Available'
            assert topic.status == 'Active'
        finally:
            await mgmt_service.delete_topic(topic_name)

    @CachedResourceGroupPreparer(name_prefix='servicebustest')
    @CachedServiceBusNamespacePreparer(name_prefix='servicebustest')
    async def test_async_mgmt_topic_create_with_topic_description(self, servicebus_namespace_connection_string, **kwargs):
        mgmt_service = ServiceBusManagementClient.from_connection_string(servicebus_namespace_connection_string)
        await clear_topics(mgmt_service)
        topic_name = "iweidk"
        try:
            await mgmt_service.create_topic(
                TopicDescription(
                    name=topic_name,
                    auto_delete_on_idle=datetime.timedelta(minutes=10),
                    default_message_time_to_live=datetime.timedelta(minutes=11),
                    duplicate_detection_history_time_window=datetime.timedelta(minutes=12),
                    enable_batched_operations=True,
                    enable_express=True,
                    enable_partitioning=True,
                    enable_subscription_partitioning=True,
                    is_anonymous_accessible=True,
                    max_size_in_megabytes=3072
                )
            )
            topic = await mgmt_service.get_topic(topic_name)
            assert topic.name == topic_name
            assert topic.auto_delete_on_idle == datetime.timedelta(minutes=10)
            assert topic.default_message_time_to_live == datetime.timedelta(minutes=11)
            assert topic.duplicate_detection_history_time_window == datetime.timedelta(minutes=12)
            assert topic.enable_batched_operations
            assert topic.enable_express
            assert topic.enable_partitioning
            assert topic.enable_subscription_partitioning
            assert topic.is_anonymous_accessible
            assert topic.max_size_in_megabytes % 3072 == 0
        finally:
            await mgmt_service.delete_topic(topic_name)

    @CachedResourceGroupPreparer(name_prefix='servicebustest')
    @CachedServiceBusNamespacePreparer(name_prefix='servicebustest')
    async def test_async_mgmt_topic_create_duplicate(self, servicebus_namespace_connection_string, **kwargs):
        mgmt_service = ServiceBusManagementClient.from_connection_string(servicebus_namespace_connection_string)
        await clear_topics(mgmt_service)
        topic_name = "dqkodq"
        try:
            await mgmt_service.create_topic(topic_name)
            with pytest.raises(ResourceExistsError):
                await mgmt_service.create_topic(topic_name)
        finally:
            await mgmt_service.delete_topic(topic_name)

    @CachedResourceGroupPreparer(name_prefix='servicebustest')
    @CachedServiceBusNamespacePreparer(name_prefix='servicebustest')
    async def test_async_mgmt_topic_update_success(self, servicebus_namespace_connection_string, **kwargs):
        mgmt_service = ServiceBusManagementClient.from_connection_string(servicebus_namespace_connection_string)
        await clear_topics(mgmt_service)
        topic_name = "fjrui"
        try:
            topic_description = await mgmt_service.create_topic(topic_name)

            # Try updating one setting.
            topic_description.default_message_time_to_live = datetime.timedelta(minutes=2)
            await mgmt_service.update_topic(topic_description)
            topic_description = await mgmt_service.get_topic(topic_name)
            assert topic_description.default_message_time_to_live == datetime.timedelta(minutes=2)

            # Now try updating all settings.
            topic_description.auto_delete_on_idle = datetime.timedelta(minutes=10)
            topic_description.default_message_time_to_live = datetime.timedelta(minutes=11)
            topic_description.duplicate_detection_history_time_window = datetime.timedelta(minutes=12)
            topic_description.enable_batched_operations = True
            topic_description.enable_express = True
            # topic_description.enable_partitioning = True # Cannot be changed after creation
            topic_description.is_anonymous_accessible = True
            topic_description.max_size_in_megabytes = 3072
            # topic_description.requires_duplicate_detection = True # Read only
            # topic_description.requires_session = True # Cannot be changed after creation
            topic_description.support_ordering = True

            await mgmt_service.update_topic(topic_description)
            topic_description = await mgmt_service.get_topic(topic_name)

            assert topic_description.auto_delete_on_idle == datetime.timedelta(minutes=10)
            assert topic_description.default_message_time_to_live == datetime.timedelta(minutes=11)
            assert topic_description.duplicate_detection_history_time_window == datetime.timedelta(minutes=12)
            assert topic_description.enable_batched_operations == True
            assert topic_description.enable_express == True
            # assert topic_description.enable_partitioning == True
            assert topic_description.is_anonymous_accessible == True
            assert topic_description.max_size_in_megabytes == 3072
            # assert topic_description.requires_duplicate_detection == True
            # assert topic_description.requires_session == True
            assert topic_description.support_ordering == True
        finally:
            await mgmt_service.delete_topic(topic_name)

    @CachedResourceGroupPreparer(name_prefix='servicebustest')
    @CachedServiceBusNamespacePreparer(name_prefix='servicebustest')
    async def test_async_mgmt_topic_update_invalid(self, servicebus_namespace_connection_string, **kwargs):
        mgmt_service = ServiceBusManagementClient.from_connection_string(servicebus_namespace_connection_string)
        await clear_topics(mgmt_service)
        topic_name = "dfjfj"
        try:
            topic_description = await mgmt_service.create_topic(topic_name)

            # handle a null update properly.
            with pytest.raises(AttributeError):
                await mgmt_service.update_topic(None)

            # handle an invalid type update properly.
            with pytest.raises(AttributeError):
                await mgmt_service.update_topic(Exception("test"))

            # change the name to a topic that doesn't exist; should fail.
            topic_description.name = "iewdm"
            with pytest.raises(HttpResponseError):
                await mgmt_service.update_topic(topic_description)
            topic_description.name = topic_name

            # change the name to a topic with an invalid name exist; should fail.
            topic_description.name = ''
            with pytest.raises(msrest.exceptions.ValidationError):
                await mgmt_service.update_topic(topic_description)
            topic_description.name = topic_name

            # change to a setting with an invalid value; should still fail.
            topic_description.duplicate_detection_history_time_window = datetime.timedelta(days=25)
            with pytest.raises(HttpResponseError):
                await mgmt_service.update_topic(topic_description)
            topic_description.duplicate_detection_history_time_window = datetime.timedelta(minutes=5)
        finally:
            await mgmt_service.delete_topic(topic_name)

    @CachedResourceGroupPreparer(name_prefix='servicebustest')
    @CachedServiceBusNamespacePreparer(name_prefix='servicebustest')
    async def test_async_mgmt_topic_delete(self, servicebus_namespace_connection_string):
        mgmt_service = ServiceBusManagementClient.from_connection_string(servicebus_namespace_connection_string)
        await clear_topics(mgmt_service)
        await mgmt_service.create_topic('test_topic')
        topics = await async_pageable_to_list(mgmt_service.list_topics())
        assert len(topics) == 1

        await mgmt_service.create_topic('txt/.-_123')
        topics = await async_pageable_to_list(mgmt_service.list_topics())
        assert len(topics) == 2

        description = await mgmt_service.get_topic('test_topic')
        await mgmt_service.delete_topic(description)

        topics = await async_pageable_to_list(mgmt_service.list_topics())
        assert len(topics) == 1 and topics[0].name == 'txt/.-_123'

        description = await mgmt_service.get_topic('txt/.-_123')
        await mgmt_service.delete_topic(description)

        topics = await async_pageable_to_list(mgmt_service.list_topics())
        assert len(topics) == 0

    @CachedResourceGroupPreparer(name_prefix='servicebustest')
    @CachedServiceBusNamespacePreparer(name_prefix='servicebustest')
    async def test_async_mgmt_topic_list(self, servicebus_namespace_connection_string, **kwargs):
        mgmt_service = ServiceBusManagementClient.from_connection_string(servicebus_namespace_connection_string)
        await clear_topics(mgmt_service)
        topics = await async_pageable_to_list(mgmt_service.list_topics())
        assert len(topics) == 0
        await mgmt_service.create_topic("test_topic_1")
        await mgmt_service.create_topic("test_topic_2")
        topics = await async_pageable_to_list(mgmt_service.list_topics())
        assert len(topics) == 2
        assert topics[0].name == "test_topic_1"
        assert topics[1].name == "test_topic_2"
        await mgmt_service.delete_topic("test_topic_1")
        await mgmt_service.delete_topic("test_topic_2")
        topics = await async_pageable_to_list(mgmt_service.list_topics())
        assert len(topics) == 0

    @CachedResourceGroupPreparer(name_prefix='servicebustest')
    @CachedServiceBusNamespacePreparer(name_prefix='servicebustest')
    async def test_async_mgmt_topic_list_runtime_info(self, servicebus_namespace_connection_string, **kwargs):
        mgmt_service = ServiceBusManagementClient.from_connection_string(servicebus_namespace_connection_string)
        await clear_topics(mgmt_service)
        topics = await async_pageable_to_list(mgmt_service.list_topics())
        topics_infos = await async_pageable_to_list(mgmt_service.list_topics_runtime_info())

        assert len(topics) == len(topics_infos) == 0

        await mgmt_service.create_topic("test_topic")

        topics = await async_pageable_to_list(mgmt_service.list_topics())
        topics_infos = await async_pageable_to_list(mgmt_service.list_topics_runtime_info())

        assert len(topics) == 1 and len(topics_infos) == 1

        assert topics[0].name == topics_infos[0].name == "test_topic"

        info = topics_infos[0]

        assert info.accessed_at is not None
        assert info.updated_at is not None
        assert info.subscription_count is 0

        assert info.message_count_details
        assert info.message_count_details.active_message_count == 0
        assert info.message_count_details.dead_letter_message_count == 0
        assert info.message_count_details.transfer_dead_letter_message_count == 0
        assert info.message_count_details.transfer_message_count == 0
        assert info.message_count_details.scheduled_message_count == 0

        await mgmt_service.delete_topic("test_topic")
        topics_infos = await async_pageable_to_list(mgmt_service.list_topics_runtime_info())
        assert len(topics_infos) == 0

    @CachedResourceGroupPreparer(name_prefix='servicebustest')
    @CachedServiceBusNamespacePreparer(name_prefix='servicebustest')
    async def test_async_mgmt_topic_get_runtime_info_basic(self, servicebus_namespace_connection_string):
        mgmt_service = ServiceBusManagementClient.from_connection_string(servicebus_namespace_connection_string)
        await clear_topics(mgmt_service)
        await mgmt_service.create_topic("test_topic")
        try:
            topic_runtime_info = await mgmt_service.get_topic_runtime_info("test_topic")

            assert topic_runtime_info
            assert topic_runtime_info.name == "test_topic"
            assert topic_runtime_info.created_at is not None
            assert topic_runtime_info.accessed_at is not None
            assert topic_runtime_info.updated_at is not None
            assert topic_runtime_info.subscription_count is 0

            assert topic_runtime_info.message_count_details
            assert topic_runtime_info.message_count_details.active_message_count == 0
            assert topic_runtime_info.message_count_details.dead_letter_message_count == 0
            assert topic_runtime_info.message_count_details.transfer_dead_letter_message_count == 0
            assert topic_runtime_info.message_count_details.transfer_message_count == 0
            assert topic_runtime_info.message_count_details.scheduled_message_count == 0
        finally:
            await mgmt_service.delete_topic("test_topic")
