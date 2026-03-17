# Chuỗi Seminar Kỹ Thuật RAGFlow (4 Tuần)

Bộ tài liệu này được thiết kế cho:
- Developer mới tham gia dự án RAGFlow.
- Người có nền tảng lập trình nhưng chưa nắm chắc AI/RAG.
- Người muốn hiểu cơ chế vận hành hệ thống RAG production thực tế.

Mục tiêu tổng sau 4 tuần:
- Hiểu được bức tranh từ mô hình nền tảng đến hệ RAG production.
- Hình dung rõ luồng dữ liệu `file -> parse -> chunk -> embed -> index -> retrieve -> prompt -> answer`.
- Có nền tảng để tối ưu hệ hiện tại hoặc thiết kế hệ RAG mới.

## Cấu trúc tài liệu

Mỗi session đã được phân rã thành nhiều file chuyên đề, tránh dồn toàn bộ nội dung vào một tài liệu lớn.

1. `docs/tranphuc8a/seminar/session1/README.md`  
   Chủ đề: Tổng quan AI Model -> RAG -> RAGFlow Architecture
2. `docs/tranphuc8a/seminar/session2/README.md`  
   Chủ đề: Ingest Pipeline và Parsing Mechanism
3. `docs/tranphuc8a/seminar/session3/README.md`  
   Chủ đề: Chunking, Embedding, Vector Database
4. `docs/tranphuc8a/seminar/session4/README.md`  
   Chủ đề: Query Pipeline, Retrieval Strategy, Prompt Construction

## Cách dùng bộ tài liệu để lên slide/seminar

- Đọc `README.md` của từng session để nắm bố cục buổi học.
- Dùng các file đánh số `01..06` trong session làm từng phần nội dung slide.
- Mỗi session đều có đủ:
  - Learning objectives.
  - Lý thuyết chi tiết theo từng khái niệm nhỏ.
  - Sơ đồ Mermaid cho kiến trúc hoặc pipeline.
  - Ví dụ thực tế theo ngữ cảnh enterprise.
  - Demo suggestion có kịch bản rõ ràng.
  - Key takeaways cuối buổi.

## Nguồn tham chiếu kỹ thuật đã đối chiếu

- Kiến thức nền RAG/Context Engine:
  - `docs/basics/rag.md`
  - `docs/basics/agent_context_engine.md`
- Tổng quan sản phẩm:
  - `README.md`
- Ingest thực thi:
  - `rag/svr/task_executor.py`
  - `rag/flow/pipeline.py`
  - `api/utils/validation_utils.py`
  - `api/utils/api_utils.py`
- Query/retrieval thực thi:
  - `api/db/services/dialog_service.py`
  - `rag/nlp/search.py`
- Parser/DeepDoc:
  - `deepdoc/README.md`
  - `deepdoc/parser/__init__.py`
  - `deepdoc/parser/pdf_parser.py`

## Kết quả mong đợi (Definition of Done)

Người học có thể:
- Giải thích vì sao hệ RAG production không chỉ là `vector search + LLM`.
- Mô tả vai trò từng thành phần trong RAGFlow, từ ingest đến query.
- Hình dung rõ luồng `file -> vector -> query -> response`.
- Xác định được các đòn bẩy tối ưu chính: parse quality, chunk design, embedding fit, retrieval fusion, prompt budget, rerank.