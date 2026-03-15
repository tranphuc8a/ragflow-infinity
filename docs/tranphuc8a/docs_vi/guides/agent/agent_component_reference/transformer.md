---
sidebar_position: 37
slug: /transformer_component
sidebar_custom_props: {
  categoryIcon: LucideFileStack
}
---
# Thành phần Transformer

Thành phần sử dụng LLM để trích xuất thông tin từ các đoạn.

---

Thành phần **Transformer** lập chỉ mục các đoạn và cấu hình định dạng lưu trữ của chúng trong công cụ tài liệu. Nó *thường* đứng trước **Indexer** trong pipeline nhập liệu, nhưng bạn cũng có thể nối nhiều thành phần **Transformer** theo chuỗi.

## Kịch bản

Thành phần **Transformer** là thiết yếu khi bạn cần LLM trích xuất thông tin mới, chẳng hạn như từ khóa, câu hỏi, siêu dữ liệu và tóm tắt, từ các đoạn gốc.

## Cấu hình

### Model

Nhấp vào menu thả xuống của **Model** để hiển thị cửa sổ cấu hình mô hình.

- **Model**: Mô hình chat cần sử dụng.
  - Đảm bảo bạn đặt đúng mô hình chat trên trang **Model providers**.
  - Bạn có thể sử dụng các mô hình khác nhau cho các thành phần khác nhau để tăng tính linh hoạt hoặc cải thiện hiệu suất tổng thể.
- **Creativity**: Phím tắt đến các cài đặt **Temperature**, **Top P**, **Presence penalty** và **Frequency penalty**, cho biết mức độ tự do của mô hình. Từ **Improvise**, **Precise** đến **Balance**, mỗi cấu hình preset tương ứng với một tổ hợp duy nhất của **Temperature**, **Top P**, **Presence penalty** và **Frequency penalty**.
  Tham số này có ba tùy chọn:
  - **Improvise**: Tạo ra các phản hồi sáng tạo hơn.
  - **Precise**: (Mặc định) Tạo ra các phản hồi bảo thủ hơn.
  - **Balance**: Mức trung gian giữa **Improvise** và **Precise**.
- **Temperature**: Mức độ ngẫu nhiên của đầu ra mô hình.
  Mặc định là 0.1.
  - Giá trị thấp hơn dẫn đến đầu ra xác định và dự đoán được hơn.
  - Giá trị cao hơn dẫn đến đầu ra sáng tạo và đa dạng hơn.
  - Nhiệt độ bằng không dẫn đến cùng một đầu ra cho cùng một prompt.
- **Top P**: Lấy mẫu Nucleus.
  - Giảm khả năng tạo ra văn bản lặp hoặc không tự nhiên bằng cách đặt ngưỡng *P* và giới hạn việc lấy mẫu đối với các token có xác suất tích lũy vượt quá *P*.
  - Mặc định là 0.3.
- **Presence penalty**: Khuyến khích mô hình bao gồm nhiều loại token hơn trong phản hồi.
  - Giá trị **presence penalty** cao hơn dẫn đến mô hình có nhiều khả năng tạo ra các token chưa xuất hiện trong văn bản đã tạo.
  - Mặc định là 0.4.
- **Frequency penalty**: Ngăn chặn mô hình lặp lại cùng các từ hoặc cụm từ quá thường xuyên.
  - Giá trị **frequency penalty** cao hơn dẫn đến mô hình bảo thủ hơn trong việc sử dụng các token lặp lại.
  - Mặc định là 0.7.
- **Max tokens**:
  Đặt độ dài tối đa của đầu ra mô hình, tính bằng số token (từ hoặc phần của từ). Mặc định bị vô hiệu hóa, cho phép mô hình tự xác định số lượng token trong phản hồi.

:::tip LƯU Ý
- Không nhất thiết phải sử dụng cùng một mô hình cho tất cả các thành phần. Nếu một mô hình cụ thể không hoạt động tốt cho một nhiệm vụ cụ thể, hãy xem xét sử dụng mô hình khác.
- Nếu bạn không chắc chắn về cơ chế của **Temperature**, **Top P**, **Presence penalty** và **Frequency penalty**, hãy đơn giản chọn một trong ba tùy chọn của **Creativity**.
:::

### Result destination

Chọn loại đầu ra sẽ được tạo bởi LLM:

- Summary (Tóm tắt)
- Keywords (Từ khóa)
- Questions (Câu hỏi)
- Metadata (Siêu dữ liệu)

### System prompt

Thông thường, bạn sử dụng system prompt để mô tả nhiệm vụ cho LLM, chỉ định cách nó nên phản hồi và nêu ra các yêu cầu khác. Chúng tôi không có kế hoạch chi tiết về chủ đề này, vì nó có thể rộng như kỹ thuật prompt.

:::tip LƯU Ý
System prompt ở đây tự động cập nhật để phù hợp với **Result destination** được chọn của bạn.
:::

### User prompt

Prompt do người dùng xác định. Ví dụ, bạn có thể gõ `/` hoặc nhấp vào **(x)** để chèn các biến của các thành phần trước đó trong pipeline nhập liệu như đầu vào của LLM.

### Output

Tên biến toàn cục cho đầu ra của thành phần **Transformer**, có thể được tham chiếu bởi các thành phần **Transformer** tiếp theo trong pipeline nhập liệu.

- Mặc định: `chunks`
- Kiểu: `Array<Object>`
