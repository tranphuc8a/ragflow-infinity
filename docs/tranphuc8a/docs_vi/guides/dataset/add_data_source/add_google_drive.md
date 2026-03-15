---
sidebar_position: 3
slug: /add_google_drive
sidebar_custom_props: {
  categoryIcon: SiGoogledrive
}
---
# Thêm Google Drive

## 1. Tạo Dự án Google Cloud

Bạn có thể tạo một dự án chuyên dụng cho RAGFlow hoặc sử dụng một dự án Google Cloud bên ngoài hiện có.

**Các bước:**
1. Mở trang tạo dự án\
`https://console.cloud.google.com/projectcreate`
![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image1.jpeg?raw=true)
2. Chọn **External** làm Audience
![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image2.png?raw=true)
3. Nhấp vào **Create**
![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image3.jpeg?raw=true)

------------------------------------------------------------------------

## 2. Cấu hình Màn hình Đồng ý OAuth

1. Đi đến **APIs & Services → OAuth consent screen**
2. Đảm bảo **User Type = External**
![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image4.jpeg?raw=true)
3. Thêm người dùng kiểm tra trong **Test Users** bằng cách nhập địa chỉ email
![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image5.jpeg?raw=true)
![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image6.jpeg?raw=true)

------------------------------------------------------------------------

## 3. Tạo Thông tin Xác thực OAuth Client

1. Điều hướng đến:\
    `https://console.cloud.google.com/auth/clients`
2. Tạo một **Web Application**
![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image7.png?raw=true)
3. Nhập tên cho client
4. Thêm các **Authorized Redirect URIs** sau:

```
http://localhost:9380/v1/connector/google-drive/oauth/web/callback
```

- Nếu sử dụng triển khai Docker:

**Authorized JavaScript origin:**
```
http://localhost:80
```

![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image8.png?raw=true)

- Nếu chạy từ source:
**Authorized JavaScript origin:**
```
http://localhost:9222
```

![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image9.png?raw=true)

5. Sau khi lưu, nhấp vào **Download JSON**. Tệp này sẽ được tải lên vào RAGFlow sau.

![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image10.png?raw=true)

------------------------------------------------------------------------

## 4. Thêm Phạm vi (Scopes)

1. Mở **Data Access → Add or remove scopes**

2. Dán và thêm các mục sau:

```
https://www.googleapis.com/auth/drive.readonly
https://www.googleapis.com/auth/drive.metadata.readonly
https://www.googleapis.com/auth/admin.directory.group.readonly
https://www.googleapis.com/auth/admin.directory.user.readonly
```

![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image11.jpeg?raw=true)
3. Cập nhật và Lưu thay đổi

![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image12.jpeg?raw=true)
![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image13.jpeg?raw=true)

------------------------------------------------------------------------

## 5. Bật các API Cần thiết

Điều hướng đến Thư viện API Google:\
`https://console.cloud.google.com/apis/library`
![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image14.png?raw=true)

Bật các API sau:

- Google Drive API
- Admin SDK API
- Google Sheets API
- Google Docs API

![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image15.png?raw=true)

![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image16.png?raw=true)

![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image17.png?raw=true)

![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image18.png?raw=true)

![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image19.png?raw=true)

![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image21.png?raw=true)

------------------------------------------------------------------------

## 6. Thêm Google Drive như Nguồn Dữ liệu trong RAGFlow

1. Đi đến **Data Sources** trong RAGFlow
2. Chọn **Google Drive**
3. Tải lên thông tin xác thực JSON đã tải xuống trước đó
![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image22.jpeg?raw=true)
4. Nhập liên kết thư mục Google Drive được chia sẻ (https://drive.google.com/drive), chẳng hạn như:
![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image23.png?raw=true)

5. Nhấp vào **Authorize with Google**
Một cửa sổ trình duyệt sẽ xuất hiện.
![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image25.jpeg?raw=true)
Nhấp vào: - **Continue** - **Select All → Continue** - Ủy quyền sẽ thành công - Chọn **OK** để thêm nguồn dữ liệu
![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image26.jpeg?raw=true)
![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image27.jpeg?raw=true)
![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image28.png?raw=true)
![placeholder-image](https://github.com/infiniflow/ragflow-docs/blob/040e4acd4c1eac6dc73dc44e934a6518de78d097/images/google_drive/image29.png?raw=true)
