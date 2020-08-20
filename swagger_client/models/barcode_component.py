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


class BarcodeComponent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, border=None, connectors=None, offset=None, error_correction_level=None, barcode_format=None, width=None, content=None, height=None, qr_version=None):
        """
        BarcodeComponent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'border': 'Border',
            'connectors': 'list[Connector]',
            'offset': 'Point',
            'error_correction_level': 'str',
            'barcode_format': 'str',
            'width': 'int',
            'content': 'str',
            'height': 'int',
            'qr_version': 'int'
        }

        self.attribute_map = {
            'border': 'border',
            'connectors': 'connectors',
            'offset': 'offset',
            'error_correction_level': 'errorCorrectionLevel',
            'barcode_format': 'barcodeFormat',
            'width': 'width',
            'content': 'content',
            'height': 'height',
            'qr_version': 'qrVersion'
        }

        self._border = border
        self._connectors = connectors
        self._offset = offset
        self._error_correction_level = error_correction_level
        self._barcode_format = barcode_format
        self._width = width
        self._content = content
        self._height = height
        self._qr_version = qr_version

    @property
    def border(self):
        """
        Gets the border of this BarcodeComponent.
        The border of the component

        :return: The border of this BarcodeComponent.
        :rtype: Border
        """
        return self._border

    @border.setter
    def border(self, border):
        """
        Sets the border of this BarcodeComponent.
        The border of the component

        :param border: The border of this BarcodeComponent.
        :type: Border
        """

        self._border = border

    @property
    def connectors(self):
        """
        Gets the connectors of this BarcodeComponent.
        Connectors containing components that can be positioned relative to this component

        :return: The connectors of this BarcodeComponent.
        :rtype: list[Connector]
        """
        return self._connectors

    @connectors.setter
    def connectors(self, connectors):
        """
        Sets the connectors of this BarcodeComponent.
        Connectors containing components that can be positioned relative to this component

        :param connectors: The connectors of this BarcodeComponent.
        :type: list[Connector]
        """

        self._connectors = connectors

    @property
    def offset(self):
        """
        Gets the offset of this BarcodeComponent.
        The offset of the component relative to the parent component

        :return: The offset of this BarcodeComponent.
        :rtype: Point
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this BarcodeComponent.
        The offset of the component relative to the parent component

        :param offset: The offset of this BarcodeComponent.
        :type: Point
        """

        self._offset = offset

    @property
    def error_correction_level(self):
        """
        Gets the error_correction_level of this BarcodeComponent.
        Specifies what degree of error correction to use, for example in QR Codes, See ISO 18004:2006, 6.5.1. This enum encapsulates the four error correction levels defined by the QR code standard

        :return: The error_correction_level of this BarcodeComponent.
        :rtype: str
        """
        return self._error_correction_level

    @error_correction_level.setter
    def error_correction_level(self, error_correction_level):
        """
        Sets the error_correction_level of this BarcodeComponent.
        Specifies what degree of error correction to use, for example in QR Codes, See ISO 18004:2006, 6.5.1. This enum encapsulates the four error correction levels defined by the QR code standard

        :param error_correction_level: The error_correction_level of this BarcodeComponent.
        :type: str
        """
        allowed_values = ["QR_L", "QR_M", "QR_Q", "QR_H"]
        if error_correction_level not in allowed_values:
            raise ValueError(
                "Invalid value for `error_correction_level` ({0}), must be one of {1}"
                .format(error_correction_level, allowed_values)
            )

        self._error_correction_level = error_correction_level

    @property
    def barcode_format(self):
        """
        Gets the barcode_format of this BarcodeComponent.
        The barcode format to generate

        :return: The barcode_format of this BarcodeComponent.
        :rtype: str
        """
        return self._barcode_format

    @barcode_format.setter
    def barcode_format(self, barcode_format):
        """
        Sets the barcode_format of this BarcodeComponent.
        The barcode format to generate

        :param barcode_format: The barcode_format of this BarcodeComponent.
        :type: str
        """
        allowed_values = ["AZTEC", "CODABAR", "CODE_39", "CODE_93", "CODE_128", "DATA_MATRIX", "EAN_8", "EAN_13", "ITF", "MAXICODE", "PDF_417", "QR_CODE", "RSS_14", "RSS_EXPANDED", "UPC_A", "UPC_E", "UPC_EAN_EXTENSION"]
        if barcode_format not in allowed_values:
            raise ValueError(
                "Invalid value for `barcode_format` ({0}), must be one of {1}"
                .format(barcode_format, allowed_values)
            )

        self._barcode_format = barcode_format

    @property
    def width(self):
        """
        Gets the width of this BarcodeComponent.
        The preferred width in pixels

        :return: The width of this BarcodeComponent.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this BarcodeComponent.
        The preferred width in pixels

        :param width: The width of this BarcodeComponent.
        :type: int
        """

        self._width = width

    @property
    def content(self):
        """
        Gets the content of this BarcodeComponent.
        The contents to encode in the barcode

        :return: The content of this BarcodeComponent.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this BarcodeComponent.
        The contents to encode in the barcode

        :param content: The content of this BarcodeComponent.
        :type: str
        """

        self._content = content

    @property
    def height(self):
        """
        Gets the height of this BarcodeComponent.
        The preferred height in pixels

        :return: The height of this BarcodeComponent.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this BarcodeComponent.
        The preferred height in pixels

        :param height: The height of this BarcodeComponent.
        :type: int
        """

        self._height = height

    @property
    def qr_version(self):
        """
        Gets the qr_version of this BarcodeComponent.


        :return: The qr_version of this BarcodeComponent.
        :rtype: int
        """
        return self._qr_version

    @qr_version.setter
    def qr_version(self, qr_version):
        """
        Sets the qr_version of this BarcodeComponent.


        :param qr_version: The qr_version of this BarcodeComponent.
        :type: int
        """

        self._qr_version = qr_version

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