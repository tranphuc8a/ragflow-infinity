# DEV-02: API Specification (Tiếng Việt)

## 1. Nguyên tắc chung

- Authentication chính: Authorization token (user token hoặc API token).
- Dạng phản hồi chuẩn: `code`, `message`, `data`.
- Route được tổ chức theo module `*_app.py` và `sdk/*.py`.

## 2. Nhóm API chính

### 2.1 System
- `/version`, `/status`, `/healthz`, `/ping`, `/oceanbase/status`
- Mục đích: kiểm tra version, tình trạng dependency, health tổng thể.

### 2.2 User/Tenant/Auth
- Login/logout, register, info, setting, tenant_info.
- Quản lý user trong tenant, role và lời mời.

### 2.3 Knowledge Base (Dataset)
- Tạo/cập nhật/xóa/list/detail dataset.
- Quản lý metadata setting, tags, pipeline logs, GraphRAG/RAPTOR/Mindmap tasks.

### 2.4 Document/Chunk/File
- Upload file, convert file->document, list/get/remove/rename/move.
- Document operations: parse, retrieval test, metadata update, chunk CRUD.

### 2.5 Dialog/Conversation/Session
- Tạo và cấu hình dialog/chatbot.
- Completion endpoints (cả chuẩn và openai-compatible).
- Quản lý sessions, history, related questions, mindmap, tts.

### 2.6 LLM/Plugin/MCP/Evaluation/Search
- Quản lý model factories, tenant model keys.
- Quản lý plugin tools, MCP server, evaluation datasets/runs, search app.

## 3. API tiêu biểu (tham khảo nhanh)

| Nhóm | Endpoint | Method | Mô tả |
|---|---|---|---|
| System | `/healthz` | GET | Health check tổng hợp |
| System | `/status` | GET | Trạng thái doc engine/storage/db/redis |
| KB | `/create` | POST | Tạo dataset |
| KB | `/detail` | GET | Lấy chi tiết dataset |
| Document | `/upload` | POST | Upload tài liệu |
| Conversation | `/completion` | POST | Sinh câu trả lời RAG |
| SDK Session | `/chats/<chat_id>/completions` | POST | Completion theo chat API |
| LLM | `/set_api_key` | POST | Thiết lập API key model |

## 4. Bảo mật và phân quyền

- Các endpoint nghiệp vụ đa số yêu cầu `login_required`.
- Quyền truy cập dataset/dialog theo tenant ownership hoặc membership.
- API token có thể dùng cho luồng tích hợp bên ngoài.

## 5. Error handling

- 401: Unauthorized.
- 404: route không tồn tại.
- Business errors: trả mã lỗi trong `code/message` theo chuẩn nội bộ.

## 6. Inventory endpoint đầy đủ

Danh sách endpoint auto-scan từ mã nguồn nằm tại:
- `02_dev/api_routes_inventory.md`

File này được sinh từ toàn bộ decorator `@manager.route(...)` trong `api/apps/**/*.py`, dùng để đối chiếu nhanh độ phủ API khi review.
