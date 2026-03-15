---
sidebar_position: 4
slug: /deploy_guide/dev/debugging_and_troubleshooting
sidebar_custom_props: {
  categoryIcon: LucideBug
}
---
# Debugging workflow và troubleshooting

Tài liệu này tập trung vào cách debug hiệu quả khi chạy RAGFlow từ source.

---

## 1. Nên debug tiến trình nào theo từng bài toán

### Debug UI / page flow

Chạy:

- frontend `npm run dev`
- backend API `python api/ragflow_server.py --debug`
- admin service `python admin/server/admin_server.py`

### Debug upload / parse / ingest / indexing

Chạy thêm:

- `python rag/svr/task_executor.py 0`

### Debug connector đồng bộ dữ liệu

Chạy thêm:

- `python rag/svr/sync_data_source.py`

## 2. Gợi ý cách debug trong VS Code

### Backend API

Cách đơn giản nhất là mở repo bằng VS Code trong WSL2 và debug trực tiếp file:

- `api/ragflow_server.py`
- tham số: `--debug`
- working directory: thư mục gốc repo
- environment:
  - `PYTHONPATH=${workspaceFolder}`

Nếu muốn attach vào process đã chạy sẵn, bật:

```bash
export RAGFLOW_DEBUGPY_LISTEN=5678
python api/ragflow_server.py --debug
```

### Task executor

Task executor không có biến môi trường attach sẵn như API server, vì vậy cách dễ nhất là launch trực tiếp file dưới debugger:

- `rag/svr/task_executor.py`
- argument: `0`
- environment: `PYTHONPATH=${workspaceFolder}`

### Admin service

Launch trực tiếp file:

- `admin/server/admin_server.py`
- environment: `PYTHONPATH=${workspaceFolder}`

### Frontend

Với frontend Vite:

- chạy `npm run dev`
- mở DevTools của browser để debug UI/network
- nếu dùng VS Code JavaScript debugger, attach vào tab đang mở `http://127.0.0.1:9222`

## 3. Điểm đặt breakpoint hữu ích

### API layer

- `api/ragflow_server.py`
- các file trong `api/apps/`
- các service trong `api/db/services/`

### Pipeline/worker

- `rag/svr/task_executor.py`
- parser logic trong `rag/app/`
- retrieval/chunking trong `rag/`
- document parsing trong `deepdoc/`

### Admin

- `admin/server/routes.py`
- `admin/server/admin_server.py`

### Frontend

- `web/src/pages/`
- `web/src/components/`
- `web/src/services/`
- `web/src/hooks/`

## 4. Các sự cố thường gặp

### 4.1 Frontend mở được nhưng API lỗi `502` hoặc request fail

Nguyên nhân thường gặp:

- backend API chưa chạy ở `9380`
- admin service chưa chạy ở `9381`
- proxy trong `web/vite.config.ts` không khớp port thực tế

Cách xử lý:

1. kiểm tra terminal backend
2. kiểm tra terminal admin
3. xác nhận port trong `web/vite.config.ts`
4. xác nhận `conf/service_conf.yaml` đang khớp với Docker ports

### 4.2 Upload file xong nhưng không parse

Nguyên nhân thường gặp:

- chưa chạy `task_executor.py`
- Redis/MySQL/Elasticsearch chưa sẵn sàng
- worker lỗi dependency hoặc lỗi kết nối object storage

Cách xử lý:

1. kiểm tra worker log
2. kiểm tra `docker compose -f docker/docker-compose-base.yml ps`
3. kiểm tra `conf/service_conf.yaml`

### 4.3 Elasticsearch không lên

Nguyên nhân phổ biến nhất trên Windows + Docker Desktop:

- chưa set `vm.max_map_count=262144`

Cách xử lý:

1. cập nhật `%USERPROFILE%\.wslconfig`
2. chạy `wsl --shutdown`
3. restart Docker Desktop
4. start lại base services

### 4.4 Port bị trùng

Nếu local machine đã dùng một số port như `9222`, `9380`, `9381`, `1200`, `5455`, bạn cần đổi đồng bộ ở:

- `docker/.env`
- `conf/service_conf.yaml`
- `web/vite.config.ts`

### 4.5 Thiếu model/API key

RAGFlow cần model provider để chat/embedding/rerank trong nhiều flow.

Bạn có thể cấu hình:

- trực tiếp trên UI sau khi login
- hoặc điền `user_default_llm` trong `conf/service_conf.yaml`

Nếu không cấu hình model phù hợp, hệ thống có thể lên UI nhưng không chat/parse hoàn chỉnh.

## 5. Build/test nhanh sau khi sửa code

### Backend tests

```bash
uv run pytest
```

Hoặc chạy file test cụ thể:

```bash
uv run pytest test/test_api.py
```

### Frontend lint/test

```bash
cd web
npm run lint
npm run test
```

### Python lint/format

```bash
ruff check
ruff format
```

## 6. Checklist trước khi kết luận môi trường dev đã ổn

Bạn nên xác nhận được các việc sau:

- mở UI ở `http://127.0.0.1:9222`
- login thành công
- cấu hình model thành công
- tạo dataset được
- upload file được
- worker parse xong tài liệu
- chat/query lấy dữ liệu được
- breakpoint ở frontend/backend đều hit được

Nếu đủ các mục trên, môi trường dev full stack của bạn đã sẵn sàng để debug hiệu quả.
