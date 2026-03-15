---
sidebar_position: -10
slug: /configure_knowledge_base
sidebar_custom_props: {
  categoryIcon: LucideCog
}
---
# Cấu hình tập dữ liệu

Hầu hết các trợ lý chat và Agent của RAGFlow đều dựa trên các tập dữ liệu. Mỗi tập dữ liệu của RAGFlow đóng vai trò như một nguồn kiến thức, *phân tích* các tệp được tải lên từ máy tính của bạn và các tham chiếu tệp được tạo trong hệ thống Tệp của RAGFlow thành 'kiến thức' thực sự cho các cuộc chat AI trong tương lai. Hướng dẫn này trình bày một số cách sử dụng cơ bản của tính năng tập dữ liệu, bao gồm các chủ đề sau:

- Tạo tập dữ liệu
- Cấu hình tập dữ liệu
- Tìm kiếm tập dữ liệu
- Xóa tập dữ liệu

## Tạo tập dữ liệu

Với nhiều tập dữ liệu, bạn có thể xây dựng các cuộc trả lời câu hỏi linh hoạt và đa dạng hơn. Để tạo tập dữ liệu đầu tiên:

![tạo tập dữ liệu](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/create_knowledge_base.jpg)

_Mỗi khi tạo tập dữ liệu, một thư mục với cùng tên được tạo trong thư mục **root/.knowledgebase**._

## Cấu hình tập dữ liệu

Ảnh chụp màn hình sau đây hiển thị trang cấu hình của một tập dữ liệu. Cấu hình đúng tập dữ liệu của bạn rất quan trọng cho các cuộc chat AI trong tương lai. Ví dụ, việc chọn sai mô hình nhúng hoặc phương pháp phân đoạn có thể gây ra mất thông tin ngữ nghĩa không mong đợi hoặc câu trả lời không phù hợp trong các cuộc chat.

![cấu hình tập dữ liệu](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/configure_knowledge_base.jpg)

Phần này bao gồm các chủ đề sau:

- Chọn phương pháp phân đoạn
- Chọn mô hình nhúng
- Tải lên tệp
- Phân tích tệp
- Can thiệp vào kết quả phân tích tệp
- Chạy kiểm tra truy xuất

### Chọn phương pháp phân đoạn

RAGFlow cung cấp nhiều mẫu phân đoạn tích hợp sẵn để tạo điều kiện phân đoạn các tệp có bố cục khác nhau và đảm bảo tính toàn vẹn ngữ nghĩa. Từ menu thả xuống phương pháp phân đoạn **Tích hợp sẵn** trong **Loại phân tích**, bạn có thể chọn mẫu mặc định phù hợp với bố cục và định dạng tệp của mình. Bảng sau đây hiển thị mô tả và các định dạng tệp tương thích của mỗi mẫu phân đoạn được hỗ trợ:

| **Mẫu**     | Mô tả                                                                        | Định dạng tệp                                                                                           |
|-------------|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Tổng quát   | Tệp được phân đoạn liên tiếp dựa trên số token đoạn được đặt trước.           | MD, MDX, DOCX, XLSX, XLS (Excel 97-2003), PPT, PDF, TXT, JPEG, JPG, PNG, TIF, GIF, CSV, JSON, EML, HTML |
| Hỏi & Đáp   | Truy xuất thông tin liên quan và tạo câu trả lời để trả lời câu hỏi.         | XLSX, XLS (Excel 97-2003), CSV/TXT                                                                      |
| Sơ yếu lý lịch | Chỉ phiên bản Enterprise. Bạn cũng có thể thử trên demo.ragflow.io.        | DOCX, PDF, TXT                                                                                          |
| Hướng dẫn   |                                                                               | PDF                                                                                                     |
| Bảng        | Chế độ bảng sử dụng công nghệ TSI để phân tích dữ liệu hiệu quả.            | XLSX, XLS (Excel 97-2003), CSV/TXT                                                                      |
| Bài báo     |                                                                               | PDF                                                                                                     |
| Sách        |                                                                               | DOCX, PDF, TXT                                                                                          |
| Luật        |                                                                               | DOCX, PDF, TXT                                                                                          |
| Thuyết trình |                                                                              | PDF, PPTX                                                                                               |
| Hình ảnh    |                                                                               | JPEG, JPG, PNG, TIF, GIF                                                                                |
| Một         | Mỗi tài liệu được phân đoạn toàn bộ (thành một).                            | DOCX, XLSX, XLS (Excel 97-2003), PDF, TXT                                                               |
| Tag         | Tập dữ liệu hoạt động như bộ tag cho các tập dữ liệu khác.                  | XLSX, CSV/TXT                                                                                           |

