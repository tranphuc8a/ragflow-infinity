---
sidebar_position: 5
slug: /python_api_reference
categoryIcon: SiPython
---

# Python API

RAGFlow Python SDK cung cấp giao diện lập trình phong phú để tương tác với RAGFlow. Tài liệu này mô tả chi tiết tất cả các phương thức có sẵn, tham số và kết quả trả về.

## MÃ LỖI

| Mã lỗi | Mô tả |
|--------|-------|
| 400 | Yêu cầu không hợp lệ |
| 401 | Xác thực thất bại |
| 403 | Không có quyền truy cập |
| 404 | Không tìm thấy tài nguyên |
| 500 | Lỗi nội bộ máy chủ |
| 1001 | Lỗi xử lý tài liệu |
| 1002 | Dung lượng vượt quá giới hạn |

---

## API Tương thích OpenAI

RAGFlow hỗ trợ định dạng API tương thích với OpenAI. Bạn có thể sử dụng thư viện `openai` Python để kết nối với RAGFlow.

```python
from openai import OpenAI

client = OpenAI(
    api_key="<YOUR_API_KEY>",
    base_url="http://<YOUR_BASE_URL>/api/v1"
)

response = client.chat.completions.create(
    model="model_name",
    messages=[
        {"role": "user", "content": "Hello!"}
    ],
    stream=False
)
print(response.choices[0].message.content)
```

---

## QUẢN LÝ TẬP DỮ LIỆU

### Tạo tập dữ liệu

```python
RAGFlow.create_dataset(
    name: str,
    avatar: str = "",
    description: str = "",
    embedding_model: str = "",
    permission: str = "me",
    chunk_method: str = "naive",
    parser_config: DataSet.ParserConfig = None
) -> DataSet
```

Tạo một tập dữ liệu (dataset) mới.

#### Tham số

- `name`: (*Bắt buộc*)  
  Tên của dataset. Chỉ hỗ trợ BMP Unicode, tối đa 128 ký tự.

- `avatar`: (*Tùy chọn*)  
  Ảnh đại diện dưới dạng base64. Tối đa 65535 ký tự.

- `description`: (*Tùy chọn*)  
  Mô tả dataset.

- `embedding_model`: (*Tùy chọn*)  
  Tên mô hình nhúng. Định dạng: `model_name@model_factory`. Ví dụ: `"BAAI/bge-zh-v1.5@BAAI"`.

- `permission`: (*Tùy chọn*)  
  Quyền truy cập. Tùy chọn:
  - `"me"`: (Mặc định) Chỉ bạn có thể quản lý.
  - `"team"`: Tất cả thành viên nhóm có thể quản lý.

- `chunk_method`: (*Tùy chọn*)  
  Phương pháp phân đoạn (chunk) tài liệu. Tùy chọn:
  - `"naive"`: (Mặc định) Phân đoạn thông thường.
  - `"manual"` | `"qa"` | `"table"` | `"paper"` | `"book"` | `"laws"` | `"presentation"` | `"picture"` | `"one"` | `"knowledge_graph"` | `"email"`

- `parser_config`: (*Tùy chọn*)  
  Cấu hình trình phân tích. Xem `DataSet.ParserConfig`.

#### Trả về

Đối tượng `DataSet`.

#### Ví dụ

```python
from ragflow_sdk import RAGFlow

rag_object = RAGFlow(api_key="<YOUR_API_KEY>", base_url="http://<YOUR_BASE_URL>")
dataset = rag_object.create_dataset(name="my_dataset")
```

---

### Xóa tập dữ liệu

```python
RAGFlow.delete_datasets(ids: list[str] = None) -> bool
```

Xóa các dataset theo ID.

#### Tham số

- `ids`: (*Tùy chọn*)  
  Danh sách ID các dataset cần xóa. Nếu để trống, xóa tất cả dataset.

#### Ví dụ

```python
rag_object.delete_datasets(ids=["dataset_id_1", "dataset_id_2"])
```

---

