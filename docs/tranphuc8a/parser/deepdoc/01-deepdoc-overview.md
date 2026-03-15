# DeepDOC 01 - Tổng quan

## 1) DeepDOC là gì trong RAGFlow?

`deepdoc` là lớp parser định dạng tài liệu, chịu trách nhiệm chuyển tài liệu thô thành dữ liệu có cấu trúc để chunk/index.

Thành phần chính:

- `deepdoc/vision/*`: OCR, layout recognition, table structure recognition
- `deepdoc/parser/*`: parser theo định dạng và parser mở rộng OCR/API

---

## 2) Vai trò của `deepdoc/parser/__init__.py`

File này export parser chuẩn dùng phổ biến:

- `PdfParser` (`RAGFlowPdfParser`)
- `PlainParser`
- `DocxParser`
- `ExcelParser`
- `PptParser`
- `HtmlParser`
- `JsonParser`
- `MarkdownParser`
- `TxtParser`

Đây là API nhập khẩu gọn cho lớp ứng dụng (`rag/app/*`).

---

## 3) Đầu ra chuẩn của parser DeepDOC

Tuỳ định dạng nhưng thường có:

1. `sections`: danh sách đoạn text (thường kèm position tag với PDF)
2. `tables`: dữ liệu bảng, có thể kèm ảnh/caption/ngữ cảnh
3. metadata phụ trợ (trong một số parser external)

Với PDF, vị trí thường được biểu diễn bằng tag dạng:

`@@page\tleft\tright\ttop\tbottom##`

---

## 4) Sơ đồ module DeepDOC

```mermaid
flowchart LR
  subgraph PARSER["deepdoc/parser"]
    PDF["pdf_parser.py"]
    DOCX["docx_parser.py"]
    XLSX["excel_parser.py"]
    PPT["ppt_parser.py"]
    TXT["txt_parser.py"]
    HTML["html_parser.py"]
    JSON["json_parser.py"]
    MD["markdown_parser.py"]
    DOCLING["docling_parser.py"]
    MINERU["mineru_parser.py"]
    PADDLE["paddleocr_parser.py"]
    TCADP["tcadp_parser.py"]
  end

  subgraph VISION["deepdoc/vision"]
    OCR[OCR]
    LAYOUT[LayoutRecognizer]
    TSR[TableStructureRecognizer]
  end

  PDF --> OCR
  PDF --> LAYOUT
  PDF --> TSR

  DOCLING --> PDF
  MINERU --> PDF
  PADDLE --> PDF
  TCADP --> PDF
```

---

## 5) Điểm mạnh / hạn chế của DeepDOC

### Điểm mạnh

- Tích hợp chặt với pipeline chunk của RAGFlow
- Hỗ trợ nhiều định dạng tài liệu
- PDF parser có cơ chế OCR fallback cho text lỗi mã hóa font

### Hạn chế

- PDF parser nội bộ khá phức tạp, khó bảo trì nếu không nắm pipeline
- Một số parser external phụ thuộc hạ tầng ngoài (API/server/model)
