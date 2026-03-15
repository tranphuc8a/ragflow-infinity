---
sidebar_position: 1
slug: /start_chat
sidebar_custom_props: {
  categoryIcon: LucideBot
}
---
# Bắt đầu chat AI

Khởi tạo cuộc trò chuyện được hỗ trợ bởi AI với trợ lý chat đã cấu hình.

---

Các cuộc chat trong RAGFlow được dựa trên một hoặc nhiều tập dữ liệu cụ thể. Sau khi tạo tập dữ liệu, hoàn tất phân tích tệp và [chạy kiểm tra truy xuất](../dataset/run_retrieval_test.md), bạn có thể bắt đầu cuộc hội thoại AI.

## Bắt đầu chat AI

Bạn bắt đầu cuộc hội thoại AI bằng cách tạo một trợ lý.

1. Nhấp vào tab **Chat** ở giữa đầu trang **>** **Tạo trợ lý** để hiển thị hộp thoại **Cấu hình Chat** *cho cuộc hội thoại tiếp theo của bạn*.

   > RAGFlow cung cấp cho bạn tính linh hoạt để chọn mô hình chat khác nhau cho từng hội thoại, đồng thời cho phép bạn thiết lập các mô hình mặc định trong **Cài đặt mô hình hệ thống**.

2. Cập nhật cài đặt dành riêng cho Trợ lý:

   - **Tên trợ lý** là tên của trợ lý chat của bạn. Mỗi trợ lý tương ứng với một hội thoại có sự kết hợp độc đáo của tập dữ liệu, prompts, cấu hình tìm kiếm kết hợp và cài đặt mô hình lớn.
   - **Phản hồi rỗng**:
     - Nếu bạn muốn *giới hạn* câu trả lời của RAGFlow vào các tập dữ liệu, hãy để lại phản hồi ở đây. Khi đó, nếu không truy xuất được câu trả lời, nó sẽ *thống nhất* phản hồi với những gì bạn đã đặt ở đây.
     - Nếu bạn muốn RAGFlow *ứng phó linh hoạt* khi không truy xuất được câu trả lời từ tập dữ liệu, hãy để trống, điều này có thể dẫn đến ảo giác.
   - **Hiển thị trích dẫn**: Đây là tính năng quan trọng của RAGFlow và được bật theo mặc định. RAGFlow không hoạt động như một hộp đen. Thay vào đó, nó hiển thị rõ ràng các nguồn thông tin mà câu trả lời của nó dựa trên.
   - Chọn các tập dữ liệu tương ứng. Bạn có thể chọn một hoặc nhiều tập dữ liệu, nhưng đảm bảo chúng sử dụng cùng mô hình nhúng, nếu không sẽ xảy ra lỗi.

