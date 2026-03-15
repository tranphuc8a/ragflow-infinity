---
sidebar_position: 6
slug: /manage_files
sidebar_custom_props: {
  categoryIcon: LucideFolderDot
}
---
# Tệp tin

Quản lý tệp trong RAGFlow cho phép bạn tải lên tệp theo từng cái hoặc hàng loạt. Sau đó, bạn có thể liên kết một tệp đã tải lên với nhiều tập dữ liệu khác nhau. Hướng dẫn này giới thiệu một số cách sử dụng cơ bản của tính năng quản lý tệp.

:::info QUAN TRỌNG
So với việc tải tệp trực tiếp lên các tập dữ liệu, việc tải tệp lên hệ thống quản lý tệp của RAGFlow rồi liên kết chúng với các tập dữ liệu khác nhau *không phải* là bước thừa, đặc biệt khi bạn muốn xóa một số tệp đã phân tích hoặc toàn bộ tập dữ liệu nhưng vẫn giữ lại tệp gốc.
:::

## Tạo thư mục

Quản lý tệp của RAGFlow cho phép bạn xây dựng hệ thống tệp với cấu trúc thư mục lồng nhau. Để tạo thư mục trong thư mục gốc của RAGFlow:

![tạo thư mục mới](https://github.com/infiniflow/ragflow/assets/93570324/3a37a5f4-43a6-426d-a62a-e5cd2ff7a533)

:::caution LƯU Ý
Mỗi tập dữ liệu trong RAGFlow có một thư mục tương ứng trong thư mục **root/.knowledgebase**. Bạn không được phép tạo thư mục con bên trong đó.
:::

## Tải lên tệp

Quản lý tệp của RAGFlow hỗ trợ tải tệp lên từ máy tính của bạn, cho phép tải lên từng tệp hoặc hàng loạt:

![tải lên tệp](https://github.com/infiniflow/ragflow/assets/93570324/5d7ded14-ce2b-4703-8567-9356a978f45c)

![tải lên hàng loạt](https://github.com/infiniflow/ragflow/assets/93570324/def0db55-824c-4236-b809-a98d8c8674e3)

## Xem trước tệp

Quản lý tệp của RAGFlow hỗ trợ xem trước các tệp ở định dạng sau:

- Tài liệu (PDF, DOCS)
- Bảng tính (XLSX)
- Hình ảnh (JPEG, JPG, PNG, TIF, GIF)

![xem trước](https://github.com/infiniflow/ragflow/assets/93570324/2e931362-8bbf-482c-ac86-b68b09d331bc)

## Liên kết tệp với tập dữ liệu

Quản lý tệp của RAGFlow cho phép bạn *liên kết* một tệp đã tải lên với nhiều tập dữ liệu, tạo ra tham chiếu tệp trong mỗi tập dữ liệu đích. Do đó, việc xóa tệp trong quản lý tệp sẽ TỰ ĐỘNG XÓA tất cả các tham chiếu tệp liên quan trong các tập dữ liệu.

![liên kết cơ sở kiến thức](https://github.com/infiniflow/ragflow/assets/93570324/6c6b8db4-3269-4e35-9434-6089887e3e3f)

Bạn có thể liên kết tệp của mình với một hoặc nhiều tập dữ liệu cùng một lúc:

![liên kết nhiều tập dữ liệu](https://github.com/infiniflow/ragflow/assets/93570324/6c508803-fb1f-435d-b688-683066fd7fff)

## Di chuyển tệp đến thư mục cụ thể

![di chuyển tệp](https://github.com/user-attachments/assets/3a2db469-6811-4ea0-be80-403b61ffe257)

## Tìm kiếm tệp hoặc thư mục

**Quản lý tệp** chỉ hỗ trợ lọc theo tên tệp và tên thư mục trong thư mục hiện tại (tệp hoặc thư mục trong thư mục con sẽ không được tìm thấy).

![tìm kiếm tệp](https://github.com/infiniflow/ragflow/assets/93570324/77ffc2e5-bd80-4ed1-841f-068e664efffe)

## Đổi tên tệp hoặc thư mục

Quản lý tệp của RAGFlow cho phép bạn đổi tên tệp hoặc thư mục:

![đổi tên tệp](https://github.com/infiniflow/ragflow/assets/93570324/5abb0704-d9e9-4b43-9ed4-5750ccee011f)

## Xóa tệp hoặc thư mục

Quản lý tệp của RAGFlow cho phép bạn xóa tệp hoặc thư mục từng cái hoặc hàng loạt.

Để xóa tệp hoặc thư mục:

![xóa tệp](https://github.com/infiniflow/ragflow/assets/93570324/85872728-125d-45e9-a0ee-21e9d4cedb8b)

Để xóa hàng loạt tệp hoặc thư mục:

![xóa hàng loạt](https://github.com/infiniflow/ragflow/assets/93570324/519b99ab-ec7f-4c8a-8cea-e0b6dcb3cb46)

> - Bạn không được phép xóa thư mục **root/.knowledgebase**.
> - Việc xóa các tệp đã được liên kết với tập dữ liệu sẽ **TỰ ĐỘNG XÓA** tất cả các tham chiếu tệp liên quan trong các tập dữ liệu.

## Tải xuống tệp đã tải lên

Quản lý tệp của RAGFlow cho phép bạn tải xuống tệp đã tải lên:

![tải xuống tệp](https://github.com/infiniflow/ragflow/assets/93570324/cf3b297f-7d9b-4522-bf5f-4f45743e4ed5)

> Tính đến RAGFlow v0.23.1, tải xuống hàng loạt chưa được hỗ trợ, và bạn cũng không thể tải xuống toàn bộ thư mục.
