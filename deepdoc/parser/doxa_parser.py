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

from __future__ import annotations

import logging
import os
import tempfile
from pathlib import Path
from typing import Any

try:
    from doxa.parser import DoxaParser as _DoxaParser
except Exception:
    _DoxaParser = None


class DoxaParser:
    def __init__(
        self,
        token: str | None = None,
        doxa_url: str | None = None,
        ipaas_token: str | None = None,
    ):
        self.logger = logging.getLogger(self.__class__.__name__)
        self._token = token or os.environ.get("DOXA_API_TOKEN", "")
        self._doxa_url = doxa_url or os.environ.get("DOXA_API_BASE", "")
        self._ipaas_token = ipaas_token or os.environ.get("DOXA_IPAAS_TOKEN", "")

    def check_installation(self) -> tuple[bool, str]:
        if _DoxaParser is None:
            return False, "DoXA SDK not installed. Please install doxa-sdk."
        if not self._token:
            return False, "DoXA token is required. Set DOXA_API_TOKEN or parser config token."
        if not self._doxa_url:
            return False, "DoXA URL is required. Set DOXA_API_BASE or parser config doxa_url."
        return True, ""

    @staticmethod
    def extract_positions(_: str) -> list[tuple[list[int], float, float, float, float]]:
        return []

    @staticmethod
    def crop(_: str, __: int = 1, need_position: bool = False):
        return (None, None) if need_position else None

    @staticmethod
    def _normalize_lines(result: Any) -> list[tuple[str, str]]:
        lines: list[tuple[str, str]] = []
        if not isinstance(result, dict):
            return lines

        page_content = result.get("parsed_document_page_content")

        def _append_text(txt: Any):
            if not isinstance(txt, str):
                return
            t = txt.strip()
            if t:
                lines.append((t, ""))

        def _from_any(item: Any):
            if isinstance(item, str):
                _append_text(item)
                return

            if isinstance(item, dict):
                for k in ("text", "content", "page_content", "markdown", "raw_text"):
                    if isinstance(item.get(k), str):
                        _append_text(item[k])
                        return
                for v in item.values():
                    _from_any(v)
                return

            if isinstance(item, list):
                for x in item:
                    _from_any(x)

        _from_any(page_content)

        if not lines:
            _from_any(result)

        return lines

    def parse_pdf(
        self,
        filepath: str,
        binary: bytes | None = None,
        callback=None,
        parse_method: str = "default",
        lang: str | None = None,
        doxa_options: dict[str, Any] | None = None,
        **kwargs,
    ):
        ok, err = self.check_installation()
        if not ok:
            raise RuntimeError(err)

        parser = _DoxaParser(token=self._token, doxa_url=self._doxa_url, ipaas_token=self._ipaas_token)

        source_path = filepath
        temp_file = None
        try:
            if binary is not None:
                suffix = Path(filepath).suffix or ".pdf"
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
                temp_file.write(binary)
                temp_file.flush()
                source_path = temp_file.name

            if callback:
                callback(0.2, "DoXA parser is processing the document.")

            # Prefer DoXA postprocess API because output is already shaped for downstream RAG use.
            result = parser.parse_document_with_rag_postprocess(input_path=source_path)
            lines = self._normalize_lines(result)

            if callback:
                callback(0.6, f"DoXA parser extracted {len(lines)} sections.")

            return lines, []
        finally:
            if temp_file is not None:
                try:
                    temp_file.close()
                    os.unlink(temp_file.name)
                except Exception:
                    self.logger.warning("Failed to clean temporary file for DoXA parser.")