### Liệt kê tập dữ liệu

```python
RAGFlow.list_datasets(
    page: int = 1,
    page_size: int = 30,
    orderby: str = "create_time",
    desc: bool = True,
    id: str = None,
    name: str = None
) -> list[DataSet]
```

Liệt kê tất cả dataset của người dùng.

#### Tham số

- `page`: (*Tùy chọn*) Số trang. Mặc định `1`.
- `page_size`: (*Tùy chọn*) Số lượng dataset mỗi trang. Mặc định `30`.
- `orderby`: (*Tùy chọn*) Sắp xếp theo trường. Mặc định `"create_time"`.
- `desc`: (*Tùy chọn*) Thứ tự giảm dần. Mặc định `True`.
- `id`: (*Tùy chọn*) Lọc theo ID dataset.
- `name`: (*Tùy chọn*) Lọc theo tên dataset (tìm kiếm mờ).

#### Ví dụ

```python
datasets = rag_object.list_datasets(page=1, page_size=10)
for ds in datasets:
    print(ds.name, ds.id)
```

---

### Cập nhật tập dữ liệu

```python
DataSet.update(update_message: dict) -> bool
```

Cập nhật thông tin của dataset.

#### Tham số

- `update_message`: Từ điển chứa các trường cần cập nhật. Các trường có thể cập nhật:
  - `name`: Tên mới
  - `description`: Mô tả mới
  - `embedding_model`: Mô hình nhúng mới
  - `chunk_method`: Phương pháp phân đoạn mới
  - `parser_config`: Cấu hình trình phân tích mới

#### Ví dụ

```python
dataset = rag_object.list_datasets(name="my_dataset")[0]
dataset.update({"name": "updated_dataset", "description": "Cập nhật mô tả"})
```

---

## QUẢN LÝ FILE TRONG TẬP DỮ LIỆU

### Tải tài liệu lên

```python
DataSet.upload_documents(document_list: list[dict]) -> list[Document]
```

Tải một hoặc nhiều tài liệu lên dataset.

#### Tham số

- `document_list`: (*Bắt buộc*)  
  Danh sách các tài liệu cần tải lên. Mỗi phần tử là một dict với:
  - `"display_name"`: Tên hiển thị
  - `"blob"`: Nội dung tệp dạng bytes

#### Ví dụ

```python
with open("test.pdf", "rb") as f:
    dataset.upload_documents([{"display_name": "test.pdf", "blob": f.read()}])
```

---

### Cập nhật tài liệu

```python
Document.update(update_message: dict) -> bool
```

Cập nhật thông tin của tài liệu.

#### Tham số

- `update_message`: Từ điển các trường cần cập nhật:
  - `"name"`: Tên tài liệu mới
  - `"chunk_method"`: Phương pháp phân đoạn mới
  - `"parser_config"`: Cấu hình trình phân tích mới

#### Ví dụ

```python
document.update({"name": "new_name.pdf"})
```

---

### Tải tài liệu về

```python
Document.download() -> bytes
```

Tải xuống nội dung tài liệu.

#### Trả về

Nội dung tài liệu dạng bytes.

#### Ví dụ

```python
content = document.download()
with open("downloaded.pdf", "wb") as f:
    f.write(content)
```

---

### Liệt kê tài liệu

```python
DataSet.list_docs(
    id: str = None,
    name: str = None,
    page: int = 1,
    page_size: int = 30,
    orderby: str = "create_time",
    desc: bool = True,
    keywords: str = ""
) -> list[Document]
```

Liệt kê tài liệu trong dataset.

#### Tham số

- `id`: (*Tùy chọn*) Lọc theo ID tài liệu.
- `name`: (*Tùy chọn*) Lọc theo tên tài liệu.
- `page`: (*Tùy chọn*) Số trang. Mặc định `1`.
- `page_size`: (*Tùy chọn*) Số lượng tài liệu mỗi trang. Mặc định `30`.
- `orderby`: (*Tùy chọn*) Sắp xếp theo trường. Mặc định `"create_time"`.
- `desc`: (*Tùy chọn*) Thứ tự giảm dần. Mặc định `True`.
- `keywords`: (*Tùy chọn*) Từ khóa tìm kiếm.

