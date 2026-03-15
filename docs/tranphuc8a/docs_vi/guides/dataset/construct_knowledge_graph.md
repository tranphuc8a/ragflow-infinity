---
sidebar_position: 8
slug: /construct_knowledge_graph
sidebar_custom_props: {
  categoryIcon: LucideWandSparkles
}
---
# Xây dựng đồ thị tri thức

Tạo đồ thị tri thức cho tập dữ liệu của bạn.

---

Để nâng cao khả năng hỏi đáp đa bước, RAGFlow thêm một bước xây dựng đồ thị tri thức giữa trích xuất dữ liệu và lập chỉ mục, như minh họa bên dưới. Bước này tạo ra các đoạn bổ sung từ các đoạn hiện có được tạo bởi phương pháp phân đoạn được chỉ định.

![Image](https://github.com/user-attachments/assets/1ec21d8e-f255-4d65-9918-69b72dfa142b)

Từ phiên bản v0.16.0 trở đi, RAGFlow hỗ trợ xây dựng đồ thị tri thức trên một tập dữ liệu, cho phép bạn xây dựng một đồ thị *thống nhất* trên nhiều tệp trong tập dữ liệu của mình. Khi một tệp mới được tải lên bắt đầu phân tích, đồ thị được tạo sẽ tự động cập nhật.

:::danger CẢNH BÁO
Xây dựng đồ thị tri thức đòi hỏi nhiều bộ nhớ, tài nguyên tính toán và token.
:::

## Kịch bản

Đồ thị tri thức đặc biệt hữu ích cho hỏi đáp đa bước liên quan đến logic *lồng nhau*. Chúng vượt trội hơn các phương pháp trích xuất truyền thống khi bạn thực hiện hỏi đáp về sách hoặc tác phẩm với các thực thể và mối quan hệ phức tạp.

:::tip LƯU Ý
RAPTOR (Recursive Abstractive Processing for Tree Organized Retrieval) cũng có thể được sử dụng cho các tác vụ hỏi đáp đa bước. Xem [Bật RAPTOR](./enable_raptor.md) để biết chi tiết. Bạn có thể sử dụng một trong hai phương pháp hoặc cả hai, nhưng hãy đảm bảo bạn hiểu chi phí bộ nhớ, tính toán và token liên quan.
:::

## Điều kiện tiên quyết

Mô hình chat mặc định của hệ thống được sử dụng để tạo đồ thị tri thức. Trước khi tiến hành, hãy đảm bảo bạn đã cấu hình đúng mô hình chat:

![Đặt mô hình mặc định](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/set_default_models.jpg)

## Cấu hình

### Entity types (*Bắt buộc*)

Các loại thực thể để trích xuất từ tập dữ liệu của bạn. Các loại mặc định là: **organization** (tổ chức), **person** (người), **event** (sự kiện) và **category** (danh mục). Thêm hoặc xóa các loại để phù hợp với tập dữ liệu cụ thể của bạn.

### Method

Phương pháp để xây dựng đồ thị tri thức:

- **General**: Sử dụng các prompt được cung cấp bởi [GraphRAG](https://github.com/microsoft/graphrag) để trích xuất các thực thể và mối quan hệ.
- **Light**: (Mặc định) Sử dụng các prompt được cung cấp bởi [LightRAG](https://github.com/HKUDS/LightRAG) để trích xuất các thực thể và mối quan hệ. Tùy chọn này tiêu thụ ít token, bộ nhớ và tài nguyên tính toán hơn.

### Entity resolution

Có bật phân giải thực thể không. Bạn có thể coi đây như một công tắc loại bỏ trùng lặp thực thể. Khi bật, LLM sẽ kết hợp các thực thể tương tự - ví dụ: '2025' và 'năm 2025', hoặc 'IT' và 'Information Technology' - để xây dựng một đồ thị hiệu quả hơn.

- (Mặc định) Tắt phân giải thực thể.
- Bật phân giải thực thể. Tùy chọn này tiêu thụ thêm token.

### Community reports

Trong một đồ thị tri thức, một cộng đồng là một cụm các thực thể được liên kết bởi các mối quan hệ. Bạn có thể để LLM tạo ra một bản tóm tắt cho mỗi cộng đồng, được gọi là báo cáo cộng đồng. Xem [tại đây](https://www.microsoft.com/en-us/research/blog/graphrag-improving-global-search-via-dynamic-community-selection/) để biết thêm thông tin. Điều này cho biết có tạo báo cáo cộng đồng không:

- Tạo báo cáo cộng đồng. Tùy chọn này tiêu thụ thêm token.
- (Mặc định) Không tạo báo cáo cộng đồng.

## Bắt đầu nhanh

1. Điều hướng đến trang **Configuration** của tập dữ liệu và cập nhật:

   - Entity types: *Bắt buộc* - Chỉ định các loại thực thể trong đồ thị tri thức cần tạo. Bạn không nhất thiết phải giữ nguyên mặc định, nhưng bạn cần tùy chỉnh chúng cho tài liệu của mình.
   - Method: *Tùy chọn*
   - Entity resolution: *Tùy chọn*
   - Community reports: *Tùy chọn*
   *Các cấu hình đồ thị tri thức mặc định cho tập dữ liệu của bạn hiện đã được đặt.*

2. Điều hướng đến trang **Files** của tập dữ liệu, nhấp vào nút **Generate** ở góc trên bên phải của trang, sau đó chọn **Knowledge graph** từ menu thả xuống để bắt đầu quá trình tạo đồ thị tri thức.

   *Bạn có thể nhấp vào nút tạm dừng trong menu thả xuống để dừng quá trình xây dựng khi cần thiết.*

3. Quay lại trang **Configuration**:

   *Khi một đồ thị tri thức được tạo, trường **Knowledge graph** thay đổi từ `Not generated` thành `Generated at a specific timestamp`. Bạn có thể xóa nó bằng cách nhấp vào nút thùng rác ở bên phải trường.*

4. Để sử dụng đồ thị tri thức đã tạo, hãy thực hiện một trong các thao tác sau:

   - Trong bảng **Chat setting** của ứng dụng chat, bật công tắc **Use knowledge graph**.
   - Nếu bạn đang sử dụng agent, hãy nhấp vào thành phần agent **Retrieval** để chỉ định (các) tập dữ liệu và bật công tắc **Use knowledge graph**.

## Câu hỏi thường gặp

### Đồ thị tri thức có tự động cập nhật khi tôi xóa một tệp liên quan không?

Không. Đồ thị tri thức *không* cập nhật *cho đến khi* bạn tạo lại đồ thị tri thức cho tập dữ liệu của mình.

### Cách xóa một đồ thị tri thức đã tạo?

Trên trang **Configuration** của tập dữ liệu, tìm trường **Knowledge graph** và nhấp vào nút thùng rác ở bên phải trường.

### Đồ thị tri thức được tạo được lưu trữ ở đâu?

Tất cả các đoạn của đồ thị tri thức đã tạo được lưu trữ trong công cụ tài liệu của RAGFlow: Elasticsearch hoặc [Infinity](https://github.com/infiniflow/infinity).

### Cách xuất một đồ thị tri thức đã tạo?

Không. Xuất đồ thị tri thức đã tạo không được hỗ trợ. Nếu bạn vẫn cho rằng tính năng này là cần thiết, vui lòng [đặt vấn đề](https://github.com/infiniflow/ragflow/issues) giải thích trường hợp sử dụng của bạn và tầm quan trọng của nó.
