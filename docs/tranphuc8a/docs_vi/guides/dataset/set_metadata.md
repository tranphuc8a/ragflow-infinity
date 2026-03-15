---
sidebar_position: -7
slug: /set_metadata
sidebar_custom_props: {
  categoryIcon: LucideCode
}
---
# Thiết lập metadata

Thêm metadata thủ công cho tệp đã tải lên.

---

Trên trang **Dataset**, bạn có thể thêm metadata cho bất kỳ tệp nào đã tải lên. Cách này cho phép bạn “gắn thẻ” thêm thông tin như URL, tác giả, ngày tháng... vào tệp hiện có. Trong chat AI, các thông tin này sẽ được gửi cùng chunk truy xuất tới LLM để tạo nội dung.

Ví dụ, nếu bạn có dataset gồm các tệp HTML và muốn LLM trích dẫn URL nguồn khi trả lời, hãy thêm tham số `"url"` vào metadata của từng tệp.

![Set metadata](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/set_metadata.jpg)

:::tip LƯU Ý
Hãy đảm bảo metadata ở định dạng JSON, nếu không thay đổi của bạn sẽ không được áp dụng.
:::

![Input metadata](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/input_metadata.jpg)

## API liên quan

[Retrieve chunks](../../references/http_api_reference.md#retrieve-chunks)

## Câu hỏi thường gặp

### Tôi có thể thiết lập metadata cho nhiều tài liệu cùng lúc không?

Từ v0.23.0 trở đi, bạn có thể đặt metadata từng tài liệu hoặc để LLM tự sinh metadata cho nhiều tệp. Xem [Extract metadata](./auto_metadata.md).