#### Ví dụ

```python
docs = dataset.list_docs(page=1, page_size=10)
for doc in docs:
    print(doc.name, doc.id)
```

---

### Xóa tài liệu

```python
DataSet.delete_docs(ids: list[str] = None) -> bool
```

Xóa tài liệu khỏi dataset.

#### Tham số

- `ids`: (*Tùy chọn*) Danh sách ID tài liệu cần xóa.

#### Ví dụ

```python
dataset.delete_docs(ids=["doc_id_1", "doc_id_2"])
```

---

### Phân tích tài liệu

```python
DataSet.async_parse_documents(document_ids: list[str]) -> bool
```

Bắt đầu phân tích (parse) các tài liệu theo ID.

#### Tham số

- `document_ids`: (*Bắt buộc*) Danh sách ID tài liệu cần phân tích.

#### Ví dụ

```python
dataset.async_parse_documents(document_ids=["doc_id_1", "doc_id_2"])
```

---

### Dừng phân tích tài liệu

```python
DataSet.async_cancel_parse_documents(document_ids: list[str]) -> bool
```

Dừng quá trình phân tích các tài liệu.

#### Tham số

- `document_ids`: (*Bắt buộc*) Danh sách ID tài liệu cần dừng phân tích.

#### Ví dụ

```python
dataset.async_cancel_parse_documents(document_ids=["doc_id_1"])
```

---

## QUẢN LÝ ĐOẠN TRONG TẬP DỮ LIỆU

### Thêm đoạn

```python
Document.add_chunk(content: str, important_keywords: list[str] = []) -> Chunk
```

Thêm thủ công một đoạn (chunk) vào tài liệu.

#### Tham số

- `content`: (*Bắt buộc*) Nội dung đoạn.
- `important_keywords`: (*Tùy chọn*) Danh sách từ khóa quan trọng.

#### Ví dụ

```python
chunk = document.add_chunk(
    content="Đây là nội dung đoạn văn.",
    important_keywords=["từ khóa 1", "từ khóa 2"]
)
```

---

### Liệt kê đoạn

```python
Document.list_chunks(
    page: int = 1,
    page_size: int = 30,
    keywords: str = ""
) -> list[Chunk]
```

Liệt kê các đoạn trong tài liệu.

#### Tham số

- `page`: (*Tùy chọn*) Số trang. Mặc định `1`.
- `page_size`: (*Tùy chọn*) Số lượng đoạn mỗi trang. Mặc định `30`.
- `keywords`: (*Tùy chọn*) Từ khóa lọc.

#### Ví dụ

```python
chunks = document.list_chunks(page=1, page_size=10)
for chunk in chunks:
    print(chunk.content[:100])
```

---

### Xóa đoạn

```python
Document.delete_chunks(chunk_ids: list[str]) -> bool
```

Xóa các đoạn khỏi tài liệu.

#### Tham số

- `chunk_ids`: (*Bắt buộc*) Danh sách ID đoạn cần xóa.

#### Ví dụ

```python
document.delete_chunks(chunk_ids=["chunk_id_1"])
```

---

### Cập nhật đoạn

```python
Chunk.update(update_message: dict) -> bool
```

Cập nhật nội dung hoặc trạng thái của đoạn.

#### Tham số

- `update_message`: Từ điển chứa các trường cần cập nhật:
  - `"content"`: Nội dung mới
  - `"important_keywords"`: Danh sách từ khóa mới
  - `"available"`: Trạng thái kích hoạt (`True`/`False`)

#### Ví dụ

```python
chunk.update({"content": "Nội dung cập nhật.", "available": True})
```

---

### Truy xuất đoạn

