---
sidebar_position: 1
slug: /agent_introduction
sidebar_custom_props: {
  categoryIcon: LucideBookOpenText
}
---
# Giới thiệu về Agent

Các khái niệm quan trọng, thao tác cơ bản, xem nhanh trình chỉnh sửa agent.

---

:::danger ĐÃ LỖI THỜI!
Phiên bản mới sẽ sớm ra mắt.
:::

## Các khái niệm quan trọng

Agent và RAG là các kỹ thuật bổ trợ cho nhau, mỗi kỹ thuật tăng cường khả năng của kỹ thuật kia trong các ứng dụng kinh doanh. RAGFlow v0.8.0 giới thiệu cơ chế agent, với trình chỉnh sửa luồng công việc không cần code ở giao diện người dùng và khung điều phối tác vụ dựa trên đồ thị toàn diện ở phía backend. Cơ chế này được xây dựng trên nền tảng các giải pháp RAG hiện có của RAGFlow và nhằm điều phối các công nghệ tìm kiếm như phân loại ý định truy vấn, dẫn dắt hội thoại và viết lại truy vấn để:

- Cung cấp khả năng truy xuất thông tin cao hơn, và
- Hỗ trợ các tình huống phức tạp hơn.

## Tạo một Agent

:::tip LƯU Ý

Trước khi tiến hành, hãy đảm bảo rằng:

1. Bạn đã cấu hình đúng LLM sẽ sử dụng. Xem hướng dẫn về [Cấu hình API key](../models/llm_api_key_setup.md) hoặc [Triển khai LLM cục bộ](../models/deploy_local_llm.mdx) để biết thêm thông tin.
2. Bạn đã cấu hình một tập dữ liệu và các tệp tương ứng đã được phân tích đúng cách. Xem hướng dẫn về [Cấu hình tập dữ liệu](../dataset/configure_knowledge_base.md) để biết thêm thông tin.

:::

Nhấp vào tab **Agent** ở giữa đầu trang để hiển thị trang **Agent**. Như hiển thị trong ảnh chụp màn hình bên dưới, các thẻ trên trang này đại diện cho các agent đã tạo, mà bạn có thể tiếp tục chỉnh sửa.

![Danh sách Agent](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/agent_list.jpg)

Chúng tôi cũng cung cấp các mẫu phù hợp với các tình huống kinh doanh khác nhau. Bạn có thể tạo agent từ một trong các mẫu agent của chúng tôi hoặc tạo từ đầu:

1. Nhấp **+ Tạo agent** để hiển thị trang **mẫu agent**:

   ![mẫu agent](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/agent_template_list.jpg)

2. Để tạo agent từ đầu, nhấp **Tạo Agent**. Hoặc, để tạo agent từ một trong các mẫu, nhấp vào thẻ mong muốn, chẳng hạn như **Deep Research**, đặt tên agent trong hộp thoại bật lên, và nhấp **OK** để xác nhận.

   *Bạn sẽ được đưa đến trang **trình chỉnh sửa luồng công việc không cần code**.*

   ![thêm thành phần](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/add_component.jpg)

3. Nhấp nút **+** trên thành phần **Begin** để chọn các thành phần mong muốn trong luồng công việc của bạn.
4. Nhấp **Lưu** để áp dụng thay đổi cho agent của bạn.
