---
sidebar_position: 40
slug: /indexer_component
sidebar_custom_props: {
  categoryIcon: LucideListPlus
}
---
# Thành phần Indexer

Một thành phần xác định cách các chunk được lập chỉ mục.

---

Thành phần **Indexer** lập chỉ mục các chunk và cấu hình định dạng lưu trữ của chúng trong document engine.

## Kịch bản sử dụng

**Indexer** là thành phần kết thúc bắt buộc cho mọi ingestion pipeline.

## Cấu hình

### Search method

Cấu hình cách lưu chunk trong document engine: toàn văn bản, embeddings hoặc cả hai.

### Filename embedding weight

Xác định mức đóng góp của tên tệp vào embedding cuối cùng, vốn là tổ hợp có trọng số giữa nội dung chunk và tên tệp. Giá trị cao hơn nghĩa là tên tệp có ảnh hưởng lớn hơn trong embedding tổng hợp.

- 0.1: Tên tệp đóng góp 10% (nội dung chunk 90%)
- 0.5 (tối đa): Tên tệp đóng góp 50% (nội dung chunk 50%)