```python
RAGFlow.retrieve(
    question: str = "",
    datasets: list[str] = None,
    document: list[str] = None,
    offset: int = 1,
    limit: int = 30,
    similarity_threshold: float = 0.2,
    vector_similarity_weight: float = 0.3,
    top_k: int = 1024,
    rerank_id: str = None,
    keyword: bool = False,
    highlight: bool = False
) -> list[Chunk]
```

Truy xuất các đoạn liên quan từ dataset.

#### Tham số

- `question`: (*Tùy chọn*) Câu truy vấn.
- `datasets`: (*Tùy chọn*) Danh sách ID dataset cần tìm kiếm.
- `document`: (*Tùy chọn*) Danh sách ID tài liệu cần lọc.
- `offset`: (*Tùy chọn*) Số trang. Mặc định `1`.
- `limit`: (*Tùy chọn*) Số lượng đoạn tối đa trả về. Mặc định `30`.
- `similarity_threshold`: (*Tùy chọn*) Ngưỡng độ tương đồng tối thiểu. Mặc định `0.2`.
- `vector_similarity_weight`: (*Tùy chọn*) Trọng số tìm kiếm vector. Mặc định `0.3`.
- `top_k`: (*Tùy chọn*) Số đoạn tối đa để rerank. Mặc định `1024`.
- `rerank_id`: (*Tùy chọn*) ID mô hình rerank.
- `keyword`: (*Tùy chọn*) Bật tìm kiếm từ khóa. Mặc định `False`.
- `highlight`: (*Tùy chọn*) Hiển thị highlight từ khóa. Mặc định `False`.

#### Ví dụ

```python
chunks = rag_object.retrieve(
    question="RAGFlow là gì?",
    datasets=["dataset_id_1"],
    limit=10,
    similarity_threshold=0.3
)
for chunk in chunks:
    print(chunk.content)
```

---

## QUẢN LÝ TRỢ LÝ CHAT

### Tạo trợ lý chat

```python
RAGFlow.create_chat(
    name: str,
    avatar: str = "",
    dataset_ids: list[str] = [],
    llm: Chat.LLM = None,
    prompt: Chat.Prompt = None
) -> Chat
```

Tạo một trợ lý chat mới.

#### Tham số

- `name`: (*Bắt buộc*) Tên trợ lý chat.
- `avatar`: (*Tùy chọn*) Ảnh đại diện base64.
- `dataset_ids`: (*Tùy chọn*) Danh sách ID dataset liên kết.
- `llm`: (*Tùy chọn*) Cấu hình mô hình LLM. Xem `Chat.LLM`.
- `prompt`: (*Tùy chọn*) Cấu hình prompt. Xem `Chat.Prompt`.

#### Ví dụ

```python
chat_assistant = rag_object.create_chat(
    name="My Assistant",
    dataset_ids=["dataset_id_1"],
    llm=Chat.LLM(model_name="gpt-4o", temperature=0.3),
)
```

---

### Cập nhật trợ lý chat

```python
Chat.update(update_message: dict) -> bool
```

Cập nhật cấu hình của trợ lý chat.

#### Tham số

- `update_message`: Từ điển các trường cần cập nhật.

#### Ví dụ

```python
chat_assistant.update({"name": "Updated Assistant"})
```

---

### Xóa trợ lý chat

```python
RAGFlow.delete_chats(ids: list[str] = None) -> bool
```

Xóa các trợ lý chat theo ID.

#### Tham số

- `ids`: (*Tùy chọn*) Danh sách ID trợ lý cần xóa.

#### Ví dụ

```python
rag_object.delete_chats(ids=["chat_id_1"])
```

---

### Liệt kê trợ lý chat

```python
RAGFlow.list_chats(
    page: int = 1,
    page_size: int = 30,
    orderby: str = "create_time",
    desc: bool = True,
    id: str = None,
    name: str = None
) -> list[Chat]
```

Liệt kê tất cả trợ lý chat.

#### Ví dụ

```python
chats = rag_object.list_chats()
for chat in chats:
    print(chat.name, chat.id)
```

---

## QUẢN LÝ PHIÊN

### Tạo phiên với trợ lý chat

