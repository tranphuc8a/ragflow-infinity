# Nghiên cứu Parser trong RAGFlow

Tài liệu này tổng hợp kiến trúc, cơ chế hoạt động và mã nguồn parser trong RAGFlow, tập trung sâu vào `deepdoc`.

## Mục lục

- [01. Kiến trúc tổng thể parser](./01-kien-truc-tong-the.md)
- [02. Danh mục parser và so sánh](./02-danh-muc-parser-va-so-sanh.md)
- [03. Luồng thực thi parser end-to-end](./03-luong-thuc-thi-parser.md)
- [04. Thêm parser mới `doxa_parser`](./04-them-doxa-parser.md)

## Phần trọng tâm: DeepDOC

- [DeepDOC - Tổng quan](./deepdoc/01-deepdoc-overview.md)
- [DeepDOC - PDF parser chi tiết](./deepdoc/02-deepdoc-pdf-parser.md)
- [DeepDOC - Parser các định dạng khác](./deepdoc/03-deepdoc-file-parsers.md)
- [DeepDOC - Điểm mở rộng và tích hợp parser mới](./deepdoc/04-deepdoc-extensibility.md)

---

## Phạm vi mã nguồn đã đọc

Các cụm file chính:

- `deepdoc/parser/*`
- `rag/app/naive.py`
- `rag/svr/task_executor.py`
- `api/utils/api_utils.py`
- `common/constants.py`
- `common/parser_config_utils.py`
- `api/utils/validation_utils.py`
- `web/src/components/layout-recognize-form-field.tsx`
- `web/src/pages/dataset/dataset-setting/*`

---

## Ghi chú

- Tài liệu dùng thuật ngữ "parser" theo 2 lớp:
  - **Parser nghiệp vụ/chunk method** (`parser_id`: naive, qa, table...)
  - **Parser định dạng tài liệu** (PDF/DOCX/Excel/Markdown...) trong `deepdoc/parser`
- Trong thực tế ingest tài liệu, 2 lớp này phối hợp với nhau, không tách rời.
