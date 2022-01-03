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
from embyapi.api.item_update_service_api import ItemUpdateServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestItemUpdateServiceApi(unittest.TestCase):
    """ItemUpdateServiceApi unit test stubs"""

    def setUp(self):
        self.api = ItemUpdateServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_items_by_itemid_metadataeditor(self):
        """Test case for get_items_by_itemid_metadataeditor

        Gets metadata editor info for an item  # noqa: E501
        """
        pass

    def test_post_items_by_itemid(self):
        """Test case for post_items_by_itemid

        Updates an item  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()