```python
Chat.create_session(name: str = "New session") -> Session
```

Tạo một phiên trò chuyện mới với trợ lý chat.

#### Tham số

- `name`: (*Tùy chọn*) Tên phiên. Mặc định `"New session"`.

#### Ví dụ

```python
session = chat_assistant.create_session(name="Phiên thử nghiệm")
```

---

### Cập nhật phiên

```python
Session.update(update_message: dict) -> bool
```

Cập nhật thông tin phiên.

#### Ví dụ

```python
session.update({"name": "Phiên đã cập nhật"})
```

---

### Liệt kê phiên

```python
Chat.list_sessions(
    page: int = 1,
    page_size: int = 30,
    orderby: str = "create_time",
    desc: bool = True,
    id: str = None,
    name: str = None
) -> list[Session]
```

Liệt kê tất cả phiên của trợ lý chat.

#### Ví dụ

```python
sessions = chat_assistant.list_sessions()
for session in sessions:
    print(session.name, session.id)
```

---

### Xóa phiên

```python
Chat.delete_sessions(ids: list[str] = None) -> bool
```

Xóa các phiên theo ID.

#### Ví dụ

```python
chat_assistant.delete_sessions(ids=["session_id_1"])
```

---

### Trò chuyện với trợ lý chat

```python
Session.ask(
    question: str,
    stream: bool = False
) -> Message | iter[Message]
```

Gửi tin nhắn đến trợ lý chat trong phiên hiện tại.

#### Tham số

- `question`: (*Bắt buộc*) Câu hỏi hoặc tin nhắn của người dùng.
- `stream`: (*Tùy chọn*) Bật chế độ luồng (streaming). Mặc định `False`.

#### Ví dụ - Không stream

```python
message = session.ask("RAGFlow là gì?", stream=False)
print(message.content)
```

#### Ví dụ - Có stream

```python
for message in session.ask("RAGFlow là gì?", stream=True):
    print(message.content, end="", flush=True)
```

---

### Tạo phiên với agent

```python
Agent.create_session() -> Session
```

Tạo một phiên mới với agent.

#### Ví dụ

```python
agent = rag_object.list_agents(name="my_agent")[0]
agent_session = agent.create_session()
```

---

### Trò chuyện với agent

```python
AgentSession.ask(
    question: str,
    stream: bool = False
) -> Message | iter[Message]
```

Gửi tin nhắn đến agent.

#### Ví dụ

```python
# Không stream
message = agent_session.ask("Tóm tắt tài liệu này", stream=False)
print(message.content)

# Có stream
for message in agent_session.ask("Phân tích dữ liệu", stream=True):
    print(message.content, end="", flush=True)
```

---

### Liệt kê phiên agent

```python
Agent.list_sessions(
    page: int = 1,
    page_size: int = 30,
    orderby: str = "create_time",
    desc: bool = True,
    id: str = None,
    user_id: str = None
) -> list[AgentSession]
```

Liệt kê các phiên của agent.

#### Ví dụ

```python
agent_sessions = agent.list_sessions()
for s in agent_sessions:
    print(s.id)
```

---

### Xóa phiên agent

```python
Agent.delete_sessions(ids: list[str] = None) -> bool
```

Xóa các phiên agent theo ID.

#### Ví dụ

```python
agent.delete_sessions(ids=["session_id_1"])
```

---

## QUẢN LÝ AGENT

### Liệt kê agent

```python
RAGFlow.list_agents(
    page: int = 1,
    page_size: int = 30,
    orderby: str = "create_time",
    desc: bool = True,
    id: str = None,
    name: str = None,
    title: str = None
) -> list[Agent]
```

Liệt kê tất cả agent.

#### Ví dụ

```python
agents = rag_object.list_agents()
for agent in agents:
    print(agent.title, agent.id)
```

---

### Tạo agent

```python
RAGFlow.create_agent(
    title: str,
    dsl: dict = {}
) -> Agent
```

Tạo một agent mới bằng DSL (Domain-Specific Language).

