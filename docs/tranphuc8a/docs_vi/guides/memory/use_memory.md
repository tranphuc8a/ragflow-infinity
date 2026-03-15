---
sidebar_position: 1
slug: /use_memory
sidebar_custom_props: {
  categoryIcon: LucideMonitorCog
}
---

# Sử dụng bộ nhớ

Module Bộ nhớ của RAGFlow được xây dựng để lưu mọi thứ, bao gồm cả các cuộc hội thoại xảy ra khi Agent đang làm việc. Nó lưu các nhật ký thô của các cuộc hội thoại, như những gì người dùng nói và những gì AI trả lời. Nó cũng lưu thêm các thông tin được tạo ra trong lúc chat, như các tóm tắt hoặc ghi chú mà AI tạo ra về tương tác. Công việc chính của nó là làm cho các cuộc hội thoại diễn ra suôn sẻ từ cuộc này sang cuộc khác, cho phép AI nhớ các thông tin cá nhân về người dùng, và để AI học từ tất cả các cuộc trò chuyện trước đây.

Module này không chỉ lưu dữ liệu thô. Nó đủ thông minh để sắp xếp thông tin thành các loại hữu ích khác nhau. Nó có thể trích xuất các sự kiện và ý nghĩa chính (bộ nhớ ngữ nghĩa), nhớ các sự kiện và câu chuyện cụ thể từ các cuộc chat trước (bộ nhớ theo sự kiện), và lưu các chi tiết cần thiết cho tác vụ hiện tại (bộ nhớ làm việc). Điều này biến một nhật ký đơn giản thành một thư viện có tổ chức về các trải nghiệm trước đây.

Nhờ đó, người dùng có thể dễ dàng mang lại bất kỳ thông tin đã lưu nào vào cuộc hội thoại mới. Ngữ cảnh quá khứ này giúp AI luôn đúng chủ đề và tránh lặp lại, làm cho các cuộc chat cảm thấy kết nối và tự nhiên hơn. Quan trọng hơn, nó cung cấp cho AI lịch sử đáng tin cậy để suy nghĩ từ đó, giúp câu trả lời của nó chính xác và hữu ích hơn.

## Tạo bộ nhớ

Module Bộ nhớ cung cấp quản lý tập trung và hợp lý của tất cả các bộ nhớ.

Khi tạo Bộ nhớ, người dùng có thể xác định chính xác loại thông tin nào cần trích xuất, giúp đảm bảo chỉ dữ liệu liên quan được nắm bắt và tổ chức. Từ đường dẫn điều hướng Tổng quan >> Bộ nhớ, người dùng có thể thực hiện các thao tác quản lý chính, bao gồm đổi tên bộ nhớ, tổ chức chúng và chia sẻ với các thành viên nhóm để hỗ trợ quy trình làm việc cộng tác.

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/memory_interface.PNG)

## Cấu hình bộ nhớ

Trên trang **Bộ nhớ**, nhấp vào bộ nhớ mong muốn **>** **Cấu hình** để xem và cập nhật cài đặt của nó.

### Tên

Tên duy nhất của bộ nhớ đã tạo.

### Mô hình nhúng

Mô hình nhúng để chuyển đổi bộ nhớ thành các embedding.

### LLM

Mô hình chat để trích xuất kiến thức từ bộ nhớ.

### Loại bộ nhớ

Những gì được lưu trong bộ nhớ:

`Thô`: Cuộc hội thoại thô giữa người dùng và Agent (Bắt buộc theo mặc định).
`Bộ nhớ ngữ nghĩa`: Kiến thức chung và sự kiện về người dùng và thế giới.
`Bộ nhớ theo sự kiện`: Hồ sơ có dấu thời gian về các sự kiện và trải nghiệm cụ thể.
`Bộ nhớ thủ tục`: Các kỹ năng đã học, thói quen và quy trình tự động.

### Kích thước bộ nhớ

Dung lượng mặc định được phân bổ cho bộ nhớ và các embedding tương ứng tính bằng byte. Mặc định là `5242880` (5MB).

