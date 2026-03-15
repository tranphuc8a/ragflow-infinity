# DEV-03: Database, ERD và Class View

## 1. Tổng quan persistence

Hệ thống dùng MySQL làm nguồn dữ liệu giao dịch chính, với các bảng trọng yếu:
- Identity/tenant: `user`, `tenant`, `user_tenant`, `invitation_code`
- Model config: `llm`, `llm_factories`, `tenant_llm`, `tenant_langfuse`
- Tri thức: `knowledgebase`, `document`, `file`, `file2document`, `task`
- Hội thoại: `dialog`, `conversation`, `api_token`, `api_4_conversation`
- Canvas/Agent: `user_canvas`, `canvas_template`, `user_canvas_version`, `mcp_server`
- Monitoring/pipeline: `pipeline_operation_log`, `sync_logs`
- Evaluation/memory/system: `evaluation_*`, `memory`, `system_settings`

## 2. ERD mức khái niệm

```mermaid
erDiagram
    USER ||--o{ USER_TENANT : belongs
    TENANT ||--o{ USER_TENANT : has
    TENANT ||--o{ KNOWLEDGEBASE : owns
    KNOWLEDGEBASE ||--o{ DOCUMENT : contains
    FILE ||--o{ FILE2DOCUMENT : maps
    DOCUMENT ||--o{ FILE2DOCUMENT : maps
    DOCUMENT ||--o{ TASK : generates

    TENANT ||--o{ DIALOG : owns
    DIALOG ||--o{ CONVERSATION : has
    TENANT ||--o{ API_TOKEN : issues
    DIALOG ||--o{ API_4_CONVERSATION : serves

    TENANT ||--o{ TENANT_LLM : configures
    LLM_FACTORIES ||--o{ LLM : provides

    KNOWLEDGEBASE ||--o{ PIPELINE_OPERATION_LOG : logs
    TENANT ||--o{ CONNECTOR : has
    CONNECTOR ||--o{ SYNC_LOGS : records
```

## 3. Class diagram mức miền nghiệp vụ

```mermaid
classDiagram
    class Tenant {
      +id
      +name
      +llm_id
      +embd_id
      +status
    }
    class User {
      +id
      +email
      +access_token
      +is_superuser
    }
    class Knowledgebase {
      +id
      +tenant_id
      +name
      +parser_id
      +parser_config
    }
    class Document {
      +id
      +kb_id
      +name
      +status
      +progress
      +chunk_num
    }
    class Task {
      +id
      +doc_id
      +task_type
      +progress
      +progress_msg
    }
    class Dialog {
      +id
      +tenant_id
      +llm_id
      +prompt_config
      +kb_ids
    }
    class Conversation {
      +id
      +dialog_id
      +message
      +reference
    }

    Tenant "1" --> "*" Knowledgebase
    Knowledgebase "1" --> "*" Document
    Document "1" --> "*" Task
    Tenant "1" --> "*" Dialog
    Dialog "1" --> "*" Conversation
    Tenant "1" --> "*" User
```

## 4. Ghi chú thiết kế

- Nhiều bảng dùng `status` để soft-delete/invalid hóa record.
- Các trường `JSONField` dùng cho cấu hình động (prompt, parser_config, metrics, dsl...).
- `Task` + `PipelineOperationLog` là lõi theo dõi vận hành ingest/pipeline.
- `content_hash` trong `document` phục vụ phát hiện thay đổi nội dung.

## 5. Chỉ mục và tối ưu truy vấn

- Các khóa tra cứu nghiệp vụ (`tenant_id`, `kb_id`, `dialog_id`, `status`) đã có index.
- Cần ưu tiên query có điều kiện tenant + status để giảm full scan.
- Dữ liệu lịch sử conversation/evaluation nên có chiến lược archive theo thời gian.
