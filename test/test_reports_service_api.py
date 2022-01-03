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
from embyapi.api.reports_service_api import ReportsServiceApi  # noqa: E501
from embyapi.rest import ApiException


class TestReportsServiceApi(unittest.TestCase):
    """ReportsServiceApi unit test stubs"""

    def setUp(self):
        self.api = ReportsServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_reports_activities(self):
        """Test case for get_reports_activities

        Gets activities entries  # noqa: E501
        """
        pass

    def test_get_reports_headers(self):
        """Test case for get_reports_headers

        Gets reports headers based on library items  # noqa: E501
        """
        pass

    def test_get_reports_items(self):
        """Test case for get_reports_items

        Gets reports based on library items  # noqa: E501
        """
        pass

    def test_get_reports_items_download(self):
        """Test case for get_reports_items_download

        Downloads report  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
