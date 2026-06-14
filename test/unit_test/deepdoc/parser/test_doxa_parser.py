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

import importlib.util
import os
from unittest import mock

import pytest


def _find_project_root(marker="pyproject.toml"):
    cur = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.exists(os.path.join(cur, marker)):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            raise FileNotFoundError(f"Could not locate project root (missing {marker})")
        cur = parent


_MODULE_PATH = os.path.join(_find_project_root(), "deepdoc", "parser", "doxa_parser.py")
_spec = importlib.util.spec_from_file_location("doxa_parser", _MODULE_PATH)
if _spec is None or _spec.loader is None:
    raise RuntimeError("Failed to load deepdoc/parser/doxa_parser.py")
doxa_parser_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(doxa_parser_module)
DoxaParser = doxa_parser_module.DoxaParser


class _FakeDoxaSDKParser:
    def __init__(self, token, doxa_url, ipaas_token):
        self.token = token
        self.doxa_url = doxa_url
        self.ipaas_token = ipaas_token

    def parse_document_with_rag_postprocess(self, input_path):
        assert isinstance(input_path, str)
        return {
            "parsed_document_page_content": [
                {"text": "  First section  "},
                {"content": "Second section"},
            ]
        }


def test_check_installation_requires_token_and_url(monkeypatch):
    monkeypatch.setattr(doxa_parser_module, "_DoxaParser", object)
    parser = DoxaParser(token="", doxa_url="")

    ok, err = parser.check_installation()

    assert ok is False
    assert "DoXA token is required" in err


def test_check_installation_requires_url(monkeypatch):
    monkeypatch.setattr(doxa_parser_module, "_DoxaParser", object)
    parser = DoxaParser(token="tok", doxa_url="")

    ok, err = parser.check_installation()

    assert ok is False
    assert "DoXA URL is required" in err


def test_parse_pdf_normalizes_rag_output(monkeypatch):
    monkeypatch.setattr(doxa_parser_module, "_DoxaParser", _FakeDoxaSDKParser)
    parser = DoxaParser(token="tok", doxa_url="https://doxa.local")
    cb = mock.Mock()

    sections, tables = parser.parse_pdf(filepath="sample.pdf", binary=b"%PDF-1.4", callback=cb)

    assert sections == [("First section", ""), ("Second section", "")]
    assert tables == []
    assert cb.call_count == 2


def test_normalize_lines_fallback_from_nested_result():
    result = {
        "foo": {
            "bar": [
                {"markdown": "# Heading"},
                {"raw_text": "Paragraph"},
            ]
        }
    }

    lines = DoxaParser._normalize_lines(result)

    assert lines == [("# Heading", ""), ("Paragraph", "")]


def test_parse_pdf_raises_when_sdk_not_available(monkeypatch):
    monkeypatch.setattr(doxa_parser_module, "_DoxaParser", None)
    parser = DoxaParser(token="tok", doxa_url="https://doxa.local")

    with pytest.raises(RuntimeError, match="DoXA SDK not installed"):
        parser.parse_pdf(filepath="sample.pdf")
