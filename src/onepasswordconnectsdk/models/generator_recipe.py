# coding: utf-8

"""
    1Password Connect

    REST API interface for 1Password Connect.  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: support@1password.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

class GeneratorRecipe(object):
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
        'length': 'int',
        'character_sets': 'list[str]'
    }

    attribute_map = {
        'length': 'length',
        'character_sets': 'characterSets'
    }

    def __init__(self, length=32, character_sets=None, local_vars_configuration=None):  # noqa: E501
        """GeneratorRecipe - a model defined in OpenAPI"""  # noqa: E501

        self._length = None
        self._character_sets = None
        self.discriminator = None

        if length is not None:
            self.length = length
        if character_sets is not None:
            self.character_sets = character_sets

    @property
    def length(self):
        """Gets the length of this GeneratorRecipe.  # noqa: E501

        Length of the generated value  # noqa: E501

        :return: The length of this GeneratorRecipe.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this GeneratorRecipe.

        Length of the generated value  # noqa: E501

        :param length: The length of this GeneratorRecipe.  # noqa: E501
        :type length: int
        """
        if (length is not None and length > 64):  # noqa: E501
            raise ValueError("Invalid value for `length`, must be a value less than or equal to `64`")  # noqa: E501
        if (length is not None and length < 1):  # noqa: E501
            raise ValueError("Invalid value for `length`, must be a value greater than or equal to `1`")  # noqa: E501

        self._length = length

    @property
    def character_sets(self):
        """Gets the character_sets of this GeneratorRecipe.  # noqa: E501


        :return: The character_sets of this GeneratorRecipe.  # noqa: E501
        :rtype: list[str]
        """
        return self._character_sets

    @character_sets.setter
    def character_sets(self, character_sets):
        """Sets the character_sets of this GeneratorRecipe.


        :param character_sets: The character_sets of this GeneratorRecipe.  # noqa: E501
        :type character_sets: list[str]
        """
        allowed_values = ["LETTERS", "DIGITS", "SYMBOLS"]  # noqa: E501
        if (not set(character_sets).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `character_sets` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(character_sets) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._character_sets = character_sets

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GeneratorRecipe):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeneratorRecipe):
            return True

        return self.to_dict() != other.to_dict()