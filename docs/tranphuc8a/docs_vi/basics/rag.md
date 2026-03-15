---
sidebar_position: 1
slug: /what-is-rag
---

# RAG (Truy xuất-Tăng cường-Sinh văn bản) là gì?

Kể từ khi các mô hình ngôn ngữ lớn (LLM) trở thành tâm điểm của công nghệ, khả năng xử lý kiến thức chung của chúng thật ấn tượng. Tuy nhiên, khi câu hỏi chuyển sang tài liệu nội bộ doanh nghiệp, cơ sở kiến thức độc quyền, hoặc dữ liệu thời gian thực, những hạn chế của LLM trở nên rõ ràng: chúng không thể truy cập thông tin riêng tư ngoài dữ liệu huấn luyện. Truy xuất-Tăng cường-Sinh văn bản (RAG) ra đời chính xác để giải quyết nhu cầu cốt lõi này. Trước khi LLM tạo ra câu trả lời, nó trước tiên truy xuất ngữ cảnh liên quan nhất từ cơ sở kiến thức bên ngoài và đưa vào như "tài liệu tham khảo" cho LLM, từ đó hướng dẫn LLM tạo ra câu trả lời chính xác. Nói ngắn gọn, RAG nâng cấp LLM từ "dựa vào trí nhớ" sang "có bằng chứng để dựa vào," cải thiện đáng kể độ chính xác và đáng tin cậy trong các lĩnh vực chuyên biệt và truy vấn thông tin thời gian thực.

## Tại sao RAG quan trọng?

Mặc dù LLM vượt trội trong hiểu và tạo ngôn ngữ, chúng có những hạn chế vốn có:

- **Kiến thức tĩnh**: Kiến thức của mô hình dựa trên ảnh chụp dữ liệu từ thời điểm huấn luyện và không thể tự động cập nhật, khó nhận biết thông tin mới nhất.
- **Điểm mù với dữ liệu bên ngoài**: Chúng không thể trực tiếp truy cập tài liệu riêng tư của doanh nghiệp, luồng thông tin thời gian thực hoặc nội dung theo lĩnh vực cụ thể.
- **Rủi ro ảo giác (Hallucination)**: Khi thiếu bằng chứng chính xác, chúng vẫn có thể bịa ra câu trả lời nghe hay nhưng sai để duy trì độ trôi chảy của cuộc trò chuyện.

Sự ra đời của RAG cung cấp cho LLM "nền tảng thực tế" có thể tin cậy trong thời gian thực. Cơ chế cốt lõi của nó được chia thành hai giai đoạn:

- **Giai đoạn Truy xuất**: Dựa trên câu hỏi của người dùng, nhanh chóng truy xuất các tài liệu hoặc đoạn dữ liệu liên quan nhất từ cơ sở kiến thức bên ngoài.
- **Giai đoạn Sinh văn bản**: LLM tổ chức và tạo ra câu trả lời cuối cùng bằng cách kết hợp thông tin đã truy xuất làm ngữ cảnh, kết hợp với khả năng ngôn ngữ của chính nó.

Điều này nâng cấp LLM từ "nói từ trí nhớ" sang "nói có tài liệu," cải thiện đáng kể độ tin cậy trong các ứng dụng chuyên nghiệp và cấp doanh nghiệp.

## RAG hoạt động như thế nào?

Truy xuất-Tăng cường-Sinh văn bản giúp LLM tạo ra câu trả lời chất lượng cao hơn bằng cách tận dụng dữ liệu thời gian thực, bên ngoài hoặc riêng tư thông qua việc giới thiệu cơ chế truy xuất thông tin. Quy trình làm việc có thể được chia thành các bước chính sau:

### Xử lý dữ liệu và vector hóa

Kiến thức cần thiết cho RAG đến từ dữ liệu phi cấu trúc ở nhiều định dạng khác nhau, chẳng hạn như tài liệu, bản ghi cơ sở dữ liệu hoặc nội dung trả về từ API. Dữ liệu này thường cần được chia chunk, sau đó chuyển đổi thành vector thông qua mô hình nhúng (embedding) và lưu trữ trong database vector.

**Tại sao cần Chunking?** Lập chỉ mục toàn bộ tài liệu trực tiếp gặp các vấn đề sau:

- **Giảm độ chính xác truy xuất**: Vector hóa tài liệu dài dẫn đến "trung bình hóa" ngữ nghĩa, mất chi tiết.
- **Giới hạn độ dài ngữ cảnh**: LLM có cửa sổ ngữ cảnh hữu hạn, đòi hỏi lọc các phần liên quan nhất để đưa vào.
- **Chi phí và hiệu quả**: Chi phí tính toán nhúng và truy xuất cao hơn cho văn bản dài.

Do đó, chiến lược chunking thông minh là chìa khóa để cân bằng tính toàn vẹn thông tin, độ chi tiết truy xuất và hiệu quả tính toán.

### Truy xuất thông tin liên quan

Truy vấn của người dùng cũng được chuyển đổi thành vector để thực hiện tìm kiếm liên quan ngữ nghĩa (ví dụ: tính cosine similarity) trong database vector, khớp và gọi lại các đoạn văn bản liên quan nhất.

### Xây dựng ngữ cảnh và tạo câu trả lời

Nội dung liên quan đã truy xuất được thêm vào ngữ cảnh của LLM như nền tảng thực tế, và LLM cuối cùng tạo ra câu trả lời. Do đó, RAG có thể được xem như Context Engineering 1.0 để xây dựng ngữ cảnh tự động.

## Tìm hiểu sâu về kiến trúc RAG hiện có: vượt ra ngoài truy xuất vector

