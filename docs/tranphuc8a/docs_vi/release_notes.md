---
sidebar_position: 2
slug: /release_notes
sidebarIcon: LucideClipboardPenLine
---

# Ghi chú phát hành

## v0.23.1

*Ngày phát hành: ngày 31 tháng 12 năm 2025*

### Tính năng mới

- Thêm tùy chọn căn chỉnh văn bản cho hộp văn bản trong chế độ xem ứng dụng trang trắng.
- Thêm công cụ MCP để lấy nội dung trang web và Arxiv.
- Bộ nhớ hiện hỗ trợ tìm kiếm chéo ngôn ngữ và mô hình nhúng đa ngôn ngữ.

### Cải tiến

- Cải tiến giao diện quản lý bộ nhớ.
- Mô-đun bộ nhớ không còn phụ thuộc vào khởi tạo module cấp cao nhất.
- Cải tiến tính ổn định của xử lý tin nhắn trong bộ nhớ.

### Sự cố đã sửa

- Sửa lỗi làm trống kết quả phân tích.
- Sửa lỗi liên quan đến phân tích đồ thị tri thức.
- Sửa lỗi làm mất cài đặt nhắc nhở khi cập nhật agent.
- Sửa lỗi liên quan đến lọc metadata ở chế độ RAG lai.

---

## v0.23.0

*Ngày phát hành: ngày 27 tháng 12 năm 2025*

### Tính năng mới

- **Giao diện bộ nhớ**: Cung cấp giao diện bộ nhớ toàn diện bao gồm lưu trữ thô, ngữ nghĩa, sự kiện và thủ tục.
- **Tái cấu trúc Agent**: Tích hợp Agent và Workflow thành một giao diện thống nhất duy nhất.
- **Đầu vào/đầu ra giọng nói**: Hỗ trợ nhập liệu bằng giọng nói và phản hồi bằng giọng nói trong chat.
- **Phân đoạn cha-con**: Thêm chiến lược phân đoạn cha-con để cải thiện độ chính xác truy xuất.
- **Tự động metadata**: Tự động trích xuất và gán metadata cho tài liệu dựa trên nội dung.
- **MCP Server**: Tích hợp Model Context Protocol (MCP) Server.

### Cải tiến

- Tối ưu đường dẫn phân tích để tăng hiệu suất.
- Cải tiến hỗ trợ phân tích tài liệu bằng VLM (Visual Language Model).
- Cải tiến trải nghiệm giao diện người dùng cho chế độ xem ứng dụng.

### Sự cố đã sửa

- Sửa nhiều lỗi liên quan đến phân tích tài liệu và truy vấn.
- Sửa lỗi stream agent bị ngắt quãng.

### Thay đổi API

- Thêm API quản lý bộ nhớ.

---

## v0.22.1

*Ngày phát hành: ngày 25 tháng 11 năm 2025*

### Tính năng mới

- Thêm công cụ Google Workspace (Gmail, Google Docs, Google Calendar).
- Thêm hỗ trợ mô hình Gemini trong các thành phần agent.

### Sự cố đã sửa

- Sửa lỗi tải lên từ nguồn dữ liệu Google Drive.
- Sửa sự cố không nhất quán trong giao diện quản lý dataset.
- Sửa lỗi phân trang trong danh sách agent session.

---

## v0.22.0

*Ngày phát hành: ngày 20 tháng 11 năm 2025*

### Tính năng mới

- **Nguồn dữ liệu đám mây**: Hỗ trợ thêm tài liệu từ AWS S3, Google Drive, Tencent COS, Azure Blob Storage và SharePoint.
- **Bảng điều khiển quản trị**: Giao diện quản trị hệ thống mới cho phép giám sát người dùng và quản lý mô hình LLM.
- **Đầu ra có cấu trúc**: Tùy chọn đầu ra JSON cho các thành phần agent.
- **Bộ nhớ đệm kết quả**: Hỗ trợ lưu kết quả truy vấn trùng lặp.
- **Chính sách quên**: Hệ thống quản lý bộ nhớ với chính sách FIFO để giải phóng không gian.

