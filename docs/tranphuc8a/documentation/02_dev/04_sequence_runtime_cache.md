# DEV-04: Sequence, Runtime và Cache

## 1. Sequence: Ingest tài liệu

```mermaid
sequenceDiagram
    autonumber
    participant U as User/Web
    participant API as Python API
    participant DB as MySQL
    participant Q as Redis Queue
    participant W as Task Executor
    participant S as MinIO
    participant D as Doc Engine

    U->>API: Upload document
    API->>DB: Save File/Document metadata
    API->>Q: Push task
    W->>Q: Consume task
    W->>S: Get binary file
    W->>W: Parse + Chunk + Embedding
    W->>D: Index chunks
    W->>DB: Update Task/Document progress
    API-->>U: Query progress/result
```

## 2. Sequence: Chat completion

```mermaid
sequenceDiagram
    autonumber
    participant C as Client
    participant API as Conversation API
    participant DB as MySQL
    participant RET as Retriever
    participant DE as Doc Engine
    participant LLM as LLM Provider

    C->>API: POST /completion
    API->>DB: Load dialog/session config
    API->>RET: Retrieve relevant chunks
    RET->>DE: Search vectors/terms
    DE-->>RET: Top-k chunks
    RET-->>API: Context chunks
    API->>LLM: Prompt + context
    LLM-->>API: Answer
    API->>DB: Save conversation/reference
    API-->>C: Answer + references
```

## 3. Kiến trúc cache/runtime config

```mermaid
flowchart LR
    APP[API/Worker] --> R[(Redis)]
    APP --> DB[(MySQL)]

    R --> A[Queue messages]
    R --> B[Distributed lock]
    R --> C[Heartbeat task executors]
    R --> D[Session/cache dữ liệu tạm]

    DB --> E[Metadata bền vững]
    DB --> F[User/Tenant/Model config]
```

## 4. State runtime của task executor

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Polling: đọc queue
    Polling --> Running: nhận task hợp lệ
    Running --> Updating: cập nhật progress
    Updating --> Running: task chưa xong
    Running --> Done: thành công
    Running --> Failed: lỗi xử lý
    Done --> Idle
    Failed --> Idle
```

## 5. Các điểm kỹ thuật quan trọng

- Worker sử dụng giới hạn đồng thời (`MAX_CONCURRENT_TASKS`, limiter semaphore).
- Có cơ chế distributed lock cho một số luồng cập nhật định kỳ.
- Tiến độ task ghi ngược về DB giúp UI/API hiển thị realtime gần đúng.
- Hàng đợi và heartbeat trong Redis là chìa khóa phát hiện worker bất thường.
