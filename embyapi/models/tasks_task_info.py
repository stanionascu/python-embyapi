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

class TasksTaskInfo(object):
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
        'name': 'str',
        'state': 'str',
        'current_progress_percentage': 'float',
        'id': 'str',
        'last_execution_result': 'TasksTaskResult',
        'triggers': 'list[TasksTaskTriggerInfo]',
        'description': 'str',
        'category': 'str',
        'is_hidden': 'bool',
        'key': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'state': 'State',
        'current_progress_percentage': 'CurrentProgressPercentage',
        'id': 'Id',
        'last_execution_result': 'LastExecutionResult',
        'triggers': 'Triggers',
        'description': 'Description',
        'category': 'Category',
        'is_hidden': 'IsHidden',
        'key': 'Key'
    }

    def __init__(self, name=None, state=None, current_progress_percentage=None, id=None, last_execution_result=None, triggers=None, description=None, category=None, is_hidden=None, key=None):  # noqa: E501
        """TasksTaskInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._state = None
        self._current_progress_percentage = None
        self._id = None
        self._last_execution_result = None
        self._triggers = None
        self._description = None
        self._category = None
        self._is_hidden = None
        self._key = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if current_progress_percentage is not None:
            self.current_progress_percentage = current_progress_percentage
        if id is not None:
            self.id = id
        if last_execution_result is not None:
            self.last_execution_result = last_execution_result
        if triggers is not None:
            self.triggers = triggers
        if description is not None:
            self.description = description
        if category is not None:
            self.category = category
        if is_hidden is not None:
            self.is_hidden = is_hidden
        if key is not None:
            self.key = key

    @property
    def name(self):
        """Gets the name of this TasksTaskInfo.  # noqa: E501


        :return: The name of this TasksTaskInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TasksTaskInfo.


        :param name: The name of this TasksTaskInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def state(self):
        """Gets the state of this TasksTaskInfo.  # noqa: E501


        :return: The state of this TasksTaskInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TasksTaskInfo.


        :param state: The state of this TasksTaskInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["Idle", "Cancelling", "Running"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def current_progress_percentage(self):
        """Gets the current_progress_percentage of this TasksTaskInfo.  # noqa: E501


        :return: The current_progress_percentage of this TasksTaskInfo.  # noqa: E501
        :rtype: float
        """
        return self._current_progress_percentage

    @current_progress_percentage.setter
    def current_progress_percentage(self, current_progress_percentage):
        """Sets the current_progress_percentage of this TasksTaskInfo.


        :param current_progress_percentage: The current_progress_percentage of this TasksTaskInfo.  # noqa: E501
        :type: float
        """

        self._current_progress_percentage = current_progress_percentage

    @property
    def id(self):
        """Gets the id of this TasksTaskInfo.  # noqa: E501


        :return: The id of this TasksTaskInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TasksTaskInfo.


        :param id: The id of this TasksTaskInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_execution_result(self):
        """Gets the last_execution_result of this TasksTaskInfo.  # noqa: E501


        :return: The last_execution_result of this TasksTaskInfo.  # noqa: E501
        :rtype: TasksTaskResult
        """
        return self._last_execution_result

    @last_execution_result.setter
    def last_execution_result(self, last_execution_result):
        """Sets the last_execution_result of this TasksTaskInfo.


        :param last_execution_result: The last_execution_result of this TasksTaskInfo.  # noqa: E501
        :type: TasksTaskResult
        """

        self._last_execution_result = last_execution_result

    @property
    def triggers(self):
        """Gets the triggers of this TasksTaskInfo.  # noqa: E501


        :return: The triggers of this TasksTaskInfo.  # noqa: E501
        :rtype: list[TasksTaskTriggerInfo]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this TasksTaskInfo.


        :param triggers: The triggers of this TasksTaskInfo.  # noqa: E501
        :type: list[TasksTaskTriggerInfo]
        """

        self._triggers = triggers

    @property
    def description(self):
        """Gets the description of this TasksTaskInfo.  # noqa: E501


        :return: The description of this TasksTaskInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TasksTaskInfo.


        :param description: The description of this TasksTaskInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def category(self):
        """Gets the category of this TasksTaskInfo.  # noqa: E501


        :return: The category of this TasksTaskInfo.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this TasksTaskInfo.


        :param category: The category of this TasksTaskInfo.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def is_hidden(self):
        """Gets the is_hidden of this TasksTaskInfo.  # noqa: E501


        :return: The is_hidden of this TasksTaskInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this TasksTaskInfo.


        :param is_hidden: The is_hidden of this TasksTaskInfo.  # noqa: E501
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def key(self):
        """Gets the key of this TasksTaskInfo.  # noqa: E501


        :return: The key of this TasksTaskInfo.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TasksTaskInfo.


        :param key: The key of this TasksTaskInfo.  # noqa: E501
        :type: str
        """

        self._key = key

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
        if issubclass(TasksTaskInfo, dict):
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
        if not isinstance(other, TasksTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
