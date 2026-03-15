---
sidebar_position: 4
slug: /enable_excel2html
sidebar_custom_props: {
  categoryIcon: LucideToggleRight
}
---
# Bật Excel2HTML

Chuyển đổi bảng tính Excel phức tạp thành bảng HTML.

---

Khi sử dụng phương pháp phân đoạn **General**, bạn có thể bật chế độ **Excel to HTML** để chuyển đổi các tệp bảng tính thành bảng HTML. Nếu bị tắt, các bảng trong bảng tính sẽ được biểu diễn dưới dạng các cặp khóa-giá trị. Đối với các bảng phức tạp không thể được biểu diễn đơn giản theo cách này, bạn phải bật tính năng này.

:::caution CẢNH BÁO
Tính năng này bị tắt theo mặc định. Nếu tập dữ liệu của bạn chứa các bảng tính với bảng phức tạp và bạn không bật tính năng này, RAGFlow sẽ không báo lỗi nhưng các bảng của bạn có thể bị hiển thị sai.
:::

## Kịch bản

Hoạt động với các bảng phức tạp không thể được biểu diễn dưới dạng các cặp khóa-giá trị. Ví dụ bao gồm các bảng trong bảng tính có nhiều cột, bảng với các ô được hợp nhất hoặc nhiều bảng trong một tờ. Trong những trường hợp như vậy, hãy xem xét việc chuyển đổi các bảng trong bảng tính này thành bảng HTML.

## Lưu ý

- Tính năng Excel2HTML chỉ áp dụng cho các tệp bảng tính (XLSX hoặc XLS (Excel 97-2003)).
- Tính năng này liên quan đến phương pháp phân đoạn **General**. Nói cách khác, nó chỉ khả dụng *khi* bạn chọn phương pháp phân đoạn **General**.
- Khi tính năng này được bật, các bảng trong bảng tính có hơn 12 hàng sẽ được chia thành các đoạn mỗi đoạn 12 hàng.

## Quy trình

1. Trên trang **Configuration** của tập dữ liệu, chọn **General** làm phương pháp phân đoạn.

   _Công tắc **Excel to HTML** xuất hiện._

2. Bật **Excel to HTML** nếu tập dữ liệu của bạn chứa các bảng trong bảng tính phức tạp không thể được biểu diễn dưới dạng các cặp khóa-giá trị.
3. Để **Excel to HTML** tắt nếu tập dữ liệu của bạn không có bảng trong bảng tính hoặc nếu các bảng trong bảng tính có thể được biểu diễn dưới dạng các cặp khóa-giá trị.
4. Nếu hỏi đáp liên quan đến bảng phức tạp không đạt yêu cầu, hãy kiểm tra xem **Excel to HTML** có được bật không.

## Câu hỏi thường gặp

### Tôi có nên bật tính năng này cho các tệp PDF có bảng phức tạp không?

Không. Tính năng này chỉ áp dụng cho các tệp bảng tính. Bật **Excel to HTML** không ảnh hưởng đến các tệp PDF của bạn.
