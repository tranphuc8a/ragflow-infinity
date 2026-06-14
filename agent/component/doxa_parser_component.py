#
#  Copyright 2026 The InfiniFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import logging
import re
from typing import Any

from agent.component.base import ComponentBase, ComponentParamBase
from deepdoc.parser.doxa_parser import DoxaParser


class DoxaParserComponentParam(ComponentParamBase):
    """
    Define the DoXA Parser component parameters.
    
    This component uses DoXA API to parse documents (PDFs, images, etc.)
    and extract structured content for further processing.
    """

    def __init__(self):
        super().__init__()
        # Input parameters
        self.file_path = ""  # Path to the file or variable reference
        self.doxa_token = ""  # DoXA API token (optional, uses env var if not provided)
        self.doxa_url = ""  # DoXA API base URL (optional, uses env var if not provided)
        self.doxa_ipaas_token = ""  # DoXA iPaaS token (optional)
        self.parse_method = "default"  # Parse method for DoXA
        self.language = "Chinese"  # Document language hint
        
        # Input/Output definitions
        self.inputs = {
            "file_path": {
                "type": "str",
                "description": "Path to the file or base64 encoded file data"
            },
            "doxa_token": {
                "type": "str",
                "description": "DoXA API token for authentication"
            },
            "doxa_url": {
                "type": "str",
                "description": "DoXA API base URL"
            },
            "doxa_ipaas_token": {
                "type": "str",
                "description": "DoXA iPaaS gateway token"
            },
            "parse_method": {
                "type": "str",
                "description": "Parsing method to use (default: 'default')"
            },
            "language": {
                "type": "str",
                "description": "Document language for context"
            }
        }
        
        self.outputs = {
            "text_sections": {
                "type": "list",
                "description": "List of extracted text sections"
            },
            "sections_count": {
                "type": "int",
                "description": "Number of sections extracted"
            },
            "raw_output": {
                "type": "dict",
                "description": "Raw DoXA parser output"
            },
            "status": {
                "type": "str",
                "description": "Processing status"
            }
        }

    def check(self):
        """Validate component parameters"""
        self.check_empty(self.file_path, "[DoXA Parser] File path")
        return True


class DoxaParserComponent(ComponentBase):
    """
    DoXA Parser component for the RAGFlow agent builder.
    
    This component integrates the DoXA document parser as a component
    in agent workflows, allowing agents to parse documents with DoXA API.
    
    Features:
    - Parse PDFs, images, and other document formats
    - Extract structured content
    - Support for language-specific processing
    - Configurable API endpoints and authentication
    """

    component_name = "DoXA Parser"

    def _run(self):
        """Execute the DoXA Parser component"""
        try:
            # Get input parameters
            file_path = self._get_input_value("file_path", self._param.file_path)
            doxa_token = self._get_input_value("doxa_token", self._param.doxa_token)
            doxa_url = self._get_input_value("doxa_url", self._param.doxa_url)
            doxa_ipaas_token = self._get_input_value("doxa_ipaas_token", self._param.doxa_ipaas_token)
            parse_method = self._get_input_value("parse_method", self._param.parse_method)
            language = self._get_input_value("language", self._param.language)

            if not file_path:
                self.set_output("status", "error")
                self.set_output("error_message", "File path is required")
                return False

            # Initialize DoXA parser
            parser = DoxaParser(
                token=doxa_token,
                doxa_url=doxa_url,
                ipaas_token=doxa_ipaas_token
            )

            # Check installation
            ok, err = parser.check_installation()
            if not ok:
                self.set_output("status", "error")
                self.set_output("error_message", f"DoXA Parser check failed: {err}")
                return False

            # Parse the document
            self._logger.info(f"Parsing document: {file_path}")
            
            sections, tables = parser.parse_pdf(
                filepath=file_path,
                callback=self._progress_callback,
                parse_method=parse_method,
                lang=language
            )

            # Process output
            text_sections = []
            if sections:
                for section in sections:
                    if isinstance(section, tuple):
                        text_sections.append(section[0])
                    else:
                        text_sections.append(str(section))

            # Set outputs
            self.set_output("text_sections", text_sections)
            self.set_output("sections_count", len(text_sections))
            self.set_output("status", "success")
            
            self._logger.info(f"Successfully parsed document. Extracted {len(text_sections)} sections.")
            return True

        except Exception as e:
            self._logger.error(f"Error in DoXA Parser component: {str(e)}")
            self.set_output("status", "error")
            self.set_output("error_message", str(e))
            return False

    def _get_input_value(self, param_name: str, default_value: Any) -> Any:
        """
        Get input value from component inputs or use default.
        
        Args:
            param_name: Name of the parameter
            default_value: Default value if not provided in inputs
            
        Returns:
            The input value or default
        """
        if param_name in self.get_input_elements():
            return self.get_input_elements()[param_name].get("value", default_value)
        return default_value

    def _progress_callback(self, progress: float, message: str):
        """Handle progress updates from DoXA parser"""
        self._logger.debug(f"DoXA Parser progress ({progress * 100:.1f}%): {message}")
        # Could be extended to update workflow progress

    @property
    def _logger(self):
        """Get logger instance"""
        return logging.getLogger(self.__class__.__name__)
