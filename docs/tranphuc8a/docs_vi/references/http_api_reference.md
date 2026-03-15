---
sidebar_position: 4
slug: /http_api_reference
categoryIcon: LucideGlobe
---

# API HTTP

Tài liệu này mô tả tất cả các HTTP REST API endpoint có sẵn trong RAGFlow. Tất cả các API yêu cầu xác thực bằng Bearer Token trong header `Authorization`.

## MÃ LỖI

| Mã | Mô tả |
|----|-------|
| 400 | Yêu cầu không hợp lệ |
| 401 | Xác thực thất bại |
| 403 | Không có quyền truy cập |
| 404 | Không tìm thấy tài nguyên |
| 500 | Lỗi nội bộ máy chủ |
| 1001 | Lỗi xử lý tài liệu |
| 1002 | Dung lượng vượt quá giới hạn |

---

## API TƯƠNG THÍCH OPENAI

### Tạo hoàn thành chat

**POST** `/api/v1/chats_openai/{chat_id}/chat/completions`

Tương thích với định dạng OpenAI API để tạo phản hồi chat.

#### Yêu cầu

- Phương thức: POST
- URL: `/api/v1/chats_openai/{chat_id}/chat/completions`
- Headers:
  - `'Content-Type: application/json'`
  - `'Authorization: Bearer <YOUR_API_KEY>'`
- Body:
  - `"model"`: `string`
  - `"messages"`: `array`
  - `"stream"`: `bool`

##### Ví dụ yêu cầu

```bash
curl --request POST \
  --url http://{address}/api/v1/chats_openai/{chat_id}/chat/completions \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer <YOUR_API_KEY>' \
  --data '{
    "model": "model_name",
    "messages": [{"role": "user", "content": "Hello!"}],
    "stream": false
  }'
```

---

### Tạo hoàn thành agent

**POST** `/api/v1/agents_openai/{agent_id}/chat/completions`

Tương thích với định dạng OpenAI API để tạo phản hồi từ agent.

---

## QUẢN LÝ TẬP DỮ LIỆU

---

### Tạo tập dữ liệu

**POST** `/api/v1/datasets`

Tạo một tập dữ liệu (dataset) mới.

#### Yêu cầu

- Phương thức: POST
- URL: `/api/v1/datasets`
- Headers:
  - `'Content-Type: application/json'`
  - `'Authorization: Bearer <YOUR_API_KEY>'`
- Body:
  - `"name"`: `string`
  - `"avatar"`: `string`
  - `"description"`: `string`
  - `"embedding_model"`: `string`
  - `"permission"`: `string`
  - `"chunk_method"`: `string`
  - `"parser_config"`: `object`

##### Ví dụ yêu cầu

```bash
curl --request POST \
     --url http://{address}/api/v1/datasets \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{
         "name": "my_dataset",
         "permission": "me",
         "chunk_method": "naive"
     }'
```

##### Tham số yêu cầu

- `name`: (*Tham số Body*), `string`, *Bắt buộc*

  Tên của dataset. Chỉ hỗ trợ BMP Unicode; tối đa 128 ký tự.

- `avatar`: (*Tham số Body*), `string`, *Tùy chọn*

  Ảnh đại diện dạng base64.

- `description`: (*Tham số Body*), `string`, *Tùy chọn*

  Mô tả dataset.

- `embedding_model`: (*Tham số Body*), `string`, *Tùy chọn*

  Tên mô hình nhúng. Bắt buộc theo định dạng `model_name@model_factory`.

- `permission`: (*Tham số Body*), `enum<string>`, *Tùy chọn*

  Quyền truy cập. Tùy chọn:
  - `"me"`: (Mặc định) Chỉ bạn có thể quản lý.
  - `"team"`: Tất cả thành viên nhóm có thể quản lý.

- `chunk_method`: (*Tham số Body*), `enum<string>`, *Tùy chọn*

  Phương pháp phân đoạn. Tùy chọn: `"naive"` | `"manual"` | `"qa"` | `"table"` | `"paper"` | `"book"` | `"laws"` | `"presentation"` | `"picture"` | `"one"` | `"knowledge_graph"` | `"email"`.

- `parser_config`: (*Tham số Body*), `object`, *Tùy chọn*

  Cấu hình trình phân tích tài liệu.

#### Phản hồi

Thành công:

```json
{
    "code": 0,
    "data": {
        "avatar": null,
        "chunk_count": 0,
        "chunk_method": "naive",
        "create_date": "Mon, 11 Nov 2024 09:07:28 GMT",
        "create_time": 1731312448237,
        "created_by": "69736c5e723611efb51b0242ac120007",
        "description": null,
        "document_count": 0,
        "embedding_model": "BAAI/bge-zh-v1.5@BAAI",
        "id": "527fa74891e811ef9c650242ac120006",
        "name": "my_dataset",
        "permission": "me",
        "tenant_id": "69736c5e723611efb51b0242ac120007",
        "token_num": 0,
        "update_date": "Mon, 11 Nov 2024 09:07:28 GMT",
        "update_time": 1731312448237
    }
}
```

Thất bại:

```json
{
    "code": 102,
    "message": "Duplicated dataset name in the same knowledgebase."
}
```

---

### Xóa tập dữ liệu

**DELETE** `/api/v1/datasets`

Xóa các dataset theo ID.

#### Yêu cầu

- Phương thức: DELETE
- URL: `/api/v1/datasets`
- Headers:
  - `'Content-Type: application/json'`
  - `'Authorization: Bearer <YOUR_API_KEY>'`
- Body:
  - `"ids"`: `list[string]`

##### Ví dụ yêu cầu

```bash
curl --request DELETE \
     --url http://{address}/api/v1/datasets \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{"ids": ["dataset_id_1", "dataset_id_2"]}'
```

#### Phản hồi

Thành công:

```json
{
    "code": 0,
    "data": true
}
```

---

### Cập nhật tập dữ liệu

**PUT** `/api/v1/datasets/{dataset_id}`

Cập nhật thông tin dataset.

#### Yêu cầu

- Phương thức: PUT
- URL: `/api/v1/datasets/{dataset_id}`
- Headers:
  - `'Content-Type: application/json'`
  - `'Authorization: Bearer <YOUR_API_KEY>'`

##### Ví dụ yêu cầu

```bash
curl --request PUT \
     --url http://{address}/api/v1/datasets/{dataset_id} \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{"name": "updated_name"}'
```

