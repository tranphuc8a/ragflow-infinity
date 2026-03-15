---
sidebar_position: 1
slug: /contributing
sidebar_custom_props: {
  categoryIcon: LucideBookA
}
---
# Hướng dẫn đóng góp

Hướng dẫn chung cho các cộng tác viên cộng đồng RAGFlow.

---

Tài liệu này cung cấp hướng dẫn và các xem xét quan trọng khi gửi đóng góp của bạn cho RAGFlow.

- Để báo cáo lỗi, hãy gửi [GitHub issue](https://github.com/infiniflow/ragflow/issues/new/choose).
- Để đặt câu hỏi thêm, bạn có thể khám phá các thảo luận hiện có hoặc bắt đầu thảo luận mới trong [Discussions](https://github.com/orgs/infiniflow/discussions).

## Bạn có thể đóng góp gì

Danh sách dưới đây đề cập đến một số đóng góp bạn có thể thực hiện, nhưng không phải là danh sách đầy đủ.

- Đề xuất hoặc triển khai tính năng mới
- Sửa lỗi
- Thêm test case hoặc demo
- Đăng blog hoặc hướng dẫn
- Cập nhật tài liệu, code hoặc chú thích hiện có
- Đề xuất mã lỗi thân thiện với người dùng hơn

## Gửi pull request (PR)

### Quy trình chung

1. Fork kho GitHub của chúng tôi.
2. Clone fork về máy cục bộ:
`git clone git@github.com:<yourname>/ragflow.git`
3. Tạo nhánh cục bộ: 
`git checkout -b my-branch`
4. Cung cấp đủ thông tin trong commit message:
`git commit -m 'Cung cấp thông tin đầy đủ trong commit message'`
5. Commit các thay đổi vào nhánh cục bộ, và đẩy lên GitHub:
`git push origin my-branch.`
6. Gửi pull request để xem xét.

### Trước khi gửi PR

- Xem xét chia một PR lớn thành nhiều PR nhỏ hơn, độc lập để giữ lịch sử phát triển có thể truy vết.
- Đảm bảo PR của bạn chỉ giải quyết một vấn đề, hoặc giữ các thay đổi không liên quan nhỏ.
- Thêm test case khi đóng góp tính năng mới. Chúng chứng minh code của bạn hoạt động đúng và bảo vệ khỏi các vấn đề tiềm ẩn từ các thay đổi trong tương lai.

### Mô tả PR của bạn

- Đảm bảo tiêu đề PR của bạn ngắn gọn và rõ ràng, cung cấp tất cả thông tin cần thiết.
- Tham chiếu đến GitHub issue tương ứng trong mô tả PR nếu có.
- Bao gồm đủ chi tiết thiết kế cho *breaking changes* hoặc *API changes* trong mô tả.

### Xem xét & hợp nhất PR

Đảm bảo PR của bạn vượt qua tất cả các bài kiểm tra Tích hợp Liên tục (CI) trước khi hợp nhất.
