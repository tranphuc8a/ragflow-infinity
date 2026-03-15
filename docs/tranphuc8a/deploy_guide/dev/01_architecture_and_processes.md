---
sidebar_position: 1
slug: /deploy_guide/dev/architecture_and_processes
sidebar_custom_props: {
  categoryIcon: LucideBlocks
}
---
# Kiến trúc local dev và các tiến trình cần chạy

Tài liệu này tóm tắt cách dự án RAGFlow được tách thành các khối chạy riêng khi phát triển tại máy local.

---

## 1. Tổng quan kiến trúc

RAGFlow trong repo này là một hệ thống full-stack gồm:

- **Frontend**: React + TypeScript + Vite trong thư mục `web/`.
- **Backend API**: Flask/Quart app trong `api/`.
- **Worker nền**: xử lý parse, embedding, indexing trong `rag/svr/`.
- **Admin service**: service riêng cho các API quản trị trong `admin/server/`.
- **Hạ tầng phụ thuộc**: MySQL, Elasticsearch/Infinity, Redis, MinIO chạy bằng Docker Compose.

## 2. Các tiến trình local cần hiểu

### 2.1 Frontend

- Thư mục: `web/`
- Lệnh dev: `npm run dev`
- Cổng mặc định: `9222`
- Proxy mặc định trong `web/vite.config.ts`:
  - `^/(api|v1)` -> `http://127.0.0.1:9380`
  - `/api/v1/admin` -> `http://127.0.0.1:9381`

Điều này có nghĩa là khi chạy local dev đầy đủ, frontend mong đợi **2 backend HTTP service**:

- API chính ở cổng `9380`
- Admin service ở cổng `9381`

### 2.2 Backend API chính

- File entrypoint: `api/ragflow_server.py`
- Cổng mặc định: `9380`
- Nhiệm vụ:
  - phục vụ API chính cho UI và SDK
  - khởi tạo DB/runtime config
  - nạp plugin
  - chạy luồng cập nhật tiến độ nền

File này có hỗ trợ `--debug` và biến môi trường `RAGFLOW_DEBUGPY_LISTEN`.

### 2.3 Task executor

- File entrypoint: `rag/svr/task_executor.py`
- Không mở HTTP port public
- Đọc task từ Redis queue và xử lý:
  - parse tài liệu
  - chunking
  - embedding
  - indexing
  - graph/memory pipeline

Nếu không chạy tiến trình này, UI vẫn mở được nhưng các tác vụ ingest/tạo dataset/chạy pipeline sẽ không hoàn tất.

### 2.4 Data sync worker

- File entrypoint: `rag/svr/sync_data_source.py`
- Dùng cho các connector đồng bộ nguồn dữ liệu như Google Drive, Notion, GitHub, Jira, Dropbox...
- **Không bắt buộc** nếu bạn chỉ debug chat/dataset upload thủ công.
- **Nên bật** nếu muốn test đầy đủ luồng connector.

### 2.5 Admin service

- File entrypoint: `admin/server/admin_server.py`
- Cổng mặc định: `9381`
- Route prefix: `/api/v1/admin`

Do frontend đã proxy sẵn sang cổng này, nếu bạn cần test trang hoặc API quản trị thì phải chạy thêm service này.

## 3. Hạ tầng phụ thuộc chạy bằng Docker

Local dev của repo này thường chạy **source code cho frontend/backend**, nhưng vẫn dùng Docker cho các service phụ thuộc.

Các service base được khởi động bằng:

```bash
docker compose -f docker/docker-compose-base.yml up -d
```

Nhóm service phụ thuộc quan trọng:

- **MySQL**: metadata/app data
- **Redis**: queue và coordination
- **MinIO**: object storage
- **Elasticsearch** hoặc **Infinity**: search/vector store

## 4. Cấu hình local hiện tại của repo

File `conf/service_conf.yaml` trong repo hiện đang trỏ tới host local:

- MySQL: `localhost:5455`
- Elasticsearch: `http://localhost:1200`
- MinIO: `localhost:9000`
- Redis: `localhost:6379`
- API chính: `0.0.0.0:9380`
- Admin: `0.0.0.0:9381`

Vì vậy, trong trạng thái repo hiện tại, cách chạy thuận tiện nhất là:

1. Docker chỉ chạy service phụ thuộc.
2. Source code chạy trực tiếp từ repo.
3. Frontend dev server proxy vào backend local.

## 5. Khuyến nghị môi trường cho Windows

Vì repo có nhiều shell script và dependency thiên về Linux (`bash`, `pkg-config`, `jemalloc`, `LD_PRELOAD`), cách chạy ổn định nhất trên Windows là:

- **Docker Desktop + WSL2 backend**
- **Ubuntu trong WSL2** để chạy Python backend và worker
- **VS Code Remote - WSL** để debug source trực tiếp

Bạn vẫn có thể chạy frontend ở Windows host, nhưng để đồng nhất môi trường và tránh sai khác path/phụ thuộc, nên chạy cả frontend trong WSL2.

## 6. Checklist local dev đầy đủ

Để coi là chạy được **toàn bộ dự án cho dev**, tối thiểu nên có các tiến trình sau:

- `docker compose -f docker/docker-compose-base.yml up -d`
- `python api/ragflow_server.py --debug`
- `python admin/server/admin_server.py`
- `python rag/svr/task_executor.py 0`
- `npm run dev` trong `web/`

Tùy nhu cầu, bổ sung thêm:

- `python rag/svr/sync_data_source.py`

Các bước chi tiết được mô tả trong các tài liệu tiếp theo.
