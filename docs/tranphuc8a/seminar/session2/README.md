# Session 2 - File Ingest Pipeline và Parsing Mechanism

## Mục tiêu buổi học

Sau buổi này, người học có thể:
- Mô tả chi tiết ingest pipeline trong RAGFlow theo code path thực tế.
- Hiểu rõ vai trò parser trong chất lượng retrieval downstream.
- Phân biệt hai lớp parser: parser nghiệp vụ (chunk method) và parser định dạng tài liệu (DeepDoc).
- Giải thích cơ chế OCR/layout/TSR và ảnh hưởng của chúng lên chunk quality.

## Lộ trình nội dung chi tiết

1. `01-ingest-overview.md`  
  Tổng quan ingest pipeline trong hệ RAG production.
2. `02-parser-role-and-taxonomy.md`  
  Vai trò parser và phân loại parser trong RAGFlow.
3. `03-deepdoc-mechanism.md`  
  Cơ chế DeepDoc: OCR, layout recognition, table structure recognition.
4. `04-ragflow-ingest-codepath.md`  
  Phân tích luồng chạy trong `rag/svr/task_executor.py` và `rag/flow/pipeline.py`.
5. `05-parser-comparison-and-tradeoff.md`  
  So sánh parser, trade-off chất lượng/chi phí/độ trễ.
6. `06-demo-checklist-and-takeaways.md`  
  Kịch bản demo, checklist quan sát, key takeaways.

## Nguồn đối chiếu kỹ thuật

- `rag/svr/task_executor.py`
- `rag/flow/pipeline.py`
- `api/utils/validation_utils.py`
- `api/utils/api_utils.py`
- `deepdoc/README.md`
- `deepdoc/parser/__init__.py`
- `deepdoc/parser/pdf_parser.py`