---
sidebar_position: 1
slug: /accelerate_agent_question_answering
---

# Tăng tốc trả lời

Danh sách kiểm tra để tăng tốc độ trả lời câu hỏi.

---

Lưu ý rằng một số cài đặt của bạn có thể tiêu tốn nhiều thời gian đáng kể. Nếu bạn thường xuyên thấy việc trả lời câu hỏi mất nhiều thời gian, đây là danh sách kiểm tra để cân nhắc:

## Cân bằng độ phức tạp của nhiệm vụ với hiệu suất và tốc độ của Agent?

Thời gian phản hồi của Agent thường phụ thuộc vào nhiều yếu tố, ví dụ như khả năng của LLM và prompt, cái sau phản ánh độ phức tạp của nhiệm vụ. Khi sử dụng Agent, bạn phải luôn cân bằng giữa yêu cầu nhiệm vụ và khả năng của LLM.

- Đối với các nhiệm vụ đơn giản, như truy xuất, viết lại, định dạng hoặc trích xuất dữ liệu có cấu trúc, hãy sử dụng các prompt ngắn gọn, loại bỏ hướng dẫn lập kế hoạch hoặc lập luận, áp đặt giới hạn độ dài đầu ra và chọn các mô hình nhỏ hơn hoặc thuộc lớp Turbo. Điều này làm giảm đáng kể độ trễ và chi phí với tác động tối thiểu đến chất lượng.

- Đối với các nhiệm vụ phức tạp, như lập luận đa bước, tổng hợp đa tài liệu hoặc quy trình dựa trên công cụ, hãy duy trì hoặc cải thiện các prompt bao gồm các bước lập kế hoạch, phản ánh và xác minh.

- Trong các hệ thống điều phối đa Agent, hãy ủy thác các nhiệm vụ con đơn giản cho các Agent con sử dụng các mô hình nhỏ hơn, nhanh hơn, và dành các mô hình mạnh hơn cho Agent trưởng để xử lý sự phức tạp và không chắc chắn.

:::tip THÔNG TIN CHÍNH
Tập trung vào việc giảm thiểu token đầu ra — thông qua tóm tắt, gạch đầu dòng hoặc giới hạn độ dài rõ ràng — vì điều này có tác động lớn hơn nhiều đến việc giảm độ trễ so với tối ưu hóa kích thước đầu vào.
:::

## Tắt Reasoning

Tắt chế độ **Reasoning** sẽ giảm thời gian suy nghĩ của LLM. Đối với mô hình như Qwen3, bạn cũng cần thêm `/no_think` vào system prompt để tắt lập luận.

## Tắt Rerank model

- Để trống trường **Rerank model** (trong thành phần **Retrieval** tương ứng) sẽ giảm đáng kể thời gian truy xuất.
- Khi sử dụng mô hình rerank, hãy đảm bảo bạn có GPU để tăng tốc; nếu không, quá trình reranking sẽ *cực kỳ* chậm.

:::tip LƯU Ý
Lưu ý rằng các mô hình rerank là thiết yếu trong một số kịch bản nhất định. Luôn có sự đánh đổi giữa tốc độ và hiệu suất; bạn phải cân nhắc ưu và nhược điểm cho trường hợp cụ thể của mình.
:::

## Kiểm tra thời gian thực hiện từng nhiệm vụ

Nhấp vào biểu tượng bóng đèn ở trên hội thoại *hiện tại* và cuộn xuống cửa sổ popup để xem thời gian thực hiện từng nhiệm vụ:

| Tên mục           | Mô tả                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------------|
| Total             | Tổng thời gian dành cho vòng hội thoại này, bao gồm truy xuất đoạn và tạo câu trả lời.       |
| Check LLM         | Thời gian xác thực LLM được chỉ định.                                                         |
| Create retriever  | Thời gian tạo bộ truy xuất đoạn.                                                              |
| Bind embedding    | Thời gian khởi tạo một instance mô hình nhúng.                                                |
| Bind LLM          | Thời gian khởi tạo một instance LLM.                                                          |
| Tune question     | Thời gian tối ưu hóa truy vấn của người dùng sử dụng bối cảnh của cuộc hội thoại đa lượt.   |
| Bind reranker     | Thời gian khởi tạo một instance mô hình reranker để truy xuất đoạn.                          |
| Generate keywords | Thời gian trích xuất từ khóa từ truy vấn của người dùng.                                     |
| Retrieval         | Thời gian truy xuất các đoạn.                                                                 |
| Generate answer   | Thời gian tạo câu trả lời.                                                                    |
