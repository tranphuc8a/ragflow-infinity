---
sidebar_position: 3
slug: /implement_deep_research
sidebar_custom_props: {
  categoryIcon: LucideScanSearch
}
---
# Triển khai nghiên cứu sâu (Deep Research)

Triển khai nghiên cứu sâu cho lý luận dựa trên Agent.

---

Từ v0.17.0 trở đi, RAGFlow hỗ trợ tích hợp lý luận dựa trên Agent trong chat AI. Sơ đồ sau minh họa luồng công việc của tính năng nghiên cứu sâu của RAGFlow:

![Image](https://github.com/user-attachments/assets/f65d4759-4f09-4d9d-9549-c0e1fe907525)

Để kích hoạt tính năng này:

1. Bật công tắc **Suy luận** trong **Cài đặt Chat**.

![chat_reasoning](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/chat_reasoning.jpg)

2. Nhập API key Tavily đúng để tận dụng tìm kiếm web dựa trên Tavily:

![chat_tavily](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/chat_tavily.jpg)

*Sau đây là ảnh chụp màn hình của một cuộc hội thoại tích hợp Deep Research:*

![Image](https://github.com/user-attachments/assets/165b88ff-1f5d-4fb8-90e2-c836b25e32e9)
