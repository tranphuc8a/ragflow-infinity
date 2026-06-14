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

import os
import sys
import importlib.util
from unittest import mock
import pytest
import tempfile
from pathlib import Path


def _find_project_root(marker="pyproject.toml"):
    """Find the project root directory"""
    cur = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.exists(os.path.join(cur, marker)):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            raise FileNotFoundError(f"Could not locate project root (missing {marker})")
        cur = parent


_PROJECT_ROOT = _find_project_root()
_COMPONENT_PATH = os.path.join(_PROJECT_ROOT, "agent", "component", "doxa_parser_component.py")

# Load the module dynamically
_spec = importlib.util.spec_from_file_location("doxa_parser_component", _COMPONENT_PATH)
if _spec is None or _spec.loader is None:
    raise RuntimeError("Failed to load agent/component/doxa_parser_component.py")
doxa_component_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(doxa_component_module)

DoxaParserComponent = doxa_component_module.DoxaParserComponent
DoxaParserComponentParam = doxa_component_module.DoxaParserComponentParam


class MockDoxaParser:
    """Mock DoXA parser for testing"""
    
    def __init__(self, token=None, doxa_url=None, ipaas_token=None):
        self.token = token
        self.doxa_url = doxa_url
        self.ipaas_token = ipaas_token
        self.check_called = False
        self.parse_called = False
    
    def check_installation(self):
        self.check_called = True
        if not self.token or not self.doxa_url:
            return False, "Missing credentials"
        return True, ""
    
    def parse_pdf(self, filepath, **kwargs):
        self.parse_called = True
        sections = [
            ("Section 1 content", ""),
            ("Section 2 content", ""),
            ("Section 3 content", ""),
        ]
        tables = []
        return sections, tables


class TestDoxaParserComponentParam:
    """Test DoxaParserComponentParam class"""
    
    def test_initialization(self):
        """Test parameter initialization"""
        param = DoxaParserComponentParam()
        
        assert param.file_path == ""
        assert param.doxa_token == ""
        assert param.doxa_url == ""
        assert param.parse_method == "default"
        assert param.language == "Chinese"
    
    def test_inputs_defined(self):
        """Test that all inputs are properly defined"""
        param = DoxaParserComponentParam()
        
        assert "file_path" in param.inputs
        assert "doxa_token" in param.inputs
        assert "doxa_url" in param.inputs
        assert "doxa_ipaas_token" in param.inputs
        assert "parse_method" in param.inputs
        assert "language" in param.inputs
    
    def test_outputs_defined(self):
        """Test that all outputs are properly defined"""
        param = DoxaParserComponentParam()
        
        assert "text_sections" in param.outputs
        assert "sections_count" in param.outputs
        assert "raw_output" in param.outputs
        assert "status" in param.outputs
    
    def test_check_validates_file_path(self):
        """Test that check() validates file_path"""
        param = DoxaParserComponentParam()
        param.file_path = ""
        
        with pytest.raises(Exception):  # Should raise validation error
            param.check()
    
    def test_check_passes_with_file_path(self):
        """Test that check() passes with file_path set"""
        param = DoxaParserComponentParam()
        param.file_path = "/path/to/file.pdf"
        
        assert param.check() is True


