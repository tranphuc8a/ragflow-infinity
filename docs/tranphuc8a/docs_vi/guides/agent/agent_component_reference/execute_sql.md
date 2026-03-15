---
sidebar_position: 25
slug: /execute_sql
sidebar_custom_props: {
  categoryIcon: RagSql
}
---
# Công cụ Execute SQL

Một công cụ thực thi truy vấn SQL trên cơ sở dữ liệu quan hệ được chỉ định.

---

Công cụ **Execute SQL** cho phép bạn kết nối cơ sở dữ liệu quan hệ và chạy truy vấn SQL, có thể nhập trực tiếp hoặc do khả năng Text2SQL của hệ thống tạo thông qua thành phần **Agent**.

## Điều kiện tiên quyết

- Một database instance đã cấu hình và đang chạy.
- Database phải thuộc một trong các loại:
  - MySQL
  - PostgreSQL
  - MariaDB
  - Microsoft SQL Server

## Ví dụ

Bạn có thể ghép thành phần **Agent** với công cụ **Execute SQL**: **Agent** tạo câu lệnh SQL, còn **Execute SQL** xử lý kết nối và thực thi truy vấn. Ví dụ có trong template Agent **SQL Assistant**:

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/exeSQL.jpg)

## Cấu hình

### SQL statement

Ô nhập văn bản cho truy vấn SQL tĩnh, ví dụ `SELECT * FROM my_table`, và truy vấn động dùng biến.

:::tip LƯU Ý
Nhấp **(x)** hoặc gõ `/` để chèn biến.
:::

Với truy vấn động, bạn có thể dùng biến như `SELECT * FROM /sys.query`; nếu ghép **Agent** với **Execute SQL** để sinh nhiệm vụ SQL, bạn có thể chèn trực tiếp đầu ra `content` của **Agent** vào trường này.

### Database type

Loại cơ sở dữ liệu hỗ trợ hiện tại:

- MySQL
- PostgreSQL
- MariaDB
- Microsoft SQL Server (Mssql)

### Database

Chỉ xuất hiện khi bạn chọn **Split** làm phương thức.

### Username

Tên người dùng có quyền truy cập database.

### Host

Địa chỉ IP của máy chủ cơ sở dữ liệu.

### Port

Số cổng mà máy chủ cơ sở dữ liệu đang lắng nghe.

### Password

Mật khẩu của người dùng cơ sở dữ liệu.

### Max records

Số bản ghi tối đa được trả về để kiểm soát kích thước phản hồi và tăng hiệu quả. Mặc định `1024`.

### Output

Công cụ **Execute SQL** cung cấp hai biến đầu ra:

- `formalized_content`: chuỗi. Nếu tham chiếu biến này trong **Message**, bản ghi trả về hiển thị dạng bảng.
- `json`: mảng object. Nếu tham chiếu biến này trong **Message**, bản ghi trả về hiển thị dạng key-value.
