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


class CanvasComponent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, border=None, specific_pages=None, connectors=None, page_selector=None, offset=None, page_operation=None, position=None):
        """
        CanvasComponent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'border': 'Border',
            'specific_pages': 'list[int]',
            'connectors': 'list[Connector]',
            'page_selector': 'str',
            'offset': 'Point',
            'page_operation': 'str',
            'position': 'str'
        }

        self.attribute_map = {
            'border': 'border',
            'specific_pages': 'specificPages',
            'connectors': 'connectors',
            'page_selector': 'pageSelector',
            'offset': 'offset',
            'page_operation': 'pageOperation',
            'position': 'position'
        }

        self._border = border
        self._specific_pages = specific_pages
        self._connectors = connectors
        self._page_selector = page_selector
        self._offset = offset
        self._page_operation = page_operation
        self._position = position

    @property
    def border(self):
        """
        Gets the border of this CanvasComponent.
        The border of the component

        :return: The border of this CanvasComponent.
        :rtype: Border
        """
        return self._border

    @border.setter
    def border(self, border):
        """
        Sets the border of this CanvasComponent.
        The border of the component

        :param border: The border of this CanvasComponent.
        :type: Border
        """

        self._border = border

    @property
    def specific_pages(self):
        """
        Gets the specific_pages of this CanvasComponent.


        :return: The specific_pages of this CanvasComponent.
        :rtype: list[int]
        """
        return self._specific_pages

    @specific_pages.setter
    def specific_pages(self, specific_pages):
        """
        Sets the specific_pages of this CanvasComponent.


        :param specific_pages: The specific_pages of this CanvasComponent.
        :type: list[int]
        """

        self._specific_pages = specific_pages

    @property
    def connectors(self):
        """
        Gets the connectors of this CanvasComponent.
        Connectors containing components that can be positioned relative to this component

        :return: The connectors of this CanvasComponent.
        :rtype: list[Connector]
        """
        return self._connectors

    @connectors.setter
    def connectors(self, connectors):
        """
        Sets the connectors of this CanvasComponent.
        Connectors containing components that can be positioned relative to this component

        :param connectors: The connectors of this CanvasComponent.
        :type: list[Connector]
        """

        self._connectors = connectors

    @property
    def page_selector(self):
        """
        Gets the page_selector of this CanvasComponent.
        Prescribes the page(s) the component needs to be overlay-ed on.

        :return: The page_selector of this CanvasComponent.
        :rtype: str
        """
        return self._page_selector

    @page_selector.setter
    def page_selector(self, page_selector):
        """
        Sets the page_selector of this CanvasComponent.
        Prescribes the page(s) the component needs to be overlay-ed on.

        :param page_selector: The page_selector of this CanvasComponent.
        :type: str
        """
        allowed_values = ["FIRST_PAGE", "LAST_PAGE", "EVEN_PAGES", "ODD_PAGES", "ALL_PAGES", "SPECIFIC_PAGES"]
        if page_selector not in allowed_values:
            raise ValueError(
                "Invalid value for `page_selector` ({0}), must be one of {1}"
                .format(page_selector, allowed_values)
            )

        self._page_selector = page_selector

    @property
    def offset(self):
        """
        Gets the offset of this CanvasComponent.
        The offset of the component relative to the parent component

        :return: The offset of this CanvasComponent.
        :rtype: Point
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this CanvasComponent.
        The offset of the component relative to the parent component

        :param offset: The offset of this CanvasComponent.
        :type: Point
        """

        self._offset = offset

    @property
    def page_operation(self):
        """
        Gets the page_operation of this CanvasComponent.
        The operation that should be executed with the stamp component

        :return: The page_operation of this CanvasComponent.
        :rtype: str
        """
        return self._page_operation

    @page_operation.setter
    def page_operation(self, page_operation):
        """
        Sets the page_operation of this CanvasComponent.
        The operation that should be executed with the stamp component

        :param page_operation: The page_operation of this CanvasComponent.
        :type: str
        """
        allowed_values = ["STAMP"]
        if page_operation not in allowed_values:
            raise ValueError(
                "Invalid value for `page_operation` ({0}), must be one of {1}"
                .format(page_operation, allowed_values)
            )

        self._page_operation = page_operation

    @property
    def position(self):
        """
        Gets the position of this CanvasComponent.
        The position where the stamp end up relative to existing content. Only foreground is supported for now

        :return: The position of this CanvasComponent.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this CanvasComponent.
        The position where the stamp end up relative to existing content. Only foreground is supported for now

        :param position: The position of this CanvasComponent.
        :type: str
        """
        allowed_values = ["FOREGROUND", "BACKGROUND"]
        if position not in allowed_values:
            raise ValueError(
                "Invalid value for `position` ({0}), must be one of {1}"
                .format(position, allowed_values)
            )

        self._position = position

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
