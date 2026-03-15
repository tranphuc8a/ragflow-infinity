---
sidebar_position: 1
slug: /launch_mcp_server
sidebar_custom_props: {
  categoryIcon: LucideTvMinimalPlay
}
---
# Khởi động máy chủ MCP RAGFlow

Khởi động máy chủ MCP từ mã nguồn hoặc qua Docker.

---

Máy chủ RAGFlow Model Context Protocol (MCP) được thiết kế như một thành phần độc lập để bổ sung cho máy chủ RAGFlow. Lưu ý rằng máy chủ MCP phải hoạt động cùng với máy chủ RAGFlow đang hoạt động đúng. 

Máy chủ MCP có thể khởi động ở chế độ self-host (mặc định) hoặc chế độ host: 

- **Chế độ Self-host**:  
  Khi khởi động máy chủ MCP ở chế độ self-host, bạn phải cung cấp API key để xác thực máy chủ MCP với máy chủ RAGFlow. Ở chế độ này, máy chủ MCP chỉ có thể truy cập *các dataset của một tenant được chỉ định* trên máy chủ RAGFlow.
- **Chế độ Host**:  
  Ở chế độ host, mỗi MCP client có thể truy cập dataset của riêng họ trên máy chủ RAGFlow. Tuy nhiên, mỗi yêu cầu client phải bao gồm API key hợp lệ để xác thực client với máy chủ RAGFlow.

Sau khi kết nối được thiết lập, máy chủ MCP giao tiếp với client theo chế độ MCP HTTP+SSE (Server-Sent Events), đẩy đơn phương các phản hồi từ máy chủ RAGFlow đến client theo thời gian thực.

## Yêu cầu

1. Đảm bảo RAGFlow đã được nâng cấp lên v0.18.0 hoặc mới hơn.
2. Chuẩn bị sẵn API key RAGFlow của bạn. Xem [Lấy API key RAGFlow](../acquire_ragflow_api_key.md).

:::tip THÔNG TIN
Nếu bạn muốn thử máy chủ MCP mà không cần nâng cấp RAGFlow, cộng tác viên cộng đồng [yiminghub2024](https://github.com/yiminghub2024) 👏 chia sẻ các bước khuyến nghị của họ [ở đây](#khởi-động-máy-chủ-mcp-mà-không-nâng-cấp-ragflow).
:::

## Khởi động máy chủ MCP 

Bạn có thể khởi động máy chủ MCP từ mã nguồn hoặc qua Docker. 

### Khởi động từ mã nguồn

1. Đảm bảo máy chủ RAGFlow v0.18.0+ đang hoạt động đúng.
2. Khởi động máy chủ MCP:

```bash
# Khởi động máy chủ MCP ở chế độ self-host, chạy một trong các lệnh sau
uv run mcp/server/server.py --host=127.0.0.1 --port=9382 --base-url=http://127.0.0.1:9380 --api-key=ragflow-xxxxx
# uv run mcp/server/server.py --host=127.0.0.1 --port=9382 --base-url=http://127.0.0.1:9380 --mode=self-host --api-key=ragflow-xxxxx

# Để khởi động máy chủ MCP ở chế độ host, thay vào đó chạy:
# uv run mcp/server/server.py --host=127.0.0.1 --port=9382 --base-url=http://127.0.0.1:9380 --mode=host
```

Trong đó: 

- `host`: Địa chỉ host của máy chủ MCP.
- `port`: Cổng lắng nghe của máy chủ MCP.
- `base_url`: Địa chỉ của máy chủ RAGFlow đang chạy.
- `mode`: Chế độ khởi động.
  - `self-host`: (mặc định) chế độ self-host.
  - `host`: chế độ host.
- `api_key`: Bắt buộc ở chế độ self-host để xác thực máy chủ MCP với máy chủ RAGFlow.

### Các transport

Máy chủ RAGFlow MCP hỗ trợ hai transport: transport SSE cũ (phục vụ tại `/sse`), được giới thiệu vào ngày 5 tháng 11 năm 2024 và không còn được hỗ trợ vào ngày 26 tháng 3 năm 2025, và transport streamable-HTTP (phục vụ tại `/mcp`). Transport SSE cũ và transport HTTP streamable với phản hồi JSON được bật theo mặc định.

### Khởi động từ Docker

#### 1. Bật máy chủ MCP

Máy chủ MCP được thiết kế như một thành phần tùy chọn bổ sung cho máy chủ RAGFlow và bị tắt theo mặc định. Để bật máy chủ MCP:

1. Điều hướng đến **docker/docker-compose.yml**.
2. Bỏ comment phần `services.ragflow.command` như được hiển thị bên dưới:

```yaml {6-13}
  services:
    ragflow:
      ...
      image: ${RAGFLOW_IMAGE}
      # Ví dụ cấu hình để thiết lập máy chủ MCP:
      command:
        - --enable-mcpserver
        - --mcp-host=0.0.0.0
        - --mcp-port=9382
        - --mcp-base-url=http://127.0.0.1:9380
        - --mcp-script-path=/ragflow/mcp/server/server.py
        - --mcp-mode=self-host
        - --mcp-host-api-key=ragflow-xxxxxxx
```

#### 2. Khởi động máy chủ RAGFlow với máy chủ MCP

Chạy `docker compose -f docker-compose.yml up` để khởi động máy chủ RAGFlow cùng với máy chủ MCP.

*ASCII art sau xác nhận khởi động thành công:*

```bash
  docker-ragflow-cpu-1  | Starting MCP Server on 0.0.0.0:9382 with base URL http://127.0.0.1:9380...
  docker-ragflow-cpu-1  | ...
  docker-ragflow-cpu-1  |  * Running on all addresses (0.0.0.0)
  docker-ragflow-cpu-1  |  * Running on http://127.0.0.1:9380
```

#### Khởi động máy chủ MCP mà không nâng cấp RAGFlow

:::info GHI NHẬN
Phần này được đóng góp bởi cộng tác viên cộng đồng [yiminghub2024](https://github.com/yiminghub2024). 👏
:::

1. Chuẩn bị tất cả các tệp và thư mục dành riêng cho MCP.  
2. Chỉnh sửa **docker-compose.yml** để bật MCP (mặc định bị tắt).
3. Khởi động máy chủ MCP:

```bash
docker compose -f docker-compose.yml up -d
```

### Kiểm tra trạng thái máy chủ MCP

Chạy lệnh sau để kiểm tra nhật ký của máy chủ RAGFlow và máy chủ MCP:

```bash
docker logs docker-ragflow-cpu-1
```

## Cân nhắc bảo mật

Vì công nghệ MCP vẫn đang ở giai đoạn đầu và chưa có thực tiễn tốt nhất chính thức nào được thiết lập cho xác thực hoặc ủy quyền, RAGFlow hiện sử dụng [API key](./acquire_ragflow_api_key.md) để xác thực danh tính. Tuy nhiên, trong môi trường công khai, giải pháp tạm thời này có thể khiến máy chủ MCP của bạn bị tấn công mạng tiềm ẩn. Do đó, khi chạy SSE server cục bộ, nên chỉ bind với localhost (`127.0.0.1`) thay vì tất cả các giao diện (`0.0.0.0`).
