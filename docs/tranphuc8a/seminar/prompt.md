
## **Role & Context**

Bạn là **software engineer trong dự án RAGFlow**, được giao nhiệm vụ thiết kế chuỗi **4 buổi seminar kỹ thuật (trong 4 tuần)** nhằm giúp:

* Developer mới tham gia dự án
* Người có background lập trình nhưng chưa hiểu AI / RAG
* Người muốn hiểu **nguyên lý hoạt động của hệ thống RAG Flow thực tế**

Seminar **không tập trung nhiều vào hướng dẫn đọc code chi tiết**, mà tập trung vào:

> ✅ công nghệ nền tảng  
> ✅ cơ chế hoạt động  
> ✅ pipeline xử lý dữ liệu  
> ✅ kiến trúc hệ thống  
> ✅ nguyên lý thiết kế

Bạn được yêu cầu đọc và phân tích:

* Toàn mã nguồn dự án
* Các thư mục tài liệu **/docs**
* Kiến trúc tổng thể của dự án
* Các pipeline chính: ingest pipeline và query pipeline

---

## **Mục tiêu sau 4 buổi**

Người học có thể:

* Hiểu rõ cơ chế hoạt động của hệ thống RAG production
* Hiểu vai trò từng thành phần và luồng hoạt động trong RAGFlow
* Hiểu các kỹ thuật cốt lõi:
  * parsing
  * chunking
  * embedding
  * vector retrieval
  * prompt construction
* Có nền tảng để:
  * thiết kế hệ RAG khác
  * optimize hệ thống hiện tại
  * tham gia phát triển dự án

---

## **Sườn nội dung gợi ý theo từng buổi**

### **Buổi 1 — Tổng quan AI Model → RAG → RAGFlow Architecture**

Nội dung bao gồm:

* Phân loại các loại model trong hệ sinh thái LLM:
  * base LLM
  * chat LLM
  * instruct model
  * embedding model
  * reranking model
* Nguyên lý hoạt động cơ bản của LLM
* Nhược điểm của LLM:
  * hallucination
  * knowledge cutoff
  * context window limitation
* Khái niệm và tác dụng của Retrieval Augmented Generation (RAG)
* Kiến trúc tổng quát của hệ RAG
* Giới thiệu RAGFlow:
  * mục tiêu thiết kế
  * kiến trúc tổng thể
  * các thành phần chính
* Luồng hoạt động end-to-end ở mức high-level

---

### **Buổi 2 — File Ingest Pipeline & Parsing Mechanism**

Nội dung bao gồm:

* Tổng quan ingest pipeline trong hệ RAG
* Vai trò của parser trong pipeline
* Nguyên tắc hoạt động của parser tài liệu:
  * text extraction
  * layout understanding
  * semantic segmentation
* Các loại parser được sử dụng trong RAGFlow
* Phân tích parser chính của RAGFlow:
  * DeepDoc parser
  * nguyên lý hoạt động
  * điểm mạnh / hạn chế
* So sánh với các parser phổ biến khác
* Demo parser tài liệu
* Demo luồng ingest upload file trong RAGFlow

---

### **Buổi 3 — Chunking, Embedding & Vector Database (Theory Deep Dive)**

Nội dung tập trung **thiên về nguyên lý kỹ thuật**:

* Chunking:
  * vì sao cần chunk
  * các chiến lược chunk:
    * fixed size
    * semantic chunking
    * sliding window
  * chunking trong dự án RAGFlow hiện tại được triển khai thế nào

* Embedding:
  * vector representation concept
  * embedding space intuition
  * similarity metric (cosine, dot, euclidean)
  * embedding trong dự án RAGFlow hiện tại được triển khai thế nào

* Vector database:
  * ANN search concept
  * indexing structure (HNSW, IVF…)
  * trade-off latency vs recall
  * vector database trong dự án RAGFlow hiện tại được triển khai thế nào

* Vai trò của 3 bước này trong performance của hệ RAG
* Luồng ingest hoàn chỉnh từ parsing → indexing

---

### **Buổi 4 — Query Pipeline, Retrieval Strategy & Prompt Construction**

Nội dung:

* Luồng user query trong hệ RAG và RAGFlow hiện tại
* Retrieval strategy:
  * top-k retrieval
  * hybrid search
  * reranking mechanism

* Context building & prompt engineering trong RAG
* Cách LLM sinh response từ context retrieve
* Demo end-to-end query flow
* Giới thiệu các chức năng nâng khác của RAGFlow như agent builder...
* Tổng kết toàn bộ kiến thức 4 buổi, rút ra bài học và kết luận

---

## **Yêu cầu thiết kế nội dung seminar**

Mỗi buổi phải có:

* Learning objectives
* Nội dung lý thuyết chi tiết
* Diagram minh họa kiến trúc hoặc pipeline
  (PlantUML hoặc Mermaid)
* Ví dụ minh họa thực tế
* Demo suggestion
* Key takeaways cuối buổi

Độ sâu kỹ thuật tăng dần theo từng buổi.

---

## **Output format**

Tạo cấu trúc tài liệu:

```text
docs/tranphuc8a/seminar/
    README.md
    session1/
    session2/
    session3/
    session4/
```

Yêu cầu:

* Ngôn ngữ: **Tiếng Việt**
* Văn phong: **technical nhưng dễ tiếp cận**
* Giải thích rõ thuật ngữ
* Nội dung đủ chi tiết để có thể dùng trực tiếp làm slide hoặc tài liệu seminar

---

## **Definition of Done**

Tài liệu được xem là hoàn thành khi:

* Người học có thể hiểu **cơ chế hoạt động của toàn bộ hệ RAGFlow**
* Có thể hình dung **luồng dữ liệu từ file → vector → query → response**
* Có nền tảng lý thuyết đủ sâu để thiết kế hoặc tối ưu hệ RAG khác

---