#### Tham số

- `title`: (*Bắt buộc*) Tiêu đề agent.
- `dsl`: (*Tùy chọn*) Định nghĩa luồng agent dưới dạng JSON.

#### Ví dụ

```python
agent = rag_object.create_agent(title="My Analysis Agent", dsl={...})
```

---

### Cập nhật agent

```python
Agent.update(update_message: dict) -> bool
```

Cập nhật cấu hình của agent.

#### Ví dụ

```python
agent.update({"title": "Updated Agent"})
```

---

### Xóa agent

```python
RAGFlow.delete_agents(ids: list[str] = None) -> bool
```

Xóa các agent theo ID.

#### Ví dụ

```python
rag_object.delete_agents(ids=["agent_id_1"])
```

---

## QUẢN LÝ BỘ NHỚ

### Tạo bộ nhớ

```python
RAGFlow.create_memory(
    name: str,
    memory_type: list[str],
    embd_id: str,
    llm_id: str = None,
    avatar: str = None,
    permission: str = "me",
    memory_size: int = 5*1024*1024,
    forgetting_policy: str = "FIFO",
    temperature: float = 0.5,
    system_prompt: str = None,
    user_prompt: str = None,
    description: str = None
) -> Memory
```

Tạo một bộ nhớ mới cho agent.

#### Tham số

- `name`: (*Bắt buộc*) Tên bộ nhớ.
- `memory_type`: (*Bắt buộc*) Danh sách loại bộ nhớ. Tùy chọn: `"raw"`, `"semantic"`, `"episodic"`, `"procedural"`.
- `embd_id`: (*Bắt buộc*) ID mô hình nhúng. Định dạng: `model_name@model_factory`.
- `llm_id`: (*Tùy chọn*) ID mô hình LLM.
- `avatar`: (*Tùy chọn*) Ảnh đại diện base64.
- `permission`: (*Tùy chọn*) Quyền truy cập: `"me"` hoặc `"team"`. Mặc định `"me"`.
- `memory_size`: (*Tùy chọn*) Kích thước tối đa (bytes). Mặc định `5*1024*1024`.
- `forgetting_policy`: (*Tùy chọn*) Chính sách quên. Mặc định `"FIFO"`.
- `temperature`: (*Tùy chọn*) Độ ngẫu nhiên [0, 1]. Mặc định `0.5`.
- `system_prompt`: (*Tùy chọn*) Prompt hệ thống.
- `user_prompt`: (*Tùy chọn*) Prompt người dùng tùy chỉnh.
- `description`: (*Tùy chọn*) Mô tả bộ nhớ.

#### Ví dụ

```python
memory = rag_object.create_memory(
    name="agent_memory",
    memory_type=["raw", "semantic"],
    embd_id="BAAI/bge-large-zh-v1.5@SILICONFLOW"
)
```

---

### Cập nhật bộ nhớ

```python
Memory.update(update_message: dict) -> bool
```

Cập nhật cấu hình bộ nhớ.

#### Tham số

- `update_message`: Từ điển các trường cần cập nhật.

#### Ví dụ

```python
memory.update({"name": "updated_memory"})
```

---

### Liệt kê bộ nhớ

```python
RAGFlow.list_memories(
    page: int = 1,
    page_size: int = 50,
    memory_type: list[str] = None,
    keywords: str = ""
) -> list[Memory]
```

Liệt kê tất cả bộ nhớ.

#### Ví dụ

```python
memories = rag_object.list_memories()
for mem in memories:
    print(mem.name, mem.id)
```

---

### Lấy cấu hình bộ nhớ

```python
Memory.get_config() -> dict
```

Lấy toàn bộ cấu hình của bộ nhớ.

#### Ví dụ

```python
config = memory.get_config()
print(config)
```

---

### Xóa bộ nhớ

```python
RAGFlow.delete_memories(ids: list[str] = None) -> bool
```

Xóa các bộ nhớ theo ID.

#### Ví dụ

