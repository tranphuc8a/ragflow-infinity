---
sidebar_position: 2
slug: /admin_cli
sidebar_custom_props: {
  categoryIcon: LucideSquareTerminal
}
---
# RAGFlow CLI

RAGFlow CLI là công cụ quản trị hệ thống dựa trên dòng lệnh cung cấp cho quản trị viên một phương pháp tương tác và kiểm soát hệ thống hiệu quả và linh hoạt. Hoạt động trên kiến trúc client-server, nó giao tiếp theo thời gian thực với Dịch vụ quản trị, nhận các lệnh quản trị viên và trả về kết quả thực thi động.

## Sử dụng RAGFlow CLI

1. Đảm bảo Dịch vụ quản trị đang chạy.

2. Cài đặt ragflow-cli.

   ```bash
   pip install ragflow-cli==0.23.1
   ```

3. Khởi chạy client CLI:

   ```bash
   ragflow-cli -h 127.0.0.1 -p 9381
   ```

    Bạn sẽ được nhắc nhập mật khẩu superuser để đăng nhập.
    Mật khẩu mặc định là admin.

    **Tham số:**
    
    - -h: Địa chỉ host của admin server RAGFlow
    
    - -p: Cổng của admin server RAGFlow

## Tài khoản quản trị mặc định

- Tên người dùng: admin@ragflow.io
- Mật khẩu: admin

## Các lệnh được hỗ trợ

Các lệnh không phân biệt chữ hoa chữ thường và phải kết thúc bằng dấu chấm phẩy (;).

### Lệnh quản lý dịch vụ

`LIST SERVICES;`

- Liệt kê tất cả các dịch vụ có sẵn trong hệ thống RAGFlow.

