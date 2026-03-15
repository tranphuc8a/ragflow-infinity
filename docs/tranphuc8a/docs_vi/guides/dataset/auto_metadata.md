---
sidebar_position: -6
slug: /auto_metadata
sidebar_custom_props: {
   categoryIcon: LucideFileCodeCorner
}
---
# Tự động trích xuất siêu dữ liệu

Tự động trích xuất siêu dữ liệu từ các tệp đã tải lên.

---

RAGFlow v0.23.0 giới thiệu tính năng Auto-metadata, sử dụng các mô hình ngôn ngữ lớn để tự động trích xuất và tạo siêu dữ liệu cho các tệp—loại bỏ nhu cầu nhập liệu thủ công. Trong một pipeline RAG điển hình, siêu dữ liệu phục vụ hai mục đích chính:

- Trong giai đoạn truy xuất: Lọc bỏ các tài liệu không liên quan, thu hẹp phạm vi tìm kiếm để cải thiện độ chính xác truy xuất.
- Trong giai đoạn tạo: Nếu một đoạn văn bản được truy xuất, siêu dữ liệu liên quan của nó cũng được chuyển đến LLM, cung cấp thông tin ngữ cảnh phong phú hơn về tài liệu nguồn để hỗ trợ tạo câu trả lời.


:::danger CẢNH BÁO
Bật trích xuất TOC đòi hỏi nhiều bộ nhớ, tài nguyên tính toán và token.
:::



## Quy trình

1. Trên trang **Configuration** của tập dữ liệu, chọn một mô hình lập chỉ mục, sẽ được sử dụng để tạo đồ thị tri thức, RAPTOR, auto-metadata, auto-keyword và các tính năng auto-question cho tập dữ liệu này.

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/indexing_model.png)


2. Nhấp vào **Auto metadata** **>** **Settings** để đi đến trang cấu hình cho các quy tắc tạo siêu dữ liệu tự động.

   _Trang cấu hình cho các quy tắc tạo siêu dữ liệu tự động xuất hiện._

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/auto_metadata_settings.png)

3. Nhấp vào **+** để thêm các trường mới và vào trang cấu hình.

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/metadata_field_settings.png)

4. Nhập tên trường, chẳng hạn như Author, và thêm mô tả cùng ví dụ trong phần Description. Điều này cung cấp ngữ cảnh cho mô hình ngôn ngữ lớn (LLM) để trích xuất giá trị chính xác hơn. Nếu để trống, LLM sẽ trích xuất các giá trị chỉ dựa trên tên trường.

5. Để hạn chế LLM tạo siêu dữ liệu từ một danh sách được xác định trước, bật chế độ Restrict to defined values và thêm thủ công các giá trị được phép. LLM sau đó sẽ chỉ tạo ra kết quả từ phạm vi preset này.

6. Sau khi được cấu hình, bật công tắc Auto-metadata trên trang Configuration. Tất cả các tệp được tải lên mới sẽ có các quy tắc này được áp dụng trong quá trình phân tích. Đối với các tệp đã được xử lý, bạn phải phân tích lại chúng để kích hoạt việc tạo siêu dữ liệu. Sau đó bạn có thể sử dụng chức năng lọc để kiểm tra trạng thái tạo siêu dữ liệu của các tệp.

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/enable_auto_metadata.png)
