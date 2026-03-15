# Hướng dẫn di chuyển dữ liệu

Một tình huống phổ biến là xử lý các tập dữ liệu lớn trên một phiên bản mạnh mẽ (ví dụ: có GPU) và sau đó di chuyển toàn bộ dịch vụ RAGFlow sang môi trường sản xuất khác (ví dụ: máy chủ chỉ dùng CPU). Hướng dẫn này giải thích cách sao lưu và khôi phục dữ liệu an toàn bằng script di chuyển được cung cấp của chúng tôi.

## Xác định dữ liệu của bạn

Theo mặc định, RAGFlow sử dụng Docker volumes để lưu tất cả dữ liệu persistent, bao gồm cơ sở dữ liệu, các tệp đã tải lên và các chỉ mục tìm kiếm. Bạn có thể xem các volumes này bằng lệnh:

```bash
docker volume ls
```

Đầu ra sẽ trông tương tự như này:

```text
DRIVER    VOLUME NAME
local     docker_esdata01
local     docker_minio_data
local     docker_mysql_data
local     docker_redis_data
```

Các volumes này chứa tất cả dữ liệu bạn cần di chuyển.

## Bước 1: Dừng dịch vụ RAGFlow

Trước khi bắt đầu di chuyển, bạn phải dừng tất cả dịch vụ RAGFlow đang chạy trên **máy nguồn**. Điều hướng đến thư mục gốc của dự án và chạy:

```bash
docker-compose -f docker/docker-compose.yml down
```

**Quan trọng:** *Không* sử dụng cờ `-v` (ví dụ: `docker-compose down -v`), vì điều này sẽ xóa tất cả Docker volumes dữ liệu của bạn. Script di chuyển bao gồm kiểm tra và sẽ ngăn bạn chạy nó nếu các dịch vụ đang hoạt động.

## Bước 2: Sao lưu dữ liệu của bạn

Chúng tôi cung cấp một script tiện lợi để đóng gói tất cả Docker volumes dữ liệu của bạn vào một thư mục sao lưu duy nhất.

Để tham khảo nhanh về các lệnh và tùy chọn của script, bạn có thể chạy:
```bash
bash docker/migration.sh help
```

Để tạo sao lưu, chạy lệnh sau từ thư mục gốc của dự án:

```bash
bash docker/migration.sh backup
```

Lệnh này sẽ tạo thư mục `backup/` trong thư mục gốc dự án chứa các kho lưu trữ nén của Docker volumes dữ liệu.

Bạn cũng có thể chỉ định tên tùy chỉnh cho thư mục sao lưu:

```bash
bash docker/migration.sh backup my_ragflow_backup
```

Lệnh này sẽ tạo thư mục có tên `my_ragflow_backup/` thay thế.

## Bước 3: Chuyển thư mục sao lưu

Sao chép toàn bộ thư mục sao lưu (ví dụ: `backup/` hoặc `my_ragflow_backup/`) từ máy nguồn của bạn đến thư mục dự án RAGFlow trên **máy đích**. Bạn có thể sử dụng các công cụ như `scp`, `rsync`, hoặc ổ đĩa vật lý để chuyển dữ liệu.

## Bước 4: Khôi phục dữ liệu của bạn

Trên **máy đích**, đảm bảo rằng dịch vụ RAGFlow không đang chạy. Sau đó, sử dụng script di chuyển để khôi phục dữ liệu từ thư mục sao lưu.

Nếu thư mục sao lưu của bạn có tên `backup/`, chạy:

```bash
bash docker/migration.sh restore
```

Nếu bạn sử dụng tên tùy chỉnh, hãy chỉ định nó trong lệnh:

```bash
bash docker/migration.sh restore my_ragflow_backup
```

Script sẽ tự động tạo các Docker volumes cần thiết và giải nén dữ liệu.

**Lưu ý:** Nếu script phát hiện thấy Docker volumes có cùng tên đã tồn tại trên máy đích, nó sẽ cảnh báo bạn rằng việc khôi phục sẽ ghi đè dữ liệu hiện có và yêu cầu xác nhận trước khi tiến hành.

## Bước 5: Khởi động dịch vụ RAGFlow

Khi quá trình khôi phục hoàn tất, bạn có thể khởi động dịch vụ RAGFlow trên máy mới:

```bash
docker-compose -f docker/docker-compose.yml up -d
```

**Lưu ý:** Nếu bạn đã build một dịch vụ bằng docker-compose trước đó, bạn có thể cần sao lưu dữ liệu cho máy đích như hướng dẫn trên và chạy:

```bash
# Hãy sao lưu bằng `sh docker/migration.sh backup backup_dir_name` trước khi thực hiện dòng sau.
# !!! dòng này với cờ -v sẽ xóa Docker volume gốc
docker-compose -f docker/docker-compose.yml down -v
docker-compose -f docker/docker-compose.yml up -d
```

Phiên bản RAGFlow của bạn bây giờ đang chạy với tất cả dữ liệu từ máy gốc.
