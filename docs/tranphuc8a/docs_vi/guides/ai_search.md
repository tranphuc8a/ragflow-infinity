---
sidebar_position: 2
slug: /ai_search
sidebar_custom_props: {
	categoryIcon: LucideSearch
}
---
# Tìm kiếm

Thực hiện tìm kiếm AI.

---

Tìm kiếm AI là cuộc hội thoại AI một lượt sử dụng chiến lược truy xuất được xác định trước (tìm kiếm kết hợp giữa độ tương đồng từ khóa có trọng số và độ tương đồng vector có trọng số) cùng với mô hình chat mặc định của hệ thống. Tính năng này không bao gồm các chiến lược RAG nâng cao như đồ thị kiến thức, từ khóa tự động, hoặc câu hỏi tự động. Các đoạn văn bản liên quan được liệt kê bên dưới phản hồi của mô hình chat theo thứ tự giảm dần dựa trên điểm tương đồng.

![Tạo ứng dụng tìm kiếm](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/create_search_app.jpg)

![Giao diện tìm kiếm](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/search_view.jpg)

:::tip LƯU Ý
Khi gỡ lỗi trợ lý chat của bạn, bạn có thể dùng tìm kiếm AI như một tham chiếu để xác minh cài đặt mô hình và chiến lược truy xuất.
:::

## Điều kiện tiên quyết

- Đảm bảo bạn đã cấu hình các mô hình mặc định của hệ thống trên trang **Nhà cung cấp mô hình**.
- Đảm bảo các tập dữ liệu đã được cấu hình đúng cách và các tài liệu đã hoàn tất quá trình phân tích tệp.

## Câu hỏi thường gặp

### Sự khác biệt chính giữa tìm kiếm AI và chat AI là gì?

Chat là cuộc hội thoại AI nhiều lượt, nơi bạn có thể định nghĩa chiến lược truy xuất (điểm reranking có trọng số có thể được dùng thay cho độ tương đồng vector có trọng số trong tìm kiếm kết hợp) và chọn mô hình chat. Trong chat AI, bạn có thể cấu hình các chiến lược RAG nâng cao như đồ thị kiến thức, từ khóa tự động, và câu hỏi tự động cho trường hợp cụ thể của mình. Các đoạn văn bản được truy xuất không được hiển thị cùng với câu trả lời.
