---
sidebar_position: -4
slug: /configure_child_chunking_strategy
sidebar_custom_props: {
  categoryIcon: LucideGroup
}
---
# Cấu hình chiến lược phân đoạn con

Đặt chiến lược phân đoạn cha-con để cải thiện việc truy xuất.

---

Một thách thức dai dẳng trong các ứng dụng RAG thực tế nằm ở sự căng thẳng cấu trúc trong pipeline "chunk-embed-retrieve" truyền thống: một đoạn văn bản đơn lẻ được giao nhiệm vụ vừa khớp ngữ nghĩa (thu hồi) vừa hiểu ngữ cảnh (sử dụng)—hai mục tiêu vốn mâu thuẫn nhau. Thu hồi đòi hỏi các đoạn chi tiết, chính xác, trong khi tạo câu trả lời yêu cầu ngữ cảnh mạch lạc, đầy đủ thông tin.

Để giải quyết sự căng thẳng này, RAGFlow trước đây đã giới thiệu tính năng nâng cao Mục lục (TOC), sử dụng một mô hình ngôn ngữ lớn (LLM) để tạo cấu trúc tài liệu và tự động bổ sung ngữ cảnh còn thiếu trong quá trình truy xuất dựa trên TOC đó. Trong phiên bản 0.23.0, khả năng này đã được tích hợp có hệ thống vào Ingestion Pipeline, và một cơ chế phân đoạn cha-con mới đã được giới thiệu.

Theo cơ chế này, một tài liệu trước tiên được phân đoạn thành các đoạn cha lớn hơn, mỗi đoạn duy trì một đơn vị ngữ nghĩa tương đối hoàn chỉnh để đảm bảo tính toàn vẹn logic và nền tảng. Mỗi đoạn cha sau đó có thể được phân chia thêm thành nhiều đoạn con để thu hồi chính xác. Trong quá trình truy xuất, hệ thống trước tiên xác định các phân đoạn văn bản liên quan nhất dựa trên các đoạn con trong khi tự động liên kết và thu hồi đoạn cha của chúng. Phương pháp này duy trì độ liên quan thu hồi cao trong khi cung cấp đủ nền tảng ngữ nghĩa cho giai đoạn tạo.

Ví dụ, khi xử lý *Sổ tay Tuân thủ*, một truy vấn của người dùng về "trách nhiệm vi phạm" có thể chính xác truy xuất một đoạn con nêu rằng: "Mức phạt vi phạm là 20% tổng giá trị hợp đồng," nhưng nếu không có ngữ cảnh, nó không thể làm rõ liệu điều khoản này áp dụng cho "vi phạm nhỏ" hay "vi phạm trọng yếu". Nhờ cơ chế phân đoạn cha-con, hệ thống trả về đoạn con này cùng với đoạn cha, chứa toàn bộ phần của điều khoản. Điều này cho phép LLM đưa ra phán quyết chính xác dựa trên ngữ cảnh rộng hơn, tránh hiểu nhầm.

Thông qua cấu trúc hai lớp "xác định vị trí chính xác + bổ sung ngữ cảnh" này, RAGFlow đảm bảo độ chính xác truy xuất đồng thời nâng cao đáng kể độ tin cậy và tính đầy đủ của các câu trả lời được tạo.

## Quy trình

1. Trên trang **Configuration** của tập dữ liệu, tìm công tắc **Child chunk are used for retrieval**:

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/child_chunking.png)

2. Đặt dấu phân cách cho các đoạn con.

3. Cấu hình này áp dụng cho thành phần **Chunker** khi sử dụng cài đặt pipeline nhập liệu:

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/child_chunking_parser.png)
