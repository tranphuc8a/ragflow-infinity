---
sidebar_position: 2
slug: /mcp_tools
sidebar_custom_props: {
  categoryIcon: LucideToolCase
}
---
# Công cụ MCP RAGFlow

Máy chủ MCP hiện cung cấp một công cụ chuyên biệt để hỗ trợ người dùng tìm kiếm thông tin liên quan được hỗ trợ bởi công nghệ RAGFlow DeepDoc:

- **retrieve**: Lấy các chunk liên quan từ `dataset_ids` được chỉ định và `document_ids` tùy chọn bằng giao diện truy xuất RAGFlow, dựa trên câu hỏi đã cho. Thông tin chi tiết của tất cả các dataset có sẵn, cụ thể là `id` và `description`, được cung cấp trong mô tả công cụ cho mỗi dataset riêng lẻ.

Để biết thêm thông tin, hãy xem triển khai Python của chúng tôi về [máy chủ MCP](https://github.com/infiniflow/ragflow/blob/main/mcp/server/server.py).