#### Phản hồi

Thành công:

```json
{
    "code": 0,
    "data": true
}
```

---

### Liệt kê tập dữ liệu

**GET** `/api/v1/datasets?page={page}&page_size={page_size}&orderby={orderby}&desc={desc}&name={name}&id={id}`

Liệt kê tất cả dataset của người dùng.

#### Yêu cầu

- Phương thức: GET
- URL: `/api/v1/datasets`
- Headers:
  - `'Authorization: Bearer <YOUR_API_KEY>'`

##### Tham số yêu cầu

- `page`: (*Tham số lọc*), `integer`, *Tùy chọn*. Mặc định `1`.
- `page_size`: (*Tham số lọc*), `integer`, *Tùy chọn*. Mặc định `30`.
- `orderby`: (*Tham số lọc*), `string`, *Tùy chọn*. Mặc định `"create_time"`.
- `desc`: (*Tham số lọc*), `boolean`, *Tùy chọn*. Mặc định `true`.
- `name`: (*Tham số lọc*), `string`, *Tùy chọn*. Tìm kiếm mờ theo tên.
- `id`: (*Tham số lọc*), `string`, *Tùy chọn*. Lọc theo ID.

---

### Lấy đồ thị tri thức

**GET** `/api/v1/datasets/{dataset_id}/knowledge_graph`

Lấy đồ thị tri thức của dataset.

---

### Xóa đồ thị tri thức

**DELETE** `/api/v1/datasets/{dataset_id}/knowledge_graph`

Xóa đồ thị tri thức của dataset.

---

### Xây dựng đồ thị tri thức

**POST** `/api/v1/datasets/{dataset_id}/knowledge_graph`

Bắt đầu xây dựng đồ thị tri thức từ tài liệu trong dataset.

---

### Xây dựng RAPTOR

**POST** `/api/v1/datasets/{dataset_id}/raptor`

Bắt đầu xây dựng cây tóm tắt RAPTOR cho dataset.

---

### Lấy trạng thái RAPTOR

**GET** `/api/v1/datasets/{dataset_id}/raptor`

Lấy trạng thái xây dựng RAPTOR của dataset.

---

## QUẢN LÝ FILE TRONG TẬP DỮ LIỆU

---

### Tải tài liệu lên

**POST** `/api/v1/datasets/{dataset_id}/documents`

Tải một hoặc nhiều tài liệu lên dataset.

#### Yêu cầu

- Phương thức: POST
- URL: `/api/v1/datasets/{dataset_id}/documents`
- Headers:
  - `'Content-Type: multipart/form-data'`
  - `'Authorization: Bearer <YOUR_API_KEY>'`
- Form:
  - `'file=@{FILE_PATH};type={MIME_TYPE}'`

##### Ví dụ yêu cầu

```bash
curl --request POST \
     --url http://{address}/api/v1/datasets/{dataset_id}/documents \
     --header 'Content-Type: multipart/form-data' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --form 'file=@./test1.txt;type=text/plain' \
     --form 'file=@./test2.pdf;type=application/pdf'
```

#### Phản hồi

Thành công:

```json
{
    "code": 0,
    "data": [
        {
            "chunk_count": 0,
            "create_date": "Mon, 11 Nov 2024 09:09:22 GMT",
            "create_time": 1731312562533,
            "created_by": "69736c5e723611efb51b0242ac120007",
            "id": "b330ec2e91ec11efbc510242ac120004",
            "knowledgebase_id": "527fa74891e811ef9c650242ac120006",
            "location": "test1.txt",
            "name": "test1.txt",
            "size": 17966,
            "source_type": "local",
            "status": "1",
            "thumbnail": null,
            "type": "doc"
        }
    ]
}
```

---

### Cập nhật tài liệu

**PUT** `/api/v1/datasets/{dataset_id}/documents/{document_id}`

Cập nhật thông tin của tài liệu.

##### Ví dụ yêu cầu

```bash
curl --request PUT \
     --url http://{address}/api/v1/datasets/{dataset_id}/documents/{document_id} \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{"chunk_method": "manual"}'
```

---

### Tải tài liệu về

**GET** `/api/v1/datasets/{dataset_id}/documents/{document_id}`

Tải xuống nội dung tài liệu.

---

### Liệt kê tài liệu

**GET** `/api/v1/datasets/{dataset_id}/documents?page={page}&page_size={page_size}&orderby={orderby}&desc={desc}&keywords={keywords}&id={id}&name={name}`

Liệt kê tài liệu trong dataset.

##### Tham số yêu cầu

- `page`: (*Tham số lọc*), `integer`, *Tùy chọn*. Mặc định `1`.
- `page_size`: (*Tham số lọc*), `integer`, *Tùy chọn*. Mặc định `30`.
- `orderby`: (*Tham số lọc*), `string`, *Tùy chọn*. Mặc định `"create_time"`.
- `desc`: (*Tham số lọc*), `boolean`, *Tùy chọn*. Mặc định `true`.
- `keywords`: (*Tham số lọc*), `string`, *Tùy chọn*. Tìm kiếm mờ theo tên.
- `id`: (*Tham số lọc*), `string`, *Tùy chọn*. Lọc theo ID tài liệu.
- `name`: (*Tham số lọc*), `string`, *Tùy chọn*. Lọc theo tên tài liệu.

---

### Xóa tài liệu

**DELETE** `/api/v1/datasets/{dataset_id}/documents`

Xóa tài liệu khỏi dataset.

##### Ví dụ yêu cầu

```bash
curl --request DELETE \
     --url http://{address}/api/v1/datasets/{dataset_id}/documents \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{"ids": ["document_id_1", "document_id_2"]}'
```

---

### Phân tích tài liệu

**POST** `/api/v1/datasets/{dataset_id}/chunks`

Bắt đầu phân tích (chunk) các tài liệu.

##### Ví dụ yêu cầu

```bash
curl --request POST \
     --url http://{address}/api/v1/datasets/{dataset_id}/chunks \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{"document_ids": ["document_id_1", "document_id_2"]}'
```

---

### Dừng phân tích tài liệu

**DELETE** `/api/v1/datasets/{dataset_id}/chunks`

Dừng quá trình phân tích tài liệu.

##### Ví dụ yêu cầu

```bash
curl --request DELETE \
     --url http://{address}/api/v1/datasets/{dataset_id}/chunks \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{"document_ids": ["document_id_1"]}'
```