- [Ví dụ](#ví-dụ-list-services)

`SHOW SERVICE <id>;`

- Hiển thị thông tin trạng thái chi tiết cho dịch vụ được xác định bởi **id**.
- [Ví dụ](#ví-dụ-show-service)

`SHOW VERSION;`

- Hiển thị phiên bản RAGFlow.
- [Ví dụ](#ví-dụ-show-version)

### Lệnh quản lý người dùng

`LIST USERS;`

- Liệt kê tất cả người dùng trong hệ thống.
- [Ví dụ](#ví-dụ-list-users)

`SHOW USER <username>;`

- Hiển thị thông tin chi tiết và quyền của người dùng được chỉ định bởi **email**. Tên người dùng phải được đặt trong dấu nháy đơn hoặc nháy kép.
- [Ví dụ](#ví-dụ-show-user)

`CREATE USER <username> <password>;`

- Tạo người dùng bằng tên người dùng và mật khẩu. Tên người dùng và mật khẩu phải được đặt trong dấu nháy đơn hoặc nháy kép.
- [Ví dụ](#ví-dụ-create-user)

`DROP USER <username>;`

- Xóa người dùng được chỉ định khỏi hệ thống. Sử dụng cẩn thận.
- [Ví dụ](#ví-dụ-drop-user)

`ALTER USER PASSWORD <username> <new_password>;`

- Thay đổi mật khẩu cho người dùng được chỉ định.
- [Ví dụ](#ví-dụ-alter-user-password)

`ALTER USER ACTIVE <username> <on/off>;`

- Thay đổi người dùng thành hoạt động hoặc không hoạt động.
- [Ví dụ](#ví-dụ-alter-user-active)

`GENERATE KEY FOR USER <username>;`

- Tạo API key mới cho người dùng được chỉ định.
- [Ví dụ](#ví-dụ-generate-key)

`LIST KEYS OF <username>;`

- Liệt kê tất cả API key liên kết với người dùng được chỉ định.
- [Ví dụ](#ví-dụ-list-keys)

`DROP KEY <key> OF <username>;`

- Xóa một API key cụ thể của người dùng được chỉ định.
- [Ví dụ](#ví-dụ-drop-key)

### Lệnh dữ liệu và Agent

`LIST DATASETS OF <username>;`

- Liệt kê các tập dữ liệu liên kết với người dùng được chỉ định.
- [Ví dụ](#ví-dụ-list-datasets-of-user)

`LIST AGENTS OF <username>;`

- Liệt kê các agent liên kết với người dùng được chỉ định.
- [Ví dụ](#ví-dụ-list-agents-of-user)

### Thông tin hệ thống

`SHOW VERSION;`
- Hiển thị phiên bản RAGFlow hiện tại.
- [Ví dụ](#ví-dụ-show-version)

`GRANT ADMIN <username>`
- Cấp quyền quản trị viên cho người dùng được chỉ định.
- [Ví dụ](#ví-dụ-grant-admin)

`REVOKE ADMIN <username>`
- Thu hồi quyền quản trị viên từ người dùng được chỉ định.
- [Ví dụ](#ví-dụ-revoke-admin)

`LIST VARS`
- Liệt kê tất cả cài đặt hệ thống.
- [Ví dụ](#ví-dụ-list-vars)

`SHOW VAR <var_name>`
- Hiển thị nội dung của một cấu hình/cài đặt hệ thống cụ thể theo tên hoặc tiền tố tên.
- [Ví dụ](#ví-dụ-show-var)

`SET VAR <var_name> <var_value>`
- Đặt giá trị cho một mục cấu hình được chỉ định.
- [Ví dụ](#ví-dụ-set-var)

`LIST CONFIGS`
- Liệt kê tất cả cấu hình hệ thống.
- [Ví dụ](#ví-dụ-list-configs)

`LIST ENVS`
- Liệt kê tất cả các biến môi trường hệ thống có thể được truy cập bởi Dịch vụ quản trị.
- [Ví dụ](#ví-dụ-list-environments)

### Meta-Commands

- \? hoặc \help
  Hiển thị thông tin trợ giúp cho các lệnh có sẵn.
- \q hoặc \quit
  Thoát ứng dụng CLI.
- [Ví dụ](#ví-dụ-meta-commands)

### Ví dụ

<span id="ví-dụ-list-services"></span>

- Liệt kê tất cả dịch vụ có sẵn.

```
ragflow> list services;
command: list services;
Listing all services
+-------------------------------------------------------------------------------------------+-----------+----+---------------+-------+----------------+---------+
| extra                                                                                     | host      | id | name          | port  | service_type   | status  |
+-------------------------------------------------------------------------------------------+-----------+----+---------------+-------+----------------+---------+
| {}                                                                                        | 0.0.0.0   | 0  | ragflow_0     | 9380  | ragflow_server | Timeout |
| {'meta_type': 'mysql', 'password': 'infini_rag_flow', 'username': 'root'}                 | localhost | 1  | mysql         | 5455  | meta_data      | Alive   |
| {'password': 'infini_rag_flow', 'store_type': 'minio', 'user': 'rag_flow'}                | localhost | 2  | minio         | 9000  | file_store     | Alive   |
| {'password': 'infini_rag_flow', 'retrieval_type': 'elasticsearch', 'username': 'elastic'} | localhost | 3  | elasticsearch | 1200  | retrieval      | Alive   |
| {'db_name': 'default_db', 'retrieval_type': 'infinity'}                                   | localhost | 4  | infinity      | 23817 | retrieval      | Timeout |
| {'database': 1, 'mq_type': 'redis', 'password': 'infini_rag_flow'}                        | localhost | 5  | redis         | 6379  | message_queue  | Alive   |
+-------------------------------------------------------------------------------------------+-----------+----+---------------+-------+----------------+---------+
```

<span id="ví-dụ-show-service"></span>

- Hiển thị ragflow_server.

```
ragflow> show service 0;
command: show service 0;
Showing service: 0
Service ragflow_0 is alive. Detail:
Confirm elapsed: 26.0 ms.
```

<span id="ví-dụ-show-version"></span>

- Hiển thị phiên bản RAGFlow.

```
ragflow> show version;
+-----------------------+
| version               |
+-----------------------+
| v0.21.0-241-gc6cf58d5 |
+-----------------------+
```

<span id="ví-dụ-list-users"></span>

- Liệt kê tất cả người dùng.

```
ragflow> list users;
command: list users;
Listing all users
+-------------------------------+----------------------+-----------+----------+
| create_date                   | email                | is_active | nickname |
+-------------------------------+----------------------+-----------+----------+
| Mon, 22 Sep 2025 10:59:04 GMT | admin@ragflow.io     | 1         | admin    |
| Sun, 14 Sep 2025 17:36:27 GMT | lynn_inf@hotmail.com | 1         | Lynn     |
+-------------------------------+----------------------+-----------+----------+
```

<span id="ví-dụ-show-user"></span>

- Hiển thị người dùng được chỉ định.

```
ragflow> show user "admin@ragflow.io";
command: show user "admin@ragflow.io";
```

<span id="ví-dụ-create-user"></span>

- Tạo người dùng mới.

```
ragflow> create user "example@ragflow.io" "psw";
command: create user "example@ragflow.io" "psw";
Create user: example@ragflow.io, password: psw, role: user
```

<span id="ví-dụ-alter-user-password"></span>

- Thay đổi mật khẩu người dùng.

```
ragflow> alter user password "example@ragflow.io" "newpsw";
command: alter user password "example@ragflow.io" "newpsw";
Alter user: example@ragflow.io, password: newpsw
Password updated successfully!
```

<span id="ví-dụ-alter-user-active"></span>

- Thay đổi trạng thái hoạt động người dùng, tắt.

```
ragflow> alter user active "example@ragflow.io" off;
command: alter user active "example@ragflow.io" off;
Alter user example@ragflow.io activate status, turn off.
Turn off user activate status successfully!
```

<span id="ví-dụ-drop-user"></span>

- Xóa người dùng.

```
ragflow> Drop user "example@ragflow.io";
command: Drop user "example@ragflow.io";
Drop user: example@ragflow.io
Successfully deleted user.
```

<span id="ví-dụ-generate-key"></span>

- Tạo API key cho người dùng.

```
admin> generate key for user "example@ragflow.io";
Generating API key for user: example@ragflow.io
```

<span id="ví-dụ-list-keys"></span>

- Liệt kê tất cả API key của người dùng.

```
admin> list keys of "example@ragflow.io";
Listing API keys for user: example@ragflow.io
```

<span id="ví-dụ-drop-key"></span>

- Xóa API key của người dùng.

```
admin> drop key "ragflow-piwVJHEk09M5UN3LS_Xx9HA7yehs3yNOc9GGsD4jzus" of "example@ragflow.io";
Dropping API key for user: example@ragflow.io
API key deleted successfully
```

<span id="ví-dụ-list-datasets-of-user"></span>

- Liệt kê tập dữ liệu của người dùng được chỉ định.

```
ragflow> list datasets of "lynn_inf@hotmail.com";
command: list datasets of "lynn_inf@hotmail.com";
Listing all datasets of user: lynn_inf@hotmail.com
```

<span id="ví-dụ-list-agents-of-user"></span>

- Liệt kê các agent của người dùng được chỉ định.

```
ragflow> list agents of "lynn_inf@hotmail.com";
command: list agents of "lynn_inf@hotmail.com";
Listing all agents of user: lynn_inf@hotmail.com
```

<span id="ví-dụ-grant-admin"></span>

- Cấp quyền quản trị viên cho người dùng được chỉ định.

```
ragflow> grant admin "anakin.skywalker@ragflow.io";
Grant successfully!
```

<span id="ví-dụ-revoke-admin"></span>

- Thu hồi quyền quản trị viên từ người dùng được chỉ định.

```
ragflow> revoke admin "anakin.skywalker@ragflow.io";
Revoke successfully!
```

<span id="ví-dụ-list-vars"></span>

- Liệt kê tất cả cài đặt hệ thống.

```
ragflow> list vars;
+-----------+---------------------+--------------+-----------+
| data_type | name                | source       | value     |
+-----------+---------------------+--------------+-----------+
| string    | default_role        | variable     | user      |
| bool      | enable_whitelist    | variable     | true      |
| string    | mail.default_sender | variable     |           |
| string    | mail.password       | variable     |           |
| integer   | mail.port           | variable     | 15        |
| string    | mail.server         | variable     | localhost |
| integer   | mail.timeout        | variable     | 10        |
| bool      | mail.use_ssl        | variable     | true      |
| bool      | mail.use_tls        | variable     | false     |
| string    | mail.username       | variable     |           |
+-----------+---------------------+--------------+-----------+
```

<span id="ví-dụ-show-var"></span>

- Hiển thị nội dung cấu hình cụ thể.

```
ragflow> show var mail.server;
+-----------+-------------+--------------+-----------+
| data_type | name        | source       | value     |
+-----------+-------------+--------------+-----------+
| string    | mail.server | variable     | localhost |
+-----------+-------------+--------------+-----------+
```

<span id="ví-dụ-set-var"></span>

- Đặt giá trị cho mục cấu hình.

```
ragflow> set var mail.server 127.0.0.1;
Set variable successfully
```

<span id="ví-dụ-list-configs"></span>

- Liệt kê tất cả cấu hình hệ thống.

```
ragflow> list configs;
```

<span id="ví-dụ-list-environments"></span>

- Liệt kê các biến môi trường hệ thống.

```
ragflow> list envs;
+-------------------------+------------------+
| env                     | value            |
+-------------------------+------------------+
| DOC_ENGINE              | elasticsearch    |
| DEFAULT_SUPERUSER_EMAIL | admin@ragflow.io |
| DB_TYPE                 | mysql            |
| DEVICE                  | cpu              |
| STORAGE_IMPL            | MINIO            |
+-------------------------+------------------+
```

<span id="ví-dụ-meta-commands"></span>

- Hiển thị thông tin trợ giúp.

```
ragflow> \help
command: \help

Commands:
LIST SERVICES
SHOW SERVICE <service>
STARTUP SERVICE <service>
SHUTDOWN SERVICE <service>
RESTART SERVICE <service>
LIST USERS
SHOW USER <user>
DROP USER <user>
CREATE USER <user> <password>
ALTER USER PASSWORD <user> <new_password>
ALTER USER ACTIVE <user> <on/off>
LIST DATASETS OF <user>
LIST AGENTS OF <user>
CREATE ROLE <role>
DROP ROLE <role>
ALTER ROLE <role> SET DESCRIPTION <description>
LIST ROLES
SHOW ROLE <role>
GRANT <action_list> ON <function> TO ROLE <role>
REVOKE <action_list> ON <function> TO ROLE <role>
ALTER USER <user> SET ROLE <role>
SHOW USER PERMISSION <user>
SHOW VERSION
GRANT ADMIN <user>
REVOKE ADMIN <user>
GENERATE KEY FOR USER <user>
LIST KEYS OF <user>
DROP KEY <key> OF <user>

Meta Commands:
  \?, \h, \help     Show this help
  \q, \quit, \exit   Quit the CLI
```

- Thoát

```
ragflow> \q
command: \q
Goodbye!
```
