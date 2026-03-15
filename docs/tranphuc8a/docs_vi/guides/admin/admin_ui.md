---
sidebar_position: 1
slug: /admin_ui
sidebar_custom_props: {
  categoryIcon: LucidePalette
}
---
# Giao diện quản trị (Admin UI)

Giao diện quản trị RAGFlow là giao diện dựa trên web cung cấp khả năng giám sát trạng thái hệ thống toàn diện và quản lý người dùng.

## Truy cập Admin UI

Để truy cập giao diện quản trị RAGFlow, hãy thêm `/admin` vào địa chỉ web UI, ví dụ: `http://[RAGFLOW_WEB_UI_ADDR]/admin`, thay `[RAGFLOW_WEB_UI_ADDR]` bằng địa chỉ web UI RAGFlow thực tế.

### Thông tin đăng nhập mặc định
| Tên người dùng     | Mật khẩu |
|--------------------|----------|
| `admin@ragflow.io` | `admin`  |

## Tổng quan Admin UI

### Trạng thái dịch vụ

Trang trạng thái dịch vụ hiển thị tất cả các dịch vụ trong hệ thống RAGFlow.

- **Danh sách dịch vụ**: Xem tất cả dịch vụ trong bảng.
- **Lọc**: Sử dụng nút lọc để lọc dịch vụ theo **Loại dịch vụ**.
- **Tìm kiếm**: Sử dụng thanh tìm kiếm để nhanh chóng tìm dịch vụ theo **Tên** hoặc **Loại dịch vụ**.
- **Thao tác** (di chuột qua hàng để thấy nút hành động):
  - **Thông tin thêm**: Hiển thị thông tin cấu hình bổ sung của dịch vụ trong hộp thoại.
  - **Chi tiết dịch vụ**: Hiển thị thông tin trạng thái chi tiết của dịch vụ trong hộp thoại. Tùy theo loại dịch vụ, thông tin trạng thái có thể được hiển thị dưới dạng văn bản thuần túy, danh sách dữ liệu key-value, bảng dữ liệu hoặc biểu đồ cột.

### Quản lý người dùng

Trang quản lý người dùng cung cấp các công cụ toàn diện để quản lý tất cả người dùng trong hệ thống RAGFlow.

- **Danh sách người dùng**: Xem tất cả người dùng trong bảng.
- **Tìm kiếm người dùng**: Sử dụng thanh tìm kiếm để tìm người dùng theo email hoặc biệt danh.
- **Lọc người dùng**: Nhấp vào biểu tượng lọc để lọc theo **Trạng thái**.
- Nhấp nút **"Người dùng mới"** để tạo tài khoản người dùng mới trong hộp thoại.
- Kích hoạt hoặc vô hiệu hóa người dùng bằng công tắc bật/tắt trong cột **Kích hoạt**, thay đổi có hiệu lực ngay lập tức.
- **Thao tác** (di chuột qua hàng để thấy nút hành động):
  - **Xem chi tiết**: Điều hướng đến trang chi tiết người dùng để xem thông tin toàn diện.
  - **Đổi mật khẩu**: Buộc đặt lại mật khẩu của người dùng.
  - **Xóa người dùng**: Xóa người dùng khỏi hệ thống với xác nhận.

### Chi tiết người dùng

Trang chi tiết người dùng hiển thị thông tin chi tiết của người dùng và tất cả tài nguyên được tạo hoặc sở hữu bởi người dùng đó, được phân loại theo loại (ví dụ: Dataset, Agent).
