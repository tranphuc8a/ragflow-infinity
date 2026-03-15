---
sidebar_position: 1
slug: /configurations
sidebar_custom_props: {
  sidebarIcon: LucideCog
}
---
# Cấu hình

Các cấu hình để triển khai RAGFlow qua Docker.

## Hướng dẫn

Về cấu hình hệ thống, bạn cần quản lý các tệp sau:

- [.env](https://github.com/infiniflow/ragflow/blob/main/docker/.env): Chứa các biến môi trường quan trọng cho Docker.
- [service_conf.yaml.template](https://github.com/infiniflow/ragflow/blob/main/docker/service_conf.yaml.template): Cấu hình các dịch vụ backend. Nó chỉ định cấu hình cấp hệ thống cho RAGFlow và được sử dụng bởi API server và task executor của nó. Khi khởi động container, tệp `service_conf.yaml` sẽ được tạo dựa trên tệp mẫu này. Quá trình này thay thế bất kỳ biến môi trường nào trong mẫu, cho phép cấu hình động phù hợp với môi trường của container.
- [docker-compose.yml](https://github.com/infiniflow/ragflow/blob/main/docker/docker-compose.yml): Tệp Docker Compose để khởi động dịch vụ RAGFlow.

Để cập nhật cổng HTTP phục vụ mặc định (80), hãy vào [docker-compose.yml](https://github.com/infiniflow/ragflow/blob/main/docker/docker-compose.yml) và thay đổi `80:80`
thành `<YOUR_SERVING_PORT>:80`.

:::tip LƯU Ý
Các cập nhật cho các cấu hình trên yêu cầu khởi động lại tất cả các container để có hiệu lực:

```bash
docker compose -f docker/docker-compose.yml up -d
```

:::

## Docker Compose

- **docker-compose.yml**
  Thiết lập môi trường cho RAGFlow và các phụ thuộc của nó.
- **docker-compose-base.yml**
  Thiết lập môi trường cho các phụ thuộc của RAGFlow: Elasticsearch/[Infinity](https://github.com/infiniflow/infinity), MySQL, MinIO và Redis.

:::danger QUAN TRỌNG
Chúng tôi không tích cực duy trì **docker-compose-CN-oc9.yml**, **docker-compose-macos.yml**, vì vậy hãy sử dụng chúng với rủi ro riêng của bạn. Tuy nhiên, bạn được hoan nghênh gửi pull request để cải thiện chúng.
:::

## Biến môi trường Docker

Tệp [.env](https://github.com/infiniflow/ragflow/blob/main/docker/.env) chứa các biến môi trường quan trọng cho Docker.

### Elasticsearch

- `STACK_VERSION`
  Phiên bản Elasticsearch. Mặc định là `8.11.3`
- `ES_PORT`
  Cổng dùng để expose dịch vụ Elasticsearch ra máy chủ, cho phép truy cập **bên ngoài** vào dịch vụ chạy trong Docker container. Mặc định là `1200`.
- `ELASTIC_PASSWORD`
  Mật khẩu cho Elasticsearch.

### Kibana

- `KIBANA_PORT`
  Cổng dùng để expose dịch vụ Kibana ra máy chủ, cho phép truy cập **bên ngoài** vào dịch vụ chạy trong Docker container. Mặc định là `6601`.
- `KIBANA_USER`
  Tên người dùng cho Kibana. Mặc định là `rag_flow`.
- `KIBANA_PASSWORD`
  Mật khẩu cho Kibana. Mặc định là `infini_rag_flow`.

### Quản lý tài nguyên

- `MEM_LIMIT`
  Lượng bộ nhớ tối đa, tính bằng byte, mà *một* Docker container cụ thể có thể sử dụng khi chạy. Mặc định là `8073741824`.

### MySQL

- `MYSQL_PASSWORD`
  Mật khẩu cho MySQL.
- `MYSQL_PORT`
  Cổng để kết nối MySQL từ container RAGFlow. Mặc định là `3306`. Thay đổi điều này nếu bạn sử dụng MySQL bên ngoài.
- `EXPOSE_MYSQL_PORT`
  Cổng dùng để expose dịch vụ MySQL ra máy chủ, cho phép truy cập **bên ngoài** vào cơ sở dữ liệu MySQL chạy trong Docker container. Mặc định là `5455`.

### MinIO

RAGFlow sử dụng MinIO như giải pháp lưu trữ đối tượng, tận dụng khả năng mở rộng của nó để lưu trữ và quản lý tất cả tệp đã tải lên.

- `MINIO_CONSOLE_PORT`
  Cổng dùng để expose giao diện console MinIO ra máy chủ, cho phép truy cập **bên ngoài** vào console web chạy trong Docker container. Mặc định là `9001`
- `MINIO_PORT`
  Cổng dùng để expose dịch vụ MinIO API ra máy chủ, cho phép truy cập **bên ngoài** vào dịch vụ lưu trữ đối tượng MinIO chạy trong Docker container. Mặc định là `9000`.
- `MINIO_USER`
  Tên người dùng cho MinIO.
- `MINIO_PASSWORD`
  Mật khẩu cho MinIO.

### Redis

- `REDIS_PORT`
  Cổng dùng để expose dịch vụ Redis ra máy chủ, cho phép truy cập **bên ngoài** vào dịch vụ Redis chạy trong Docker container. Mặc định là `6379`.
- `REDIS_USERNAME`
  Tên người dùng Redis ACL tùy chọn khi sử dụng xác thực Redis 6+.
- `REDIS_PASSWORD`
  Mật khẩu cho Redis.

### RAGFlow

- `SVR_HTTP_PORT`
  Cổng dùng để expose dịch vụ HTTP API của RAGFlow ra máy chủ, cho phép truy cập **bên ngoài** vào dịch vụ chạy trong Docker container. Mặc định là `9380`.
- `RAGFLOW-IMAGE`
  Phiên bản Docker image. Mặc định là `infiniflow/ragflow:v0.23.1` (RAGFlow Docker image không có mô hình nhúng).

:::tip LƯU Ý
Nếu bạn không thể tải xuống RAGFlow Docker image, hãy thử các mirror sau.

- Đối với phiên bản `nightly`:
  - `RAGFLOW_IMAGE=swr.cn-north-4.myhuaweicloud.com/infiniflow/ragflow:nightly` hoặc,
  - `RAGFLOW_IMAGE=registry.cn-hangzhou.aliyuncs.com/infiniflow/ragflow:nightly`.
:::

### Dịch vụ nhúng

- `TEI_MODEL`
  Mô hình nhúng mà text-embeddings-inference phục vụ. Các giá trị được phép là một trong `Qwen/Qwen3-Embedding-0.6B` (mặc định), `BAAI/bge-m3`, và `BAAI/bge-small-en-v1.5`.

- `TEI_PORT`
  Cổng dùng để expose dịch vụ text-embeddings-inference ra máy chủ, cho phép truy cập **bên ngoài** vào dịch vụ text-embeddings-inference chạy trong Docker container. Mặc định là `6380`.

### Múi giờ

- `TZ`
  Múi giờ địa phương. Mặc định là `Asia/Shanghai`.

### Trang mirror Hugging Face

- `HF_ENDPOINT`
  Trang mirror cho huggingface.co. Bị vô hiệu hóa theo mặc định. Bạn có thể bỏ chú thích dòng này nếu bạn có quyền truy cập hạn chế vào miền Hugging Face chính.

### MacOS

- `MACOS`
  Tối ưu hóa cho macOS. Bị vô hiệu hóa theo mặc định. Bạn có thể bỏ chú thích dòng này nếu hệ điều hành của bạn là macOS.

### Đăng ký người dùng

- `REGISTER_ENABLED`
  - `1`: (Mặc định) Cho phép đăng ký người dùng.
  - `0`: Vô hiệu hóa đăng ký người dùng.

## Cấu hình dịch vụ

[service_conf.yaml.template](https://github.com/infiniflow/ragflow/blob/main/docker/service_conf.yaml.template) chỉ định cấu hình cấp hệ thống cho RAGFlow và được sử dụng bởi API server và task executor của nó.

### `ragflow`

- `host`: Địa chỉ IP của API server trong Docker container. Mặc định là `0.0.0.0`.
- `port`: Cổng phục vụ của API server trong Docker container. Mặc định là `9380`.

### `mysql`

- `name`: Tên cơ sở dữ liệu MySQL. Mặc định là `rag_flow`.
- `user`: Tên người dùng cho MySQL.
- `password`: Mật khẩu cho MySQL.
- `port`: Cổng phục vụ MySQL trong Docker container. Mặc định là `3306`.
- `max_connections`: Số lượng kết nối đồng thời tối đa đến cơ sở dữ liệu MySQL. Mặc định là `100`.
- `stale_timeout`: Timeout tính bằng giây.

### `minio`

- `user`: Tên người dùng cho MinIO.
- `password`: Mật khẩu cho MinIO.
- `host`: IP *và* cổng phục vụ MinIO trong Docker container. Mặc định là `minio:9000`.

### `redis`

- `host`: IP *và* cổng phục vụ Redis trong Docker container. Mặc định là `redis:6379`.
- `db`: Chỉ số cơ sở dữ liệu Redis để sử dụng. Mặc định là `1`.
- `username`: Tên người dùng Redis ACL tùy chọn (Redis 6+).
- `password`: Mật khẩu cho người dùng Redis được chỉ định.

### `oauth`

Cấu hình OAuth để đăng ký hoặc đăng nhập vào RAGFlow bằng tài khoản bên thứ ba.

- `<channel>`: ID channel tùy chỉnh.
  - `type`: Loại xác thực, các tùy chọn bao gồm `oauth2`, `oidc`, `github`. Mặc định là `oauth2`, khi tham số `issuer` được cung cấp, mặc định là `oidc`.
  - `icon`: ID biểu tượng, các tùy chọn bao gồm `github`, `sso`, mặc định là `sso`.
  - `display_name`: Tên channel, mặc định là định dạng Title Case của ID channel.
  - `client_id`: Bắt buộc, định danh duy nhất được gán cho ứng dụng client.
  - `client_secret`: Bắt buộc, khóa bí mật cho ứng dụng client, được sử dụng để giao tiếp với máy chủ xác thực.
  - `authorization_url`: URL cơ sở để lấy ủy quyền người dùng.
  - `token_url`: URL để đổi mã ủy quyền và lấy access token.
  - `userinfo_url`: URL để lấy thông tin người dùng (tên người dùng, email, v.v.).
  - `issuer`: URL cơ sở của nhà cung cấp danh tính. Các client OIDC có thể lấy động siêu dữ liệu của nhà cung cấp danh tính (`authorization_url`, `token_url`, `userinfo_url`) thông qua `issuer`.
  - `scope`: Phạm vi quyền được yêu cầu, một chuỗi phân cách bằng dấu cách. Ví dụ: `openid profile email`.
  - `redirect_uri`: Bắt buộc, URI mà máy chủ ủy quyền chuyển hướng đến trong luồng xác thực để trả về kết quả. Phải khớp với URI callback đã đăng ký với máy chủ xác thực. Định dạng: `https://your-app.com/v1/user/oauth/callback/<channel>`.

:::tip LƯU Ý
Sau đây là các phương pháp tốt nhất để cấu hình các phương thức xác thực bên thứ ba khác nhau. Bạn có thể cấu hình một hoặc nhiều phương thức xác thực bên thứ ba cho RAGFlow:
```yaml
oauth:
  oauth2:
    display_name: "OAuth2"
    client_id: "your_client_id"
    client_secret: "your_client_secret"
    authorization_url: "https://your-oauth-provider.com/oauth/authorize"
    token_url: "https://your-oauth-provider.com/oauth/token"
    userinfo_url: "https://your-oauth-provider.com/oauth/userinfo"
    redirect_uri: "https://your-app.com/v1/user/oauth/callback/oauth2"

  oidc:
    display_name: "OIDC"
    client_id: "your_client_id"
    client_secret: "your_client_secret"
    issuer: "https://your-oauth-provider.com/oidc"
    scope: "openid email profile"
    redirect_uri: "https://your-app.com/v1/user/oauth/callback/oidc"

  github:
    type: "github"
    icon: "github"
    display_name: "Github"
    client_id: "your_client_id"
    client_secret: "your_client_secret"
    redirect_uri: "https://your-app.com/v1/user/oauth/callback/github"
```
:::

### `user_default_llm`

LLM mặc định để sử dụng cho người dùng RAGFlow mới. Bị vô hiệu hóa theo mặc định. Để bật tính năng này, hãy bỏ chú thích các dòng tương ứng trong **service_conf.yaml.template**.

- `factory`: Nhà cung cấp LLM. Các tùy chọn có sẵn:
  - `"OpenAI"`
  - `"DeepSeek"`
  - `"Moonshot"`
  - `"Tongyi-Qianwen"`
  - `"VolcEngine"`
  - `"ZHIPU-AI"`
- `api_key`: API key cho LLM được chỉ định. Bạn cần đăng ký API key mô hình trực tuyến.
- `allowed_factories`: Nếu điều này được đặt, người dùng chỉ được phép thêm các nhà máy trong danh sách này.
  - `"OpenAI"`
  - `"DeepSeek"`
  - `"Moonshot"`

:::tip LƯU Ý
Nếu bạn không đặt LLM mặc định ở đây, hãy cấu hình LLM mặc định trên trang **Cài đặt** trong RAGFlow UI.
:::
