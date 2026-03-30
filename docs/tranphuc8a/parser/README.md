# Nghiên cứu Parser trong RAGFlow

Tài liệu này tổng hợp kiến trúc, cơ chế hoạt động và mã nguồn parser trong RAGFlow, tập trung sâu vào `deepdoc`.

## Trang này dùng để làm gì

- Đọc nhanh toàn bộ thay đổi liên quan tích hợp DoXA parser.
- Nắm dependency cần có trước khi chạy.
- Hiểu thiết kế cài đặt theo 2 luồng ingest (Traditional và Dataflow).
- Xem sơ đồ mã nguồn để biết file nào chịu trách nhiệm phần nào.
- Đi theo link để đọc tài liệu chi tiết khi cần.

## Mục lục

- [01. Kiến trúc tổng thể parser](./01-kien-truc-tong-the.md)
- [02. Danh mục parser và so sánh](./02-danh-muc-parser-va-so-sanh.md)
- [03. Luồng thực thi parser end-to-end](./03-luong-thuc-thi-parser.md)
- [04. Thêm parser mới `doxa_parser`](./04-them-doxa-parser.md)
- [05. Kế hoạch tích hợp DoXA parser](./05-doxa-parser-integration-plan.md)
- [06. Contract và cấu hình DoXA](./06-doxa-contract-and-config.md)
- [07. Deploy và runbook xử lý sự cố DoXA](./07-doxa-deploy-and-runbook.md)

## Tóm tắt thay đổi đã triển khai

- Thêm adapter parser DoXA ở backend.
- Nối DoXA vào Lane A (traditional ingest) và Lane B (pipeline/dataflow ingest).
- Bổ sung lựa chọn DoXA trong UI parser method.
- Bổ sung form cấu hình DoXA cho cả Dataset và Pipeline PDF parser node.
- Bổ sung locale en/vi cho các nhãn và tooltip DoXA.
- Bổ sung test unit và test integration wiring để khóa thay đổi.

## Dependency và yêu cầu môi trường

- Python package: doxa-sdk.
- Biến môi trường hỗ trợ:
- DOXA_API_TOKEN
- DOXA_API_BASE
- DOXA_IPAAS_TOKEN (tùy chọn)

Chi tiết cấu hình: [06-doxa-contract-and-config.md](./06-doxa-contract-and-config.md).

## Thiết kế cài đặt (dễ hiểu)

### 1) Adapter layer

- File trung tâm: [deepdoc/parser/doxa_parser.py](../../../deepdoc/parser/doxa_parser.py).
- Nhiệm vụ:
- Kiểm tra điều kiện chạy (SDK, token, URL).
- Gọi DoXA API parse.
- Chuẩn hóa output về dạng mà RAGFlow đang tiêu thụ.

### 2) Nối vào Traditional ingest (Lane A)

- File chính: [rag/app/naive.py](../../../rag/app/naive.py).
- Điểm nối:
- Hàm by_doxa.
- Đăng ký doxa vào PARSERS.
- Đảm bảo đường chunk xử lý đúng như các parser tương đương.

### 3) Nối vào Dataflow ingest (Lane B)

- File chính: [rag/flow/parser/parser.py](../../../rag/flow/parser/parser.py).
- Điểm nối:
- Cho phép parse_method là doxa trong validate.
- Thêm nhánh parse PDF bằng DoXA trong runtime parser node.

### 4) UI cấu hình

- Selector parser method: [web/src/components/layout-recognize-form-field.tsx](../../../web/src/components/layout-recognize-form-field.tsx).
- Form DoXA options mới: [web/src/components/doxa-options-form-field.tsx](../../../web/src/components/doxa-options-form-field.tsx).
- Pipeline PDF form: [web/src/pages/agent/form/parser-form/pdf-form-fields.tsx](../../../web/src/pages/agent/form/parser-form/pdf-form-fields.tsx).
- Locale:
- [web/src/locales/en.ts](../../../web/src/locales/en.ts)
- [web/src/locales/vi.ts](../../../web/src/locales/vi.ts)

## Sơ đồ mã nguồn (source map)

