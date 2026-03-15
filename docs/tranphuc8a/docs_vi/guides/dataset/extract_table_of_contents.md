---
sidebar_position: 4
slug: /enable_table_of_contents
sidebar_custom_props: {
  categoryIcon: LucideTableOfContents
}
---
# Trích xuất mục lục

Trích xuất mục lục (TOC) từ tài liệu để cung cấp RAG ngữ cảnh dài và cải thiện việc truy xuất.

---

Trong quá trình lập chỉ mục, kỹ thuật này sử dụng LLM để trích xuất và tạo thông tin chương, được thêm vào mỗi đoạn để cung cấp đủ ngữ cảnh toàn cục. Ở giai đoạn truy xuất, nó trước tiên sử dụng các đoạn khớp bởi tìm kiếm, sau đó bổ sung các đoạn còn thiếu dựa trên cấu trúc mục lục. Điều này giải quyết các vấn đề do phân mảnh đoạn và ngữ cảnh không đủ, cải thiện chất lượng câu trả lời.

:::danger CẢNH BÁO
Bật trích xuất TOC đòi hỏi nhiều bộ nhớ, tài nguyên tính toán và token.
:::

## Điều kiện tiên quyết

Mô hình chat mặc định của hệ thống được sử dụng để tóm tắt nội dung được phân cụm. Trước khi tiến hành, hãy đảm bảo bạn đã cấu hình đúng mô hình chat:

![Đặt mô hình mặc định](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/set_default_models.jpg)

## Bắt đầu nhanh

1. Điều hướng đến trang **Configuration**.

2. Bật **TOC Enhance**.

3. Để sử dụng kỹ thuật này trong quá trình truy xuất, hãy thực hiện một trong các thao tác sau:

   - Trong bảng **Chat setting** của ứng dụng chat, bật công tắc **TOC Enhance**.
   - Nếu bạn đang sử dụng agent, hãy nhấp vào thành phần agent **Retrieval** để chỉ định (các) tập dữ liệu và bật công tắc **TOC Enhance**.

## Câu hỏi thường gặp

### Các tệp đã được phân tích trước đó có được tìm kiếm sử dụng tính năng nâng cao TOC sau khi tôi bật `TOC Enhance` không?

Không. Chỉ các tệp được phân tích sau khi bạn bật **TOC Enhance** mới được tìm kiếm sử dụng tính năng nâng cao TOC. Để áp dụng tính năng này cho các tệp được phân tích trước khi bật **TOC Enhance**, bạn phải phân tích lại chúng.