```python
rag_object.delete_memories(ids=["memory_id_1"])
```

---

### Liệt kê tin nhắn trong bộ nhớ

```python
Memory.list_messages(
    agent_id: str = None,
    session_id: str = None,
    page: int = 1,
    page_size: int = 50
) -> list[MemoryMessage]
```

Liệt kê các tin nhắn trong bộ nhớ.

#### Ví dụ

```python
messages = memory.list_messages(page=1, page_size=20)
for msg in messages:
    print(msg.message_id, msg.message_type)
```

---

### Thêm tin nhắn vào bộ nhớ

```python
RAGFlow.add_message(
    memory_ids: list[str],
    agent_id: str,
    session_id: str,
    user_input: str,
    agent_response: str,
    user_id: str = None
) -> bool
```

Thêm một cặp tin nhắn (hỏi-đáp) vào các bộ nhớ được chỉ định.

#### Tham số

- `memory_ids`: (*Bắt buộc*) Danh sách ID bộ nhớ cần lưu tin nhắn.
- `agent_id`: (*Bắt buộc*) ID của agent nguồn.
- `session_id`: (*Bắt buộc*) ID của phiên.
- `user_input`: (*Bắt buộc*) Văn bản nhập của người dùng.
- `agent_response`: (*Bắt buộc*) Phản hồi của agent.
- `user_id`: (*Tùy chọn*) ID người dùng.

#### Ví dụ

```python
rag_object.add_message(
    memory_ids=["memory_id_1"],
    agent_id="agent_id_1",
    session_id="session_id_1",
    user_input="RAGFlow là gì?",
    agent_response="RAGFlow là một RAG engine mã nguồn mở."
)
```

---

### Quên tin nhắn

```python
Memory.forget_message(message_id: int) -> bool
```

Đặt tin nhắn thành trạng thái "đã quên" - sẽ không được truy xuất nữa.

#### Tham số

- `message_id`: (*Bắt buộc*) ID số nguyên của tin nhắn cần quên.

#### Ví dụ

```python
memory.forget_message(message_id=233)
```

---

### Cập nhật trạng thái tin nhắn

```python
Memory.update_message_status(message_id: int, status: bool) -> bool
```

Bật hoặc tắt một tin nhắn.

#### Tham số

- `message_id`: (*Bắt buộc*) ID tin nhắn.
- `status`: (*Bắt buộc*) `True` = bật, `False` = tắt.

#### Ví dụ

```python
memory.update_message_status(message_id=270, status=False)
```

---

### Tìm kiếm tin nhắn

```python
Memory.search_messages(
    query: str,
    memory_ids: list[str] = None,
    agent_id: str = None,
    session_id: str = None,
    similarity_threshold: float = 0.2,
    keywords_similarity_weight: float = 0.7,
    top_n: int = 10
) -> list[MemoryMessage]
```

Tìm kiếm tin nhắn liên quan đến truy vấn.

#### Ví dụ

```python
results = memory.search_messages(
    query="RAGFlow là gì?",
    top_n=5
)
for msg in results:
    print(msg.content[:200])
```

---

### Lấy tin nhắn gần đây

```python
Memory.get_recent_messages(
    memory_ids: list[str] = None,
    agent_id: str = None,
    session_id: str = None,
    limit: int = 10
) -> list[MemoryMessage]
```

Lấy các tin nhắn gần đây nhất từ bộ nhớ.

#### Ví dụ

```python
recent = memory.get_recent_messages(limit=5)
for msg in recent:
    print(msg.valid_at, msg.content[:100])
```

---

### Lấy nội dung tin nhắn

```python
Memory.get_message_content(message_id: int) -> MemoryMessage
```

Lấy toàn bộ nội dung và vector nhúng của một tin nhắn cụ thể.

#### Tham số

- `message_id`: (*Bắt buộc*) ID tin nhắn.

#### Ví dụ

```python
msg = memory.get_message_content(message_id=270)
print(msg.content)
print(len(msg.content_embed))  # Kích thước vector nhúng
```