### Cải tiến

- Tối ưu pipeline nhập dữ liệu.
- Cải tiến xử lý bảng biểu và hình ảnh trong tài liệu PDF.

### Sự cố đã sửa

- Sửa rò rỉ bộ nhớ trong phân tích PDF dài.
- Sửa lỗi hiển thị kết quả khi truy vấn song song.

---

## v0.21.1

*Ngày phát hành: ngày 31 tháng 10 năm 2025*

### Sự cố đã sửa

- Sửa lỗi nghiêm trọng trong phân tích tài liệu MinerU.
- Sửa lỗi thứ tự chunk không đúng với tài liệu nhiều trang.
- Sửa lỗi phân tích bảng trong định dạng DOCX.

---

## v0.21.0

*Ngày phát hành: ngày 25 tháng 10 năm 2025*

### Tính năng mới

- **Phân tích MinerU**: Tích hợp công cụ phân tích PDF MinerU cho kết quả chất lượng cao hơn.
- **Pipeline nhập dữ liệu có thể điều phối**: Xây dựng luồng nhập dữ liệu tùy chỉnh với các thành phần agent.
- **Hỗ trợ OCR nâng cao**: Cải thiện chất lượng nhận dạng văn bản trong hình ảnh.
- **Webhook**: Hỗ trợ webhook để tích hợp sự kiện bên ngoài.

### Cải tiến

- Tăng tốc độ lập chỉ mục cho tài liệu lớn.
- Phân tích phương trình toán học được cải thiện.

### API mới

- Thêm endpoint để quản lý pipeline nhập dữ liệu.

---

## v0.20.3

*Ngày phát hành: ngày 26 tháng 9 năm 2025*

### Sự cố đã sửa

- Sửa lỗi rò rỉ bộ nhớ trong phân tích PDF.
- Sửa lỗi khi sử dụng nhiều mô hình nhúng song song.

---

## v0.20.2

*Ngày phát hành: ngày 18 tháng 9 năm 2025*

### Cải tiến

- Cải tiến hiệu suất phân tích PDF.
- Tối ưu sử dụng bộ nhớ cho pipeline RAG.

### Sự cố đã sửa

- Sửa lỗi không phân tích được tài liệu password-protected.
- Sửa lỗi hiển thị metadata trống.

---

## v0.20.1

*Ngày phát hành: ngày 11 tháng 9 năm 2025*

### Sự cố đã sửa

- Sửa lỗi nghiêm trọng trong thành phần Phân loại (Categorize) agent.
- Sửa lỗi stream không hoàn chỉnh với mô hình Claude.
- Sửa lỗi giao diện người dùng trong trang cấu hình agent.

---

## v0.20.0

*Ngày phát hành: ngày 8 tháng 9 năm 2025*

### Tính năng mới

- **Điều phối Agent/Workflow thống nhất**: Hợp nhất Agent và Workflow thành một hệ thống điều phối duy nhất để đơn giản hóa việc xây dựng ứng dụng AI.
- **MCP (Model Context Protocol)**: Tích hợp MCP để kết nối các công cụ bên ngoài với agent.
- **Tự động kết thúc vòng lặp**: Phát hiện và kết thúc vòng lặp vô hạn trong agent.
- **Giao diện ứng dụng mới**: Giao diện thiết kế lại cho mục đích nhúng vào trang web.

### Cải tiến

- Cải tiến trải nghiệm xây dựng agent bằng kéo thả.
- Cải tiến xử lý lỗi trong pipeline RAG.
- Tăng cường khả năng gỡ lỗi với nhật ký chi tiết hơn.

### Sự cố đã sửa

- Sửa nhiều lỗi rò rỉ bộ nhớ.
- Sửa lỗi xử lý file TXT với mã hóa đặc biệt.

---

## v0.19.2

*Ngày phát hành: ngày 20 tháng 6 năm 2025*

### Sự cố đã sửa

- Sửa lỗi trong thành phần Retrieval của agent.
- Sửa lỗi thời gian chờ trong phân tích tài liệu dài.
- Sửa lỗi hiển thị trích dẫn nguồn.

