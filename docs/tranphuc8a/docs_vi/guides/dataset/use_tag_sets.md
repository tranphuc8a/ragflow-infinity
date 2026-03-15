---
sidebar_position: 6
slug: /use_tag_sets
sidebar_custom_props: {
  categoryIcon: LucideTags
}
---
# Sử dụng tập thẻ

Sử dụng tập thẻ để tự động gắn thẻ các đoạn trong tập dữ liệu của bạn.

---

Độ chính xác truy xuất là thước đo cho một framework RAG sẵn sàng sản xuất. Ngoài các phương pháp nâng cao truy xuất như auto-keyword, auto-question và đồ thị tri thức, RAGFlow giới thiệu tính năng auto-tagging để giải quyết các khoảng cách ngữ nghĩa. Tính năng auto-tagging tự động ánh xạ các thẻ trong các tập thẻ do người dùng xác định đến các đoạn liên quan trong tập dữ liệu của bạn dựa trên độ tương đồng với mỗi đoạn. Cơ chế tự động hóa này cho phép bạn áp dụng một "lớp" tri thức chuyên biệt theo lĩnh vực bổ sung vào các tập dữ liệu hiện có, điều này đặc biệt hữu ích khi xử lý số lượng lớn các đoạn.

Để sử dụng tính năng này, hãy đảm bảo bạn có ít nhất một tập thẻ được cấu hình đúng, chỉ định (các) tập thẻ trên trang **Configuration** của tập dữ liệu, sau đó phân tích lại tài liệu để bắt đầu quá trình auto-tagging. Trong quá trình này, mỗi đoạn trong tập dữ liệu được so sánh với mọi mục trong (các) tập thẻ được chỉ định, và các thẻ được tự động áp dụng dựa trên độ tương đồng.

## Kịch bản

Auto-tagging áp dụng trong các tình huống mà các đoạn tương tự nhau đến mức các đoạn dự định không thể được phân biệt với phần còn lại. Ví dụ, khi bạn có một vài đoạn về iPhone và phần lớn về vỏ iPhone hoặc phụ kiện iPhone, rất khó để truy xuất các đoạn về iPhone mà không có thông tin bổ sung.

## 1. Tạo tập thẻ

Bạn có thể coi một tập thẻ như một tập đóng, và các thẻ để gắn vào các đoạn trong tập dữ liệu của bạn *chỉ* đến từ tập thẻ được chỉ định. Bạn sử dụng tập thẻ để "thông báo" cho RAGFlow biết đoạn nào cần gắn thẻ và thẻ nào cần áp dụng.

### Chuẩn bị tệp bảng thẻ

Một tập thẻ có thể bao gồm một hoặc nhiều tệp bảng ở định dạng XLSX, CSV hoặc TXT. Mỗi tệp bảng trong tập thẻ chứa hai cột, **Description** và **Tag**:

- Cột đầu tiên cung cấp mô tả về các thẻ được liệt kê trong cột thứ hai. Những mô tả này có thể là các đoạn ví dụ hoặc các truy vấn ví dụ. Độ tương đồng sẽ được tính toán giữa mỗi mục trong cột này và mọi đoạn trong tập dữ liệu của bạn.
- Cột **Tag** bao gồm các thẻ để ghép nối với các mục mô tả. Nhiều thẻ phải được phân tách bằng dấu phẩy (,).

:::tip LƯU Ý
Theo nguyên tắc chung, hãy xem xét việc bao gồm các mục sau trong bảng thẻ:

- Mô tả về các đoạn dự định, cùng với các thẻ tương ứng.
- Truy vấn của người dùng không thể truy xuất phản hồi đúng sử dụng các phương pháp khác, đảm bảo các thẻ của chúng khớp với các đoạn dự định trong tập dữ liệu.
:::

### Tạo tập thẻ

:::danger QUAN TRỌNG
Tập thẻ *không* tham gia vào lập chỉ mục hoặc truy xuất tài liệu. Không chỉ định tập thẻ khi cấu hình trợ lý chat hoặc agent.
:::

