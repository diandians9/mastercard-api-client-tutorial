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


class CardAccountDataOutbound(object):
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
        'account_number': 'str',
        'expiry_month': 'str',
        'expiry_year': 'str'
    }

    attribute_map = {
        'account_number': 'accountNumber',
        'expiry_month': 'expiryMonth',
        'expiry_year': 'expiryYear'
    }

    def __init__(self, account_number=None, expiry_month=None, expiry_year=None):  # noqa: E501
        """CardAccountDataOutbound - a model defined in OpenAPI"""  # noqa: E501

        self._account_number = None
        self._expiry_month = None
        self._expiry_year = None
        self.discriminator = None

        if account_number is not None:
            self.account_number = account_number
        if expiry_month is not None:
            self.expiry_month = expiry_month
        if expiry_year is not None:
            self.expiry_year = expiry_year

    @property
    def account_number(self):
        """Gets the account_number of this CardAccountDataOutbound.  # noqa: E501

         The account number of the credit or debit card.   __Min Length:9__<br>  __Max Length:19__   # noqa: E501

        :return: The account_number of this CardAccountDataOutbound.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this CardAccountDataOutbound.

         The account number of the credit or debit card.   __Min Length:9__<br>  __Max Length:19__   # noqa: E501

        :param account_number: The account_number of this CardAccountDataOutbound.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def expiry_month(self):
        """Gets the expiry_month of this CardAccountDataOutbound.  # noqa: E501

          The expiry month for the account. Two numeric digits must be supplied.   __Format: MM__<br> __Exact Length:2__   # noqa: E501

        :return: The expiry_month of this CardAccountDataOutbound.  # noqa: E501
        :rtype: str
        """
        return self._expiry_month

    @expiry_month.setter
    def expiry_month(self, expiry_month):
        """Sets the expiry_month of this CardAccountDataOutbound.

          The expiry month for the account. Two numeric digits must be supplied.   __Format: MM__<br> __Exact Length:2__   # noqa: E501

        :param expiry_month: The expiry_month of this CardAccountDataOutbound.  # noqa: E501
        :type: str
        """

        self._expiry_month = expiry_month

    @property
    def expiry_year(self):
        """Gets the expiry_year of this CardAccountDataOutbound.  # noqa: E501

        __(Required as minimum for Tokenization)__  The expiry year for the account. __Format: YY__ <br> __Exact Length:2__   # noqa: E501

        :return: The expiry_year of this CardAccountDataOutbound.  # noqa: E501
        :rtype: str
        """
        return self._expiry_year

    @expiry_year.setter
    def expiry_year(self, expiry_year):
        """Sets the expiry_year of this CardAccountDataOutbound.

        __(Required as minimum for Tokenization)__  The expiry year for the account. __Format: YY__ <br> __Exact Length:2__   # noqa: E501

        :param expiry_year: The expiry_year of this CardAccountDataOutbound.  # noqa: E501
        :type: str
        """

        self._expiry_year = expiry_year

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
        if not isinstance(other, CardAccountDataOutbound):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other