Bạn cũng có thể thay đổi phương pháp phân đoạn của tệp trên trang **Tệp**.

![thay đổi phương pháp phân đoạn](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/change_chunking_method.jpg)

<details>
  <summary>Từ v0.21.0 trở đi, RAGFlow hỗ trợ pipeline nhập liệu để tùy chỉnh quy trình nhập liệu và làm sạch dữ liệu.</summary>
   
  Để sử dụng pipeline dữ liệu tùy chỉnh:

  1. Trên trang **Agent**, nhấp **+ Tạo agent** > **Tạo từ đầu**.
  2. Chọn **Pipeline nhập liệu** và đặt tên pipeline dữ liệu của bạn trong popup, sau đó nhấp **Lưu** để hiển thị canvas pipeline dữ liệu.
  3. Sau khi cập nhật pipeline dữ liệu, nhấp **Lưu** ở góc trên bên phải canvas.
  4. Điều hướng đến trang **Cấu hình** của tập dữ liệu, chọn **Chọn pipeline** trong **Pipeline nhập liệu**.
     
     *Pipeline dữ liệu đã lưu của bạn sẽ xuất hiện trong menu thả xuống bên dưới.*

</details>

### Chọn mô hình nhúng

Mô hình nhúng chuyển đổi các đoạn thành các embedding. Nó không thể thay đổi sau khi tập dữ liệu có các đoạn. Để chuyển sang mô hình nhúng khác, bạn phải xóa tất cả các đoạn hiện có trong tập dữ liệu. Lý do rõ ràng là chúng ta *phải* đảm bảo rằng các tệp trong một tập dữ liệu cụ thể được chuyển đổi thành embedding bằng *cùng* mô hình nhúng (đảm bảo chúng được so sánh trong cùng không gian nhúng).

:::danger QUAN TRỌNG
Một số mô hình nhúng được tối ưu hóa cho các ngôn ngữ cụ thể, vì vậy hiệu suất có thể bị ảnh hưởng nếu bạn sử dụng chúng để nhúng các tài liệu bằng ngôn ngữ khác.
:::

### Tải lên tệp

- Hệ thống Tệp của RAGFlow cho phép bạn liên kết một tệp với nhiều tập dữ liệu, trong trường hợp đó mỗi tập dữ liệu đích lưu tham chiếu đến tệp.
- Trong **Cơ sở kiến thức**, bạn cũng có tùy chọn tải lên một tệp đơn hoặc một thư mục tệp (tải lên hàng loạt) từ máy tính của mình lên một tập dữ liệu, trong trường hợp đó tập dữ liệu giữ bản sao tệp.

Mặc dù tải tệp trực tiếp lên tập dữ liệu có vẻ tiện lợi hơn, chúng tôi *rất khuyến nghị* tải tệp lên hệ thống Tệp của RAGFlow và sau đó liên kết chúng với các tập dữ liệu đích. Theo cách này, bạn có thể tránh xóa vĩnh viễn các tệp tải lên tập dữ liệu.

### Phân tích tệp

Phân tích tệp là chủ đề quan trọng trong cấu hình tập dữ liệu. Ý nghĩa của phân tích tệp trong RAGFlow có hai mặt: phân đoạn tệp dựa trên bố cục tệp và xây dựng các chỉ mục nhúng và toàn văn bản (từ khóa) trên các đoạn này. Sau khi chọn phương pháp phân đoạn và mô hình nhúng, bạn có thể bắt đầu phân tích tệp:

![phân tích tệp](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/parse_file.jpg)

- Như hiển thị trên, RAGFlow cho phép bạn sử dụng phương pháp phân đoạn khác cho một tệp cụ thể, cung cấp sự linh hoạt vượt ra ngoài phương pháp mặc định.
- Như hiển thị trên, RAGFlow cho phép bạn bật hoặc tắt từng tệp riêng lẻ, cung cấp kiểm soát tốt hơn đối với các cuộc chat AI dựa trên tập dữ liệu.

### Can thiệp vào kết quả phân tích tệp

RAGFlow có tính năng hiển thị và giải thích được, cho phép bạn xem kết quả phân đoạn và can thiệp khi cần thiết. Để làm như vậy:

1. Nhấp vào tệp đã hoàn thành phân tích tệp để xem kết quả phân đoạn:

   _Bạn sẽ được chuyển đến trang **Đoạn**:_

   ![đoạn](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/file_chunks.jpg)

2. Di chuột qua mỗi ảnh chụp màn hình để xem nhanh mỗi đoạn.

3. Nhấp đúp vào văn bản đã phân đoạn để thêm từ khóa, câu hỏi, tag hoặc thực hiện các thay đổi *thủ công* khi cần:

   ![cập nhật đoạn](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/add_keyword_question.jpg)

:::caution LƯU Ý
Bạn có thể thêm từ khóa vào một đoạn tệp để tăng xếp hạng của nó cho các truy vấn chứa các từ khóa đó. Hành động này làm tăng trọng số từ khóa và có thể cải thiện vị trí của nó trong danh sách tìm kiếm.
:::

4. Trong Kiểm tra truy xuất, đặt câu hỏi nhanh trong **Văn bản kiểm tra** để kiểm tra xem cấu hình của bạn có hoạt động không:

   _Như bạn có thể thấy từ kết quả sau, RAGFlow phản hồi với các trích dẫn trung thực._

   ![kiểm tra truy xuất](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/retrieval_test.jpg)

### Chạy kiểm tra truy xuất

RAGFlow sử dụng kết hợp tìm kiếm toàn văn bản và tìm kiếm vector trong các cuộc chat. Trước khi thiết lập cuộc chat AI, hãy xem xét điều chỉnh các tham số sau để đảm bảo thông tin dự định luôn xuất hiện trong câu trả lời:

- Ngưỡng tương đồng: Các đoạn có tương đồng dưới ngưỡng sẽ bị lọc. Theo mặc định, nó được đặt là 0.2.
- Trọng số tương đồng vector: Tỷ lệ phần trăm mà tương đồng vector đóng góp vào điểm tổng thể. Theo mặc định, nó được đặt là 0.3.

Xem [Chạy kiểm tra truy xuất](./run_retrieval_test.md) để biết chi tiết.

## Tìm kiếm tập dữ liệu

Tính đến RAGFlow v0.23.1, tính năng tìm kiếm vẫn ở dạng cơ bản, chỉ hỗ trợ tìm kiếm tập dữ liệu theo tên.

![tìm kiếm tập dữ liệu](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/search_datasets.jpg)

## Xóa tập dữ liệu

Bạn được phép xóa một tập dữ liệu. Di chuột qua ba dấu chấm của thẻ tập dữ liệu mong muốn và tùy chọn **Xóa** xuất hiện. Khi bạn xóa tập dữ liệu, thư mục liên kết trong thư mục **root/.knowledge** sẽ TỰ ĐỘNG BỊ XÓA. Hậu quả là:

- Các tệp tải lên trực tiếp vào tập dữ liệu sẽ biến mất;
- Các tham chiếu tệp, mà bạn đã tạo từ trong hệ thống Tệp của RAGFlow, sẽ biến mất, nhưng các tệp liên kết vẫn tồn tại.

![xóa tập dữ liệu](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/delete_datasets.jpg)