Một hệ thống RAG cấp công nghiệp không đơn giản như "tìm kiếm vector + LLM"; độ phức tạp và thách thức chủ yếu nằm trong quá trình truy xuất.

### Độ phức tạp của dữ liệu: xử lý tài liệu đa phương thức

**Thách thức cốt lõi**: Kiến thức doanh nghiệp chủ yếu tồn tại dưới dạng tài liệu đa phương thức chứa văn bản, biểu đồ, bảng và công thức. Trích xuất OCR đơn giản mất nhiều thông tin ngữ nghĩa.

**Thực hành nâng cao**: Các giải pháp hàng đầu, như RAGFlow, có xu hướng sử dụng Mô hình Ngôn ngữ Thị giác (VLM) hoặc các mô hình phân tích chuyên biệt như DeepDoc để "dịch" tài liệu đa phương thức thành văn bản đơn phương thức giàu thông tin cấu trúc và ngữ nghĩa.

### Sự phức tạp của chunking: sự đánh đổi giữa độ chính xác và ngữ cảnh

Pipeline "chunk-embed-retrieve" đơn giản có mâu thuẫn vốn có:
- **Khớp ngữ nghĩa** yêu cầu chunk văn bản nhỏ để đảm bảo ngữ nghĩa rõ ràng.
- **Hiểu ngữ cảnh** yêu cầu chunk văn bản lớn để đảm bảo thông tin hoàn chỉnh và mạch lạc.

**Thực hành nâng cao**: Các giải pháp hàng đầu, như RAGFlow, sử dụng các kỹ thuật tăng cường ngữ nghĩa như xây dựng bảng nội dung ngữ nghĩa và đồ thị kiến thức.

### Tại sao database vector không đủ cho RAG?

Database vector xuất sắc trong tìm kiếm tương đồng ngữ nghĩa, nhưng RAG đòi hỏi câu trả lời chính xác và đáng tin cậy:
- **Tìm kiếm kết hợp**: Chỉ dựa vào truy xuất vector có thể bỏ lỡ các từ khóa chính xác. Tìm kiếm kết hợp, kết hợp truy xuất vector với truy xuất từ khóa (BM25), đảm bảo cả phạm vi ngữ nghĩa và độ chính xác từ khóa.
- **Biểu diễn Tensor hoặc Đa vector**: Để hỗ trợ dữ liệu đa phương thức.
- **Lọc siêu dữ liệu (Metadata Filtering)**: Lọc theo thuộc tính như ngày, phòng ban và loại là yêu cầu cứng trong các kịch bản kinh doanh.

## RAG và bộ nhớ: Truy xuất cùng nguồn nhưng khác luồng

Trong framework agent, bản chất của cơ chế bộ nhớ giống với RAG: cả hai đều truy xuất thông tin liên quan từ lưu trữ dựa trên nhu cầu hiện tại. Sự khác biệt chính nằm ở nguồn dữ liệu:
- **RAG**: Nhắm mục tiêu vào dữ liệu tĩnh hoặc động riêng tư đã tồn tại từ trước do người dùng cung cấp trước (ví dụ: tài liệu, cơ sở dữ liệu).
- **Bộ nhớ**: Nhắm mục tiêu vào dữ liệu động được agent tạo ra hoặc nhận thức trong thời gian thực trong quá trình tương tác (ví dụ: lịch sử cuộc trò chuyện, trạng thái môi trường, kết quả thực thi công cụ).

## Ứng dụng RAG

RAG đã chứng tỏ giá trị rõ ràng trong một số kịch bản điển hình:

1. **Q&A Kiến thức Doanh nghiệp và Tìm kiếm Nội bộ**  
   Bằng cách vector hóa dữ liệu riêng tư của doanh nghiệp và kết hợp với LLM, RAG có thể trả về câu trả lời ngôn ngữ tự nhiên dựa trên các nguồn có thẩm quyền.

2. **Hiểu Tài liệu Phức tạp và Q&A Chuyên nghiệp**  
   Đối với các tài liệu có cấu trúc phức tạp như hợp đồng và quy định, giá trị của RAG nằm ở khả năng tạo ra câu trả lời chính xác, có thể kiểm chứng.

3. **Hợp nhất Kiến thức Động và Hỗ trợ Quyết định**  
   Trong các kịch bản kinh doanh đòi hỏi tổng hợp thông tin từ nhiều nguồn, RAG phát triển thành hệ thống điều phối kiến thức và hỗ trợ lý luận.

## Tương lai của RAG

Sự phát triển của RAG đang diễn ra theo một số hướng rõ ràng:

1. **RAG như nền tảng dữ liệu cho Agents**  
   RAG và agent có mối quan hệ kiến trúc và kịch bản. Để agent đạt được quyết định và thực thi tự động, đáng tin cậy, chúng phải dựa vào kiến thức chính xác và kịp thời.

2. **RAG Nâng cao: Sử dụng LLM để tối ưu hóa chính quá trình truy xuất**  
   Tính năng cốt lõi của RAG thế hệ tiếp theo là tận dụng đầy đủ khả năng lý luận của LLM để tối ưu hóa quá trình truy xuất.

3. **Hướng tới Context Engineering 2.0**  
   RAG hiện tại có thể được xem là Context Engineering 1.0. Context Engineering 2.0 sắp tới sẽ mở rộng với công nghệ RAG làm cốt lõi, trở thành hệ thống tự động lắp ráp ngữ cảnh toàn diện cho agent.

Bản chất của RAG là xây dựng giao diện dữ liệu bên ngoài chuyên dụng, hiệu quả và đáng tin cậy cho các mô hình ngôn ngữ lớn; cốt lõi của nó là Truy xuất, không phải Sinh văn bản.
