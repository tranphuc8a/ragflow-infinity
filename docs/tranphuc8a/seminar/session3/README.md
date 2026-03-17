# Session 3 - Chunking, Embedding và Vector Database (Theory Deep Dive)

## Mục tiêu buổi học

Sau buổi này, người học có thể:
- Phân tích trade-off cốt lõi của chunking trong RAG production.
- Hiểu trực quan embedding space và các metric similarity.
- Giải thích ANN indexing và đánh đổi latency/recall.
- Liên hệ lý thuyết với cách RAGFlow triển khai ingest và retrieval.

## Lộ trình nội dung chi tiết

1. `01-why-chunking-matters.md`  
  Vì sao chunking là điểm nghẽn chất lượng của RAG.
2. `02-chunking-strategies.md`  
  Fixed-size, semantic, sliding window và tiêu chí chọn.
3. `03-embedding-intuition.md`  
  Embedding concept, similarity metric, lỗi thường gặp.
4. `04-vector-db-ann.md`  
  ANN, HNSW/IVF/PQ, latency vs recall.
5. `05-ragflow-implementation.md`  
  Mapping lý thuyết sang `task_executor.py`, `rag/nlp/search.py`.
6. `06-demo-and-takeaways.md`  
  Kịch bản demo tuning và key takeaways.

## Nguồn đối chiếu kỹ thuật

- `api/utils/api_utils.py`
- `rag/nlp/__init__.py`
- `rag/svr/task_executor.py`
- `rag/nlp/search.py`
- `docs/basics/rag.md`