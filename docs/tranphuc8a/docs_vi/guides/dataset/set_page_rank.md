---
sidebar_position: -2
slug: /set_page_rank
sidebar_custom_props: {
  categoryIcon: LucideStickyNote
}
---
# Thiết lập page rank

Tạo chiến lược truy xuất theo bước bằng page rank.

---

## Kịch bản

Trong chat AI, bạn có thể cấu hình trợ lý chat hoặc agent trả lời bằng kiến thức truy xuất từ nhiều dataset, miễn chúng dùng cùng embedding model. Nếu bạn muốn thông tin từ một số dataset được ưu tiên hơn hoặc được truy xuất trước, hãy dùng tính năng page rank của RAGFlow để tăng thứ hạng các chunk từ các dataset đó.

:::info LƯU Ý
Tính năng page rank này hoạt động ở cấp toàn bộ dataset, không phải từng tệp/tài liệu riêng lẻ.
:::

## Cấu hình

Trên trang **Configuration** của dataset, kéo thanh trượt **Page rank** để đặt giá trị page rank. Bạn cũng có thể nhập trực tiếp giá trị ở ô bên cạnh thanh trượt.

:::info LƯU Ý
Giá trị page rank phải là số nguyên. Phạm vi: [0,100]

- 0: Tắt (mặc định)
- Giá trị cụ thể: Bật
:::

:::tip LƯU Ý
Nếu đặt giá trị không nguyên (ví dụ 1.7), hệ thống sẽ làm tròn xuống số nguyên gần nhất, trong trường hợp này là 1.
:::

## Cơ chế chấm điểm

Nếu bạn đặt **similarity threshold** của trợ lý chat là 0.2, chỉ các chunk có hybrid score lớn hơn 0.2 x 100 = 20 mới được truy xuất và gửi tới mô hình chat để tạo nội dung.

Nếu dataset A (tin 2024) có page rank 1 và dataset B (tin 2023) có page rank 0, điểm hybrid cuối của các chunk truy xuất sẽ được điều chỉnh tương ứng. Một chunk từ dataset A có điểm ban đầu 50 sẽ được cộng 1 x 100 = 100 điểm, thành điểm cuối 150. Nhờ đó, chunk từ dataset A luôn đứng trước chunk từ dataset B.
