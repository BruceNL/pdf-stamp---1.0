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

# import models into model package
from .barcode_component import BarcodeComponent
from .blockchain_config import BlockchainConfig
from .blockchain_proof_component import BlockchainProofComponent
from .border import Border
from .canvas_component import CanvasComponent
from .color import Color
from .connector import Connector
from .content_request import ContentRequest
from .content_response import ContentResponse
from .default_job_settings import DefaultJobSettings
from .dimension import Dimension
from .error import Error
from .error_response import ErrorResponse
from .hyperlink_component import HyperlinkComponent
from .image_component import ImageComponent
from .input_result_location import InputResultLocation
from .input_settings import InputSettings
from .lifecycle import Lifecycle
from .line_component import LineComponent
from .pdf_stamper_job_request import PdfStamperJobRequest
from .pdf_stamper_job_result import PdfStamperJobResult
from .point import Point
from .rgb_value import RGBValue
from .result_settings import ResultSettings
from .stamp_component import StampComponent
from .stamper_config import StamperConfig
from .stamper_config_response import StamperConfigResponse
from .storage_location import StorageLocation
from .stream_location import StreamLocation
from .text_component import TextComponent