---

## QUẢN LÝ ĐOẠN TRONG TẬP DỮ LIỆU

---

### Thêm đoạn

**POST** `/api/v1/datasets/{dataset_id}/documents/{document_id}/chunks`

Thêm thủ công một đoạn vào tài liệu.

#### Yêu cầu

- Phương thức: POST
- Body:
  - `"content"`: `string` (*Bắt buộc*)
  - `"important_keywords"`: `list[string]`

##### Ví dụ yêu cầu

```bash
curl --request POST \
     --url http://{address}/api/v1/datasets/{dataset_id}/documents/{document_id}/chunks \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{
         "content": "Đây là nội dung đoạn mới.",
         "important_keywords": ["từ khóa 1", "từ khóa 2"]
     }'
```

---

### Liệt kê đoạn

**GET** `/api/v1/datasets/{dataset_id}/documents/{document_id}/chunks?keywords={keywords}&page={page}&page_size={page_size}&id={id}`

Liệt kê các đoạn trong tài liệu.

---

### Xóa đoạn

**DELETE** `/api/v1/datasets/{dataset_id}/documents/{document_id}/chunks`

Xóa đoạn khỏi tài liệu.

---

### Cập nhật đoạn

**PUT** `/api/v1/datasets/{dataset_id}/documents/{document_id}/chunks/{chunk_id}`

Cập nhật nội dung hoặc trạng thái của đoạn.

##### Ví dụ yêu cầu

```bash
curl --request PUT \
     --url http://{address}/api/v1/datasets/{dataset_id}/documents/{document_id}/chunks/{chunk_id} \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{
         "content": "Nội dung cập nhật.",
         "important_keywords": ["từ khóa"],
         "available": true
     }'
```

---

### Lấy tóm tắt metadata

**GET** `/api/v1/datasets/{dataset_id}/documents/{document_id}/metadata`

Lấy tóm tắt metadata của tài liệu.

---

### Cập nhật metadata

**PUT** `/api/v1/datasets/{dataset_id}/documents/{document_id}/metadata`

Cập nhật metadata của tài liệu.

---

### Xóa metadata

**DELETE** `/api/v1/datasets/{dataset_id}/documents/{document_id}/metadata`

Xóa metadata khỏi tài liệu.

---

### Truy xuất đoạn

**GET** `/api/v1/retrieval`

Truy xuất các đoạn liên quan từ dataset dựa trên truy vấn.

#### Yêu cầu

- Phương thức: POST
- URL: `/api/v1/retrieval`
- Headers:
  - `'Content-Type: application/json'`
  - `'Authorization: Bearer <YOUR_API_KEY>'`
- Body:
  - `"question"`: `string` (*Bắt buộc*)
  - `"dataset_ids"`: `list[string]` (*Bắt buộc*)
  - `"document_ids"`: `list[string]`
  - `"similarity_threshold"`: `float`
  - `"vector_similarity_weight"`: `float`
  - `"top_k"`: `integer`
  - `"rerank_id"`: `string`
  - `"keyword"`: `bool`
  - `"highlight"`: `bool`
  - `"offset"`: `integer`
  - `"limit"`: `integer`

##### Ví dụ yêu cầu

```bash
curl --request POST \
     --url http://{address}/api/v1/retrieval \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{
         "question": "RAGFlow là gì?",
         "dataset_ids": ["dataset_id_1"],
         "limit": 10
     }'
```

##### Tham số yêu cầu

- `question`: (*Tham số Body*), `string`, *Bắt buộc*. Câu truy vấn.
- `dataset_ids`: (*Tham số Body*), `list[string]`, *Bắt buộc*. Danh sách ID dataset tìm kiếm.
- `document_ids`: (*Tham số Body*), `list[string]`, *Tùy chọn*. Lọc theo ID tài liệu.
- `similarity_threshold`: (*Tham số Body*), `float`, *Tùy chọn*. Ngưỡng độ tương đồng. Mặc định `0.2`.
- `vector_similarity_weight`: (*Tham số Body*), `float`, *Tùy chọn*. Trọng số tìm kiếm vector [0, 1]. Mặc định `0.3`.
- `top_k`: (*Tham số Body*), `integer`, *Tùy chọn*. Số đoạn tối đa để rerank. Mặc định `1024`.
- `rerank_id`: (*Tham số Body*), `string`, *Tùy chọn*. ID mô hình rerank.
- `keyword`: (*Tham số Body*), `bool`, *Tùy chọn*. Bật tìm kiếm từ khóa. Mặc định `false`.
- `highlight`: (*Tham số Body*), `bool`, *Tùy chọn*. Hiển thị highlight. Mặc định `false`.
- `offset`: (*Tham số Body*), `integer`, *Tùy chọn*. Vị trí bắt đầu. Mặc định `1`.
- `limit`: (*Tham số Body*), `integer`, *Tùy chọn*. Số kết quả tối đa. Mặc định `30`.

#### Phản hồi

Thành công:

```json
{
    "code": 0,
    "data": {
        "chunks": [
            {
                "content": "Nội dung đoạn liên quan...",
                "dataset_id": "527fa74891e811ef9c650242ac120006",
                "document_id": "b330ec2e91ec11efbc510242ac120004",
                "document_keyword": "test1.txt",
                "highlight": "<em>RAGFlow</em> là một RAG engine...",
                "id": "chunk_id",
                "image_id": null,
                "important_keywords": [],
                "positions": [[1, 100]],
                "similarity": 0.85,
                "term_similarity": 0.6,
                "vector_similarity": 0.9
            }
        ],
        "doc_aggs": [
            {
                "count": 5,
                "doc_id": "b330ec2e91ec11efbc510242ac120004",
                "doc_name": "test1.txt"
            }
        ],
        "total": 5
    }
}
```

---

## QUẢN LÝ TRỢ LÝ CHAT

---

### Tạo trợ lý chat

**POST** `/api/v1/chats`

Tạo một trợ lý chat mới.

#### Yêu cầu

- Phương thức: POST
- URL: `/api/v1/chats`
- Headers:
  - `'Content-Type: application/json'`
  - `'Authorization: Bearer <YOUR_API_KEY>'`
- Body:
  - `"name"`: `string` (*Bắt buộc*)
  - `"avatar"`: `string`
  - `"dataset_ids"`: `list[string]`
  - `"llm"`: `object`
  - `"prompt"`: `object`

