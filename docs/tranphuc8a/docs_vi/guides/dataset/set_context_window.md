---
sidebar_position: -8
slug: /set_context_window
sidebar_custom_props: {
   categoryIcon: LucideListChevronsUpDown
}
---
# Thiết lập kích thước cửa sổ ngữ cảnh

Thiết lập kích thước cửa sổ ngữ cảnh cho hình ảnh và bảng để cải thiện hiệu năng RAG ngữ cảnh dài.

---

RAGFlow sử dụng DeepDoc tích hợp cùng các mô hình tài liệu bên ngoài như MinerU và Docling để phân tích bố cục tài liệu. Ở các phiên bản trước, hình ảnh và bảng được trích xuất theo bố cục tài liệu được xem là chunk độc lập. Vì vậy nếu truy vấn không khớp trực tiếp nội dung ảnh/bảng, các phần tử này có thể không được truy xuất. Trong tài liệu thực tế, biểu đồ/bảng thường gắn với văn bản xung quanh mô tả chúng, nên khả năng truy xuất theo ngữ cảnh là rất quan trọng.

Để giải quyết, RAGFlow 0.23.0 giới thiệu tính năng **Image & table context window**. Lấy cảm hứng từ dự án RAG đa phương thức mã nguồn mở RAG-Anything, tính năng này cho phép gom văn bản xung quanh và phần tử trực quan lân cận thành một chunk theo kích thước cửa sổ do người dùng cấu hình. Điều này giúp chúng được truy xuất cùng nhau, cải thiện đáng kể độ chính xác truy hồi cho biểu đồ và bảng.

## Quy trình

1. Trên trang **Configuration** của dataset, tìm thanh trượt **Image & table context window**:

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/image_table_context_window.png)

2. Điều chỉnh số lượng token ngữ cảnh theo nhu cầu.

   *Con số trong khung đỏ thể hiện khoảng **N token** văn bản phía trên và phía dưới ảnh/bảng sẽ được lấy và chèn vào chunk ảnh/bảng như thông tin ngữ cảnh. Quá trình này tối ưu ranh giới theo dấu câu để giữ tính toàn vẹn ngữ nghĩa.*