---

## v0.19.1

*Ngày phát hành: ngày 13 tháng 6 năm 2025*

### Sự cố đã sửa

- Sửa lỗi thành phần Code không chạy được trong một số môi trường.
- Sửa lỗi khớp nhãn tag trong tìm kiếm.

---

## v0.19.0

*Ngày phát hành: ngày 7 tháng 6 năm 2025*

### Tính năng mới

- **Tìm kiếm chéo ngôn ngữ**: Tìm kiếm tài liệu bằng ngôn ngữ khác với ngôn ngữ của tài liệu.
- **Thành phần Code**: Thêm thành phần thực thi code Python trực tiếp trong agent.
- **Hỗ trợ Claude 4**: Tích hợp mô hình Anthropic Claude 4.
- **Tùy chỉnh prompt ToC**: Tùy chỉnh prompt trích xuất mục lục.

### Cải tiến

- Cải tiến xử lý tài liệu song ngữ.
- Tăng độ chính xác truy xuất với mô hình rerank mới.

### Các mô hình mới được hỗ trợ

- Anthropic Claude 4 Sonnet, Claude 4 Haiku

---

## v0.18.1

*Ngày phát hành: ngày 25 tháng 4 năm 2025*

### Sự cố đã sửa

- Sửa lỗi MCP Server không kết nối được.
- Sửa lỗi phân tích bảng phức tạp trong PDF.

---

## v0.18.0

*Ngày phát hành: ngày 18 tháng 4 năm 2025*

### Tính năng mới

- **MCP Server**: Triển khai RAGFlow như một MCP Server, cho phép các client AI như Claude Desktop kết nối trực tiếp.
- **VLM cho DeepDoc**: Sử dụng mô hình ngôn ngữ thị giác (VLM) để cải thiện phân tích hình ảnh trong tài liệu.
- **Thẻ dataset tùy chỉnh**: Thêm nhãn tag tùy chỉnh cho từng dataset.

### Cải tiến

- Tối ưu tốc độ nhúng (embedding) cho tập lớn.
- Cải tiến UI cho trình xây dựng agent.

### Các mô hình mới được hỗ trợ

- Google Gemini 2.0, 2.5 Pro/Flash

---

## v0.17.3

*Ngày phát hành: ngày 28 tháng 3 năm 2025*

### Sự cố đã sửa

- Sửa lỗi thành phần Deep Research.
- Sửa lỗi khi sử dụng thư viện Tavily với token hết hạn.

---

## v0.17.2

*Ngày phát hành: ngày 21 tháng 3 năm 2025*

### Sự cố đã sửa

- Sửa lỗi xử lý tài liệu với nội dung hỗn hợp ngôn ngữ.
- Sửa lỗi hiển thị kết quả trong một số tình huống phân trang.

---

## v0.17.1

*Ngày phát hành: ngày 14 tháng 3 năm 2025*

### Sự cố đã sửa

- Sửa lỗi nghiêm trọng trong phân tích PDF với layout phức tạp.

---

## v0.17.0

*Ngày phát hành: ngày 8 tháng 3 năm 2025*

### Tính năng mới

- **Deep Research**: Thêm thành phần Deep Research mới cho phép agent thực hiện nghiên cứu sâu nhiều bước.
- **Tìm kiếm web Tavily**: Tích hợp Tavily Search để agent tìm kiếm thông tin thời gian thực.
- **Dropdown chọn trình phân tích PDF**: Cho phép chọn trình phân tích PDF (DeepDoc, MinerU, v.v.) ngay trong giao diện.
- **Kết quả theo luồng (streaming)**: Hỗ trợ đầy đủ streaming trong hội thoại agent.

### Cải tiến

- Cải tiến độ chính xác phân tích bảng và biểu đồ.
- Tối ưu tốc độ xử lý tài liệu dài.

---

## v0.16.3

*Ngày phát hành: ngày 28 tháng 2 năm 2025*

### Sự cố đã sửa

