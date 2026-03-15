# DeepDOC 03 - Parser định dạng khác trong DeepDOC

## 1) DOCX parser

File: `deepdoc/parser/docx_parser.py`

Class: `RAGFlowDocxParser`

Cơ chế chính:

- Đọc paragraph theo `python-docx`
- Theo dõi page break để lọc theo `from_page/to_page`
- Trích bảng và chuyển thành câu mô tả theo cột/header
- Có xử lý ảnh trong paragraph qua `LazyDocxImage`

Phù hợp: tài liệu văn bản có cấu trúc paragraph + bảng.

---

## 2) Excel/CSV parser

File: `deepdoc/parser/excel_parser.py`

Class: `RAGFlowExcelParser`

Cơ chế chính:

- Tự nhận dạng Excel vs CSV
- Fallback nhiều lớp (`openpyxl` -> `pandas`)
- Có mode xuất HTML bảng (`html(...)`)
- Có hỗ trợ quét ảnh nhúng trong sheet

Phù hợp: dữ liệu dạng bảng, cần chunk theo row/table.

---

## 3) PPT parser

File: `deepdoc/parser/ppt_parser.py`

Class: `RAGFlowPptParser`

Cơ chế:

- Duyệt slide -> shape
- Hỗ trợ text frame, list bullet, table, group shape
- Sắp xếp shape theo toạ độ để giữ reading order tương đối

---

## 4) TXT / HTML / Markdown / JSON parser

### TXT (`txt_parser.py`)

- `parser_txt(...)` tách theo delimiter regex + giới hạn token

### HTML (`html_parser.py`)

- Parse DOM bằng BeautifulSoup
- Loại script/style/comment
- Gom block + table, chunk theo token

### Markdown (`markdown_parser.py`)

- Tách table markdown/html khỏi remainder
- Trích element theo header/list/code/blockquote/text

### JSON (`json_parser.py`)

- Hỗ trợ JSON và JSONL
- Chia nhỏ theo max chunk size nhưng vẫn giữ cấu trúc nested

---

## 5) Parser external OCR/API cho PDF

- `docling_parser.py` -> `DoclingParser`
- `mineru_parser.py` -> `MinerUParser`
- `paddleocr_parser.py` -> `PaddleOCRParser`
- `tcadp_parser.py` -> `TCADPParser`

Điểm chung:

- phần lớn kế thừa/tương thích API với parser PDF để tái dùng crop/position
- yêu cầu môi trường hoặc API key/server riêng
- thường có `check_installation()` để fail-fast

---

## 6) So sánh nhanh nhóm parser định dạng

| Nhóm | Độ giữ cấu trúc | Chi phí chạy | Độ phức tạp |
|---|---|---|---|
| PDF DeepDOC nội bộ | Cao | Trung bình-cao | Cao |
| PDF external OCR | Cao (tuỳ backend) | Trung bình-cao | Trung bình-cao |
| DOCX/PPT | Trung bình-cao | Trung bình | Trung bình |
| Excel/CSV | Cao với bảng | Trung bình | Trung bình |
| TXT/JSON | Trung bình | Thấp | Thấp |
