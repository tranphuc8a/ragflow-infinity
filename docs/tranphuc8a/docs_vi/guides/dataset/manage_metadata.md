---
sidebar_position: -5
slug: /manage_metadata
sidebar_custom_props: {
  categoryIcon: LucideCode
}
---
# Quản lý siêu dữ liệu

Quản lý siêu dữ liệu cho tập dữ liệu và các tài liệu riêng lẻ của bạn.

---

Từ phiên bản v0.23.0 trở đi, RAGFlow cho phép bạn quản lý siêu dữ liệu cả ở cấp độ tập dữ liệu và cho từng tệp riêng lẻ.

## Quy trình

1. Nhấp vào **Metadata** trong tập dữ liệu của bạn để truy cập trang **Manage Metadata**.

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/click_metadata.png)

2. Trên trang **Manage Metadata**, bạn có thể thực hiện một trong các thao tác sau:
   - Edit Values: Bạn có thể sửa đổi các giá trị hiện có. Nếu bạn đổi tên hai giá trị thành giống nhau, chúng sẽ tự động được hợp nhất.
   - Delete: Bạn có thể xóa các giá trị cụ thể hoặc toàn bộ trường. Những thay đổi này sẽ áp dụng cho tất cả các tệp liên quan.

   _Trang cấu hình cho các quy tắc tạo siêu dữ liệu tự động xuất hiện._

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/manage_metadata.png)

3. Để quản lý siêu dữ liệu cho một tệp duy nhất, hãy điều hướng đến trang chi tiết của tệp như hiển thị bên dưới. Nhấp vào phương pháp phân tích (ví dụ: **General**), sau đó chọn **Set Metadata** để xem hoặc chỉnh sửa siêu dữ liệu của tệp. Tại đây, bạn có thể thêm, xóa hoặc sửa đổi các trường siêu dữ liệu cho tệp cụ thể này. Bất kỳ chỉnh sửa nào được thực hiện ở đây sẽ được phản ánh trong thống kê toàn cục trên trang quản lý Metadata chính cho cơ sở tri thức.

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/set_metadata.png)
![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/edit_metadata.png)

4. Chức năng lọc hoạt động ở hai cấp độ: quản lý cơ sở tri thức và truy xuất. Trong tập dữ liệu, nhấp vào nút Filter để xem số lượng tệp liên quan đến từng giá trị dưới các trường siêu dữ liệu hiện có. Bằng cách chọn các giá trị cụ thể, bạn có thể hiển thị tất cả các tệp được liên kết.

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/filter_metadata.png)

5. Lọc siêu dữ liệu cũng được hỗ trợ trong giai đoạn truy xuất. Trong Chat, ví dụ, bạn có thể đặt các quy tắc lọc siêu dữ liệu sau khi cấu hình cơ sở tri thức:

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/metadata_filtering_rules.png)

- Chế độ **Automatic**: Hệ thống tự động lọc tài liệu dựa trên truy vấn của người dùng và siêu dữ liệu hiện có trong cơ sở tri thức.
- Chế độ **Semi-automatic**: Người dùng trước tiên xác định phạm vi lọc ở cấp độ trường (ví dụ: cho **Author**), sau đó hệ thống tự động lọc trong phạm vi preset đó.
- Chế độ **Manual**: Người dùng đặt thủ công các điều kiện lọc chính xác, cụ thể theo giá trị, được hỗ trợ bởi các toán tử như **Equals**, **Not equals**, **In**, **Not in** và nhiều hơn nữa.
