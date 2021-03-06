# coding: utf-8

"""
    MDES for Merchants

    The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br> __Authentication__ Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br> 1 . A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br>  __Encryption__<br>  All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br> __Additional Encryption of Sensitive Data__ In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java)   # noqa: E501

    The version of the OpenAPI document: 1.2.9
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class MediaContent(object):
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
        'type': 'str',
        'data': 'str',
        'height': 'str',
        'width': 'str'
    }

    attribute_map = {
        'type': 'type',
        'data': 'data',
        'height': 'height',
        'width': 'width'
    }

    def __init__(self, type=None, data=None, height=None, width=None):  # noqa: E501
        """MediaContent - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._data = None
        self._height = None
        self._width = None
        self.discriminator = None

        self.type = type
        self.data = data
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width

    @property
    def type(self):
        """Gets the type of this MediaContent.  # noqa: E501

        What type of media this is. Specified as a MIME type, which will be one of the following supported types   * applicatoin/pdf (for images must be a vector PDF image) * image/png (includes alpha channel) * text/plain  * text/html  __Max Length:32__    # noqa: E501

        :return: The type of this MediaContent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MediaContent.

        What type of media this is. Specified as a MIME type, which will be one of the following supported types   * applicatoin/pdf (for images must be a vector PDF image) * image/png (includes alpha channel) * text/plain  * text/html  __Max Length:32__    # noqa: E501

        :param type: The type of this MediaContent.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def data(self):
        """Gets the data of this MediaContent.  # noqa: E501

        The data for this item of media. Base64-encoded data, given in the format as specified in ‘type’.   # noqa: E501

        :return: The data of this MediaContent.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this MediaContent.

        The data for this item of media. Base64-encoded data, given in the format as specified in ‘type’.   # noqa: E501

        :param data: The data of this MediaContent.  # noqa: E501
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def height(self):
        """Gets the height of this MediaContent.  # noqa: E501

        For image assets, the height of this image. Specified in pixels.     __Max Length:6__    # noqa: E501

        :return: The height of this MediaContent.  # noqa: E501
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this MediaContent.

        For image assets, the height of this image. Specified in pixels.     __Max Length:6__    # noqa: E501

        :param height: The height of this MediaContent.  # noqa: E501
        :type: str
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this MediaContent.  # noqa: E501

        For image assets, the width of this image. Specified in pixels.        __Max Length:6__    # noqa: E501

        :return: The width of this MediaContent.  # noqa: E501
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this MediaContent.

        For image assets, the width of this image. Specified in pixels.        __Max Length:6__    # noqa: E501

        :param width: The width of this MediaContent.  # noqa: E501
        :type: str
        """

        self._width = width

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
        if not isinstance(other, MediaContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
