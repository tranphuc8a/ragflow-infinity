---
sidebar_position: -3
slug: /select_pdf_parser
sidebar_custom_props: {
  categoryIcon: LucideFileText
}
---
# Chọn trình phân tích PDF

Chọn mô hình thị giác để phân tích các tệp PDF của bạn.

---

RAGFlow không phải là một giải pháp cho tất cả. Nó được xây dựng để linh hoạt và hỗ trợ tùy chỉnh sâu hơn để đáp ứng các trường hợp sử dụng phức tạp hơn. Từ phiên bản v0.17.0 trở đi, RAGFlow tách các tác vụ trích xuất dữ liệu đặc thù của DeepDoc khỏi các phương pháp phân đoạn **đối với tệp PDF**. Sự phân tách này cho phép bạn tự chủ chọn một mô hình thị giác cho các tác vụ OCR (Nhận dạng ký tự quang học), TSR (Nhận dạng cấu trúc bảng) và DLR (Nhận dạng bố cục tài liệu) cân bằng giữa tốc độ và hiệu suất để phù hợp với các trường hợp sử dụng cụ thể của bạn. Nếu các tệp PDF của bạn chỉ chứa văn bản thuần túy, bạn có thể bỏ qua các tác vụ này bằng cách chọn tùy chọn **Naive**, để giảm tổng thời gian phân tích.

![data extraction](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/data_extraction.jpg)

## Điều kiện tiên quyết

- Menu thả xuống trình phân tích PDF chỉ xuất hiện khi bạn chọn phương pháp phân đoạn tương thích với PDF, bao gồm:
  - **General**
  - **Manual**
  - **Paper**
  - **Book**
  - **Laws**
  - **Presentation**
  - **One**
- Để sử dụng mô hình thị giác bên thứ ba để phân tích PDF, hãy đảm bảo bạn đã đặt VLM mặc định trong **Set default models** trên trang **Model providers**.

## Bắt đầu nhanh

1. Trên trang **Configuration** của tập dữ liệu, chọn phương pháp phân đoạn, ví dụ **General**.

   _Menu thả xuống **PDF parser** xuất hiện._

2. Chọn tùy chọn phù hợp nhất với kịch bản của bạn:

- DeepDoc: (Mặc định) Mô hình thị giác mặc định thực hiện các tác vụ OCR, TSR và DLR trên các tệp PDF, nhưng có thể mất nhiều thời gian.
- Naive: Bỏ qua các tác vụ OCR, TSR và DLR nếu _tất cả_ các tệp PDF của bạn là văn bản thuần túy.
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

## Câu hỏi thường gặp

### Khi nào tôi nên chọn DeepDoc hoặc mô hình thị giác bên thứ ba làm trình phân tích PDF?

Sử dụng mô hình thị giác để trích xuất dữ liệu nếu các tệp PDF của bạn chứa văn bản được định dạng hoặc dựa trên hình ảnh thay vì văn bản thuần túy. DeepDoc là mô hình thị giác mặc định nhưng có thể mất nhiều thời gian. Bạn cũng có thể chọn VLM nhẹ hoặc hiệu suất cao tùy thuộc vào nhu cầu và khả năng phần cứng của bạn.

### Tôi có thể chọn mô hình thị giác để phân tích các tệp DOCX không?

Không, bạn không thể. Menu thả xuống này chỉ dành cho PDF. Để sử dụng tính năng này, hãy chuyển đổi các tệp DOCX sang PDF trước.