```text
UI (Dataset/Agent Forms)
  -> layout-recognize-form-field.tsx
  -> doxa-options-form-field.tsx
  -> parser-form/pdf-form-fields.tsx
      -> parser_config / setups.pdf config

Backend runtime
  Lane A (Traditional): rag/app/naive.py -> by_doxa -> deepdoc/parser/doxa_parser.py
  Lane B (Dataflow):    rag/flow/parser/parser.py -> doxa branch -> deepdoc/parser/doxa_parser.py

Adapter
  deepdoc/parser/doxa_parser.py
    -> check_installation
    -> parse_pdf (DoXA SDK)
    -> normalize output

Tests
  test/unit_test/deepdoc/parser/test_doxa_parser.py
  test/unit_test/common/test_parser_config_utils.py
  test/unit_test/rag/test_doxa_lane_wiring.py
```

## Giải thích chi tiết từng nhóm thay đổi

### Backend

- [deepdoc/parser/doxa_parser.py](../../../deepdoc/parser/doxa_parser.py): tạo adapter DoXA, chuẩn hóa output, bảo vệ lỗi cấu hình/dependency.
- [rag/app/naive.py](../../../rag/app/naive.py): thêm entrypoint by_doxa và map parser doxa cho ingest truyền thống.
- [rag/flow/parser/parser.py](../../../rag/flow/parser/parser.py): thêm validate parse_method doxa và nhánh chạy parser DoXA cho node PDF.
- [common/parser_config_utils.py](../../../common/parser_config_utils.py): normalize alias model@doxa -> DoXA.

### Frontend

- [web/src/components/layout-recognize-form-field.tsx](../../../web/src/components/layout-recognize-form-field.tsx): thêm lựa chọn DoXA và gắn DoXA options.
- [web/src/components/doxa-options-form-field.tsx](../../../web/src/components/doxa-options-form-field.tsx): form cấu hình URL/token/iPaaS token.
- [web/src/pages/agent/form/parser-form/pdf-form-fields.tsx](../../../web/src/pages/agent/form/parser-form/pdf-form-fields.tsx): hiển thị field DoXA riêng cho pipeline parser node.
- [web/src/locales/en.ts](../../../web/src/locales/en.ts), [web/src/locales/vi.ts](../../../web/src/locales/vi.ts): bổ sung key dịch cho nhãn/tooltip DoXA.

### Test

- [test/unit_test/deepdoc/parser/test_doxa_parser.py](../../../test/unit_test/deepdoc/parser/test_doxa_parser.py): test adapter DoXA và normalize output.
- [test/unit_test/common/test_parser_config_utils.py](../../../test/unit_test/common/test_parser_config_utils.py): test normalize alias @doxa.
- [test/unit_test/rag/test_doxa_lane_wiring.py](../../../test/unit_test/rag/test_doxa_lane_wiring.py): test wiring cho 2 lane bằng kiểm tra source/AST.

## Trạng thái hoàn tất

- Plan tích hợp đã được đánh dấu hoàn tất tại [05-doxa-parser-integration-plan.md](./05-doxa-parser-integration-plan.md).
- Contract + cấu hình đã có ở [06-doxa-contract-and-config.md](./06-doxa-contract-and-config.md).
- Vận hành + xử lý sự cố đã có ở [07-doxa-deploy-and-runbook.md](./07-doxa-deploy-and-runbook.md).

## Phần trọng tâm: DeepDOC

- [DeepDOC - Tổng quan](./deepdoc/01-deepdoc-overview.md)
- [DeepDOC - PDF parser chi tiết](./deepdoc/02-deepdoc-pdf-parser.md)
- [DeepDOC - Parser các định dạng khác](./deepdoc/03-deepdoc-file-parsers.md)
- [DeepDOC - Điểm mở rộng và tích hợp parser mới](./deepdoc/04-deepdoc-extensibility.md)

---

## Phạm vi mã nguồn đã đọc

Các cụm file chính:

- `deepdoc/parser/*`
- `rag/app/naive.py`
- `rag/svr/task_executor.py`
- `api/utils/api_utils.py`
- `common/constants.py`
- `common/parser_config_utils.py`
- `api/utils/validation_utils.py`
- `web/src/components/layout-recognize-form-field.tsx`
- `web/src/pages/dataset/dataset-setting/*`

---

## Ghi chú

- Tài liệu dùng thuật ngữ "parser" theo 2 lớp:
  - **Parser nghiệp vụ/chunk method** (`parser_id`: naive, qa, table...)
  - **Parser định dạng tài liệu** (PDF/DOCX/Excel/Markdown...) trong `deepdoc/parser`
- Trong thực tế ingest tài liệu, 2 lớp này phối hợp với nhau, không tách rời.
