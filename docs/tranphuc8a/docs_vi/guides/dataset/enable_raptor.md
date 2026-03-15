---
sidebar_position: 7
slug: /enable_raptor
sidebar_custom_props: {
  categoryIcon: LucideNetwork
}
---
# Bật RAPTOR

Phương pháp tóm tắt đệ quy được sử dụng trong truy xuất và tóm tắt tri thức ngữ cảnh dài, cân bằng giữa hiểu ngữ nghĩa rộng và chi tiết tinh tế.

---

RAPTOR (Recursive Abstractive Processing for Tree Organized Retrieval) là một kỹ thuật tiền xử lý tài liệu nâng cao được giới thiệu trong một [bài báo năm 2024](https://arxiv.org/html/2401.18059v1). Được thiết kế để giải quyết các vấn đề hỏi đáp đa bước, RAPTOR thực hiện phân cụm và tóm tắt đệ quy các đoạn tài liệu để xây dựng cấu trúc cây phân cấp. Điều này cho phép truy xuất nhận biết ngữ cảnh hơn trên các tài liệu dài. RAGFlow v0.6.0 tích hợp RAPTOR để phân cụm tài liệu như một phần của pipeline tiền xử lý dữ liệu giữa trích xuất dữ liệu và lập chỉ mục, như minh họa bên dưới.

![document_clustering](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/document_clustering_as_preprocessing.jpg)

Các thử nghiệm của chúng tôi với phương pháp mới này cho thấy kết quả tiên tiến nhất (SOTA) trong các tác vụ hỏi đáp đòi hỏi lập luận phức tạp, đa bước. Bằng cách kết hợp truy xuất RAPTOR với các phương pháp phân đoạn tích hợp sẵn và/hoặc các phương pháp RAG khác, bạn có thể cải thiện hơn nữa độ chính xác hỏi đáp.

:::danger CẢNH BÁO
Bật RAPTOR đòi hỏi nhiều bộ nhớ, tài nguyên tính toán và token.
:::

## Nguyên tắc cơ bản

Sau khi các tài liệu gốc được chia thành các đoạn, các đoạn được phân cụm theo độ tương đồng ngữ nghĩa thay vì theo thứ tự gốc của chúng trong văn bản. Các cụm sau đó được tóm tắt thành các đoạn cấp cao hơn bởi mô hình chat mặc định của hệ thống. Quá trình này được áp dụng đệ quy, tạo thành cấu trúc cây với các cấp độ tóm tắt khác nhau từ dưới lên. Như minh họa trong hình bên dưới, các đoạn ban đầu tạo thành các nút lá (màu xanh) và được tóm tắt đệ quy thành một nút gốc (màu cam).

![raptor](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/clustering_and_summarizing.jpg)

Việc phân cụm và tóm tắt đệ quy nắm bắt hiểu biết rộng (bởi nút gốc) cũng như các chi tiết tinh tế (bởi các nút lá) cần thiết cho hỏi đáp đa bước.

## Kịch bản

Đối với các tác vụ hỏi đáp đa bước liên quan đến lập luận phức tạp, đa bước, thường tồn tại khoảng cách ngữ nghĩa giữa câu hỏi và câu trả lời. Kết quả là, tìm kiếm bằng câu hỏi thường thất bại trong việc truy xuất các đoạn liên quan đóng góp cho câu trả lời đúng. RAPTOR giải quyết thách thức này bằng cách cung cấp cho mô hình chat các đoạn phong phú hơn, nhận biết ngữ cảnh hơn và liên quan hơn để tóm tắt, cho phép hiểu toàn diện mà không mất đi các chi tiết chi tiết.

:::tip LƯU Ý
Đồ thị tri thức cũng có thể được sử dụng cho các tác vụ hỏi đáp đa bước. Xem [Xây dựng đồ thị tri thức](./construct_knowledge_graph.md) để biết chi tiết. Bạn có thể sử dụng một trong hai phương pháp hoặc cả hai, nhưng hãy đảm bảo bạn hiểu chi phí bộ nhớ, tính toán và token liên quan.
:::

## Điều kiện tiên quyết

Mô hình chat mặc định của hệ thống được sử dụng để tóm tắt nội dung được phân cụm. Trước khi tiến hành, hãy đảm bảo bạn đã cấu hình đúng mô hình chat:

![Đặt mô hình mặc định](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/set_default_models.jpg)

## Cấu hình

Tính năng RAPTOR bị tắt theo mặc định. Để bật nó, hãy bật thủ công công tắc **Use RAPTOR to enhance retrieval** trên trang **Configuration** của tập dữ liệu.

### Prompt

Prompt sau sẽ được áp dụng *đệ quy* để tóm tắt cụm, với `{cluster_content}` là tham số nội bộ. Chúng tôi khuyến nghị bạn giữ nguyên hiện tại. Thiết kế sẽ được cập nhật kịp thời.

```
Please summarize the following paragraphs... Paragraphs as following:
      {cluster_content}
The above is the content you need to summarize.
```

### Max token

Số token tối đa cho mỗi đoạn tóm tắt được tạo. Mặc định là 256, với giới hạn tối đa là 2048.

### Threshold

Trong RAPTOR, các đoạn được phân cụm theo độ tương đồng ngữ nghĩa của chúng. Tham số **Threshold** đặt độ tương đồng tối thiểu cần thiết để các đoạn được nhóm lại với nhau.

Mặc định là 0.1, với giới hạn tối đa là 1. **Threshold** cao hơn có nghĩa là ít đoạn hơn trong mỗi cụm, trong khi thấp hơn có nghĩa là nhiều hơn.

### Max cluster

Số lượng cụm tối đa cần tạo. Mặc định là 64, với giới hạn tối đa là 1024.

### Random seed

Seed ngẫu nhiên. Nhấp vào **+** để thay đổi giá trị seed.

## Bắt đầu nhanh

1. Điều hướng đến trang **Configuration** của tập dữ liệu và cập nhật:

   - Prompt: *Tùy chọn* - Chúng tôi khuyến nghị bạn giữ nguyên cho đến khi bạn hiểu cơ chế đằng sau.
   - Max token: *Tùy chọn*
   - Threshold: *Tùy chọn*
   - Max cluster: *Tùy chọn*

2. Điều hướng đến trang **Files** của tập dữ liệu, nhấp vào nút **Generate** ở góc trên bên phải của trang, sau đó chọn **RAPTOR** từ menu thả xuống để bắt đầu quá trình xây dựng RAPTOR.

   *Bạn có thể nhấp vào nút tạm dừng trong menu thả xuống để dừng quá trình xây dựng khi cần thiết.*

3. Quay lại trang **Configuration**:

   *Trường **RAPTOR** thay đổi từ `Not generated` thành `Generated at a specific timestamp` khi cấu trúc cây phân cấp RAPTOR được tạo. Bạn có thể xóa nó bằng cách nhấp vào nút thùng rác ở bên phải trường.*

4. Khi cấu trúc cây phân cấp RAPTOR được tạo, trợ lý chat và thành phần agent **Retrieval** của bạn sẽ sử dụng nó để truy xuất theo mặc định.
