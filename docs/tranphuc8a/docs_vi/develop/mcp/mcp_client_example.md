---
sidebar_position: 3
slug: /mcp_client
sidebar_custom_props: {
  categoryIcon: LucideBookMarked
}

---
# Ví dụ MCP client RAGFlow

Ví dụ MCP client bằng Python và curl.

------

## Ví dụ MCP Python client

Chúng tôi cung cấp ví dụ MCP client *nguyên mẫu* để kiểm thử [tại đây](https://github.com/infiniflow/ragflow/blob/main/mcp/client/client.py).

:::info QUAN TRỌNG
Nếu máy chủ MCP của bạn đang chạy ở chế độ host, hãy bao gồm API key đã lấy trong `headers` của client khi kết nối bất đồng bộ:

```python
async with sse_client("http://localhost:9382/sse", headers={"api_key": "YOUR_KEY_HERE"}) as streams:
    # Phần còn lại của code...
```

Ngoài ra, để tuân theo [OAuth 2.1 Mục 5](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-5), bạn có thể chạy code sau *thay thế* để kết nối với máy chủ MCP:

```python
async with sse_client("http://localhost:9382/sse", headers={"Authorization": "YOUR_KEY_HERE"}) as streams:
    # Phần còn lại của code...
```
:::

## Sử dụng curl để tương tác với máy chủ MCP RAGFlow

Khi tương tác với máy chủ MCP qua HTTP requests, hãy theo trình tự khởi tạo sau:

1. **Client gửi yêu cầu `initialize`** với phiên bản giao thức và khả năng.
2. **Server phản hồi với phản hồi `initialize`**, bao gồm giao thức được hỗ trợ và khả năng.
3. **Client xác nhận sẵn sàng với thông báo `initialized`**.  
   _Kết nối được thiết lập giữa client và server, và các thao tác tiếp theo (như liệt kê công cụ) có thể tiến hành._

:::tip LƯU Ý
Để biết thêm thông tin về quá trình khởi tạo này, hãy xem [tại đây](https://modelcontextprotocol.io/docs/concepts/architecture#1-initialization). 
:::

Trong các phần sau, chúng tôi sẽ hướng dẫn bạn qua một quá trình gọi công cụ hoàn chỉnh.

### 1. Lấy session ID

Mỗi yêu cầu curl với máy chủ MCP phải bao gồm session ID:

```bash
$ curl -N -H "api_key: YOUR_API_KEY" http://127.0.0.1:9382/sse
```

:::tip LƯU Ý
Xem [tại đây](../acquire_ragflow_api_key.md) để biết thông tin về cách lấy API key.
:::

#### Transport

Transport sẽ stream các thông báo như kết quả công cụ, phản hồi server và ping keepalive.

_Server trả về session ID:_

```bash
event: endpoint
data: /messages/?session_id=5c6600ef61b845a788ddf30dceb25c54
```

### 2. Gửi yêu cầu `Initialize`

Client gửi yêu cầu `initialize` với phiên bản giao thức và khả năng:

```bash
session_id="5c6600ef61b845a788ddf30dceb25c54" && \

curl -X POST "http://127.0.0.1:9382/messages/?session_id=$session_id" \
  -H "api_key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
      "protocolVersion": "1.0",
      "capabilities": {},
      "clientInfo": {
        "name": "ragflow-mcp-client",
        "version": "0.1"
      }
    }
  }'
```

### 3. Xác nhận sẵn sàng

Client xác nhận sẵn sàng với thông báo `initialized`:

```bash
curl -X POST "http://127.0.0.1:9382/messages/?session_id=$session_id" \
  -H "api_key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "notifications/initialized",
    "params": {}
  }'
```

### 4. Liệt kê công cụ

```bash
curl -X POST "http://127.0.0.1:9382/messages/?session_id=$session_id" \
  -H "api_key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/list",
    "params": {}
  }'
```

### 5. Gọi công cụ

```bash
curl -X POST "http://127.0.0.1:9382/messages/?session_id=$session_id" \
  -H "api_key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 4,
    "method": "tools/call",
    "params": {
      "name": "ragflow_retrieval",
      "arguments": {
        "dataset_ids": ["your-dataset-id"],
        "question": "Câu hỏi của bạn"
      }
    }
  }'
```
