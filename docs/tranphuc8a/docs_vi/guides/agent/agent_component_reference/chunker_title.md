---
sidebar_position: 31
slug: /chunker_title_component
sidebar_custom_props: {
  categoryIcon: LucideBlocks
}
---
# Thành phần phân đoạn theo tiêu đề

Một thành phần chia văn bản thành các đoạn theo cấp độ tiêu đề.

---

Thành phần **Title chunker** là bộ tách văn bản dùng cấp tiêu đề được chỉ định làm dấu phân tách để xác định ranh giới đoạn và tạo các chunk.

## Kịch bản sử dụng

Thành phần **Title chunker** là tùy chọn, thường đặt ngay sau **Parser**.

:::caution CẢNH BÁO
Đặt **Title chunker** sau **Token chunker** là không hợp lệ và sẽ gây lỗi. Hạn chế này hiện chưa được hệ thống cưỡng chế tự động, bạn cần tự chú ý.
:::

## Cấu hình

### Hierarchy

Chỉ định cấp tiêu đề để xác định ranh giới đoạn:

- H1
- H2
- H3 (Mặc định)
- H4

Nhấp **+ Add** để thêm cấp tiêu đề hoặc cập nhật trường **Regular Expressions** tương ứng cho mẫu tiêu đề tùy chỉnh.

### Output

Tên biến toàn cục cho đầu ra của thành phần **Title chunker**, có thể được tham chiếu bởi các thành phần phía sau trong ingestion pipeline.

- Mặc định: `chunks`
- Kiểu: `Array<Object>`
