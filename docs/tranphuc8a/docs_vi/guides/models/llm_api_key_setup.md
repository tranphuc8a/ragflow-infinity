---
sidebar_position: 1
slug: /llm_api_key_setup
sidebar_custom_props: {
  categoryIcon: LucideKey
}
---
# Cấu hình API key mô hình

API key là cần thiết để RAGFlow tương tác với mô hình AI trực tuyến. Hướng dẫn này cung cấp thông tin về việc thiết lập API key mô hình của bạn trong RAGFlow.

## Lấy API key mô hình

RAGFlow hỗ trợ hầu hết các LLM chính thống. Vui lòng tham khảo [Các mô hình được hỗ trợ](../../references/supported_models.mdx) để xem danh sách đầy đủ các mô hình được hỗ trợ. Bạn cần đăng ký API key mô hình trực tuyến. Lưu ý rằng hầu hết các nhà cung cấp LLM cấp tín dụng dùng thử cho các tài khoản mới tạo, sẽ hết hạn sau vài tháng, hoặc một lượng hạn ngạch miễn phí có giới hạn.

:::note
Nếu bạn thấy LLM trực tuyến của mình không có trong danh sách, đừng nản lòng. Danh sách đang được mở rộng, và bạn có thể [gửi yêu cầu tính năng](https://github.com/infiniflow/ragflow/issues/new?assignees=&labels=feature+request&projects=&template=feature_request.yml&title=%5BFeature+Request%5D%3A+) cho chúng tôi! Ngoài ra, nếu bạn có các mô hình tùy chỉnh hoặc triển khai cục bộ, bạn có thể [liên kết chúng với RAGFlow bằng Ollama, Xinference hoặc LocalAI](./deploy_local_llm.mdx).
:::

## Cấu hình API key mô hình

Bạn có hai lựa chọn để cấu hình API key mô hình:

- Cấu hình trong **service_conf.yaml.template** trước khi khởi động RAGFlow.
- Cấu hình trên trang **Nhà cung cấp mô hình** sau khi đăng nhập vào RAGFlow.

### Cấu hình API key mô hình trước khi khởi động RAGFlow

1. Điều hướng đến **./docker/ragflow**.
2. Tìm mục **user_default_llm**:
   - Cập nhật `factory` bằng LLM bạn đã chọn.
   - Cập nhật `api_key` bằng của bạn.
   - Cập nhật `base_url` nếu bạn sử dụng proxy để kết nối với dịch vụ từ xa.
3. Khởi động lại hệ thống để áp dụng thay đổi.
4. Đăng nhập vào RAGFlow.
   _Sau khi đăng nhập vào RAGFlow, bạn sẽ thấy mô hình đã chọn xuất hiện trong **Các mô hình đã thêm** trên trang **Nhà cung cấp mô hình**._

### Cấu hình API key mô hình sau khi đăng nhập vào RAGFlow

:::caution CẢNH BÁO
Sau khi đăng nhập vào RAGFlow, việc cấu hình API key mô hình qua tệp **service_conf.yaml.template** sẽ không còn có hiệu lực.
:::

Sau khi đăng nhập vào RAGFlow, bạn *chỉ* có thể cấu hình API Key trên trang **Nhà cung cấp mô hình**:

1. Nhấp vào logo của bạn ở góc trên bên phải trang **>** **Nhà cung cấp mô hình**.
2. Tìm thẻ mô hình của bạn trong **Các mô hình sẽ thêm** và nhấp **Thêm mô hình**.
3. Dán API key mô hình của bạn.
4. Điền URL cơ sở nếu bạn sử dụng proxy để kết nối với dịch vụ từ xa.
5. Nhấp **OK** để xác nhận thay đổi.