3. Cập nhật cài đặt dành riêng cho Prompt:

   - Trong **Hệ thống**, bạn điền các prompts cho LLM, bạn cũng có thể để nguyên prompt mặc định để bắt đầu.
   - **Ngưỡng tương đồng** đặt "ngưỡng" tương đồng cho mỗi đoạn văn bản. Mặc định là 0.2. Các đoạn văn bản có điểm tương đồng thấp hơn sẽ bị lọc khỏi phản hồi cuối cùng.
   - **Trọng số tương đồng vector** được đặt là 0.3 theo mặc định. RAGFlow sử dụng hệ thống điểm kết hợp để đánh giá mức độ liên quan của các đoạn văn bản khác nhau. Giá trị này đặt trọng số được gán cho thành phần tương đồng vector trong điểm kết hợp.
     - Nếu **Mô hình Rerank** để trống, hệ thống điểm kết hợp sử dụng tương đồng từ khóa và tương đồng vector, và trọng số mặc định cho thành phần tương đồng từ khóa là 1-0.3=0.7.
     - Nếu **Mô hình Rerank** được chọn, hệ thống điểm kết hợp sử dụng tương đồng từ khóa và điểm reranker, và trọng số mặc định cho điểm reranker là 1-0.7=0.3.
   - **Top N** xác định số lượng đoạn văn bản *tối đa* để cung cấp cho LLM. Nói cách khác, ngay cả khi nhiều đoạn được truy xuất, chỉ N đoạn đầu tiên mới được cung cấp làm đầu vào.
   - **Tối ưu hóa đa lượt** nâng cao truy vấn của người dùng bằng cách sử dụng ngữ cảnh hiện có trong cuộc hội thoại nhiều lượt. Được bật theo mặc định. Khi được bật, nó sẽ tiêu thụ thêm token LLM và tăng đáng kể thời gian tạo câu trả lời.
   - **Sử dụng đồ thị kiến thức** chỉ ra liệu có sử dụng đồ thị kiến thức trong các tập dữ liệu được chỉ định khi truy xuất cho trả lời câu hỏi đa bước hay không. Khi được bật, điều này sẽ liên quan đến tìm kiếm lặp đi lặp lại qua các đoạn thực thể, quan hệ và báo cáo cộng đồng, làm tăng đáng kể thời gian truy xuất.
   - **Suy luận** chỉ ra liệu có tạo câu trả lời thông qua các quy trình suy luận như Deepseek-R1/OpenAI o1 hay không. Khi được bật, mô hình chat tự động tích hợp Deep Research trong quá trình trả lời câu hỏi khi gặp chủ đề không biết. Điều này liên quan đến việc mô hình chat tìm kiếm kiến thức bên ngoài một cách linh động và tạo câu trả lời cuối cùng thông qua suy luận.
   - **Mô hình Rerank** đặt mô hình reranker để sử dụng. Để trống theo mặc định.
   - [Tìm kiếm đa ngôn ngữ](../../references/glossary.mdx#cross-language-search): Tùy chọn
     Chọn một hoặc nhiều ngôn ngữ đích từ menu thả xuống. Mô hình chat mặc định của hệ thống sau đó sẽ dịch truy vấn của bạn sang ngôn ngữ đích đã chọn.
   - **Biến** đề cập đến các biến (khóa) được sử dụng trong system prompt. `{knowledge}` là biến dành riêng. Nhấp **Thêm** để thêm nhiều biến cho system prompt.

4. Cập nhật Cài đặt dành riêng cho Mô hình:

   - Trong **Mô hình**: bạn chọn mô hình chat. Mặc dù bạn đã chọn mô hình chat mặc định trong **Cài đặt mô hình hệ thống**, RAGFlow cho phép bạn chọn mô hình chat thay thế cho hội thoại của mình.
   - **Sáng tạo**: Tắt tắt tắt đến **Nhiệt độ**, **Top P**, **Phạt hiện diện** và **Phạt tần suất**, chỉ ra mức độ tự do của mô hình.
   - **Nhiệt độ**: Mức độ ngẫu nhiên của đầu ra mô hình. Mặc định là 0.1.
   - **Top P**: Lấy mẫu hạt nhân. Mặc định là 0.3.
   - **Phạt hiện diện**: Khuyến khích mô hình bao gồm nhiều token đa dạng hơn trong phản hồi. Mặc định là 0.4.
   - **Phạt tần suất**: Ngăn mô hình lặp lại cùng các từ hoặc cụm từ quá thường xuyên. Mặc định là 0.7.

5. Bây giờ, hãy bắt đầu:

   ![chat_thermal_solution](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/chat_thermal_solution.jpg)

:::tip LƯU Ý

1. Nhấp vào biểu tượng bóng đèn ở trên câu trả lời để xem system prompt mở rộng:

   ![prompt_display](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/prompt_display.jpg)

   *Biểu tượng bóng đèn chỉ có sẵn cho hội thoại hiện tại.*

2. Cuộn xuống prompt mở rộng để xem thời gian tiêu thụ cho từng tác vụ:

   ![time_elapsed](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/time_elapsed.jpg)
:::

## Cập nhật cài đặt của trợ lý chat hiện có

![chat_setting](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/chat_setting.jpg)

## Tích hợp khả năng chat vào ứng dụng hoặc trang web của bạn

RAGFlow cung cấp các API HTTP và Python để tích hợp khả năng của RAGFlow vào ứng dụng của bạn. Đọc các tài liệu sau để biết thêm thông tin:

- [Lấy API key RAGFlow](../../develop/acquire_ragflow_api_key.md)
- [Tài liệu tham khảo HTTP API](../../references/http_api_reference.md)
- [Tài liệu tham khảo Python API](../../references/python_api_reference.md)

Bạn có thể dùng iframe để nhúng trợ lý chat đã tạo vào trang web bên thứ ba:

1. Trước khi tiến hành, bạn phải [lấy API key](../../develop/acquire_ragflow_api_key.md); nếu không, thông báo lỗi sẽ xuất hiện.
2. Di chuột qua trợ lý chat mong muốn **>** **Chỉnh sửa** để hiển thị cửa sổ **iframe**:

   ![chat-embed](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/embed_chat_into_webpage.jpg)

3. Sao chép iframe và nhúng vào trang web của bạn.

![chat-embed](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/embedded_chat_app.jpg)
