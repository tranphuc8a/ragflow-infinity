# Session 1 - Tổng quan AI Model -> RAG -> RAGFlow Architecture

## Mục tiêu buổi học

Sau buổi này, người học có thể:
- Phân biệt các nhóm model trong hệ sinh thái LLM.
- Hiểu cơ chế sinh ngôn ngữ cơ bản của LLM và các giới hạn production.
- Giải thích vì sao RAG xuất hiện và giải quyết vấn đề nào của LLM thuần.
- Trình bày kiến trúc tổng quan của RAGFlow theo góc nhìn hệ thống.

## Lộ trình nội dung chi tiết

1. `01-llm-ecosystem.md`  
  Các loại model: base, instruct, chat, embedding, rerank.
2. `02-llm-core-mechanism.md`  
  Cơ chế hoạt động của LLM, tokenization, xác suất sinh chuỗi.
3. `03-llm-limitations.md`  
  Hallucination, knowledge cutoff, context window, thiếu grounding.
4. `04-rag-foundation.md`  
  Nguyên lý RAG và kiến trúc tổng quát ingest/query.
5. `05-ragflow-architecture.md`  
  Kiến trúc RAGFlow và end-to-end flow ở mức high-level.
6. `06-demo-and-takeaways.md`  
  Kịch bản demo, câu hỏi thảo luận, key takeaways.

## Cách triển khai slide đề xuất

- Mở đầu bằng vấn đề: vì sao LLM thuần chưa đủ cho enterprise.
- Dùng file `01` đến `05` làm trục kiến thức chính.
- Chốt buổi bằng `06` để nối sang session 2 (ingest và parser).

## Nguồn đối chiếu kỹ thuật

- `README.md`
- `docs/basics/rag.md`
- `docs/basics/agent_context_engine.md`