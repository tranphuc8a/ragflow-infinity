---
sidebar_position: 30
slug: /parser_component
sidebar_custom_props: {
  categoryIcon: LucideFilePlay
}
---
# Thành phần Parser

Thành phần thiết lập các quy tắc phân tích cú pháp cho tập dữ liệu của bạn.

---

Thành phần **Parser** được tự động điền vào canvas pipeline nhập liệu và là bắt buộc trong tất cả các quy trình pipeline nhập liệu. Giống như giai đoạn **Extract** trong quy trình ETL truyền thống, thành phần **Parser** trong pipeline nhập liệu xác định cách các loại tệp khác nhau được phân tích thành dữ liệu có cấu trúc. Nhấp vào thành phần để hiển thị bảng cấu hình. Trong bảng cấu hình này, bạn thiết lập các quy tắc phân tích cho các loại tệp khác nhau.

## Cấu hình

Trong bảng cấu hình, bạn có thể thêm nhiều trình phân tích và thiết lập các quy tắc phân tích tương ứng hoặc xóa các trình phân tích không cần thiết. Hãy đảm bảo tập hợp trình phân tích của bạn bao gồm tất cả các loại tệp cần thiết; nếu không, lỗi sẽ xảy ra khi bạn chọn pipeline nhập liệu này trên trang **Files** của tập dữ liệu.

Thành phần **Parser** hỗ trợ phân tích các loại tệp sau:

| Loại tệp      | Định dạng tệp            |
|---------------|--------------------------|
| PDF           | PDF                      |
| Bảng tính     | XLSX, XLS, CSV           |
| Hình ảnh      | PNG, JPG, JPEG, GIF, TIF |
| Email         | EML                      |
| Văn bản & Đánh dấu | TXT, MD, MDX, HTML, JSON |
| Word          | DOCX                     |
| PowerPoint    | PPTX, PPT                |
| Âm thanh      | MP3, WAV                 |
| Video         | MP4, AVI, MKV            |

### Trình phân tích PDF

Đầu ra của trình phân tích PDF là `json`. Trong trình phân tích PDF, bạn chọn phương pháp phân tích phù hợp nhất với các tệp PDF của mình.

