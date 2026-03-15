---
sidebar_position: 4
slug: /message_component
sidebar_custom_props: {
  categoryIcon: LucideMessageSquareReply
}
---
# Thành phần Message

Một thành phần gửi thông điệp tĩnh hoặc động.

---

Là thành phần cuối của workflow, **Message** trả về dữ liệu đầu ra cuối cùng của workflow kèm nội dung thông điệp đã định nghĩa trước. Hệ thống sẽ chọn ngẫu nhiên một thông điệp nếu có nhiều thông điệp.

## Cấu hình

### Status

Mã trạng thái HTTP (`200` ~ `399`) trả về khi toàn bộ workflow hoàn tất. Chỉ khả dụng khi bạn chọn **Final response** ở **Execution mode** trong thành phần [Begin](./begin.md).

### Messages

Thông điệp cần gửi. Nhấp `(x)` hoặc gõ `/` để chèn biến nhanh.

Nhấp **+ Add message** để thêm lựa chọn thông điệp. Khi có nhiều thông điệp, thành phần **Message** sẽ chọn ngẫu nhiên một thông điệp để gửi.

### Save to memory

Lưu cuộc hội thoại vào các memory được chỉ định. Mở danh sách để chọn tất cả memory khả dụng hoặc chọn từng memory cụ thể.

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/save_to_memory.png)