:::tip LƯU Ý
Một tin nhắn 1KB với embedding 1024 chiều chiếm khoảng 9KB bộ nhớ (1KB + 1024 x 8Bytes = 9KB). Với giới hạn mặc định 5 MB, hệ thống có thể lưu khoảng 500 tin nhắn như vậy.
:::

### Quyền

- **Chỉ mình tôi**: Độc quyền cho người dùng.
- **Nhóm**: Chia sẻ bộ nhớ này với các thành viên nhóm.

## Quản lý bộ nhớ

Trong trang Bộ nhớ riêng lẻ, bạn có thể tinh chỉnh cách các mục đã lưu được sử dụng trong các lời gọi Agent. Mỗi mục có thể được bật hoặc tắt chọn lọc, cho phép bạn kiểm soát các thông tin nào vẫn còn hoạt động mà không cần xóa vĩnh viễn.

Khi một số chi tiết không còn liên quan, bạn cũng có thể chọn quên hoàn toàn các mục bộ nhớ cụ thể. Điều này giữ cho Bộ nhớ sạch sẽ, tập trung và dễ duy trì theo thời gian, đảm bảo rằng Agent chỉ dựa vào thông tin cập nhật và hữu ích.

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/memory_interface.PNG)

Các mục bộ nhớ bị quên thủ công hoàn toàn bị loại trừ khỏi kết quả được trả về bởi các lời gọi Agent, đảm bảo chúng không còn ảnh hưởng đến hành vi downstream. Điều này giúp các phản hồi tập trung vào thông tin liên quan nhất và được lưu giữ có chủ đích.

Khi Bộ nhớ đạt đến giới hạn lưu trữ và chính sách quên tự động được áp dụng, các mục đã bị quên thủ công trước đó cũng được ưu tiên xóa. Điều này cho phép hệ thống lấy lại dung lượng thông minh hơn trong khi tôn trọng các quyết định quản lý trước đó của người dùng.

## Nâng cao ngữ cảnh Agent

Trong cài đặt thành phần [Retrieval](../agent/agent_component_reference/retrieval.mdx) và [Message](../agent/agent_component_reference/message.mdx), một khả năng gọi Bộ nhớ mới có sẵn. Trong thành phần Message, người dùng có thể cấu hình Agent để ghi dữ liệu được chọn vào Bộ nhớ được chỉ định, trong khi thành phần Retrieval có thể được đặt để đọc từ Bộ nhớ đó để trả lời các truy vấn trong tương lai. Điều này cho phép một Agent bot Q&A đơn giản tích lũy ngữ cảnh theo thời gian và phản hồi với các câu trả lời phong phú hơn, có nhận thức về bộ nhớ.

### Truy xuất từ bộ nhớ

Đối với bất kỳ cấu hình Agent nào sử dụng Bộ nhớ, cần có thành phần **Retrieval** để đưa thông tin đã lưu trở lại cuộc hội thoại. Bằng cách bao gồm Retrieval bên cạnh các thành phần có nhận thức về Bộ nhớ, Agent có thể nhất quán nhớ lại và áp dụng dữ liệu quá khứ liên quan bất cứ khi nào cần.

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/retrieve_from_memory.PNG)

### Lưu vào bộ nhớ

Đồng thời bạn hoàn tất cài đặt thành phần **Retrieval**, hãy chọn Bộ nhớ tương ứng trong thành phần **Message** trong **Lưu vào Bộ nhớ**:

![](https://raw.githubusercontent.com/infiniflow/ragflow-docs/main/images/save_to_memory.png)

## Câu hỏi thường gặp

### Tôi có thể chia sẻ bộ nhớ của mình không?

Có, bạn có thể. Bộ nhớ của bạn có thể được chia sẻ giữa các Agent. Xem các chủ đề sau:

- [Tạo bộ nhớ](#tạo-bộ-nhớ)
- [Nâng cao ngữ cảnh Agent](#nâng-cao-ngữ-cảnh-agent)

Nếu bạn muốn chia sẻ bộ nhớ với các thành viên nhóm, hãy đảm bảo bạn đã cấu hình quyền nhóm của nó. Xem [Chia sẻ bộ nhớ](../team/share_memory.md) để biết chi tiết.