1. Nhấp vào **+ Create dataset** để tạo tập dữ liệu.
2. Điều hướng đến trang **Configuration** của tập dữ liệu đã tạo, chọn **Built-in** trong **Ingestion pipeline**, sau đó chọn **Tag** làm phương pháp phân đoạn mặc định từ menu thả xuống **Built-in**.
3. Quay lại trang **Files** và tải lên và phân tích tệp bảng ở định dạng XLSX, CSV hoặc TXT.
   _Đám mây thẻ xuất hiện trong phần **Tag view**, cho biết tập thẻ đã được tạo:_
   ![Image](https://github.com/user-attachments/assets/abefbcbf-c130-4abe-95e1-267b0d2a0505)
4. Nhấp vào tab **Table** để xem bảng tần số thẻ:
   ![Image](https://github.com/user-attachments/assets/af91d10c-5ea5-491f-ab21-3803d5ebf59f)

## 2. Gắn thẻ cho các đoạn

Sau khi tập thẻ được tạo, bạn có thể áp dụng nó cho tập dữ liệu:

1. Điều hướng đến trang **Configuration** của tập dữ liệu.
2. Chọn tập thẻ từ menu thả xuống **Tag sets** và nhấp vào **Save** để xác nhận.

   :::tip LƯU Ý
   Nếu tập thẻ không có trong menu thả xuống, hãy kiểm tra xem nó đã được tạo hoặc cấu hình đúng chưa.
   :::

3. Phân tích lại tài liệu để bắt đầu quá trình auto-tagging.
   _Trong kịch bản chat AI sử dụng tập dữ liệu được gắn thẻ tự động, mỗi truy vấn sẽ được gắn thẻ sử dụng (các) tập thẻ tương ứng và các đoạn có các thẻ này sẽ có cơ hội được truy xuất cao hơn._

## 3. Cập nhật tập thẻ

Tạo tập thẻ *không* phải là một lần cho tất cả. Thường thì bạn cần cập nhật hoặc xóa các thẻ hiện có hoặc thêm các mục mới.

- Bạn có thể cập nhật tập thẻ hiện có trong bảng tần số thẻ.
- Để thêm các mục mới, bạn có thể thêm và phân tích các tệp bảng mới ở định dạng XLSX, CSV hoặc TXT.

### Cập nhật tập thẻ trong bảng tần số thẻ

1. Điều hướng đến trang **Configuration** trong tập thẻ của bạn.
2. Nhấp vào tab **Table** trong **Tag view** để xem bảng tần số thẻ, nơi bạn có thể cập nhật tên thẻ hoặc xóa thẻ.

:::danger QUAN TRỌNG
Khi tập thẻ được cập nhật, bạn phải phân tích lại tài liệu trong tập dữ liệu để các thẻ của chúng có thể được cập nhật tương ứng.
:::

### Thêm tệp bảng mới

1. Điều hướng đến trang **Configuration** trong tập thẻ của bạn.
2. Điều hướng đến trang **Dataset** và tải lên và phân tích tệp bảng ở định dạng XLSX, CSV hoặc TXT.

:::danger QUAN TRỌNG
Nếu bạn thêm tệp bảng mới vào tập thẻ, thì việc có phân tích lại tài liệu trong tập dữ liệu không là tùy quyết của bạn.
:::

## Câu hỏi thường gặp

### Tôi có thể tham chiếu nhiều hơn một tập thẻ không?

Có, bạn có thể. Thường thì một tập thẻ là đủ. Khi sử dụng nhiều tập thẻ, hãy đảm bảo chúng độc lập với nhau; nếu không, hãy xem xét hợp nhất các tập thẻ.

### Sự khác biệt giữa tập thẻ và tập dữ liệu tiêu chuẩn?

Tập dữ liệu tiêu chuẩn là một tập dữ liệu. Nó sẽ được tìm kiếm bởi công cụ tài liệu của RAGFlow và các đoạn được truy xuất sẽ được cung cấp cho LLM. Ngược lại, tập thẻ chỉ được sử dụng để gắn thẻ vào các đoạn trong tập dữ liệu. Nó không trực tiếp tham gia vào quá trình truy xuất, và bạn không nên chọn tập thẻ khi chọn tập dữ liệu cho trợ lý chat hoặc agent.

### Sự khác biệt giữa auto-tag và auto-keyword?

Cả hai tính năng đều nâng cao truy xuất trong RAGFlow. Tính năng auto-keyword dựa vào LLM và tiêu thụ số lượng token đáng kể, trong khi tính năng auto-tag dựa trên độ tương đồng vector và (các) tập thẻ được xác định trước. Bạn có thể coi các từ khóa được áp dụng trong tính năng auto-keyword là một tập mở, vì chúng được tạo bởi LLM. Ngược lại, tập thẻ có thể được coi là tập đóng do người dùng xác định, yêu cầu tải lên (các) tập thẻ ở các định dạng được chỉ định trước khi sử dụng.
