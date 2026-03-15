---
sidebar_position: 1
slug: /begin_component
sidebar_custom_props: {
  categoryIcon: LucideHome
}
---
# Thành phần Begin

Thành phần bắt đầu trong workflow.

---

**Begin** thiết lập lời chào mở đầu hoặc nhận đầu vào từ người dùng. Nó tự động có trên canvas khi bạn tạo agent (từ template hoặc từ đầu). Chỉ nên có một **Begin** trong workflow.

## Kịch bản sử dụng

**Begin** là bắt buộc trong mọi trường hợp và không thể xóa.

## Cấu hình

### Mode

Xác định cách kích hoạt workflow:

- Conversational: Agent được kích hoạt từ hội thoại.
- Task: Agent khởi chạy không qua hội thoại.
- Webhook: Nhận HTTP request bên ngoài qua webhook để tự động kích hoạt workflow.

### Methods

Các phương thức HTTP hỗ trợ, chỉ khả dụng khi chọn **Webhook**.

### Security

Phương thức xác thực (chỉ khi **Webhook**):

- **token**: Xác thực bằng token.
- **basic**: Xác thực cơ bản.
- **jwt**: Xác thực JWT.

### Schema

Xác định cấu trúc dữ liệu request trong chế độ **Webhook**:

- Content type:
  - `application/json`
  - `multipart/form-data`
  - `application/x-www-form-urlencoded`
  - `text-plain`
  - `application/octet-stream`
- Query parameters
- Header parameters
- Request body parameters

### Response

Chỉ khả dụng khi **Webhook**.

- **Accepted response**: Sau khi request hợp lệ, trả về thành công ngay và workflow chạy bất đồng bộ.
  - Mã HTTP cấu hình ở **Begin**, trong khoảng `200-399`.
- **Final response**: Hệ thống chỉ trả về sau khi toàn bộ workflow hoàn tất.
  - Mã HTTP cấu hình ở [message](./message.md), trong khoảng `200-399`.

### Opening greeting

**Chỉ cho Conversational mode.**

Lời chào mở đầu của agent trong hội thoại.

### Global variables

Bạn có thể định nghĩa biến toàn cục trong **Begin**, bắt buộc hoặc tùy chọn. Nhấp **+ Add variable** để thêm biến với các thuộc tính:

- **Name**: _Bắt buộc_
- **Type**: _Bắt buộc_ (`Single-line text`, `Paragraph text`, `Dropdown options`, `file upload`, `Number`, `Boolean`)
- **Key**: _Bắt buộc_
- **Optional**: Công tắc tùy chọn

:::tip LƯU Ý
Để truyền tham số từ client, gọi:

- HTTP method [Converse with agent](../../../references/http_api_reference.md#converse-with-agent), hoặc
- Python method [Converse with agent](../../../references/python_api_reference.md#converse-with-agent).
:::

:::danger QUAN TRỌNG
Nếu đặt key type là **file**, hãy đảm bảo số token tệp tải lên không vượt quá giới hạn token của nhà cung cấp mô hình, nếu không văn bản sẽ bị cắt.
:::

:::note
Bạn có thể tinh chỉnh hiệu quả parse/embedding bằng biến môi trường `DOC_BULK_SIZE` và `EMBEDDING_BATCH_SIZE`.
:::

## Câu hỏi thường gặp

### Tệp tải lên có nằm trong dataset không?

Không. Tệp tải lên làm input cho agent không được lưu trong dataset, nên không dùng OCR/DLR/TSR tích hợp hay chunking tích hợp của RAGFlow.

### Giới hạn kích thước tệp tải lên

Không có giới hạn kích thước _cụ thể_ cho tệp tải lên agent. Tuy nhiên, nhà cung cấp mô hình thường có giới hạn token (ví dụ 8196 đến 128k); nếu vượt giới hạn, phần văn bản thuần sẽ bị cắt.

:::tip LƯU Ý
`MAX_CONTENT_LENGTH` trong `/docker/.env` và `client_max_body_size` trong `/docker/nginx/nginx.conf` áp dụng cho upload vào dataset hoặc File system của RAGFlow, KHÔNG áp dụng cho trường hợp này.
:::
