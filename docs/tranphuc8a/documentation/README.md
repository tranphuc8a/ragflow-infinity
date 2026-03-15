# Bộ tài liệu dự án RAGFlow (Tiếng Việt)

Thư mục này tổng hợp tài liệu **BA + Dev** cho dự án RAGFlow, được tổ chức theo hướng dễ đọc, có sơ đồ Mermaid, bám sát mã nguồn hiện tại.

## 1) Cấu trúc tài liệu

### BA Docs
- `01_ba/01_phan_tich_yeu_cau.md` — **Phân tích đầy đủ**: 12 UC, 100+ yêu cầu chức năng chi tiết theo từng tính năng nhỏ
- `01_ba/02_usecase_activity_dataflow_state.md` — Use case diagram, Activity, Dataflow, State machine

### Dev Docs
- `02_dev/01_kien_truc_tong_the.md` — Kiến trúc tổng thể, sơ đồ component
- `02_dev/02_api_spec.md` — API specification, auth, nhóm endpoint
- `02_dev/03_database_class.md` — ERD và class diagram
- `02_dev/04_sequence_runtime_cache.md` — Sequence diagram, runtime, cache
- `02_dev/05_deployment_van_hanh.md` — Deployment và vận hành
- `02_dev/06_cau_truc_thu_muc.md` — **Cây thư mục**: giải thích chi tiết từng dir/file, vai trò, chức năng liên quan
- `02_dev/api_routes_inventory.md` — Inventory 294 endpoint auto-scan từ mã nguồn

## 2) Phạm vi

- Bao phủ cả kiến trúc Python backend (`api/`, `rag/`, `deepdoc/`, `agent/`) và Go services (`cmd/`, `internal/`).
- Tập trung vào các luồng chính:
  - Quản lý dataset/document/chunk.
  - Truy vấn chat RAG.
  - Pipeline xử lý tài liệu (parse/chunk/embed/index).
  - Quản trị hệ thống, token, health.

## 3) Nguồn tham chiếu chính trong code

- Entrypoint Python: `api/ragflow_server.py`, `api/apps/__init__.py`
- API modules: `api/apps/*_app.py`, `api/apps/sdk/*.py`
- Data model: `api/db/db_models.py`
- Task executor: `rag/svr/task_executor.py`
- Hạ tầng dịch vụ: `docker/docker-compose-base.yml`, `docker/.env`
- Go servers: `cmd/server_main.go`, `cmd/admin_server.go`

## 4) Lưu ý cập nhật

Khi có thay đổi API, hãy cập nhật:
1. `02_dev/02_api_spec.md`
2. `02_dev/api_routes_inventory.md` (quét lại tự động)
3. Sơ đồ sequence/dataflow nếu thay đổi luồng xử lý.
