---
sidebar_position: 20
slug: /sandbox_quickstart
sidebar_custom_props: {
  categoryIcon: LucideCodesandbox
}
---
# Bắt đầu nhanh với Sandbox

Một backend thực thi code bảo mật, có thể cắm vào được thiết kế cho RAGFlow và các ứng dụng khác yêu cầu môi trường thực thi code cô lập.

## Tính năng:

- Tích hợp RAGFlow liền mạch — Hoạt động ngay lập tức với thành phần code của RAGFlow.
- Bảo mật cao — Sử dụng gVisor để sandbox cấp syscall để cô lập thực thi.
- Sandbox tùy chỉnh — Dễ dàng chỉnh sửa các profile seccomp để điều chỉnh hạn chế syscall.
- Hỗ trợ Runtime có thể cắm vào — Có thể mở rộng để hỗ trợ bất kỳ runtime ngôn ngữ lập trình nào.
- Thân thiện với lập trình viên — Thiết lập nhanh với Makefile tiện lợi.

## Kiến trúc

Kiến trúc bao gồm các Docker base image cô lập cho mỗi runtime ngôn ngữ được hỗ trợ, được quản lý bởi dịch vụ executor manager. Executor manager điều phối thực thi code trong sandbox bằng cách sử dụng gVisor để chặn syscall và các profile seccomp tùy chọn để lọc syscall nâng cao.

## Điều kiện tiên quyết

- Bản phân phối Linux tương thích với gVisor.
- gVisor được cài đặt và cấu hình.
- Docker phiên bản 25.0 trở lên (API 1.44+). Đảm bảo image executor manager của bạn đi kèm Docker CLI `29.1.0` trở lên để tương thích với các Docker daemon mới nhất.
- Docker Compose phiên bản 2.26.1 trở lên (tương tự yêu cầu RAGFlow).
- Trình quản lý gói và dự án uv được cài đặt.
- (Tùy chọn) GNU Make để quản lý dòng lệnh đơn giản hóa.

:::tip LƯU Ý
Thông báo lỗi `client version 1.43 is too old. Minimum supported API version is 1.44` cho thấy phiên bản Docker CLI tích hợp sẵn trong image executor manager thấp hơn `29.1.0` yêu cầu bởi Docker daemon đang sử dụng. Để giải quyết vấn đề này, hãy kéo `infiniflow/sandbox-executor-manager:latest` mới nhất từ Docker Hub hoặc rebuild nó trong `./sandbox/executor_manager`.
:::

## Build các Docker base image

Sandbox sử dụng các base image cô lập cho môi trường thực thi containerized bảo mật.

Build các base image thủ công:

```bash
docker build -t sandbox-base-python:latest ./sandbox_base_image/python
docker build -t sandbox-base-nodejs:latest ./sandbox_base_image/nodejs
```

Hoặc, build tất cả các base image cùng một lúc bằng Makefile:

```bash
make build
```

Tiếp theo, build image executor manager:

```bash
docker build -t sandbox-executor-manager:latest ./executor_manager
```

## Chạy với RAGFlow

1. Xác minh rằng gVisor đã được cài đặt và hoạt động đúng cách.

2. Cấu hình tệp .env tại docker/.env:

- Bỏ chú thích các biến môi trường liên quan đến sandbox.
- Bật profile sandbox ở cuối tệp.

3. Thêm mục sau vào tệp /etc/hosts để phân giải dịch vụ executor manager:

    ```bash
    127.0.0.1 es01 infinity mysql minio redis sandbox-executor-manager
    ```

4. Khởi động dịch vụ RAGFlow như bình thường.

## Chạy độc lập

### Thiết lập thủ công

1. Khởi tạo các biến môi trường:

    ```bash
    cp .env.example .env
    ```

2. Khởi chạy các dịch vụ sandbox bằng Docker Compose:

    ```bash
    docker compose -f docker-compose.yml up
    ```

3. Kiểm tra thiết lập sandbox:

    ```bash
    source .venv/bin/activate
    export PYTHONPATH=$(pwd)
    uv pip install -r executor_manager/requirements.txt
    uv run tests/sandbox_security_tests_full.py
    ```

### Sử dụng Makefile

Chạy tất cả thiết lập, build, khởi chạy và kiểm tra bằng một lệnh duy nhất:

```bash
make
```

### Giám sát

Để theo dõi log của container executor manager:

```bash
docker logs -f sandbox-executor-manager
```

Hoặc sử dụng phím tắt Makefile:

```bash
make logs
```