##### Ví dụ yêu cầu

```bash
curl --request POST \
     --url http://{address}/api/v1/chats \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{
         "name": "my_chat_assistant",
         "dataset_ids": ["dataset_id_1"],
         "llm": {"model_name": "gpt-4o", "temperature": 0.3}
     }'
```

##### Tham số yêu cầu

- `name`: (*Tham số Body*), `string`, *Bắt buộc*. Tên trợ lý chat.
- `avatar`: (*Tham số Body*), `string`, *Tùy chọn*. Ảnh đại diện base64.
- `dataset_ids`: (*Tham số Body*), `list[string]`, *Tùy chọn*. Danh sách dataset liên kết.
- `llm`: (*Tham số Body*), `object`, *Tùy chọn*. Cấu hình mô hình LLM:
  - `model_name`: Tên mô hình. Định dạng `model_name@factory`.
  - `temperature`: Độ ngẫu nhiên [0, 1].
  - `top_p`: Top-p sampling.
  - `presence_penalty`: Phạt lặp lại.
  - `frequency_penalty`: Phạt tần số.
  - `max_tokens`: Số token tối đa.
- `prompt`: (*Tham số Body*), `object`, *Tùy chọn*. Cấu hình prompt:
  - `system`: Prompt hệ thống.
  - `prologue`: Câu mở đầu.
  - `similarity_threshold`: Ngưỡng tương đồng.
  - `keywords_similarity_weight`: Trọng số từ khóa.
  - `top_n`: Số đoạn truy xuất.
  - `variables`: Biến tùy chỉnh.

#### Phản hồi

Thành công:

```json
{
    "code": 0,
    "data": {
        "create_date": "Mon, 11 Nov 2024 09:10:00 GMT",
        "create_time": 1731312600000,
        "description": null,
        "dataset_ids": ["527fa74891e811ef9c650242ac120006"],
        "id": "chat_id_here",
        "name": "my_chat_assistant",
        "tenant_id": "69736c5e723611efb51b0242ac120007"
    }
}
```

---

### Cập nhật trợ lý chat

**PUT** `/api/v1/chats/{chat_id}`

Cập nhật cấu hình của trợ lý chat.

##### Ví dụ yêu cầu

```bash
curl --request PUT \
     --url http://{address}/api/v1/chats/{chat_id} \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{"name": "updated_name"}'
```

---

### Xóa trợ lý chat

**DELETE** `/api/v1/chats`

Xóa trợ lý chat theo ID.

##### Ví dụ yêu cầu

```bash
curl --request DELETE \
     --url http://{address}/api/v1/chats \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{"ids": ["chat_id_1", "chat_id_2"]}'
```

---

### Liệt kê trợ lý chat

**GET** `/api/v1/chats?page={page}&page_size={page_size}&orderby={orderby}&desc={desc}&name={name}&id={id}`

Liệt kê tất cả trợ lý chat.

---

## QUẢN LÝ PHIÊN

---

### Tạo phiên với trợ lý chat

**POST** `/api/v1/chats/{chat_id}/sessions`

Tạo một phiên trò chuyện mới.

##### Ví dụ yêu cầu

```bash
curl --request POST \
     --url http://{address}/api/v1/chats/{chat_id}/sessions \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{"name": "New Session"}'
```

---

### Cập nhật phiên

**PUT** `/api/v1/chats/{chat_id}/sessions/{session_id}`

Cập nhật thông tin phiên.

---

### Liệt kê phiên

**GET** `/api/v1/chats/{chat_id}/sessions?page={page}&page_size={page_size}&orderby={orderby}&desc={desc}&name={name}&id={id}&user_id={user_id}`

Liệt kê tất cả phiên của trợ lý chat.

---

### Xóa phiên

**DELETE** `/api/v1/chats/{chat_id}/sessions`

Xóa các phiên theo ID.

##### Ví dụ yêu cầu

```bash
curl --request DELETE \
     --url http://{address}/api/v1/chats/{chat_id}/sessions \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{"ids": ["session_id_1"]}'
```

---

### Trò chuyện với trợ lý chat

**POST** `/api/v1/chats/{chat_id}/completions`

Gửi tin nhắn đến trợ lý chat và nhận phản hồi.

#### Yêu cầu

- Phương thức: POST
- URL: `/api/v1/chats/{chat_id}/completions`
- Headers:
  - `'Content-Type: application/json'`
  - `'Authorization: Bearer <YOUR_API_KEY>'`
- Body:
  - `"question"`: `string` (*Bắt buộc*)
  - `"session_id"`: `string`
  - `"stream"`: `bool`
  - `"user_id"`: `string`

##### Ví dụ yêu cầu

```bash
curl --request POST \
     --url http://{address}/api/v1/chats/{chat_id}/completions \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{
         "question": "RAGFlow là gì?",
         "session_id": "session_id_here",
         "stream": false
     }'
```

##### Tham số yêu cầu

- `question`: (*Tham số Body*), `string`, *Bắt buộc*. Câu hỏi của người dùng.
- `session_id`: (*Tham số Body*), `string`, *Tùy chọn*. ID phiên. Nếu để trống, tạo phiên mới.
- `stream`: (*Tham số Body*), `bool`, *Tùy chọn*. Bật chế độ luồng. Mặc định `true`.
- `user_id`: (*Tham số Body*), `string`, *Tùy chọn*. ID người dùng tùy chỉnh.

#### Phản hồi (không stream)

Thành công:

```json
{
    "code": 0,
    "data": {
        "answer": "RAGFlow là một RAG engine mã nguồn mở...",
        "reference": {
            "chunks": [
                {
                    "chunk_id": "chunk_id_here",
                    "content": "Nội dung đoạn...",
                    "dataset_id": "dataset_id_here",
                    "document_id": "doc_id_here",
                    "document_name": "document.pdf",
                    "highlight": "Nội dung <em>highlight</em>...",
                    "similarity": 0.85
                }
            ],
            "doc_aggs": [...]
        },
        "session_id": "session_id_here"
    }
}
```

---

### Tạo phiên với agent (Đã lỗi thời)

**POST** `/api/v1/agents/{agent_id}/sessions`

> **Đã lỗi thời (Deprecated)**: Sử dụng API agent mới thay thế.

---

### Trò chuyện với agent

**POST** `/api/v1/agents/{agent_id}/completions`

