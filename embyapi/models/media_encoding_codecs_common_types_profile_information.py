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

class MediaEncodingCodecsCommonTypesProfileInformation(object):
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
        'short_name': 'str',
        'description': 'str',
        'details': 'str',
        'id': 'str'
    }

    attribute_map = {
        'short_name': 'ShortName',
        'description': 'Description',
        'details': 'Details',
        'id': 'Id'
    }

    def __init__(self, short_name=None, description=None, details=None, id=None):  # noqa: E501
        """MediaEncodingCodecsCommonTypesProfileInformation - a model defined in Swagger"""  # noqa: E501
        self._short_name = None
        self._description = None
        self._details = None
        self._id = None
        self.discriminator = None
        if short_name is not None:
            self.short_name = short_name
        if description is not None:
            self.description = description
        if details is not None:
            self.details = details
        if id is not None:
            self.id = id

    @property
    def short_name(self):
        """Gets the short_name of this MediaEncodingCodecsCommonTypesProfileInformation.  # noqa: E501


        :return: The short_name of this MediaEncodingCodecsCommonTypesProfileInformation.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this MediaEncodingCodecsCommonTypesProfileInformation.


        :param short_name: The short_name of this MediaEncodingCodecsCommonTypesProfileInformation.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def description(self):
        """Gets the description of this MediaEncodingCodecsCommonTypesProfileInformation.  # noqa: E501


        :return: The description of this MediaEncodingCodecsCommonTypesProfileInformation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MediaEncodingCodecsCommonTypesProfileInformation.


        :param description: The description of this MediaEncodingCodecsCommonTypesProfileInformation.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def details(self):
        """Gets the details of this MediaEncodingCodecsCommonTypesProfileInformation.  # noqa: E501


        :return: The details of this MediaEncodingCodecsCommonTypesProfileInformation.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this MediaEncodingCodecsCommonTypesProfileInformation.


        :param details: The details of this MediaEncodingCodecsCommonTypesProfileInformation.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def id(self):
        """Gets the id of this MediaEncodingCodecsCommonTypesProfileInformation.  # noqa: E501


        :return: The id of this MediaEncodingCodecsCommonTypesProfileInformation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MediaEncodingCodecsCommonTypesProfileInformation.


        :param id: The id of this MediaEncodingCodecsCommonTypesProfileInformation.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(MediaEncodingCodecsCommonTypesProfileInformation, dict):
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
        if not isinstance(other, MediaEncodingCodecsCommonTypesProfileInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other