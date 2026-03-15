---
sidebar_position: 35
slug: /docs_generator
---

# Thành phần Docs Generator

Thành phần tạo các tài liệu PDF, DOCX hoặc TXT có thể tải xuống từ nội dung định dạng markdown với hỗ trợ Unicode đầy đủ.

---

Thành phần **Docs Generator** cho phép bạn tạo các tài liệu chuyên nghiệp trực tiếp trong quy trình agent của mình. Nó nhận văn bản có định dạng markdown và chuyển đổi thành các tệp có thể tải xuống, lý tưởng để tạo báo cáo, tóm tắt hoặc bất kỳ đầu ra tài liệu có cấu trúc nào.

## Tính năng chính

- **Nhiều định dạng đầu ra**: PDF, DOCX và TXT
- **Hỗ trợ Unicode đầy đủ**: Tự động chuyển đổi phông chữ cho CJK (Tiếng Trung, Nhật, Hàn), tiếng Ả Rập, tiếng Do Thái và các ngôn ngữ không phải Latin khác
- **Định dạng phong phú**: Tiêu đề, danh sách, bảng, khối mã và nhiều hơn nữa
- **Tùy chỉnh kiểu dáng**: Phông chữ, lề, khổ trang và hướng
- **Phần bổ sung tài liệu**: Logo, hình mờ, số trang và dấu thời gian
- **Tải xuống trực tiếp**: Tạo nút tải xuống cho giao diện chat

## Điều kiện tiên quyết

- Nội dung cần chuyển đổi thành tài liệu (thường từ thành phần **Agent** hoặc thành phần tạo văn bản khác).

## Ví dụ

Bạn có thể ghép thành phần **Agent** với **Docs Generator** để tạo tài liệu động dựa trên truy vấn của người dùng. **Agent** tạo ra nội dung và **Docs Generator** chuyển đổi nó thành tệp có thể tải xuống. Kết nối đầu ra với thành phần **Message** để hiển thị nút tải xuống trong chat.

Quy trình điển hình trông như sau:

```
Begin → Agent → Docs Generator → Message
```

Trong thành phần **Message**, tham chiếu biến đầu ra `download` từ **Docs Generator** để hiển thị nút tải xuống trong giao diện chat.

## Cấu hình

### Content

Nội dung văn bản chính cần đưa vào tài liệu. Hỗ trợ định dạng Markdown:

- **In đậm**: `**text**` hoặc `__text__`
- **In nghiêng**: `*text*` hoặc `_text_`
- **Mã nội dòng**: `` `code` ``
- **Tiêu đề**: `# Tiêu đề 1`, `## Tiêu đề 2`, `### Tiêu đề 3`
- **Danh sách gạch đầu dòng**: `- mục` hoặc `* mục`
- **Danh sách đánh số**: `1. mục`
- **Bảng**: `| Cột 1 | Cột 2 |`
- **Đường ngang**: `---`
- **Khối mã**: ` ``` code ``` `

:::tip LƯU Ý
Nhấp vào **(x)** hoặc gõ `/` để chèn biến từ các thành phần ngược dòng.
:::

### Title

Tùy chọn. Tiêu đề tài liệu hiển thị ở đầu tệp được tạo.

### Subtitle

Tùy chọn. Phụ đề hiển thị bên dưới tiêu đề.

### Output format

Định dạng tệp cho tài liệu được tạo:

- **PDF** (mặc định): Định dạng Portable Document Format với hỗ trợ đầy đủ về kiểu dáng.
- **DOCX**: Định dạng Microsoft Word.
- **TXT**: Định dạng văn bản thuần túy.

### Logo image

Tùy chọn. Hình ảnh logo để hiển thị ở đầu tài liệu. Bạn có thể:

- Tải lên tệp hình ảnh bằng bộ chọn tệp
- Dán đường dẫn hình ảnh, URL hoặc dữ liệu mã hóa base64

### Logo position

Vị trí ngang của logo:

- **left** (mặc định)
- **center**
- **right**

### Logo dimensions

- **Logo width**: Chiều rộng tính bằng inch (mặc định: `2.0`)
- **Logo height**: Chiều cao tính bằng inch (mặc định: `1.0`)

### Font family

Phông chữ được sử dụng xuyên suốt tài liệu:

- **Helvetica** (mặc định)
- **Times-Roman**
- **Courier**
- **Helvetica-Bold**
- **Times-Bold**

### Font size

Cỡ chữ cơ sở tính bằng điểm. Mặc định là `12`.

### Title font size

Cỡ chữ cho tiêu đề tài liệu. Mặc định là `24`.

### Page size

Khổ giấy cho tài liệu:

- **A4** (mặc định)
- **Letter**

### Orientation

Hướng trang:

- **Portrait** (mặc định)
- **Landscape**

### Margins

Lề trang tính bằng inch:

- **Margin top**: Mặc định là `1.0`
- **Margin bottom**: Mặc định là `1.0`
- **Margin left**: Mặc định là `1.0`
- **Margin right**: Mặc định là `1.0`

### Filename

Tùy chọn. Tên tệp tùy chỉnh cho tài liệu được tạo. Nếu để trống, tên tệp sẽ được tự động tạo với dấu thời gian.

### Output directory

Thư mục máy chủ nơi các tài liệu được tạo sẽ được lưu. Mặc định là `/tmp/pdf_outputs`.

### Add page numbers

Khi bật, số trang được thêm vào phần chân của mỗi trang. Mặc định là `true`.

### Add timestamp

Khi bật, dấu thời gian tạo được thêm vào phần chân tài liệu. Mặc định là `true`.

