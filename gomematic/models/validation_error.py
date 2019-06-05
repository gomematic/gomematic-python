# coding: utf-8

"""
    Gomematic OpenAPI

    API definition for Gomematic  # noqa: E501

    The version of the OpenAPI document: 1.0.0-alpha1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ValidationError(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'status': 'int',
        'message': 'str',
        'errors': 'list[ValidationErrorErrors]'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'errors': 'errors'
    }

    def __init__(self, status=None, message=None, errors=None):  # noqa: E501
        """ValidationError - a model defined in OpenAPI"""  # noqa: E501

        self._status = None
        self._message = None
        self._errors = None
        self.discriminator = None

        self.status = status
        self.message = message
        if errors is not None:
            self.errors = errors

    @property
    def status(self):
        """Gets the status of this ValidationError.  # noqa: E501


        :return: The status of this ValidationError.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ValidationError.


        :param status: The status of this ValidationError.  # noqa: E501
        :type: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def message(self):
        """Gets the message of this ValidationError.  # noqa: E501


        :return: The message of this ValidationError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ValidationError.


        :param message: The message of this ValidationError.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def errors(self):
        """Gets the errors of this ValidationError.  # noqa: E501


        :return: The errors of this ValidationError.  # noqa: E501
        :rtype: list[ValidationErrorErrors]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ValidationError.


        :param errors: The errors of this ValidationError.  # noqa: E501
        :type: list[ValidationErrorErrors]
        """

        self._errors = errors

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ValidationError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
