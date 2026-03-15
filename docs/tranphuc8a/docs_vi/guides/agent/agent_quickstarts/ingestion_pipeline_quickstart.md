---
sidebar_position: 5
slug: /ingestion_pipeline_quickstart
sidebar_custom_props: {
  categoryIcon: LucideRoute
}
---

# Hướng dẫn nhanh về pipeline nhập liệu

Pipeline nhập liệu của RAGFlow là một quy trình tùy chỉnh, từng bước chuẩn bị tài liệu của bạn cho việc truy xuất và trả lời AI chất lượng cao. Bạn có thể coi đây như các khối xây dựng: bạn kết nối các "thành phần" xử lý khác nhau để tạo một pipeline phù hợp với tài liệu và nhu cầu cụ thể của mình.

---

RAGFlow là một nền tảng RAG mã nguồn mở với khả năng xử lý tài liệu mạnh mẽ. Mô-đun tích hợp sẵn của nó, DeepDoc, sử dụng phân tích thông minh để tách tài liệu để truy xuất chính xác. Để xử lý các nhu cầu thực tế đa dạng—như nguồn tệp đa dạng, bố cục phức tạp và ngữ nghĩa phong phú hơn—RAGFlow nay giới thiệu *pipeline nhập liệu*.

Pipeline nhập liệu cho phép bạn tùy chỉnh mọi bước xử lý tài liệu:

- Áp dụng các quy tắc phân tích và tách khác nhau cho từng kịch bản
- Thêm tiền xử lý như tóm tắt hoặc trích xuất từ khóa
- Kết nối với ổ đĩa đám mây và nguồn dữ liệu trực tuyến
- Sử dụng các mô hình nhận biết bố cục nâng cao cho bảng và nội dung hỗn hợp

Pipeline linh hoạt này thích ứng với dữ liệu của bạn, cải thiện chất lượng câu trả lời trong RAG.

## 1. Hiểu các thành phần pipeline cốt lõi

- Thành phần **Parser**: Đọc và hiểu các tệp của bạn (PDF, hình ảnh, email, v.v.), trích xuất văn bản và cấu trúc.
- Thành phần **Transformer**: Cải thiện văn bản bằng cách sử dụng AI để thêm tóm tắt, từ khóa hoặc câu hỏi để cải thiện tìm kiếm.
- Thành phần **Chunker**: Tách văn bản dài thành các đoạn kích thước tối ưu ("phân đoạn") để truy xuất AI tốt hơn.
- Thành phần **Indexer**: Bước cuối cùng. Gửi dữ liệu đã xử lý đến công cụ tài liệu (hỗ trợ tìm kiếm toàn văn bản và vector hybrid).

## 2. Tạo pipeline nhập liệu

1. Đi đến trang **Agent**.
2. Nhấp vào **Create agent** và bắt đầu từ canvas trống hoặc mẫu có sẵn (khuyến nghị cho người mới bắt đầu).
3. Trên canvas, kéo và kết nối các thành phần từ bảng bên phải để thiết kế luồng của bạn (ví dụ: Parser → Chunker → Transformer → Indexer).

*Bây giờ hãy xây dựng một pipeline nhập liệu điển hình!*

## 3. Cấu hình thành phần Parser

Thành phần **Parser** chuyển đổi các tệp của bạn thành văn bản có cấu trúc trong khi vẫn giữ nguyên bố cục, bảng, tiêu đề và các định dạng khác. Nó hỗ trợ 8 danh mục tệp, hơn 23 định dạng bao gồm PDF, Hình ảnh, Âm thanh, Video, Email, Bảng tính (Excel), Word, PPT, HTML và Markdown. Sau đây là một số cấu hình chính:

- Đối với tệp PDF, chọn một trong các tùy chọn sau:
  - **DeepDoc** (Mặc định): Mô hình tích hợp của RAGFlow. Tốt nhất cho tài liệu được quét hoặc bố cục phức tạp với bảng.
  - **MinerU**: Hàng đầu ngành cho các phần tử phức tạp như công thức toán học và bố cục phức tạp.
  - **Naive**: Trích xuất văn bản đơn giản. Dùng cho các tệp PDF dạng văn bản thuần túy không có phần tử phức tạp.
- Đối với tệp hình ảnh: Mặc định sử dụng OCR. Cũng có thể cấu hình Vision Language Models (VLM) để hiểu thị giác nâng cao.
- Đối với tệp Email: Chọn các trường cụ thể để phân tích (ví dụ: "subject", "body") để trích xuất chính xác.
- Đối với Bảng tính: Xuất theo định dạng HTML, giữ nguyên cấu trúc hàng/cột.
- Đối với Word/PPT: Xuất theo định dạng JSON, giữ nguyên phân cấp tài liệu (tiêu đề, đoạn văn, slide).
- Đối với Văn bản & Đánh dấu (HTML/MD): Tự động loại bỏ thẻ định dạng, tạo ra văn bản sạch.

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/parser1.png)
![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/parser2.png)

## 4. Cấu hình thành phần Chunker

Thành phần chunker tách văn bản một cách thông minh. Mục tiêu của nó là ngăn tràn cửa sổ ngữ cảnh AI và cải thiện độ chính xác ngữ nghĩa trong tìm kiếm hybrid. Có hai phương pháp cốt lõi (có thể dùng tuần tự):

