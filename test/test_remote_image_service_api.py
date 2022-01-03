# coding: utf-8

"""
    Emby Server API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import embyapi
from embyapi.api.remote_image_service_api import RemoteImageServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestRemoteImageServiceApi(unittest.TestCase):
    """RemoteImageServiceApi unit test stubs"""

    def setUp(self):
        self.api = RemoteImageServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_images_remote(self):
        """Test case for get_images_remote

        Gets a remote image  # noqa: E501
        """
        pass

    def test_get_items_by_id_remoteimages(self):
        """Test case for get_items_by_id_remoteimages

        Gets available remote images for an item  # noqa: E501
        """
        pass

    def test_get_items_by_id_remoteimages_providers(self):
        """Test case for get_items_by_id_remoteimages_providers

        Gets available remote image providers for an item  # noqa: E501
        """
        pass

    def test_post_items_by_id_remoteimages_download(self):
        """Test case for post_items_by_id_remoteimages_download

        Downloads a remote image for an item  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
