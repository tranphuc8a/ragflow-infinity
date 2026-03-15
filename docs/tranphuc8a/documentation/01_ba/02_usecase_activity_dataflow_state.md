# BA-02: Use case chi tiết, Activity, Dataflow, State

## 1. Activity: Luồng ingest tài liệu

```mermaid
flowchart TD
    A[Bắt đầu upload tài liệu] --> B[Kiểm tra quyền truy cập dataset]
    B -->|Không hợp lệ| X[Trả lỗi xác thực/phân quyền]
    B -->|Hợp lệ| C[Lưu metadata Document/File vào DB]
    C --> D[Tạo Task parse/index]
    D --> E[Đẩy message vào Redis queue]
    E --> F[Task Executor nhận task]
    F --> G[Đọc file từ MinIO/Storage]
    G --> H[Parse + Chunk]
    H --> I[Embedding + Index vào Doc Engine]
    I --> J[Cập nhật progress/status]
    J --> K[Kết thúc]
```

## 2. Dataflow: Luồng hỏi đáp RAG

```mermaid
flowchart LR
    U[Người dùng/API Client] --> A[Conversation API]
    A --> B[Dialog config + Prompt config]
    A --> C[Retriever]
    C --> D[(Doc Engine: ES/Infinity)]
    D --> C
    C --> E[Context Chunks]
    B --> F[Prompt Builder]
    E --> F
    F --> G[LLM Gateway]
    G --> H[Answer + Reference]
    H --> I[(Conversation Store)]
    H --> U
```

## 3. State machine: Trạng thái tài liệu ingest

```mermaid
stateDiagram-v2
    [*] --> Created
    Created --> Queued: run=1
    Queued --> Processing: worker nhận task
    Processing --> Indexed: parse/chunk/index thành công
    Processing --> Failed: lỗi parse/index
    Processing --> Canceled: run=2 hoặc cancel task
    Failed --> Queued: retry
    Canceled --> Queued: chạy lại
    Indexed --> [*]
```

## 4. Activity: Luồng chat completion

```mermaid
flowchart TD
    A[Nhận câu hỏi] --> B[Kiểm tra session/dialog/token]
    B -->|Lỗi| X[Trả lỗi]
    B --> C[Truy xuất chunks liên quan]
    C --> D[Tạo prompt hệ thống + ngữ cảnh]
    D --> E[Gọi LLM]
    E --> F[Tạo answer + reference]
    F --> G[Lưu hội thoại]
    G --> H[Trả kết quả]
```

## 5. Quy tắc nghiệp vụ chính

- Chỉ user thuộc tenant hợp lệ mới thao tác dataset/dialog/tokens.
- Mỗi tài liệu có vòng đời ingest riêng; trạng thái và tiến độ phải truy vết được.
- Luồng chat cần liên kết cấu hình dialog (LLM, top_k/top_n, similarity, rerank).
- Câu trả lời ưu tiên có trích dẫn/reference để tăng khả năng kiểm chứng.

## 6. Điểm kiểm soát rủi ro

- Sai cấu hình model key hoặc doc engine dẫn tới lỗi runtime.
- Dữ liệu ingest không chuẩn (file hỏng, parser mismatch) làm giảm chất lượng retrieval.
- Cần giám sát queue/worker heartbeat để phát hiện tắc nghẽn pipeline.
