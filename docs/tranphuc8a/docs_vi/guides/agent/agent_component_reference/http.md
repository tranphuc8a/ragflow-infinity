---
sidebar_position: 30
slug: /http_request_component
sidebar_custom_props: {
  categoryIcon: RagHTTP
}
---
# Thành phần HTTP request

Một thành phần gọi dịch vụ từ xa.

---

Thành phần **HTTP request** cho phép truy cập API/dịch vụ từ xa bằng URL và phương thức HTTP, rồi nhận phản hồi. Bạn có thể tùy chỉnh header, tham số, proxy và timeout, dùng các phương thức phổ biến như GET và POST. Thành phần này hữu ích khi trao đổi dữ liệu với hệ thống bên ngoài trong workflow.

## Điều kiện tiên quyết

- API hoặc dịch vụ từ xa có thể truy cập.
- Thêm Token/thông tin xác thực vào header nếu dịch vụ đích yêu cầu.

## Cấu hình

### Url

*Bắt buộc*. Địa chỉ yêu cầu đầy đủ, ví dụ: `http://api.example.com/data`.

### Method

Phương thức HTTP để chọn:

- GET
- POST
- PUT

### Timeout

Thời gian chờ tối đa (giây). Mặc định `60`.

### Headers

Bạn có thể đặt header tùy chỉnh, ví dụ:

```http
{
  "Accept": "application/json",
  "Cache-Control": "no-cache",
  "Connection": "keep-alive"
}
```

### Proxy

Tùy chọn. Địa chỉ proxy dùng cho yêu cầu này.

### Clean HTML

`Boolean`: Có loại bỏ thẻ HTML khỏi kết quả trả về và chỉ giữ văn bản thuần hay không.

### Parameter

*Tùy chọn*. Tham số gửi kèm yêu cầu HTTP, hỗ trợ key-value:

- Để gán giá trị bằng biến hệ thống động, đặt là Variable.
- Để ghi đè giá trị động trong một số điều kiện và dùng giá trị tĩnh cố định, chọn Value.

:::tip LƯU Ý
- Với GET, tham số được nối vào cuối URL.
- Với POST/PUT, tham số được gửi trong phần body.
:::

#### Ví dụ cấu hình

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/http_settings.png)

#### Ví dụ phản hồi

```html
{ "args": { "App": "RAGFlow", "Query": "How to do?", "Userid": "241ed25a8e1011f0b979424ebc5b108b" }, "headers": { "Accept": "/", "Accept-Encoding": "gzip, deflate, br, zstd", "Cache-Control": "no-cache", "Host": "httpbin.org", "User-Agent": "python-requests/2.32.2", "X-Amzn-Trace-Id": "Root=1-68c9210c-5aab9088580c130a2f065523" }, "origin": "185.36.193.38", "url": "https://httpbin.org/get?Userid=241ed25a8e1011f0b979424ebc5b108b&App=RAGFlow&Query=How+to+do%3F" }
```

### Output

Tên biến toàn cục cho đầu ra của thành phần HTTP request, có thể được tham chiếu bởi thành phần khác trong workflow.

- `Result`: `string` phản hồi do dịch vụ từ xa trả về.

## Ví dụ

Ví dụ sử dụng: workflow gửi GET request từ **Begin** tới `https://httpbin.org/get` thông qua **HTTP Request_0**, truyền tham số tới server, rồi xuất kết quả qua **Message_0**.

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/http_usage.PNG)