Gửi tin nhắn đến agent và nhận phản hồi.

#### Yêu cầu

- Phương thức: POST
- URL: `/api/v1/agents/{agent_id}/completions`
- Headers:
  - `'Content-Type: application/json'`
  - `'Authorization: Bearer <YOUR_API_KEY>'`
- Body:
  - `"question"`: `string`
  - `"session_id"`: `string`
  - `"stream"`: `bool`
  - `"user_id"`: `string`
  - `"sync"`: `bool`

##### Ví dụ yêu cầu

```bash
curl --request POST \
     --url http://{address}/api/v1/agents/{agent_id}/completions \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{
         "question": "Phân tích dữ liệu này",
         "session_id": "session_id_here",
         "stream": false
     }'
```

#### Phản hồi (không stream)

```json
{
    "code": 0,
    "data": {
        "answer": "Đây là kết quả phân tích...",
        "reference": {},
        "session_id": "session_id_here",
        "trace": [
            {
                "component_id": "begin",
                "component_name": "Begin",
                "input": null,
                "output": {"answer": "Phân tích dữ liệu này"},
                "elapsed_time": 0.001
            }
        ]
    }
}
```

#### Phản hồi (có stream - SSE)

```
data: {"code": 0, "data": {"answer": "Đây ", "reference": {}, "session_id": "..."}}

data: {"code": 0, "data": {"answer": "Đây là", "reference": {}, "session_id": "..."}}

data: {"code": 0, "data": true}
```

---

### Liệt kê phiên agent

**GET** `/api/v1/agents/{agent_id}/sessions?page={page}&page_size={page_size}&orderby={orderby}&desc={desc}&id={id}&user_id={user_id}`

Liệt kê các phiên của agent.

---

### Xóa phiên agent

**DELETE** `/api/v1/agents/{agent_id}/sessions`

Xóa các phiên agent theo ID.

##### Ví dụ yêu cầu

```bash
curl --request DELETE \
     --url http://{address}/api/v1/agents/{agent_id}/sessions \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{"ids": ["session_id_1"]}'
```

---

### Tạo câu hỏi liên quan

**GET** `/api/v1/chats/{chat_id}/related_questions?question={question}`

Tạo các câu hỏi liên quan dựa trên câu hỏi ban đầu.

##### Ví dụ yêu cầu

```bash
curl --request GET \
     --url 'http://{address}/api/v1/chats/{chat_id}/related_questions?question=RAGFlow+là+gì' \
     --header 'Authorization: Bearer <YOUR_API_KEY>'
```

#### Phản hồi

```json
{
    "code": 0,
    "data": [
        "RAGFlow hoạt động như thế nào?",
        "RAGFlow khác gì so với các RAG framework khác?",
        "Làm thế nào để tích hợp RAGFlow vào ứng dụng?"
    ]
}
```

---

## QUẢN LÝ AGENT

---

### Liệt kê agent

**GET** `/api/v1/agents?page={page}&page_size={page_size}&orderby={orderby}&desc={desc}&title={title}&id={id}`

Liệt kê tất cả agent.

##### Ví dụ yêu cầu

```bash
curl --request GET \
     --url http://{address}/api/v1/agents \
     --header 'Authorization: Bearer <YOUR_API_KEY>'
```

---

### Tạo agent

**POST** `/api/v1/agents`

Tạo một agent mới bằng DSL.

#### Yêu cầu

- Phương thức: POST
- Body:
  - `"title"`: `string` (*Bắt buộc*)
  - `"dsl"`: `object`

##### Ví dụ yêu cầu

```bash
curl --request POST \
     --url http://{address}/api/v1/agents \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{
         "title": "My Agent",
         "dsl": {}
     }'
```

---

### Cập nhật agent

**PUT** `/api/v1/agents/{agent_id}`

Cập nhật cấu hình agent.

---

### Xóa agent

**DELETE** `/api/v1/agents`

Xóa các agent theo ID.

##### Ví dụ yêu cầu

```bash
curl --request DELETE \
     --url http://{address}/api/v1/agents \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{"ids": ["agent_id_1"]}'
```

---

## QUẢN LÝ BỘ NHỚ

---

### Tạo bộ nhớ

**POST** `/api/v1/memories`

Tạo một đối tượng bộ nhớ mới cho agent.

#### Yêu cầu

- Phương thức: POST
- URL: `/api/v1/memories`
- Headers:
  - `'Content-Type: application/json'`
  - `'Authorization: Bearer <YOUR_API_KEY>'`
- Body:
  - `"name"`: `string` (*Bắt buộc*)
  - `"memory_type"`: `list[string]` (*Bắt buộc*)
  - `"embd_id"`: `string` (*Bắt buộc*)
  - `"llm_id"`: `string`
  - `"avatar"`: `string`
  - `"permission"`: `string`
  - `"memory_size"`: `integer`
  - `"forgetting_policy"`: `string`
  - `"temperature"`: `float`
  - `"system_prompt"`: `string`
  - `"user_prompt"`: `string`
  - `"description"`: `string`

##### Ví dụ yêu cầu

```bash
curl --location 'http://{address}/api/v1/memories' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_API_KEY>' \
--data '{
    "name": "new_memory_1",
    "memory_type": ["raw", "semantic"],
    "embd_id": "BAAI/bge-large-zh-v1.5@SILICONFLOW"
}'
```

##### Tham số yêu cầu

- `name`: (*Tham số Body*), `string`, *Bắt buộc*

  Tên bộ nhớ. Chỉ hỗ trợ BMP Unicode; tối đa 128 ký tự.

- `memory_type`: (*Tham số Body*), `list[string]`, *Bắt buộc*

  Loại bộ nhớ. Tùy chọn:
  - `"raw"`: Lưu trữ thô (hội thoại gốc)
  - `"semantic"`: Bộ nhớ ngữ nghĩa (trích xuất)
  - `"episodic"`: Bộ nhớ sự kiện
  - `"procedural"`: Bộ nhớ thủ tục

- `embd_id`: (*Tham số Body*), `string`, *Bắt buộc*

  ID mô hình nhúng. Định dạng `model_name@model_factory`.

- `llm_id`: (*Tham số Body*), `string`, *Tùy chọn*

  ID mô hình LLM dùng để trích xuất bộ nhớ.

- `avatar`: (*Tham số Body*), `string`, *Tùy chọn*

  Ảnh đại diện dạng base64.