class TestDoxaParserComponent:
    """Test DoxaParserComponent class"""
    
    def test_component_name(self):
        """Test component name"""
        assert DoxaParserComponent.component_name == "DoXA Parser"
    
    def test_initialization(self):
        """Test component initialization"""
        component = DoxaParserComponent()
        assert component is not None
    
    @mock.patch('agent.component.doxa_parser_component.DoxaParser', MockDoxaParser)
    def test_run_success(self, monkeypatch):
        """Test successful parsing"""
        component = DoxaParserComponent()
        component._param = DoxaParserComponentParam()
        component._param.file_path = "test.pdf"
        component._param.doxa_token = "test_token"
        component._param.doxa_url = "http://localhost:8000"
        
        # Mock the input elements
        component.get_input_elements = mock.Mock(return_value={})
        component.set_output = mock.Mock()
        component._progress_callback = mock.Mock()
        
        result = component._run()
        
        assert result is True
        assert component.set_output.call_count > 0
    
    @mock.patch('agent.component.doxa_parser_component.DoxaParser', MockDoxaParser)
    def test_run_missing_file_path(self, monkeypatch):
        """Test error when file_path is missing"""
        component = DoxaParserComponent()
        component._param = DoxaParserComponentParam()
        component._param.file_path = ""
        
        # Mock the input elements
        component.get_input_elements = mock.Mock(return_value={})
        component.set_output = mock.Mock()
        
        result = component._run()
        
        assert result is False
        component.set_output.assert_any_call("status", "error")
    
    @mock.patch('agent.component.doxa_parser_component.DoxaParser')
    def test_run_parser_check_fails(self, mock_parser_class, monkeypatch):
        """Test error when parser check fails"""
        mock_parser = mock.Mock()
        mock_parser.check_installation.return_value = (False, "SDK not installed")
        mock_parser_class.return_value = mock_parser
        
        component = DoxaParserComponent()
        component._param = DoxaParserComponentParam()
        component._param.file_path = "test.pdf"
        component._param.doxa_token = "test_token"
        component._param.doxa_url = "http://localhost:8000"
        
        # Mock the input elements
        component.get_input_elements = mock.Mock(return_value={})
        component.set_output = mock.Mock()
        
        result = component._run()
        
        assert result is False
        component.set_output.assert_any_call("status", "error")
        component.set_output.assert_any_call("error_message", "DoXA Parser check failed: SDK not installed")
    
    @mock.patch('agent.component.doxa_parser_component.DoxaParser', MockDoxaParser)
    def test_run_error_handling(self, monkeypatch):
        """Test error handling"""
        component = DoxaParserComponent()
        component._param = DoxaParserComponentParam()
        component._param.file_path = "test.pdf"
        component._param.doxa_token = "test_token"
        component._param.doxa_url = "http://localhost:8000"
        
        # Mock the input elements
        component.get_input_elements = mock.Mock(return_value={})
        component.set_output = mock.Mock()
        
        # Force an exception
        with mock.patch.object(component, '_get_input_value', side_effect=Exception("Test error")):
            result = component._run()
        
        assert result is False
        component.set_output.assert_any_call("status", "error")


class TestDoxaParserComponentIntegration:
    """Integration tests for DoXA Parser Component"""
    
    def test_component_with_mock_doxa_parser(self):
        """Test component with mock DoXA parser"""
        with mock.patch('agent.component.doxa_parser_component.DoxaParser', MockDoxaParser):
            component = DoxaParserComponent()
            component._param = DoxaParserComponentParam()
            component._param.file_path = "test.pdf"
            component._param.doxa_token = "token123"
            component._param.doxa_url = "http://localhost:8000"
            component._param.language = "English"
            
            # Mock the input elements
            component.get_input_elements = mock.Mock(return_value={})
            outputs = {}
            component.set_output = lambda k, v: outputs.update({k: v})
            
            result = component._run()
            
            assert result is True
            assert outputs.get("status") == "success"
            assert outputs.get("sections_count") == 3
            assert len(outputs.get("text_sections", [])) == 3
    
    def test_parameter_validation(self):
        """Test parameter validation"""
        param = DoxaParserComponentParam()
        
        # Valid parameters
        param.file_path = "/path/to/file.pdf"
        param.parse_method = "default"
        param.language = "Chinese"
        
        assert param.check() is True
        
        # Invalid parameters
        param.file_path = ""
        with pytest.raises(Exception):
            param.check()


class TestDoxaParserComponentOutputs:
    """Test DoXA Parser Component outputs"""
    
    def test_output_structure(self):
        """Test that output structure is correct"""
        param = DoxaParserComponentParam()
        
        expected_outputs = {
            "text_sections": {"type": "list"},
            "sections_count": {"type": "int"},
            "raw_output": {"type": "dict"},
            "status": {"type": "str"},
        }
        
        for output_name, output_spec in expected_outputs.items():
            assert output_name in param.outputs
            assert param.outputs[output_name]["type"] == output_spec["type"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
