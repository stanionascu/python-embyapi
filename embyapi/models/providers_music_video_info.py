# coding: utf-8

"""
    Emby Server API

    Explore the Emby Server API  # noqa: E501

    OpenAPI spec version: 4.1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProvidersMusicVideoInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'artists': 'list[str]',
        'name': 'str',
        'metadata_language': 'str',
        'metadata_country_code': 'str',
        'provider_ids': 'dict(str, str)',
        'year': 'int',
        'index_number': 'int',
        'parent_index_number': 'int',
        'premiere_date': 'datetime',
        'is_automated': 'bool'
    }

    attribute_map = {
        'artists': 'Artists',
        'name': 'Name',
        'metadata_language': 'MetadataLanguage',
        'metadata_country_code': 'MetadataCountryCode',
        'provider_ids': 'ProviderIds',
        'year': 'Year',
        'index_number': 'IndexNumber',
        'parent_index_number': 'ParentIndexNumber',
        'premiere_date': 'PremiereDate',
        'is_automated': 'IsAutomated'
    }

    def __init__(self, artists=None, name=None, metadata_language=None, metadata_country_code=None, provider_ids=None, year=None, index_number=None, parent_index_number=None, premiere_date=None, is_automated=None):  # noqa: E501
        """ProvidersMusicVideoInfo - a model defined in Swagger"""  # noqa: E501
        self._artists = None
        self._name = None
        self._metadata_language = None
        self._metadata_country_code = None
        self._provider_ids = None
        self._year = None
        self._index_number = None
        self._parent_index_number = None
        self._premiere_date = None
        self._is_automated = None
        self.discriminator = None
        if artists is not None:
            self.artists = artists
        if name is not None:
            self.name = name
        if metadata_language is not None:
            self.metadata_language = metadata_language
        if metadata_country_code is not None:
            self.metadata_country_code = metadata_country_code
        if provider_ids is not None:
            self.provider_ids = provider_ids
        if year is not None:
            self.year = year
        if index_number is not None:
            self.index_number = index_number
        if parent_index_number is not None:
            self.parent_index_number = parent_index_number
        if premiere_date is not None:
            self.premiere_date = premiere_date
        if is_automated is not None:
            self.is_automated = is_automated

    @property
    def artists(self):
        """Gets the artists of this ProvidersMusicVideoInfo.  # noqa: E501


        :return: The artists of this ProvidersMusicVideoInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._artists

    @artists.setter
    def artists(self, artists):
        """Sets the artists of this ProvidersMusicVideoInfo.


        :param artists: The artists of this ProvidersMusicVideoInfo.  # noqa: E501
        :type: list[str]
        """

        self._artists = artists

    @property
    def name(self):
        """Gets the name of this ProvidersMusicVideoInfo.  # noqa: E501


        :return: The name of this ProvidersMusicVideoInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProvidersMusicVideoInfo.


        :param name: The name of this ProvidersMusicVideoInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def metadata_language(self):
        """Gets the metadata_language of this ProvidersMusicVideoInfo.  # noqa: E501


        :return: The metadata_language of this ProvidersMusicVideoInfo.  # noqa: E501
        :rtype: str
        """
        return self._metadata_language

    @metadata_language.setter
    def metadata_language(self, metadata_language):
        """Sets the metadata_language of this ProvidersMusicVideoInfo.


        :param metadata_language: The metadata_language of this ProvidersMusicVideoInfo.  # noqa: E501
        :type: str
        """

        self._metadata_language = metadata_language

    @property
    def metadata_country_code(self):
        """Gets the metadata_country_code of this ProvidersMusicVideoInfo.  # noqa: E501


        :return: The metadata_country_code of this ProvidersMusicVideoInfo.  # noqa: E501
        :rtype: str
        """
        return self._metadata_country_code

    @metadata_country_code.setter
    def metadata_country_code(self, metadata_country_code):
        """Sets the metadata_country_code of this ProvidersMusicVideoInfo.


        :param metadata_country_code: The metadata_country_code of this ProvidersMusicVideoInfo.  # noqa: E501
        :type: str
        """

        self._metadata_country_code = metadata_country_code

    @property
    def provider_ids(self):
        """Gets the provider_ids of this ProvidersMusicVideoInfo.  # noqa: E501


        :return: The provider_ids of this ProvidersMusicVideoInfo.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._provider_ids

    @provider_ids.setter
    def provider_ids(self, provider_ids):
        """Sets the provider_ids of this ProvidersMusicVideoInfo.


        :param provider_ids: The provider_ids of this ProvidersMusicVideoInfo.  # noqa: E501
        :type: dict(str, str)
        """

        self._provider_ids = provider_ids

    @property
    def year(self):
        """Gets the year of this ProvidersMusicVideoInfo.  # noqa: E501


        :return: The year of this ProvidersMusicVideoInfo.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this ProvidersMusicVideoInfo.


        :param year: The year of this ProvidersMusicVideoInfo.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def index_number(self):
        """Gets the index_number of this ProvidersMusicVideoInfo.  # noqa: E501


        :return: The index_number of this ProvidersMusicVideoInfo.  # noqa: E501
        :rtype: int
        """
        return self._index_number

    @index_number.setter
    def index_number(self, index_number):
        """Sets the index_number of this ProvidersMusicVideoInfo.


        :param index_number: The index_number of this ProvidersMusicVideoInfo.  # noqa: E501
        :type: int
        """

        self._index_number = index_number

    @property
    def parent_index_number(self):
        """Gets the parent_index_number of this ProvidersMusicVideoInfo.  # noqa: E501


        :return: The parent_index_number of this ProvidersMusicVideoInfo.  # noqa: E501
        :rtype: int
        """
        return self._parent_index_number

    @parent_index_number.setter
    def parent_index_number(self, parent_index_number):
        """Sets the parent_index_number of this ProvidersMusicVideoInfo.


        :param parent_index_number: The parent_index_number of this ProvidersMusicVideoInfo.  # noqa: E501
        :type: int
        """

        self._parent_index_number = parent_index_number

    @property
    def premiere_date(self):
        """Gets the premiere_date of this ProvidersMusicVideoInfo.  # noqa: E501


        :return: The premiere_date of this ProvidersMusicVideoInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._premiere_date

    @premiere_date.setter
    def premiere_date(self, premiere_date):
        """Sets the premiere_date of this ProvidersMusicVideoInfo.


        :param premiere_date: The premiere_date of this ProvidersMusicVideoInfo.  # noqa: E501
        :type: datetime
        """

        self._premiere_date = premiere_date

    @property
    def is_automated(self):
        """Gets the is_automated of this ProvidersMusicVideoInfo.  # noqa: E501


        :return: The is_automated of this ProvidersMusicVideoInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_automated

    @is_automated.setter
    def is_automated(self, is_automated):
        """Sets the is_automated of this ProvidersMusicVideoInfo.


        :param is_automated: The is_automated of this ProvidersMusicVideoInfo.  # noqa: E501
        :type: bool
        """

        self._is_automated = is_automated

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ProvidersMusicVideoInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProvidersMusicVideoInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
