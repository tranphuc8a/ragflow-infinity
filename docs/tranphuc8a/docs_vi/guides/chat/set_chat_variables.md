---
sidebar_position: 4
slug: /set_chat_variables
sidebar_custom_props: {
  categoryIcon: LucideVariable
}
---
# Thiết lập biến

Thiết lập các biến để sử dụng cùng với system prompt cho LLM của bạn.

---

Khi cấu hình system prompt cho mô hình chat, các biến đóng vai trò quan trọng trong việc tăng cường tính linh hoạt và khả năng tái sử dụng. Với các biến, bạn có thể điều chỉnh động system prompt được gửi đến mô hình. Trong ngữ cảnh RAGFlow, nếu bạn đã định nghĩa các biến trong **Cài đặt Chat**, ngoại trừ biến dành riêng của hệ thống `{knowledge}`, bạn phải truyền giá trị cho chúng từ [HTTP API](../../references/http_api_reference.md#converse-with-chat-assistant) của RAGFlow hoặc thông qua [Python SDK](../../references/python_api_reference.md#converse-with-chat-assistant) của nó.

:::danger QUAN TRỌNG
Trong RAGFlow, các biến liên kết chặt chẽ với system prompt. Khi bạn thêm biến trong phần **Biến**, hãy bao gồm nó trong system prompt. Ngược lại, khi xóa biến, hãy đảm bảo nó được xóa khỏi system prompt; nếu không sẽ xảy ra lỗi.
:::

## Nơi thiết lập biến

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/chat_variables.jpg)

## 1. Quản lý biến

Trong phần **Biến**, bạn thêm, xóa hoặc cập nhật các biến.

### `{knowledge}` - một biến dành riêng

`{knowledge}` là biến dành riêng của hệ thống, đại diện cho các đoạn văn bản được truy xuất từ (các) tập dữ liệu được chỉ định bởi **Cơ sở kiến thức** trong tab **Cài đặt trợ lý**. Nếu trợ lý chat của bạn được liên kết với một số tập dữ liệu nhất định, bạn có thể giữ nguyên nó.

:::info LƯU Ý
Hiện tại không có sự khác biệt nào dù `{knowledge}` được đặt là tùy chọn hay bắt buộc, nhưng lưu ý rằng thiết kế này sẽ được cập nhật trong thời gian tới.
:::

Từ v0.17.0 trở đi, bạn có thể bắt đầu chat AI mà không cần chỉ định tập dữ liệu. Trong trường hợp này, chúng tôi khuyến nghị bỏ biến `{knowledge}` để tránh tham chiếu không cần thiết và giữ trống trường **Phản hồi rỗng** để tránh lỗi.

### Biến tùy chỉnh

Ngoài `{knowledge}`, bạn cũng có thể định nghĩa các biến riêng của mình để kết hợp với system prompt. Để sử dụng các biến tùy chỉnh này, bạn phải truyền giá trị cho chúng thông qua các API chính thức của RAGFlow. Công tắc **Tùy chọn** xác định liệu các biến này có bắt buộc trong các API tương ứng hay không:

- **Tắt** (Mặc định): Biến là bắt buộc và phải được cung cấp.
- **Bật**: Biến là tùy chọn và có thể bỏ qua nếu không cần thiết.

## 2. Cập nhật system prompt

Sau khi bạn thêm hoặc xóa biến trong phần **Biến**, hãy đảm bảo các thay đổi của bạn được phản ánh trong system prompt để tránh mâu thuẫn hoặc lỗi. Đây là một ví dụ:

```
Bạn là trợ lý thông minh. Hãy trả lời câu hỏi bằng cách tóm tắt các đoạn từ (các) tập dữ liệu được chỉ định...

Câu trả lời của bạn nên tuân theo phong cách {style} chuyên nghiệp.

...

Đây là cơ sở kiến thức:
{knowledge}
Trên đây là cơ sở kiến thức.
```

:::tip LƯU Ý
Nếu bạn đã xóa `{knowledge}`, hãy đảm bảo bạn xem xét và cập nhật toàn bộ system prompt kỹ lưỡng để đạt được kết quả tối ưu.
:::

## Các API

Cách *duy nhất* để truyền giá trị cho các biến tùy chỉnh được định nghĩa trong hộp thoại **Cấu hình Chat** là gọi [HTTP API](../../references/http_api_reference.md#converse-with-chat-assistant) của RAGFlow hoặc thông qua [Python SDK](../../references/python_api_reference.md#converse-with-chat-assistant) của nó.

### HTTP API

Xem [Trò chuyện với trợ lý chat](../../references/http_api_reference.md#converse-with-chat-assistant). Đây là ví dụ:

```json {9}
curl --request POST \
     --url http://{address}/api/v1/chats/{chat_id}/completions \
     --header 'Content-Type: application/json' \
     --header 'Authorization: Bearer <YOUR_API_KEY>' \
     --data-binary '
     {
          "question": "xxxxxxxxx",
          "stream": true,
          "style":"hilarious"
     }'
```

### Python API

Xem [Trò chuyện với trợ lý chat](../../references/python_api_reference.md#converse-with-chat-assistant). Đây là ví dụ:

```python {18}
from ragflow_sdk import RAGFlow

rag_object = RAGFlow(api_key="<YOUR_API_KEY>", base_url="http://<YOUR_BASE_URL>:9380")
assistant = rag_object.list_chats(name="Miss R")
assistant = assistant[0]
session = assistant.create_session()    

print("\n==================== Miss R =====================\n")
print("Hello. What can I do for you?")

while True:
    question = input("\n==================== User =====================\n> ")
    style = input("Please enter your preferred style (e.g., formal, informal, hilarious): ")
    
    print("\n==================== Miss R =====================\n")
    
    cont = ""
    for ans in session.ask(question, stream=True, style=style):
        print(ans.content[len(cont):], end='', flush=True)
        cont = ans.content
```