- Sửa lỗi phân tích đồ thị tri thức cho tài liệu lớn.
- Sửa lỗi hiển thị nhãn tag bị trùng.

---

## v0.16.2

*Ngày phát hành: ngày 22 tháng 2 năm 2025*

### Sự cố đã sửa

- Sửa lỗi nghiêm trọng liên quan đến truy vấn GraphRAG.

---

## v0.16.1

*Ngày phát hành: ngày 15 tháng 2 năm 2025*

### Sự cố đã sửa

- Sửa lỗi tương thích DeepSeek R1 trong một số nhà cung cấp.
- Sửa lỗi thao tác đồ thị tri thức.

---

## v0.16.0

*Ngày phát hành: ngày 8 tháng 2 năm 2025*

### Tính năng mới

- **Hỗ trợ DeepSeek R1/V3**: Tích hợp các mô hình DeepSeek R1 và V3 mới nhất.
- **Tái cấu trúc GraphRAG**: Thiết kế lại mô-đun đồ thị tri thức với hiệu suất và độ chính xác cao hơn.
- **Dataset thẻ (Tag dataset)**: Sử dụng nhãn thẻ (tag) để lọc và tổ chức tài liệu trong truy vấn.
- **Hỗ trợ RAPTOR**: Thêm RAPTOR (Recursive Abstractive Processing for Tree-Organized Retrieval) để tóm tắt đệ quy.

### Cải tiến

- Tối ưu cơ chế xây dựng đồ thị tri thức.
- Cải tiến chất lượng tóm tắt tài liệu.

### Các mô hình mới được hỗ trợ

- DeepSeek R1, DeepSeek V3

---

## v0.15.1

*Ngày phát hành: ngày 28 tháng 12 năm 2024*

### Sự cố đã sửa

- Sửa lỗi trong API phiên agent.
- Sửa lỗi phân trang trong danh sách tài liệu.

---

## v0.15.0

*Ngày phát hành: ngày 20 tháng 12 năm 2024*

### Tính năng mới

- **API agent mới**: REST API đầy đủ cho quản lý và thực thi agent.
- **Page rank**: Sắp xếp kết quả truy xuất theo mức độ liên quan dựa trên page rank.
- **Công cụ tìm kiếm Wikipedia**: Thêm thành phần tìm kiếm Wikipedia cho agent.
- **Hỗ trợ Infinity Engine**: Infinity là engine tài liệu thay thế cho Elasticsearch.

### Cải tiến

- Tăng tốc pipeline truy vấn cho tập dữ liệu lớn.
- Cải tiến hỗ trợ tệp Excel và CSV.

---

## v0.14.1

*Ngày phát hành: ngày 29 tháng 11 năm 2024*

### Sự cố đã sửa

- Sửa lỗi engine Infinity khi xử lý tài liệu.
- Sửa lỗi giao diện quản lý dataset.

---

## v0.14.0

*Ngày phát hành: ngày 22 tháng 11 năm 2024*

### Tính năng mới

- **Hỗ trợ Infinity/Elasticsearch**: Chuyển đổi giữa Elasticsearch và Infinity làm engine tài liệu.
- **Phân tích nâng cao**: Thêm hỗ trợ phân tích bảng trong PDF phức tạp.
- **Pipeline RAPTOR**: Hỗ trợ đầy đủ pipeline RAPTOR cho tóm tắt phân cấp.

### Cải tiến

- Tăng tốc độ nhúng tài liệu lớn.
- Cải tiến độ chính xác nhận dạng ký tự trong OCR.

---

## v0.13.0

*Ngày phát hành: ngày 25 tháng 10 năm 2024*

### Tính năng mới

- **Quản lý nhóm (Team Management)**: Hỗ trợ cộng tác nhóm với phân quyền chi tiết.
- **Giao diện Agent mới**: Giao diện thiết kế lại cho xây dựng và quản lý agent.
- **Công cụ SQL**: Thêm thành phần thực thi truy vấn SQL cho agent.

### Cải tiến

