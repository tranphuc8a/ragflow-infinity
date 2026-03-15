---
sidebar_position: 32
slug: /chunker_token_component
sidebar_custom_props: {
  categoryIcon: LucideBlocks
}
---
# Thành phần phân đoạn theo token

Một thành phần chia văn bản thành các đoạn, tôn trọng giới hạn token tối đa và dùng dấu phân tách để tìm điểm cắt tối ưu.

---

Thành phần **Token chunker** là bộ tách văn bản tạo chunk theo độ dài token tối đa được khuyến nghị, dùng dấu phân tách để đảm bảo điểm cắt hợp lý. Nó chia văn bản dài thành các đoạn có kích thước phù hợp và liên quan ngữ nghĩa.

## Kịch bản sử dụng

Thành phần **Token chunker** là tùy chọn, thường đặt ngay sau **Parser** hoặc **Title chunker**.

## Cấu hình

### Recommended chunk size

Giới hạn token tối đa được khuyến nghị cho mỗi chunk. Thành phần **Token chunker** tạo chunk tại các dấu phân tách đã chỉ định. Nếu chạm ngưỡng token trước khi gặp dấu phân tách, chunk sẽ được tạo tại điểm đó.

### Overlapped percent (%)

Xác định phần trăm chồng lấp giữa các chunk. Mức chồng lấp phù hợp giúp giữ tính liền mạch ngữ nghĩa mà không tạo quá nhiều token dư thừa cho LLM.

- Mặc định: 0
- Tối đa: 30%

### Delimiters

Mặc định là `\n`. Nhấp nút **Recycle bin** bên phải để xóa, hoặc nhấp **+ Add** để thêm dấu phân tách.

### Output

Tên biến toàn cục cho đầu ra của thành phần **Token chunker**, có thể được tham chiếu bởi các thành phần phía sau trong ingestion pipeline.

- Mặc định: `chunks`
- Kiểu: `Array<Object>`
