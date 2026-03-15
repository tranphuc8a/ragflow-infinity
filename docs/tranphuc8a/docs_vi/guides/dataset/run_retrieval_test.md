---
sidebar_position: 10
slug: /run_retrieval_test
sidebar_custom_props: {
  categoryIcon: LucideTextSearch
}
---
# Chạy kiểm tra truy xuất

Thực hiện kiểm tra truy xuất trên tập dữ liệu của bạn để kiểm tra xem các đoạn dự định có thể được truy xuất không.

---

Sau khi các tệp được tải lên và phân tích, bạn nên chạy kiểm tra truy xuất trước khi tiếp tục cấu hình trợ lý chat. Chạy kiểm tra truy xuất *không* phải là bước không cần thiết hoặc thừa! Giống như tinh chỉnh một công cụ chính xác, RAGFlow yêu cầu điều chỉnh cẩn thận để đạt hiệu suất hỏi đáp tối ưu. Cài đặt tập dữ liệu, cấu hình trợ lý chat và các mô hình lớn và nhỏ được chỉ định đều có thể ảnh hưởng đáng kể đến kết quả cuối cùng. Chạy kiểm tra truy xuất xác minh liệu các đoạn dự định có thể được phục hồi không, cho phép bạn nhanh chóng xác định các lĩnh vực cần cải thiện hoặc xác định bất kỳ vấn đề nào cần giải quyết. Ví dụ, khi gỡ lỗi hệ thống hỏi đáp của bạn, nếu bạn biết rằng các đoạn đúng có thể được truy xuất, bạn có thể tập trung nỗ lực vào nơi khác. Ví dụ, trong issue [#5627](https://github.com/infiniflow/ragflow/issues/5627), vấn đề được phát hiện là do giới hạn của LLM.

Trong quá trình kiểm tra truy xuất, các đoạn được tạo từ phương pháp phân đoạn được chỉ định của bạn được truy xuất sử dụng tìm kiếm hybrid. Tìm kiếm này kết hợp độ tương đồng từ khóa có trọng số với độ tương đồng cosine vector có trọng số hoặc điểm reranking có trọng số, tùy thuộc vào cài đặt của bạn:

- Nếu không có mô hình rerank nào được chọn, độ tương đồng từ khóa có trọng số sẽ được kết hợp với độ tương đồng cosine vector có trọng số.
- Nếu một mô hình rerank được chọn, độ tương đồng từ khóa có trọng số sẽ được kết hợp với điểm reranking vector có trọng số.

Ngược lại, các đoạn được tạo từ [xây dựng đồ thị tri thức](./construct_knowledge_graph.md) chỉ được truy xuất sử dụng độ tương đồng cosine vector.

## Điều kiện tiên quyết

- Các tệp của bạn được tải lên và phân tích thành công trước khi chạy kiểm tra truy xuất.
- Đồ thị tri thức phải được xây dựng thành công trước khi bật **Use knowledge graph**.

## Cấu hình

### Similarity threshold

Đây đặt ngưỡng để truy xuất các đoạn: các đoạn có độ tương đồng dưới ngưỡng sẽ bị lọc bỏ. Theo mặc định, ngưỡng được đặt là 0.2. Điều này có nghĩa là chỉ các đoạn có điểm tương đồng hybrid từ 20 trở lên mới được truy xuất.

### Vector similarity weight

Đây đặt trọng số của độ tương đồng vector trong điểm tương đồng tổng hợp, dù được sử dụng với độ tương đồng cosine vector hay điểm reranking. Theo mặc định, nó được đặt là 0.3, làm cho trọng số của thành phần kia là 0.7 (1 - 0.3).

### Rerank model

- Nếu để trống, RAGFlow sẽ sử dụng kết hợp độ tương đồng từ khóa có trọng số và độ tương đồng cosine vector có trọng số.
- Nếu một mô hình rerank được chọn, độ tương đồng từ khóa có trọng số sẽ được kết hợp với điểm reranking vector có trọng số.

:::danger QUAN TRỌNG
Sử dụng mô hình rerank sẽ tăng đáng kể thời gian nhận phản hồi.
:::

### Use knowledge graph

Trong một đồ thị tri thức, mô tả thực thể, mô tả mối quan hệ hoặc báo cáo cộng đồng tồn tại như là một đoạn độc lập. Công tắc này cho biết có thêm các đoạn này vào việc truy xuất không.

Công tắc bị tắt theo mặc định. Khi bật, RAGFlow thực hiện các thao tác sau trong kiểm tra truy xuất:

1. Trích xuất các thực thể và loại thực thể từ truy vấn của bạn sử dụng LLM.
2. Truy xuất N thực thể hàng đầu từ đồ thị dựa trên các giá trị PageRank của chúng, sử dụng các loại thực thể được trích xuất.
3. Tìm các thực thể tương tự và các mối quan hệ N-hop của chúng từ đồ thị sử dụng các nhúng của các thực thể truy vấn đã trích xuất.
4. Truy xuất các mối quan hệ tương tự từ đồ thị sử dụng nhúng truy vấn.
5. Xếp hạng các thực thể và mối quan hệ đã truy xuất này bằng cách nhân giá trị PageRank của mỗi cái với điểm tương đồng của nó với truy vấn, trả về top n là kết quả truy xuất cuối cùng.
6. Truy xuất báo cáo cho cộng đồng liên quan đến nhiều thực thể nhất trong kết quả truy xuất cuối cùng.
   *Mô tả thực thể đã truy xuất, mô tả mối quan hệ và báo cáo cộng đồng top 1 được gửi đến LLM để tạo nội dung.*

:::danger QUAN TRỌNG
Sử dụng đồ thị tri thức trong kiểm tra truy xuất sẽ tăng đáng kể thời gian nhận phản hồi.
:::

### Cross-language search

Để thực hiện [tìm kiếm đa ngôn ngữ](../../references/glossary.mdx#cross-language-search), hãy chọn một hoặc nhiều ngôn ngữ mục tiêu từ menu thả xuống. Mô hình chat mặc định của hệ thống sau đó sẽ dịch truy vấn của bạn nhập vào trường Test text sang (các) ngôn ngữ mục tiêu được chọn. Việc dịch này đảm bảo khớp ngữ nghĩa chính xác qua các ngôn ngữ, cho phép bạn truy xuất kết quả liên quan bất kể sự khác biệt ngôn ngữ.

:::tip LƯU Ý
- Khi chọn ngôn ngữ mục tiêu, hãy đảm bảo rằng các ngôn ngữ này có trong tập dữ liệu để đảm bảo tìm kiếm hiệu quả.
- Nếu không có ngôn ngữ mục tiêu nào được chọn, hệ thống sẽ chỉ tìm kiếm bằng ngôn ngữ của truy vấn, có thể khiến thông tin liên quan bằng ngôn ngữ khác bị bỏ lỡ.
:::

### Test text

Trường này là nơi bạn nhập truy vấn kiểm tra.

## Quy trình

1. Điều hướng đến trang **Retrieval testing** của tập dữ liệu, nhập truy vấn vào **Test text** và nhấp vào **Testing** để chạy kiểm tra.
2. Nếu kết quả không đạt yêu cầu, hãy điều chỉnh các tùy chọn được liệt kê trong phần Configuration và chạy lại kiểm tra.

   *Sau đây là ảnh chụp màn hình của kiểm tra truy xuất được thực hiện mà không sử dụng đồ thị tri thức. Nó thể hiện tìm kiếm hybrid kết hợp độ tương đồng từ khóa có trọng số và độ tương đồng cosine vector có trọng số. Điểm tương đồng hybrid tổng thể là 28.56, được tính là 25.17 (điểm tương đồng thuật ngữ) x 0.7 + 36.49 (điểm tương đồng vector) x 0.3:*
   ![Image](https://github.com/user-attachments/assets/541554d4-3f3e-44e1-954b-0ae77d7372c6)

   *Sau đây là ảnh chụp màn hình của kiểm tra truy xuất được thực hiện sử dụng đồ thị tri thức. Nó cho thấy rằng chỉ có độ tương đồng vector được sử dụng cho các đoạn được tạo bởi đồ thị tri thức:*
   ![Image](https://github.com/user-attachments/assets/30a03091-0f7b-4058-901a-f4dc5ca5aa6b)

:::caution CẢNH BÁO
Nếu bạn đã điều chỉnh các cài đặt mặc định, chẳng hạn như trọng số tương đồng từ khóa hoặc ngưỡng tương đồng, để đạt kết quả tối ưu, hãy lưu ý rằng những thay đổi này sẽ không được tự động lưu. Bạn phải áp dụng chúng cho cài đặt trợ lý chat hoặc cài đặt thành phần agent **Retrieval**.
:::

## Câu hỏi thường gặp

### LLM có được sử dụng khi công tắc Use Knowledge Graph được bật không?

Có, LLM của bạn sẽ được tham gia để phân tích truy vấn và trích xuất các thực thể và mối quan hệ liên quan từ đồ thị tri thức. Điều này cũng giải thích tại sao thêm token và thời gian sẽ được tiêu thụ.