- `permission`: (*Tham số Body*), `enum<string>`, *Tùy chọn*

  Quyền truy cập: `"me"` hoặc `"team"`. Mặc định `"me"`.

- `memory_size`: (*Tham số Body*), `integer`, *Tùy chọn*

  Kích thước bộ nhớ tối đa (bytes). Mặc định `5*1024*1024` (5 MB). Tối đa `10*1024*1024` (10 MB).

- `forgetting_policy`: (*Tham số Body*), `enum<string>`, *Tùy chọn*

  Chính sách quên khi đầy bộ nhớ. Tùy chọn:
  - `"FIFO"`: (Mặc định) Ưu tiên xóa tin nhắn có `forget_at` sớm nhất.

- `temperature`: (*Tham số Body*), `float`, *Tùy chọn*

  Độ ngẫu nhiên [0, 1]. Mặc định `0.5`.

- `system_prompt`: (*Tham số Body*), `string`, *Tùy chọn*

  Prompt hệ thống cho LLM trích xuất bộ nhớ.

- `user_prompt`: (*Tham số Body*), `string`, *Tùy chọn*

  Prompt người dùng tùy chỉnh.

- `description`: (*Tham số Body*), `string`, *Tùy chọn*

  Mô tả bộ nhớ.

#### Phản hồi

Thành công:

```json
{
    "code": 0,
    "data": {
    ...your new memory here
    },
    "message": true
}
```

Thất bại:

```json
{
    "code": 101,
    "message": "Memory name cannot be empty or whitespace."
}
```

---

### Cập nhật bộ nhớ

**PUT** `/api/v1/memories/{memory_id}`

Cập nhật cấu hình của bộ nhớ.

#### Yêu cầu

- Phương thức: PUT
- URL: `/api/v1/memories/{memory_id}`

##### Ví dụ yêu cầu

```bash
curl --location --request PUT 'http://{address}/api/v1/memories/d6775d4eeada11f08ca284ba59bc53c7' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_API_KEY>' \
--data '{
    "name": "name_update",
}'
```

##### Tham số yêu cầu

- `memory_id`: (*Tham số đường dẫn*). ID bộ nhớ cần cập nhật.
- `name`: (*Tham số Body*), `string`, *Tùy chọn*. Tên mới.
- `avatar`: (*Tham số Body*), `string`, *Tùy chọn*. Ảnh đại diện cập nhật.
- `permission`: (*Tham số Body*), `enum<string>`, *Tùy chọn*. Quyền truy cập.
- `llm_id`: (*Tham số Body*), `string`, *Tùy chọn*. ID mô hình LLM mới.
- `description`: (*Tham số Body*), `string`, *Tùy chọn*. Mô tả.
- `memory_size`: (*Tham số Body*), `integer`, *Tùy chọn*. Kích thước bộ nhớ.
- `forgetting_policy`: (*Tham số Body*), `enum<string>`, *Tùy chọn*. Chính sách quên.
- `temperature`: (*Tham số Body*), `float`, *Tùy chọn*. Độ ngẫu nhiên.
- `system_prompt`: (*Tham số Body*), `string`, *Tùy chọn*. Prompt hệ thống.
- `user_prompt`: (*Tham số Body*), `string`, *Tùy chọn*. Prompt người dùng.

---

### Liệt kê bộ nhớ

**GET** `/api/v1/memories?tenant_id={tenant_ids}&memory_type={memory_types}&storage_type={storage_type}&keywords={keywords}&page={page}&page_size={page_size}`

Liệt kê tất cả bộ nhớ.

##### Ví dụ yêu cầu

```bash
curl --location 'http://{address}/api/v1/memories?keywords=&page_size=50&page=1&memory_type=semantic%2Cepisodic' \
--header 'Authorization: Bearer <YOUR_API_KEY>'
```

##### Tham số yêu cầu

- `tenant_id`: (*Tham số lọc*), `string` hoặc `list[string]`, *Tùy chọn*. ID chủ sở hữu.
- `memory_type`: (*Tham số lọc*), `string` hoặc `list[string]`, *Tùy chọn*. Loại bộ nhớ.
- `storage_type`: (*Tham số lọc*), `enum<string>`, *Tùy chọn*. Định dạng lưu trữ.
- `keywords`: (*Tham số lọc*), `string`, *Tùy chọn*. Tìm kiếm mờ theo tên.
- `page`: (*Tham số lọc*), `integer`, *Tùy chọn*. Mặc định `1`.
- `page_size`: (*Tham số lọc*), `integer`, *Tùy chọn*. Mặc định `50`.

---

### Lấy cấu hình bộ nhớ

**GET** `/api/v1/memories/{memory_id}/config`

Lấy toàn bộ cấu hình của bộ nhớ.

##### Ví dụ yêu cầu

```bash
curl --location 'http://{address}/api/v1/memories/6c8983badede11f083f184ba59bc53c7/config' \
--header 'Authorization: Bearer <YOUR_API_KEY>'
```

---

### Xóa bộ nhớ

**DELETE** `/api/v1/memories/{memory_id}`

Xóa một bộ nhớ.

##### Ví dụ yêu cầu

```bash
curl --location --request DELETE 'http://{address}/api/v1/memories/d6775d4eeada11f08ca284ba59bc53c7' \
--header 'Authorization: Bearer <YOUR_API_KEY>'
```

---

### Liệt kê tin nhắn trong bộ nhớ

**GET** `/api/v1/memories/{memory_id}?agent_id={agent_id}&keywords={session_id}&page={page}&page_size={page_size}`

Liệt kê tin nhắn trong bộ nhớ.

##### Ví dụ yêu cầu

```bash
curl --location 'http://{address}/api/v1/memories/6c8983badede11f083f184ba59bc53c?page=1' \
--header 'Authorization: Bearer <YOUR_API_KEY>'
```

---

### Thêm tin nhắn

**POST** `/api/v1/messages`

Thêm tin nhắn vào các bộ nhớ được chỉ định.

#### Yêu cầu

- Phương thức: POST
- URL: `/api/v1/messages`
- Body:
  - `"memory_id"`: `list[string]` (*Bắt buộc*)
  - `"agent_id"`: `string` (*Bắt buộc*)
  - `"session_id"`: `string` (*Bắt buộc*)
  - `"user_input"`: `string` (*Bắt buộc*)
  - `"agent_response"`: `string` (*Bắt buộc*)
  - `"user_id"`: `string`

