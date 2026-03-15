---
sidebar_position: 0
slug: /admin_service
sidebar_custom_props: {
  categoryIcon: LucideActivity
}
---
# Dịch vụ quản trị (Admin Service)

Dịch vụ quản trị là dịch vụ quản lý backend cốt lõi của hệ thống RAGFlow, cung cấp khả năng quản trị hệ thống toàn diện thông qua các giao diện API tập trung để quản lý và điều khiển toàn bộ nền tảng. Áp dụng kiến trúc client-server, dịch vụ hỗ trợ truy cập và thao tác qua cả giao diện Web UI và Admin CLI, đảm bảo thực thi các tác vụ quản trị linh hoạt và hiệu quả.

Các chức năng cốt lõi của Dịch vụ quản trị bao gồm giám sát theo thời gian thực trạng thái hoạt động của máy chủ RAGFlow và các thành phần phụ thuộc quan trọng—như MySQL, Elasticsearch, Redis và MinIO—cùng với quản lý người dùng đầy đủ tính năng. Ở chế độ quản trị viên, dịch vụ cho phép thực hiện các thao tác chính như xem thông tin người dùng, tạo người dùng, cập nhật mật khẩu, chỉnh sửa trạng thái kích hoạt và xóa hoàn toàn dữ liệu người dùng. Các tính năng này vẫn có thể truy cập qua Admin CLI ngay cả khi giao diện quản lý web bị tắt, đảm bảo hệ thống luôn được kiểm soát mọi lúc.

Với thiết kế giao diện thống nhất, Dịch vụ quản trị kết hợp sự tiện lợi của quản trị trực quan với hiệu quả và ổn định của các thao tác dòng lệnh, phục vụ như nền tảng quan trọng cho hoạt động đáng tin cậy và quản lý an toàn của hệ thống RAGFlow.

## Khởi động Dịch vụ quản trị

### Khởi chạy từ mã nguồn

1. Trước khi khởi động Dịch vụ quản trị, hãy đảm bảo hệ thống RAGFlow đã được khởi động.

2. Khởi chạy từ mã nguồn:

   ```bash
   python admin/server/admin_server.py
   ```

   Dịch vụ sẽ khởi động và lắng nghe các kết nối đến từ CLI trên cổng đã cấu hình.

### Sử dụng Docker image

1. Trước khi khởi động, hãy cấu hình tệp `docker_compose.yml` để kích hoạt admin server:

   ```bash
   command:
     - --enable-adminserver
   ```

2. Khởi động các container, dịch vụ sẽ khởi động và lắng nghe các kết nối đến từ CLI trên cổng đã cấu hình.
