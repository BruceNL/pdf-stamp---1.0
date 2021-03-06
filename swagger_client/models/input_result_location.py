# coding: utf-8

"""
    PDF stamper

    The PDF Stamper API enables the possibility to add both static and dynamic stamps on existing PDFs. The stamps can consist of one or more barcode, hyperlink, image, line or text elements.    The flow is generally as follows:  1. Make a configuration containing the stamp information  2. Create a job specifying the desired configuration  3. Add one or more PDF files to the job  4. Start the job for processing  5. Retrieve the processed files    Full API Documentation: https://docs.sphereon.com/api/pdf-stamper/1.0  Interactive testing: A web based test console is available in the Sphereon API Store at https://store.sphereon.com

    OpenAPI spec version: 1.0
    Contact: dev@sphereon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class InputResultLocation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, result=None, input=None, correlation_id=None):
        """
        InputResultLocation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'result': 'StreamLocation',
            'input': 'StreamLocation',
            'correlation_id': 'str'
        }

        self.attribute_map = {
            'result': 'result',
            'input': 'input',
            'correlation_id': 'correlationId'
        }

        self._result = result
        self._input = input
        self._correlation_id = correlation_id

    @property
    def result(self):
        """
        Gets the result of this InputResultLocation.
        Optional result stream location, otherwise the default job settings will be honored for the results

        :return: The result of this InputResultLocation.
        :rtype: StreamLocation
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this InputResultLocation.
        Optional result stream location, otherwise the default job settings will be honored for the results

        :param result: The result of this InputResultLocation.
        :type: StreamLocation
        """

        self._result = result

    @property
    def input(self):
        """
        Gets the input of this InputResultLocation.
        The input stream location of the pre stamped PDF file

        :return: The input of this InputResultLocation.
        :rtype: StreamLocation
        """
        return self._input

    @input.setter
    def input(self, input):
        """
        Sets the input of this InputResultLocation.
        The input stream location of the pre stamped PDF file

        :param input: The input of this InputResultLocation.
        :type: StreamLocation
        """

        self._input = input

    @property
    def correlation_id(self):
        """
        Gets the correlation_id of this InputResultLocation.
        The id to associate with this input result location pair. Will be created (using a UUID) if not provided

        :return: The correlation_id of this InputResultLocation.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """
        Sets the correlation_id of this InputResultLocation.
        The id to associate with this input result location pair. Will be created (using a UUID) if not provided

        :param correlation_id: The correlation_id of this InputResultLocation.
        :type: str
        """

        self._correlation_id = correlation_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