- Theo Tokens (Mặc định):
  - Chunk Size: Mặc định là 512 token. Cân bằng giữa chất lượng truy xuất và tính tương thích của mô hình.
  - Overlap: Đặt **Overlapped percent** để lặp lại phần cuối của một đoạn vào đầu của đoạn tiếp theo. Cải thiện tính liên tục ngữ nghĩa.
  - Separators: Mặc định sử dụng `\n` (xuống dòng) để tách trước tiên ở các ranh giới đoạn văn tự nhiên, tránh cắt giữa câu.
- Theo Title (Phân cấp):
  - Tốt nhất cho các tài liệu có cấu trúc như sổ tay, bài báo, hợp đồng pháp lý.
  - Hệ thống tách tài liệu theo cấu trúc chương/mục. Mỗi đoạn đại diện cho một đơn vị cấu trúc hoàn chỉnh.

:::caution QUAN TRỌNG
Trong thiết kế hiện tại, nếu sử dụng cả phương pháp Token và Title, hãy kết nối thành phần **Token chunker** trước, sau đó thành phần **Title chunker**. Kết nối **Title chunker** trực tiếp với **Parser** có thể gây lỗi định dạng cho Email, Hình ảnh, Bảng tính và tệp Văn bản.
:::

## 5. Cấu hình thành phần Transformer

Thành phần **Transformer** được thiết kế để thu hẹp "Khoảng cách ngữ nghĩa". Nói chung, nó sử dụng các mô hình AI để thêm siêu dữ liệu ngữ nghĩa, làm cho nội dung của bạn dễ khám phá hơn trong quá trình truy xuất. Nó có bốn loại tạo:

- Summary: Tạo tổng quan ngắn gọn.
- Keywords: Trích xuất các thuật ngữ chính.
- Questions: Tạo các câu hỏi mà mỗi đoạn văn bản có thể trả lời.
- Metadata: Trích xuất siêu dữ liệu tùy chỉnh.

Nếu bạn có nhiều **Transformer**, hãy đảm bảo tách riêng các thành phần **Transformer** cho từng chức năng (ví dụ: một cho Summary, một cho Keywords).

Sau đây là một số cấu hình chính:

- Chế độ mô hình: (chọn một)
  - Improvise: Sáng tạo hơn, tốt cho việc tạo câu hỏi.
  - Precise: Trung thành nghiêm ngặt với văn bản, tốt cho trích xuất Summary/Keyword.
  - Balance: Mức trung gian cho hầu hết các kịch bản.
- Kỹ thuật prompt: System prompt cho từng loại tạo đều mở và có thể tùy chỉnh.
- Kết nối: **Transformer** có thể kết nối sau **Parser** (xử lý cả tài liệu) HOẶC sau **Chunker** (xử lý từng đoạn).
- Tham chiếu biến: Nút không tự động thu thập nội dung. Trong User prompt, tham chiếu thủ công các biến ngược dòng bằng cách gõ `/` và chọn đầu ra cụ thể (ví dụ: `/{Parser.output}` hoặc `/{Chunker.output}`).
- Kết nối chuỗi: Khi nối nhiều **Transformer**, **Transformer** thứ hai sẽ xử lý đầu ra của **Transformer** đầu tiên (ví dụ: tạo Keywords từ Summary) nếu các biến được tham chiếu đúng cách.

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/transformer1.png)
![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/transformer2.png)
![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/transformer3.png)

## 6. Cấu hình thành phần Indexer

Thành phần **Indexer** lập chỉ mục để truy xuất tối ưu. Đây là bước cuối cùng ghi dữ liệu đã xử lý vào công cụ tìm kiếm (như Infinity, Elasticsearch, OpenSearch). Sau đây là một số cấu hình chính:

- Phương pháp tìm kiếm:
  - Full-text: Tìm kiếm từ khóa cho các kết quả khớp chính xác (mã, tên).
  - Embedding: Tìm kiếm ngữ nghĩa sử dụng độ tương đồng vector.
  - Hybrid (Khuyến nghị): Kết hợp cả hai phương pháp để có khả năng thu hồi tốt nhất.
- Chiến lược truy xuất:
  - Processed text (Mặc định): Lập chỉ mục văn bản đã phân đoạn.
  - Questions: Lập chỉ mục các câu hỏi được tạo. Thường cho kết quả khớp độ tương đồng cao hơn so với text-to-text.
  - Augmented context: Lập chỉ mục tóm tắt thay vì văn bản thô. Tốt cho khớp chủ đề rộng.
- Filename weight: Thanh trượt để bao gồm tên tệp tài liệu như thông tin ngữ nghĩa trong truy xuất.
- Embedding model: Tự động sử dụng mô hình được đặt khi tạo tập dữ liệu.

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/indexer.png)

:::caution QUAN TRỌNG
Để tìm kiếm đồng thời trên nhiều tập dữ liệu, tất cả các tập dữ liệu được chọn phải sử dụng cùng một mô hình nhúng.
:::

## 7. Chạy thử

Nhấp vào **Run** trên canvas pipeline của bạn để tải lên tệp mẫu và xem kết quả từng bước.

## 8. Kết nối pipeline với tập dữ liệu

1. Khi tạo hoặc chỉnh sửa tập dữ liệu, tìm phần **Ingestion pipeline**.
2. Nhấp vào **Choose pipeline** và chọn pipeline đã lưu của bạn.

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/dataset_ingestion_settings.png)

*Bây giờ, tất cả các tệp được tải lên tập dữ liệu này sẽ được xử lý bởi pipeline tùy chỉnh của bạn.*
