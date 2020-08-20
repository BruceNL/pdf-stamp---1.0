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

from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.hyperlink_component import HyperlinkComponent


class TestHyperlinkComponent(unittest.TestCase):
    """ HyperlinkComponent unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHyperlinkComponent(self):
        """
        Test HyperlinkComponent
        """
        model = swagger_client.models.hyperlink_component.HyperlinkComponent()


if __name__ == '__main__':
    unittest.main()
