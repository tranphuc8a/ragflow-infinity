---
sidebar_position: 3
slug: /deploy_guide/dev/build_and_run_full_stack
sidebar_custom_props: {
  categoryIcon: LucidePlay
}
---
# Build và run toàn bộ dự án cho local dev

Tài liệu này mô tả quy trình chạy **full stack** từ source để có thể debug.

---

## 1. Mô hình chạy được khuyến nghị

- **Docker** chỉ dùng cho hạ tầng phụ thuộc.
- **Python source** chạy trực tiếp từ repo.
- **Frontend Vite** chạy trực tiếp từ `web/`.

Đây là mô hình nhanh nhất để vừa code vừa debug.

## 2. Start hạ tầng phụ thuộc

Từ thư mục gốc repo:

```bash
docker compose -f docker/docker-compose-base.yml up -d
```

### Kiểm tra container

```bash
docker compose -f docker/docker-compose-base.yml ps
```

Bạn cần thấy ít nhất các service sau ở trạng thái chạy:

- `mysql`
- `redis`
- `minio`
- `es01` hoặc `infinity`

## 3. Kiểm tra file cấu hình local

Repo hiện có sẵn file `conf/service_conf.yaml` với local port map phù hợp cho source dev.

Trước khi chạy backend, hãy xác nhận nhanh các giá trị sau:

- `mysql.host: localhost`
- `mysql.port: 5455`
- `redis.host: localhost:6379`
- `minio.host: localhost:9000`
- `es.hosts: http://localhost:1200`
- `ragflow.http_port: 9380`
- `admin.http_port: 9381`

Nếu bạn thay đổi port ở `docker/.env`, hãy đổi đồng bộ ở file này.

## 4. Start backend API chính

Mở terminal 1 trong WSL2:

```bash
source .venv/bin/activate
export PYTHONPATH=$(pwd)
python api/ragflow_server.py --debug
```

### Nếu cần attach debugger từ ngoài process

`api/ragflow_server.py` có hỗ trợ biến môi trường `RAGFLOW_DEBUGPY_LISTEN`:

```bash
source .venv/bin/activate
export PYTHONPATH=$(pwd)
export RAGFLOW_DEBUGPY_LISTEN=5678
python api/ragflow_server.py --debug
```

Khi log hiện `debugpy listen on 5678`, bạn có thể attach debugger từ VS Code.

## 5. Start admin service

Mở terminal 2:

```bash
source .venv/bin/activate
export PYTHONPATH=$(pwd)
python admin/server/admin_server.py
```

Service này chạy ở cổng `9381` và phục vụ các route `/api/v1/admin`.

## 6. Start task executor

Mở terminal 3:

### Cách đơn giản để debug

```bash
source .venv/bin/activate
export PYTHONPATH=$(pwd)
python rag/svr/task_executor.py 0
```

### Cách gần với production hơn trên Linux/WSL2

```bash
source .venv/bin/activate
export PYTHONPATH=$(pwd)
JEMALLOC_PATH=$(pkg-config --variable=libdir jemalloc)/libjemalloc.so
LD_PRELOAD=$JEMALLOC_PATH python rag/svr/task_executor.py 0
```

Nếu cần song song nhiều worker, dùng các consumer id khác nhau:

```bash
python rag/svr/task_executor.py 0
python rag/svr/task_executor.py 1
```

Một worker thường đủ cho debug chức năng.

## 7. Start data sync worker (tùy chọn)

Mở terminal 4 nếu bạn cần test connector/sync data source:

```bash
source .venv/bin/activate
export PYTHONPATH=$(pwd)
python rag/svr/sync_data_source.py
```

Nếu bạn chỉ debug upload file, parse và chat thông thường, có thể bỏ qua tiến trình này.

## 8. Start frontend

Mở terminal 5:

```bash
cd web
npm run dev
```

Mặc định frontend sẽ chạy ở cổng `9222` và proxy sang:

- `9380` cho API chính
- `9381` cho admin API

## 9. Kiểm tra toàn bộ hệ thống sau khi start

### URL truy cập

- Frontend: `http://127.0.0.1:9222`
- Backend API: `http://127.0.0.1:9380`
- Admin API: `http://127.0.0.1:9381/api/v1/admin`
- MinIO Console: `http://127.0.0.1:9001`

### Dấu hiệu hoạt động bình thường

- backend API log ra banner RAGFlow và bắt đầu listen ở `9380`
- admin service listen ở `9381`
- task executor liên tục report heartbeat và chờ task
- frontend Vite hiển thị local URL
- upload tài liệu từ UI tạo task và worker bắt đầu xử lý

## 10. Lệnh stop

### Dừng frontend/backend local

Dừng từng terminal bằng `Ctrl+C`.

### Dừng base services Docker

```bash
docker compose -f docker/docker-compose-base.yml down
```

### Dừng và xóa volume khi cần reset dữ liệu dev

```bash
docker compose -f docker/docker-compose-base.yml down -v
```

> Lưu ý: `-v` sẽ xóa dữ liệu MySQL/MinIO/Elasticsearch trong môi trường dev local.

## 11. Luồng khởi động nhanh mỗi ngày

Sau khi setup xong, thông thường mỗi ngày chỉ cần:

```bash
# terminal A
docker compose -f docker/docker-compose-base.yml up -d

# terminal B
source .venv/bin/activate
export PYTHONPATH=$(pwd)
python api/ragflow_server.py --debug

# terminal C
source .venv/bin/activate
export PYTHONPATH=$(pwd)
python admin/server/admin_server.py

# terminal D
source .venv/bin/activate
export PYTHONPATH=$(pwd)
python rag/svr/task_executor.py 0

# terminal E
cd web
npm run dev
```

Đó là bộ lệnh tối thiểu để chạy full stack local dev.
