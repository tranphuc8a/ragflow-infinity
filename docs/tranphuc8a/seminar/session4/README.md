# Session 4 - Query Pipeline, Retrieval Strategy và Prompt Construction

## Mục tiêu buổi học

Sau buổi này, người học có thể:
- Mô tả đầy đủ query pipeline trong RAGFlow từ request đến final response.
- Hiểu sâu chiến lược retrieval: top-k, hybrid search, rerank, TOC/children expansion.
- Thiết kế context building và prompt construction theo tư duy production.
- Hiểu cách hệ thống gắn citation và đánh giá chất lượng đầu ra.

## Lộ trình nội dung chi tiết

1. `01-query-flow-overview.md`  
   Luồng end-to-end trong `async_chat`.
2. `02-retrieval-strategy-deepdive.md`  
   Top-k, hybrid, rerank và các cờ nâng cao.
3. `03-context-building-and-prompting.md`  
   Cách xây prompt, quản lý token budget, chống nhiễu ngữ cảnh.
4. `04-citation-and-answer-generation.md`  
   Cơ chế citation insertion, reference packaging, telemetry.
5. `05-agentic-features-and-extensions.md`  
   Liên hệ với tính năng nâng cao như canvas/agent builder.
6. `06-demo-recap-and-next-step.md`  
   Kịch bản demo, tổng kết 4 buổi, hướng học tiếp.

## Nguồn đối chiếu kỹ thuật

- `api/db/services/dialog_service.py`
- `rag/nlp/search.py`
- `docs/guides/ai_search.md`
- `docs/references/python_api_reference.md`