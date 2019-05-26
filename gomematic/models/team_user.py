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


class TeamUser(object):
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
        'team_id': 'str',
        'user_id': 'str',
        'perm': 'str'
    }

    attribute_map = {
        'team_id': 'team_id',
        'user_id': 'user_id',
        'perm': 'perm'
    }

    def __init__(self, team_id=None, user_id=None, perm=None):  # noqa: E501
        """TeamUser - a model defined in OpenAPI"""  # noqa: E501

        self._team_id = None
        self._user_id = None
        self._perm = None
        self.discriminator = None

        self.team_id = team_id
        self.user_id = user_id
        self.perm = perm

    @property
    def team_id(self):
        """Gets the team_id of this TeamUser.  # noqa: E501


        :return: The team_id of this TeamUser.  # noqa: E501
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this TeamUser.


        :param team_id: The team_id of this TeamUser.  # noqa: E501
        :type: str
        """
        if team_id is None:
            raise ValueError("Invalid value for `team_id`, must not be `None`")  # noqa: E501

        self._team_id = team_id

    @property
    def user_id(self):
        """Gets the user_id of this TeamUser.  # noqa: E501


        :return: The user_id of this TeamUser.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TeamUser.


        :param user_id: The user_id of this TeamUser.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def perm(self):
        """Gets the perm of this TeamUser.  # noqa: E501


        :return: The perm of this TeamUser.  # noqa: E501
        :rtype: str
        """
        return self._perm

    @perm.setter
    def perm(self, perm):
        """Sets the perm of this TeamUser.


        :param perm: The perm of this TeamUser.  # noqa: E501
        :type: str
        """
        if perm is None:
            raise ValueError("Invalid value for `perm`, must not be `None`")  # noqa: E501

        self._perm = perm

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
        if not isinstance(other, TeamUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other