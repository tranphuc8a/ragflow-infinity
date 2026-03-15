---
sidebar_position: 2
slug: /launch_ragflow_from_source
sidebar_custom_props: {
  categoryIcon: LucideMonitorPlay
}
---
# Khởi động dịch vụ từ mã nguồn

Hướng dẫn giải thích cách thiết lập dịch vụ RAGFlow từ mã nguồn. Theo hướng dẫn này, bạn sẽ có thể debug bằng mã nguồn.

## Đối tượng mục tiêu

Các nhà phát triển đã thêm tính năng mới hoặc sửa đổi code hiện có và muốn debug bằng mã nguồn, *với điều kiện* máy của họ đã được cài đặt môi trường triển khai mục tiêu.

## Yêu cầu hệ thống

- CPU &ge; 4 nhân
- RAM &ge; 16 GB
- Ổ đĩa &ge; 50 GB
- Docker &ge; 24.0.0 & Docker Compose &ge; v2.26.1

:::tip LƯU Ý
Nếu bạn chưa cài đặt Docker trên máy cục bộ (Windows, Mac, hoặc Linux), hãy xem hướng dẫn [Cài đặt Docker Engine](https://docs.docker.com/engine/install/).
:::

## Khởi động dịch vụ từ mã nguồn

Để khởi động dịch vụ RAGFlow từ mã nguồn:

### Clone kho RAGFlow

```bash
git clone https://github.com/infiniflow/ragflow.git
cd ragflow/
```

### Cài đặt các phụ thuộc Python

1. Cài đặt uv:
   
   ```bash
   pipx install uv
   ```

2. Cài đặt các phụ thuộc Python của dịch vụ RAGFlow:

   ```bash
   uv sync --python 3.12 --frozen
   ```
   *Một môi trường ảo có tên `.venv` được tạo ra, và tất cả các phụ thuộc Python được cài đặt vào môi trường mới.*

   Nếu bạn cần chạy test với dịch vụ RAGFlow, hãy cài đặt các phụ thuộc test:

   ```bash
   uv sync --python 3.12 --group test --frozen && uv pip install sdk/python --group test
   ```

### Khởi động các dịch vụ bên thứ ba

Lệnh sau khởi động các dịch vụ 'base' (MinIO, Elasticsearch, Redis, và MySQL) bằng Docker Compose:

```bash
docker compose -f docker/docker-compose-base.yml up -d
```

### Cập nhật cài đặt `host` và `port` cho các dịch vụ bên thứ ba

1. Thêm dòng sau vào `/etc/hosts` để phân giải tất cả các host được chỉ định trong **docker/service_conf.yaml.template** thành `127.0.0.1`:

   ```
   127.0.0.1       es01 infinity mysql minio redis
   ```

2. Trong **docker/service_conf.yaml.template**, cập nhật cổng mysql thành `5455` và cổng es thành `1200`, như được chỉ định trong **docker/.env**.

### Khởi động dịch vụ backend RAGFlow

1. Comment dòng `nginx` trong **docker/entrypoint.sh**.

   ```
   # /usr/sbin/nginx
   ```

2. Kích hoạt môi trường ảo Python:

   ```bash
   source .venv/bin/activate
   export PYTHONPATH=$(pwd)
   ```

3. **Tùy chọn:** Nếu bạn không thể truy cập HuggingFace, hãy đặt biến môi trường HF_ENDPOINT để sử dụng trang mirror:
 
   ```bash
   export HF_ENDPOINT=https://hf-mirror.com
   ```

4. Kiểm tra cấu hình trong **conf/service_conf.yaml**, đảm bảo tất cả các host và cổng được đặt đúng.
   
5. Chạy script **entrypoint.sh** để khởi động dịch vụ backend:

   ```shell
   JEMALLOC_PATH=$(pkg-config --variable=libdir jemalloc)/libjemalloc.so;
   LD_PRELOAD=$JEMALLOC_PATH python rag/svr/task_executor.py 1;
   ```
   ```shell
   python api/ragflow_server.py;
   ```

### Khởi động dịch vụ frontend RAGFlow

1. Điều hướng đến thư mục `web` và cài đặt các phụ thuộc frontend:

   ```bash
   cd web
   npm install
   ```

2. Cập nhật `server.proxy.target` trong **vite.config.ts** thành `http://127.0.0.1:9380`:

   ```bash
   vim vite.config.ts
   ```

3. Khởi động dịch vụ frontend RAGFlow:

   ```bash
   npm run dev 
   ```

   *Thông báo sau xuất hiện, hiển thị địa chỉ IP và số cổng của dịch vụ frontend:*  

   ![](https://github.com/user-attachments/assets/0daf462c-a24d-4496-a66f-92533534e187)

### Truy cập dịch vụ RAGFlow

Trong trình duyệt web, nhập `http://127.0.0.1:<PORT>/`, đảm bảo số cổng khớp với số được hiển thị trong ảnh chụp màn hình ở trên.

### Dừng dịch vụ RAGFlow khi hoàn thành phát triển

1. Dừng dịch vụ frontend RAGFlow:
   ```bash
   pkill npm
   ```

2. Dừng dịch vụ backend RAGFlow:
   ```bash
   pkill -f "docker/entrypoint.sh"
   ```