### Watermark text

Tùy chọn. Văn bản để hiển thị như hình mờ chéo trên mỗi trang. Hữu ích để đánh dấu tài liệu là "Draft", "Confidential", v.v.

## Output

Thành phần **Docs Generator** cung cấp các biến đầu ra sau:

| Tên biến     | Kiểu       | Mô tả                                                                    |
|--------------|------------|--------------------------------------------------------------------------|
| `file_path`  | `string`   | Đường dẫn máy chủ nơi tài liệu được tạo được lưu.                       |
| `pdf_base64` | `string`   | Nội dung tài liệu được mã hóa ở định dạng base64.                        |
| `download`   | `string`   | JSON chứa thông tin tải xuống cho giao diện chat.                        |
| `success`    | `boolean`  | Cho biết liệu tài liệu đã được tạo thành công hay không.                 |

### Hiển thị nút tải xuống

Để hiển thị nút tải xuống trong chat, thêm thành phần **Message** sau **Docs Generator** và tham chiếu biến `download`:

1. Kết nối đầu ra **Docs Generator** với thành phần **Message**.
2. Trong trường nội dung của thành phần **Message**, gõ `/` và chọn `{Docs Generator_0@download}`.
3. Khi agent chạy, nút tải xuống sẽ xuất hiện trong chat, cho phép người dùng tải xuống tài liệu được tạo.

Nút tải xuống tự động xử lý:
- Phát hiện loại tệp (PDF, DOCX, TXT)
- MIME type phù hợp cho tải xuống trình duyệt
- Giải mã base64 để phân phối tệp trực tiếp

## Hỗ trợ Unicode và đa ngôn ngữ

**Docs Generator** bao gồm xử lý phông chữ thông minh cho nội dung quốc tế:

### Cách hoạt động

1. **Phân tích nội dung**: Thành phần quét văn bản để tìm các ký tự không phải Latin.
2. **Tự động chuyển đổi phông chữ**: Khi phát hiện nội dung CJK hoặc các ngôn ngữ phức tạp khác, hệ thống tự động chuyển sang phông chữ CID tương thích (STSong-Light cho tiếng Trung, HeiseiMin-W3 cho tiếng Nhật, HYSMyeongJo-Medium cho tiếng Hàn).
3. **Nội dung Latin**: Đối với các tài liệu chỉ chứa ký tự Latin (bao gồm Latin mở rộng, Cyrillic và Hy Lạp), phông chữ do người dùng chọn sẽ được sử dụng.

### Các ngôn ngữ được hỗ trợ

| Ngôn ngữ                    | Phạm vi Unicode | Phông chữ sử dụng   |
|-----------------------------|-----------------|---------------------|
| Tiếng Trung (CJK)           | U+4E00–U+9FFF   | STSong-Light        |
| Tiếng Nhật (Hiragana/Katakana) | U+3040–U+30FF | HeiseiMin-W3        |
| Tiếng Hàn (Hangul)          | U+AC00–U+D7AF   | HYSMyeongJo-Medium  |
| Tiếng Ả Rập                 | U+0600–U+06FF   | CID font fallback   |
| Tiếng Do Thái               | U+0590–U+05FF   | CID font fallback   |
| Devanagari (Tiếng Hindi)    | U+0900–U+097F   | CID font fallback   |
| Tiếng Thái                  | U+0E00–U+0E7F   | CID font fallback   |

### Cài đặt phông chữ

Để hỗ trợ đa ngôn ngữ đầy đủ trong các triển khai tự lưu trữ, hãy đảm bảo các phông chữ Unicode được cài đặt:

**Linux (Debian/Ubuntu):**
```bash
apt-get install fonts-freefont-ttf fonts-noto-cjk
```

**Docker:** Image Docker RAGFlow chính thức bao gồm các phông chữ này. Đối với các image tùy chỉnh, hãy thêm các gói phông chữ vào Dockerfile của bạn:
```dockerfile
RUN apt-get update && apt-get install -y fonts-freefont-ttf fonts-noto-cjk
```

:::tip LƯU Ý
Các phông chữ CID (STSong-Light, HeiseiMin-W3, v.v.) được tích hợp sẵn trong ReportLab và không cần cài đặt thêm. Chúng được sử dụng tự động khi phát hiện nội dung CJK.
:::

## Xử lý sự cố

### Các ký tự xuất hiện như hộp hoặc dấu hỏi

Điều này cho thấy thiếu hỗ trợ phông chữ. Hãy đảm bảo:
1. Nội dung chứa các ký tự Unicode được hỗ trợ.
2. Đối với các triển khai tự lưu trữ, phông chữ Unicode được cài đặt trên máy chủ.
3. Tài liệu đang được xem trong trình đọc PDF hỗ trợ phông chữ nhúng.

### Nút tải xuống không xuất hiện

Hãy đảm bảo:
1. Thành phần **Message** được kết nối sau **Docs Generator**.
2. Biến `download` được tham chiếu đúng cách bằng cách sử dụng `/` (xuất hiện dưới dạng `{Docs Generator_0@download}` khi sao chép).
3. Quá trình tạo tài liệu hoàn thành thành công (kiểm tra đầu ra `success`).

### Bảng lớn không hiển thị đúng

Đối với các bảng có nhiều cột hoặc nội dung ô lớn:
- Thành phần tự động chuyển đổi các bảng rộng sang định dạng danh sách định nghĩa để dễ đọc hơn.
- Hãy xem xét chia các bảng lớn thành nhiều bảng nhỏ hơn.
- Sử dụng hướng landscape cho các bảng rộng.
