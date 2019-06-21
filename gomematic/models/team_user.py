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
        'team': 'Team',
        'user_id': 'str',
        'user': 'User',
        'perm': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'team_id': 'team_id',
        'team': 'team',
        'user_id': 'user_id',
        'user': 'user',
        'perm': 'perm',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, team_id=None, team=None, user_id=None, user=None, perm=None, created_at=None, updated_at=None):  # noqa: E501
        """TeamUser - a model defined in OpenAPI"""  # noqa: E501

        self._team_id = None
        self._team = None
        self._user_id = None
        self._user = None
        self._perm = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.team_id = team_id
        if team is not None:
            self.team = team
        self.user_id = user_id
        if user is not None:
            self.user = user
        self.perm = perm
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

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
    def team(self):
        """Gets the team of this TeamUser.  # noqa: E501


        :return: The team of this TeamUser.  # noqa: E501
        :rtype: Team
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this TeamUser.


        :param team: The team of this TeamUser.  # noqa: E501
        :type: Team
        """

        self._team = team

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
    def user(self):
        """Gets the user of this TeamUser.  # noqa: E501


        :return: The user of this TeamUser.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TeamUser.


        :param user: The user of this TeamUser.  # noqa: E501
        :type: User
        """

        self._user = user

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
        allowed_values = ["user", "admin", "owner"]  # noqa: E501
        if perm not in allowed_values:
            raise ValueError(
                "Invalid value for `perm` ({0}), must be one of {1}"  # noqa: E501
                .format(perm, allowed_values)
            )

        self._perm = perm

    @property
    def created_at(self):
        """Gets the created_at of this TeamUser.  # noqa: E501


        :return: The created_at of this TeamUser.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TeamUser.


        :param created_at: The created_at of this TeamUser.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TeamUser.  # noqa: E501


        :return: The updated_at of this TeamUser.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TeamUser.


        :param updated_at: The updated_at of this TeamUser.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