- Cải tiến hiệu suất pipeline RAG cho tập dữ liệu lớn.
- Tối ưu sử dụng GPU cho mô hình nhúng.

---

## v0.12.0

*Ngày phát hành: ngày 27 tháng 9 năm 2024*

### Tính năng mới

- **Agentic RAG**: Ra mắt hệ thống xây dựng agent dựa trên RAG cho phép tích hợp nhiều nguồn dữ liệu và công cụ.
- **Thành phần tùy chỉnh**: Cho phép xây dựng thành phần agent tùy chỉnh.
- **Phân tích hình ảnh**: Hỗ trợ trích xuất và phân tích nội dung hình ảnh.

### Cải tiến

- Tăng hiệu suất tổng thể pipeline RAG.
- Cải tiến khả năng tích hợp LLM bên thứ ba.

---

## v0.11.0

*Ngày phát hành: ngày 30 tháng 8 năm 2024*

### Tính năng mới

- **Kết quả theo luồng**: Hỗ trợ streaming đầy đủ cho hội thoại RAG.
- **GraphRAG**: Tích hợp GraphRAG để truy vấn dựa trên đồ thị tri thức.
- **Hỗ trợ thêm định dạng**: Thêm hỗ trợ cho EPUB, RTF và các định dạng tài liệu khác.

---

## v0.10.0

*Ngày phát hành: ngày 2 tháng 8 năm 2024*

### Tính năng mới

- **Trợ lý chat đa dataset**: Một trợ lý chat có thể kết nối nhiều dataset.
- **API REST đầy đủ**: Cung cấp REST API đầy đủ cho tích hợp bên ngoài.
- **Hỗ trợ MinIO**: Lưu trữ tài liệu trên MinIO hoặc Amazon S3.

---

## v0.9.0

*Ngày phát hành: ngày 5 tháng 7 năm 2024*

### Tính năng mới

- **Cải thiện trình phân tích PDF**: Nâng cấp đáng kể chất lượng nhận dạng bố cục và văn bản trong PDF.
- **Công cụ reranking**: Hỗ trợ thêm mô hình reranking để cải thiện thứ tự kết quả.

---

## v0.8.0

*Ngày phát hành: ngày 7 tháng 6 năm 2024*

### Tính năng mới

- **Quản lý dataset nâng cao**: Mới nhất là nhập tài liệu hàng loạt và tổ chức theo thư mục.
- **Tích hợp nhiều nhà cung cấp LLM hơn**: Thêm hỗ trợ Baidu, Spark, MiniMax.

---

## v0.7.0

*Ngày phát hành: ngày 10 tháng 5 năm 2024*

### Tính năng mới

- **Lịch sử hội thoại**: Lưu và quản lý lịch sử hội thoại.
- **Hỗ trợ thêm loại tệp**: Thêm hỗ trợ phân tích HTML, Markdown và Email.

---

## v0.6.0

*Ngày phát hành: ngày 12 tháng 4 năm 2024*

### Tính năng mới

- **Phân đoạn nâng cao**: Hỗ trợ nhiều chiến lược phân đoạn tài liệu.
- **Giao diện người dùng mới**: Thiết kế lại hoàn toàn giao diện người dùng.
- **Hỗ trợ đa ngôn ngữ**: Cải thiện hỗ trợ tài liệu tiếng Trung, Nhật, Hàn và các ngôn ngữ khác.

---

## v0.5.0

*Ngày phát hành: ngày 15 tháng 3 năm 2024*

### Tính năng mới

- **Phát hành công khai**: Phiên bản mã nguồn mở đầu tiên của RAGFlow.
- **Phân tích tài liệu sâu**: Phân tích tài liệu PDF, Word, Excel, PowerPoint với độ chính xác cao.
- **Tích hợp LLM**: Hỗ trợ OpenAI GPT, Azure OpenAI, Moonshot, Tongyi Qianwen.
- **Pipeline RAG đầy đủ**: Lập chỉ mục → Nhúng → Truy xuất → Tạo kết quả.
- **Trợ lý chat**: Giao diện chat dựa trên web với trích dẫn nguồn.