##### Ví dụ yêu cầu

```bash
curl --location 'http://{address}/api/v1/messages' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_API_KEY>' \
--data '{
    "memory_id": ["6c8983badede11f083f184ba59bc53c7", "87ebb892df1711f08d6b84ba59bc53c7"],
    "agent_id": "8db9c8eddfcc11f0b5da84ba59bc53c7",
    "session_id": "bf0a50abeb8111f0917884ba59bc53c7",
    "user_id": "55777efac9df11f09cd07f49bd527ade",
    "user_input": "your user input here",
    "agent_response": "your agent response here"
}'
```

#### Phản hồi

Thành công:

```json
{
    "code": 0,
    "data": null,
    "message": "All add to task."
}
```

---

### Quên tin nhắn

**DELETE** `/api/v1/messages/{memory_id}:{message_id}`

Đặt tin nhắn thành trạng thái "đã quên". Tin nhắn này sẽ không được agent truy xuất và được ưu tiên xóa bởi chính sách quên.

##### Ví dụ yêu cầu

```bash
curl --location --request DELETE 'http://{address}/api/v1/messages/6c8983badede11f083f184ba59bc53c7:272' \
--header 'Authorization: Bearer <YOUR_API_KEY>'
```

---

### Cập nhật trạng thái tin nhắn

**PUT** `/api/v1/messages/{memory_id}:{message_id}`

Bật hoặc tắt một tin nhắn. Tin nhắn bị tắt sẽ không được agent truy xuất.

##### Ví dụ yêu cầu

```bash
curl --location --request PUT 'http://{address}/api/v1/messages/6c8983badede11f083f184ba59bc53c7:270' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_API_KEY>' \
--data '{
    "status": false
}'
```

##### Tham số yêu cầu

- `status`: (*Tham số Body*), `bool`, *Bắt buộc*. `True` = bật, `False` = tắt.

---

### Tìm kiếm tin nhắn

**GET** `/api/v1/messages/search?query={question}&memory_id={memory_id}&similarity_threshold={similarity_threshold}&keywords_similarity_weight={keywords_similarity_weight}&top_n={top_n}`

Tìm kiếm tin nhắn liên quan trong bộ nhớ dựa trên câu truy vấn.

##### Ví dụ yêu cầu

```bash
curl --location 'http://{address}/api/v1/messages/search?query=%22who%20are%20you%3F%22&memory_id=6c8983badede11f083f184ba59bc53c7&similarity_threshold=0.2&keywords_similarity_weight=0.7&top_n=10' \
--header 'Authorization: Bearer <YOUR_API_KEY>'
```

##### Tham số yêu cầu

- `question`: (*Tham số lọc*), `string`, *Bắt buộc*. Câu truy vấn.
- `memory_id`: (*Tham số lọc*), `string` hoặc `list[string]`, *Bắt buộc*. ID bộ nhớ.
- `agent_id`: (*Tham số lọc*), `string`, *Tùy chọn*. Lọc theo agent.
- `session_id`: (*Tham số lọc*), `string`, *Tùy chọn*. Lọc theo phiên.
- `similarity_threshold`: (*Tham số lọc*), `float`, *Tùy chọn*. Ngưỡng tương đồng [0, 1]. Mặc định `0.2`.
- `keywords_similarity_weight`: (*Tham số lọc*), `float`, *Tùy chọn*. Trọng số từ khóa [0, 1]. Mặc định `0.7`.
- `top_n`: (*Tham số lọc*), `integer`, *Tùy chọn*. Số kết quả tối đa. Mặc định `10`.

---

### Lấy tin nhắn gần đây

**GET** `/api/v1/messages?memory_id={memory_id}&agent_id={agent_id}&session_id={session_id}&limit={limit}`

Lấy các tin nhắn gần đây từ bộ nhớ.

##### Ví dụ yêu cầu

```bash
curl --location 'http://{address}/api/v1/messages?memory_id=6c8983badede11f083f184ba59bc53c7&limit=10' \
--header 'Authorization: Bearer <YOUR_API_KEY>'
```

##### Tham số yêu cầu

- `memory_id`: (*Tham số lọc*), `string` hoặc `list[string]`, *Bắt buộc*. ID bộ nhớ.
- `agent_id`: (*Tham số lọc*), `string`, *Tùy chọn*. Lọc theo agent.
- `session_id`: (*Tham số lọc*), `string`, *Tùy chọn*. Lọc theo phiên.
- `limit`: (*Tham số lọc*), `integer`, *Tùy chọn*. Số tin nhắn tối đa. Mặc định `10`.

---

### Lấy nội dung tin nhắn

**GET** `/api/v1/messages/{memory_id}:{message_id}/content`

Lấy toàn bộ nội dung và vector nhúng của tin nhắn.

##### Ví dụ yêu cầu

```bash
curl --location 'http://{address}/api/v1/messages/6c8983badede11f083f184ba59bc53c7:270/content' \
--header 'Authorization: Bearer <YOUR_API_KEY>'
```

---

## HỆ THỐNG

---

### Kiểm tra trạng thái hệ thống

**GET** `/v1/system/healthz`

Kiểm tra trạng thái sức khỏe của các thành phần phụ thuộc của RAGFlow (cơ sở dữ liệu, Redis, document engine, object storage).

#### Yêu cầu

- Phương thức: GET
- URL: `/v1/system/healthz`
- Headers:
  - `'Content-Type: application/json'`
  (Không cần Authorization)

##### Ví dụ yêu cầu

```bash
curl --request GET
     --url http://{address}/v1/system/healthz
     --header 'Content-Type: application/json'
```

#### Phản hồi

- **200 OK** – Tất cả dịch vụ hoạt động bình thường

```json
{
  "db": "ok",
  "redis": "ok",
  "doc_engine": "ok",
  "storage": "ok",
  "status": "ok"
}
```

- **500 Internal Server Error** – Ít nhất một dịch vụ gặp sự cố

```json
{
  "db": "ok",
  "redis": "nok",
  "doc_engine": "ok",
  "storage": "ok",
  "status": "nok",
  "_meta": {
    "redis": {
      "elapsed": "5.2",
      "error": "Lost connection!"
    }
  }
}
```

