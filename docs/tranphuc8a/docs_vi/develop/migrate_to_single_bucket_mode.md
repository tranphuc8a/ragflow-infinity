---
sidebar_position: 20
slug: /migrate_to_single_bucket_mode
---

# Chuyển đổi từ chế độ nhiều bucket sang một bucket

Theo mặc định, RAGFlow tạo một bucket cho mỗi Knowledge Base (dataset) và một bucket cho mỗi thư mục người dùng. Điều này có thể gây vấn đề khi:

- Nhà cung cấp đám mây của bạn tính phí theo bucket
- Chính sách IAM của bạn hạn chế việc tạo bucket
- Bạn muốn tất cả dữ liệu được tổ chức trong một bucket duy nhất với cấu trúc thư mục

**Chế độ Một Bucket** cho phép bạn cấu hình RAGFlow để sử dụng một bucket duy nhất với cấu trúc thư mục thay vì nhiều bucket.

:::info GHI NHẬN
Tài liệu này được đóng góp bởi cộng tác viên cộng đồng của chúng tôi [arogan178](https://github.com/arogan178). Chúng tôi có thể không tích cực duy trì tài liệu này.
:::

## Cách hoạt động

### Chế độ Mặc định (Nhiều Bucket)

```
bucket: kb_12345/
  └── document_1.pdf
bucket: kb_67890/
  └── document_2.pdf
bucket: folder_abc/
  └── file_3.txt
```

### Chế độ Một Bucket (với prefix_path)

```
bucket: ragflow-bucket/
  └── ragflow/
      ├── kb_12345/
      │   └── document_1.pdf
      ├── kb_67890/
      │   └── document_2.pdf
      └── folder_abc/
          └── file_3.txt
```

## Cấu hình

### Cấu hình MinIO

Chỉnh sửa `service_conf.yaml` của bạn hoặc đặt biến môi trường:

```yaml
minio:
  user: "your-access-key"
  password: "your-secret-key"
  host: "minio.example.com:443"
  bucket: "ragflow-bucket" # Tên bucket mặc định
  prefix_path: "ragflow" # Đường dẫn tiền tố tùy chọn
```

Hoặc sử dụng biến môi trường:

```bash
export MINIO_USER=your-access-key
export MINIO_PASSWORD=your-secret-key
export MINIO_HOST=minio.example.com:443
export MINIO_BUCKET=ragflow-bucket
export MINIO_PREFIX_PATH=ragflow
```

### Cấu hình S3 (đã được hỗ trợ)

```yaml
s3:
  access_key: "your-access-key"
  secret_key: "your-secret-key"
  endpoint_url: "https://s3.amazonaws.com"
  bucket: "my-ragflow-bucket"
  prefix_path: "production"
  region: "us-east-1"
```

## Ví dụ chính sách IAM

Khi sử dụng chế độ một bucket, bạn chỉ cần quyền cho một bucket:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:*"],
      "Resource": [
        "arn:aws:s3:::ragflow-bucket",
        "arn:aws:s3:::ragflow-bucket/*"
      ]
    }
  ]
}
```

## Chuyển từ Nhiều Bucket sang Một Bucket

Nếu bạn đang chuyển từ chế độ nhiều bucket sang một bucket:

1. **Đặt biến môi trường** cho cấu hình mới
2. **Khởi động lại** các dịch vụ RAGFlow
3. **Chuyển dữ liệu hiện có** (tùy chọn):

```bash
# Ví dụ sử dụng mc (MinIO Client)
mc alias set old-minio http://old-minio:9000 ACCESS_KEY SECRET_KEY
mc alias set new-minio https://new-minio:443 ACCESS_KEY SECRET_KEY

# Liệt kê tất cả bucket knowledge base
mc ls old-minio/ | grep kb_ | while read -r line; do
    bucket=$(echo $line | awk '{print $5}')
    # Sao chép mỗi bucket sang cấu trúc mới
    mc cp --recursive old-minio/$bucket/ new-minio/ragflow-bucket/ragflow/$bucket/
done
```

## Chuyển đổi giữa các chế độ

### Bật Chế độ Một Bucket

```yaml
minio:
  bucket: "my-single-bucket"
  prefix_path: "ragflow"
```

### Tắt (Sử dụng Chế độ Nhiều Bucket)

```yaml
minio:
  # Để trống hoặc comment bucket và prefix_path
  # bucket: ''
  # prefix_path: ''
```

## Xử lý sự cố

### Vấn đề: Lỗi Access Denied

**Giải pháp**: Đảm bảo chính sách IAM của bạn cấp quyền truy cập vào bucket được chỉ định trong cấu hình.

### Vấn đề: Không tìm thấy tệp sau khi chuyển chế độ

**Giải pháp**: Cấu trúc đường dẫn thay đổi giữa các chế độ. Bạn cần chuyển dữ liệu hiện có.

### Vấn đề: Kết nối không thành công với HTTPS

**Giải pháp**: Đảm bảo `secure: True` được đặt trong kết nối MinIO (được xử lý tự động cho cổng 443).

## Các Backend Lưu trữ Được Hỗ trợ

- ✅ **MinIO** - Hỗ trợ đầy đủ với chế độ một bucket
- ✅ **AWS S3** - Hỗ trợ đầy đủ với chế độ một bucket
- ✅ **Alibaba OSS** - Hỗ trợ đầy đủ với chế độ một bucket
- ✅ **Azure Blob** - Sử dụng cấu trúc dựa trên container (mô hình khác)
- ⚠️ **OpenDAL** - Phụ thuộc vào backend lưu trữ cơ bản

## Cân nhắc về Hiệu suất

- **Chế độ một bucket** có thể có hiệu suất tốt hơn một chút cho các hoạt động liệt kê bucket
- **Chế độ nhiều bucket** cung cấp sự cô lập và tổ chức tốt hơn cho các triển khai lớn
- Chọn dựa trên yêu cầu cụ thể và ràng buộc cơ sở hạ tầng của bạn
