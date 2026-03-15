---
sidebar_position: 3
slug: /switch_doc_engine
sidebar_custom_props: {
  categoryIcon: LucideShuffle
}
---
# Chuyển đổi document engine

Chuyển doc engine từ Elasticsearch sang Infinity.

---

RAGFlow sử dụng Elasticsearch theo mặc định để lưu trữ toàn văn và vector. Để chuyển sang [Infinity](https://github.com/infiniflow/infinity/), hãy làm theo các bước sau:

:::caution CẢNH BÁO
Chuyển sang Infinity trên máy Linux/arm64 chưa được hỗ trợ chính thức.
:::

1. Dừng tất cả các container đang chạy:

   ```bash
   $ docker compose -f docker/docker-compose.yml down -v
   ```

:::caution CẢNH BÁO
`-v` sẽ xóa các volumes của Docker container, và dữ liệu hiện có sẽ bị xóa.
:::

2. Đặt `DOC_ENGINE` trong **docker/.env** thành `infinity`.

3. Khởi động lại các container:

   ```bash
   $ docker compose -f docker-compose.yml up -d
   ```