Giải thích:  
- Mỗi dịch vụ được báo cáo là `"ok"` hoặc `"nok"`.  
- `status` phản ánh trạng thái tổng thể.  
- Nếu có dịch vụ `"nok"`, thông tin lỗi chi tiết xuất hiện trong `_meta`.

---

## QUẢN LÝ FILE

---

### Tải file lên

**POST** `/api/v1/file/upload`

Tải một hoặc nhiều tệp lên hệ thống.

#### Yêu cầu

- Phương thức: POST
- URL: `/api/v1/file/upload`
- Headers:
  - `'Content-Type: multipart/form-data'`
  - `'Authorization: Bearer <YOUR_API_KEY>'`
- Form:
  - `'file=@{FILE_PATH}'`
  - `'parent_id'`: `string` (tùy chọn)

##### Ví dụ yêu cầu

```bash
curl --request POST \
     --url http://{address}/api/v1/file/upload \
     --header 'Content-Type: multipart/form-data' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --form 'file=@./test1.txt' \
     --form 'file=@./test2.pdf' \
     --form 'parent_id={folder_id}'
```

##### Tham số yêu cầu

- `'file'`: (*Tham số Form*), `file`, *Bắt buộc*. Tệp cần tải lên. Có thể tải nhiều tệp một lúc.
- `'parent_id'`: (*Tham số Form*), `string`, *Tùy chọn*. ID thư mục cha. Nếu không chỉ định, tải lên thư mục gốc.

#### Phản hồi

Thành công:

```json
{
    "code": 0,
    "data": [
        {
            "id": "b330ec2e91ec11efbc510242ac120004",
            "name": "test1.txt",
            "size": 17966,
            "type": "doc",
            "parent_id": "527fa74891e811ef9c650242ac120006",
            "location": "test1.txt",
            "create_time": 1729763127646
        }
    ]
}
```

---

### Tạo file hoặc thư mục

**POST** `/api/v1/file/create`

Tạo một tệp hoặc thư mục mới trong hệ thống.

##### Ví dụ yêu cầu

```bash
curl --request POST \
     --url http://{address}/api/v1/file/create \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{
          "name": "New Folder",
          "type": "FOLDER",
          "parent_id": "{folder_id}"
     }'
```

##### Tham số yêu cầu

- `"name"`: (*Tham số Body*), `string`, *Bắt buộc*. Tên tệp hoặc thư mục.
- `"parent_id"`: (*Tham số Body*), `string`, *Tùy chọn*. ID thư mục cha.
- `"type"`: (*Tham số Body*), `string`, *Bắt buộc*. Loại: `"FOLDER"` hoặc `"VIRTUAL"`.

---

### Liệt kê file

**GET** `/api/v1/file/list?parent_id={parent_id}&keywords={keywords}&page={page}&page_size={page_size}&orderby={orderby}&desc={desc}`

Liệt kê tệp và thư mục trong một thư mục.

##### Tham số yêu cầu

- `parent_id`: (*Tham số lọc*). ID thư mục cha. Mặc định là thư mục gốc.
- `keywords`: (*Tham số lọc*). Từ khóa lọc theo tên.
- `page`: (*Tham số lọc*). Số trang. Mặc định `1`.
- `page_size`: (*Tham số lọc*). Số tệp mỗi trang. Mặc định `15`.
- `orderby`: (*Tham số lọc*). Sắp xếp theo trường. Mặc định `create_time`.
- `desc`: (*Tham số lọc*). Thứ tự giảm dần. Mặc định `true`.

---

### Lấy thư mục gốc

**GET** `/api/v1/file/root_folder`

Lấy thông tin thư mục gốc của người dùng.

---

### Lấy thư mục cha

**GET** `/api/v1/file/parent_folder?file_id={file_id}`

Lấy thư mục cha trực tiếp của một tệp.

---

### Lấy tất cả thư mục cha

**GET** `/api/v1/file/all_parent_folder?file_id={file_id}`

Lấy toàn bộ cây thư mục cha của một tệp.

---

### Xóa file

**POST** `/api/v1/file/rm`

Xóa một hoặc nhiều tệp hoặc thư mục.

##### Ví dụ yêu cầu

```bash
curl --request POST \
     --url http://{address}/api/v1/file/rm \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{
          "file_ids": ["file_id_1", "file_id_2"]
     }'
```

---

### Đổi tên file

**POST** `/api/v1/file/rename`

Đổi tên tệp hoặc thư mục.

##### Ví dụ yêu cầu

```bash
curl --request POST \
     --url http://{address}/api/v1/file/rename \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{
          "file_id": "{file_id}",
          "name": "new_name.txt"
     }'
```

> **Lưu ý**: Không hỗ trợ thay đổi phần mở rộng tệp.

---

### Tải file về

**GET** `/api/v1/file/get/{file_id}`

Tải xuống nội dung tệp.

##### Ví dụ yêu cầu

```bash
curl --request GET \
     --url http://{address}/api/v1/file/get/{file_id} \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --output ./downloaded_file.txt
```

---

### Di chuyển file

**POST** `/api/v1/file/mv`

Di chuyển một hoặc nhiều tệp vào thư mục đích.

##### Ví dụ yêu cầu

```bash
curl --request POST \
     --url http://{address}/api/v1/file/mv \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{
          "src_file_ids": ["file_id_1", "file_id_2"],
          "dest_file_id": "{destination_folder_id}"
     }'
```

---

### Chuyển đổi file thành tài liệu và liên kết với dataset

**POST** `/api/v1/file/convert`

Chuyển đổi tệp thành tài liệu và liên kết chúng với các dataset được chỉ định.

##### Ví dụ yêu cầu

```bash
curl --request POST \
     --url http://{address}/api/v1/file/convert \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data '{
          "file_ids": ["file_id_1", "file_id_2"],
          "kb_ids": ["dataset_id_1", "dataset_id_2"]
     }'
```

##### Tham số yêu cầu

- `"file_ids"`: (*Tham số Body*), `list[string]`, *Bắt buộc*. ID tệp cần chuyển đổi. Nếu cung cấp ID thư mục, tất cả tệp trong thư mục sẽ được chuyển đổi.
- `"kb_ids"`: (*Tham số Body*), `list[string]`, *Bắt buộc*. ID các dataset đích.

#### Phản hồi

Thành công:

```json
{
    "code": 0,
    "data": [
        {
            "id": "file2doc_id_1",
            "file_id": "file_id_1",
            "document_id": "document_id_1"
        }
    ]
}
```