- DeepDoc: (Mặc định) Mô hình thị giác mặc định thực hiện các tác vụ OCR, TSR và DLR trên các tệp PDF phức tạp, nhưng có thể mất nhiều thời gian.
- Naive: Bỏ qua các tác vụ OCR, TSR và DLR nếu *tất cả* các tệp PDF của bạn là văn bản thuần túy.
- [MinerU](https://github.com/opendatalab/MinerU): (Thử nghiệm) Công cụ mã nguồn mở chuyển đổi PDF sang các định dạng có thể đọc bằng máy.
- [Docling](https://github.com/docling-project/docling): (Thử nghiệm) Công cụ xử lý tài liệu mã nguồn mở cho gen AI.
- Mô hình thị giác bên thứ ba từ nhà cung cấp mô hình cụ thể.

:::danger QUAN TRỌNG
Bắt đầu từ phiên bản v0.22.0, RAGFlow bao gồm MinerU (&ge; 2.6.3) như một trình phân tích PDF tùy chọn với nhiều backend. Lưu ý rằng RAGFlow chỉ hoạt động như một *remote client* cho MinerU, gọi API MinerU để phân tích tài liệu và đọc các tệp được trả về. Để sử dụng tính năng này:
:::

1. Chuẩn bị dịch vụ API MinerU có thể truy cập được (FastAPI server).
2. Trong tệp **.env** hoặc từ trang **Model providers** trong giao diện người dùng, cấu hình RAGFlow như một remote client cho MinerU:
   - `MINERU_APISERVER`: Điểm cuối API MinerU (ví dụ: `http://mineru-host:8886`).
   - `MINERU_BACKEND`: Backend MinerU:
      - `"pipeline"` (mặc định)
      - `"vlm-http-client"`
      - `"vlm-transformers"`
      - `"vlm-vllm-engine"`
      - `"vlm-mlx-engine"`
      - `"vlm-vllm-async-engine"`
      - `"vlm-lmdeploy-engine"`.
   - `MINERU_SERVER_URL`: (tùy chọn) Server HTTP vLLM downstream (ví dụ: `http://vllm-host:30000`). Áp dụng khi `MINERU_BACKEND` được đặt thành `"vlm-http-client"`.
   - `MINERU_OUTPUT_DIR`: (tùy chọn) Thư mục cục bộ để giữ đầu ra của dịch vụ API MinerU (zip/JSON) trước khi nhập.
   - `MINERU_DELETE_OUTPUT`: Có xóa đầu ra tạm thời khi dùng thư mục tạm thời không:
     - `1`: Xóa.
     - `0`: Giữ lại.
3. Trong giao diện người dùng web, điều hướng đến trang **Configuration** của tập dữ liệu và tìm phần **Ingestion pipeline**:
   - Nếu bạn quyết định sử dụng phương pháp phân đoạn từ menu thả xuống **Built-in**, hãy đảm bảo nó hỗ trợ phân tích PDF, sau đó chọn **MinerU** từ menu thả xuống **PDF parser**.
   - Nếu bạn sử dụng pipeline nhập liệu tùy chỉnh, hãy chọn **MinerU** trong phần **PDF parser** của thành phần **Parser**.

:::note
Tất cả các biến môi trường MinerU là tùy chọn. Khi được đặt, các giá trị này được sử dụng để tự động cung cấp mô hình OCR MinerU cho người thuê khi sử dụng lần đầu. Để tránh việc tự động cung cấp, hãy bỏ qua cài đặt biến môi trường và chỉ cấu hình MinerU từ trang **Model providers** trong giao diện người dùng.
:::

:::caution CẢNH BÁO
Các mô hình thị giác bên thứ ba được đánh dấu là **Thử nghiệm**, vì chúng tôi chưa thử nghiệm đầy đủ các mô hình này cho các tác vụ trích xuất dữ liệu nêu trên.
:::

### Trình phân tích bảng tính

Trình phân tích bảng tính xuất `html`, bảo toàn bố cục ban đầu và cấu trúc bảng. Bạn có thể xóa trình phân tích này nếu tập dữ liệu của bạn không chứa bảng tính.

### Trình phân tích hình ảnh

Trình phân tích hình ảnh sử dụng mô hình OCR gốc để trích xuất văn bản theo mặc định. Bạn có thể chọn mô hình VLM thay thế, với điều kiện bạn đã cấu hình đúng nó trên trang **Model provider**.

### Trình phân tích Email

Với trình phân tích Email, bạn chọn các trường để phân tích từ Email, chẳng hạn như **subject** và **body**. Trình phân tích sẽ trích xuất văn bản từ các trường được chỉ định này.

### Trình phân tích Text&Markup

Trình phân tích Text&Markup tự động xóa tất cả các thẻ định dạng (ví dụ: thẻ từ các tệp HTML và Markdown) để tạo ra văn bản thuần túy sạch.

### Trình phân tích Word

Trình phân tích Word xuất `json`, bảo toàn thông tin cấu trúc tài liệu gốc, bao gồm tiêu đề, đoạn văn, bảng, tiêu đề đầu trang và chân trang.

### Trình phân tích PowerPoint (PPT)

Trình phân tích PowerPoint trích xuất nội dung từ các tệp PowerPoint sang `json`, xử lý từng slide riêng lẻ và phân biệt giữa tiêu đề, nội dung văn bản và ghi chú của slide đó.

### Trình phân tích âm thanh

Trình phân tích âm thanh chuyển đổi các tệp âm thanh thành văn bản. Để sử dụng trình phân tích này, bạn phải cấu hình mô hình ASR trên trang **Model provider** trước.

### Trình phân tích video

Trình phân tích video chuyển đổi các tệp video thành văn bản. Để sử dụng trình phân tích này, bạn phải cấu hình mô hình VLM trên trang **Model provider** trước.

## Output

Tên biến toàn cục cho đầu ra của thành phần **Parser**, có thể được tham chiếu bởi các thành phần tiếp theo trong pipeline nhập liệu.

| Tên biến   | Kiểu            |
|------------|-----------------|
| `markdown` | `string`        |
| `text`     | `string`        |
| `html`     | `string`        |
| `json`     | `Array<Object>` |
