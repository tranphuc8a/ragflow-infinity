# Ke hoach chi tiet tich hop DoXA Parser vao RAGFlow

## 1) Muc tieu

- Them DoXA Parser thanh mot lua chon parser moi trong RAGFlow.
- Dam bao hoat dong dong nhat tren ca 2 luong ingest:
  - Luong chunk_method truyen thong.
  - Luong Ingestion Pipeline (Canvas/Dataflow).
- Dam bao fallback an toan khi thieu token, thieu dependency, hoac loi ket noi DoXA.
- Han che anh huong den cac parser hien co (DeepDOC, MinerU, Docling, TCADP, PaddleOCR).

## 2) Pham vi va khong pham vi

### 2.1 Pham vi

- Tich hop backend parser adapter cho DoXA.
- Noi adapter vao 2 duong parser runtime:
  - rag/app/naive.py (traditional ingest)
  - rag/flow/parser/parser.py (dataflow ingest)
- Bo sung tuy chon parser trong UI cho Dataset va Canvas.
- Bo sung cau hinh, tai lieu van hanh, test va rollout checklist.

### 2.2 Khong pham vi

- Khong thay doi chien luoc chunk_method tong quat (naive, qa, table, ...).
- Khong doi schema DB parser_id hien tai trong phase 1.
- Khong thuc hien toi uu hieu nang nang cao cho DoXA o phase dau.

## 3) Kien truc hien tai can dong bo

### 3.1 Lane A: Traditional ingest

- Parser chinh theo parser_id/chunk_method va parser_config.
- Nhung diem mo rong chinh:
  - rag/svr/task_executor.py
  - rag/app/naive.py
  - common/parser_config_utils.py
  - api/utils/api_utils.py
  - api/apps/sdk/doc.py

### 3.2 Lane B: Ingestion Pipeline (Canvas/Dataflow)

- Parser node co cau hinh parse_method rieng theo file type.
- Nhung diem mo rong chinh:
  - rag/flow/parser/parser.py
  - web/src/pages/agent/form/parser-form/*
  - web/src/components/layout-recognize-form-field.tsx

### 3.3 Nguyen tac tich hop

- Mot adapter DoXA dung chung cho ca 2 lane.
- Mot mapping output chuan (sections, tables, positions, image) de tiep tuc pipeline hien co.
- Cung mot cach xu ly loi va fallback tren ca 2 lane.

## 4) Thiet ke ky thuat de xuat

## 4.1 Tao adapter backend cho DoXA

- Tao file moi: deepdoc/parser/doxa_parser.py
- Cac ham can co:
  - check_installation()
  - parse_pdf(filepath, binary, callback, parse_method, lang, ...)
  - crop(...) neu can cho extraction vi tri/hinh anh
  - extract_positions(...) neu output DoXA co position tag
- Dau vao:
  - binary hoac filepath
  - token/base_url/timeout/retry
  - tuy chon parser method cua DoXA neu co
- Dau ra can map ve format ma he thong dang dung:
  - sections: danh sach doan text va thong tin vi tri
  - tables: danh sach bang

## 4.2 Cau hinh va bao mat

- Bo sung bien moi truong (de xac nhan voi team truoc khi chot ten):
  - DOXA_API_BASE
  - DOXA_API_TOKEN
  - DOXA_TIMEOUT_SEC
  - DOXA_MAX_RETRY
- Khong log token.
- Loi auth/ket noi phai duoc thong bao ro trong progress callback.

## 4.3 Tich hop vao Lane A (traditional)

- File: rag/app/naive.py
  - Them ham by_doxa(...)
  - Dang ky PARSERS them key doxa
  - Ho tro parser_config.layout_recognize = DoXA
- File: common/parser_config_utils.py
  - Bo sung normalize alias cho doxa neu can pattern model@doxa
- File: api/utils/api_utils.py
  - Xem xet default parser_config cho naive khi chon DoXA
- File: api/apps/sdk/doc.py
  - Neu co danh sach valid chunk_method/parse option can bo sung tuong thich

## 4.4 Tich hop vao Lane B (dataflow)

- File: rag/flow/parser/parser.py
  - Bo sung parse_method doxa trong _pdf
  - Bo sung validate parse_method trong ParserParam.check
  - Dam bao output format json/markdown van dung
- File: web/src/components/layout-recognize-form-field.tsx
  - Bo sung option DoXA vao ParseDocumentType hoac optionsWithoutLLM
- File: web/src/pages/agent/form/parser-form/*
  - Dam bao ParserMethodFormField hien DoXA cho PDF
  - Neu can thi bo sung tuy chon phu cua DoXA

## 4.5 Dong bo UX va tooltip

- Tach noi dung tooltip parser method theo context:
  - Dataset config
  - Canvas parser node
- Tranh thong diep gay hieu nham "chi hoat dong voi PDF" cho cac file type khac trong Canvas.

## 5) Danh sach thay doi theo file

### 5.1 Backend

- Them moi:
  - deepdoc/parser/doxa_parser.py
- Chinh sua:
  - rag/app/naive.py
  - rag/flow/parser/parser.py
  - common/parser_config_utils.py
  - api/utils/api_utils.py (neu can)
  - api/apps/sdk/doc.py (neu can)

### 5.2 Frontend

- Chinh sua:
  - web/src/components/layout-recognize-form-field.tsx
  - web/src/pages/agent/form/parser-form/common-form-fields.tsx
  - web/src/pages/agent/form/parser-form/pdf-form-fields.tsx
  - web/src/locales/en.ts
  - cac locale khac theo chinh sach i18n

### 5.3 Docs

- Chinh sua/bo sung:
  - docs huong dan deploy parser
  - docs huong dan su dung parser trong Dataset va Canvas
  - runbook su co DoXA

## 6) Ke hoach implement theo giai doan

## Giai doan 0: Spike va chot contract

- Muc tieu: xac minh API DoXA parser va output schema.
- Dau ra:
  - bang mapping output DoXA -> output chuan RAGFlow
  - danh sach tham so bat buoc/tuy chon

## Giai doan 1: Adapter va unit test co lap

- Implement deepdoc/parser/doxa_parser.py
- Viet unit test parser adapter:
  - parse thanh cong
  - loi auth
  - timeout va retry
  - output rong

## Giai doan 2: Noi vao Lane A

- Them by_doxa trong rag/app/naive.py
- Dang ky parser doxa trong PARSERS
- Test ingest file PDF theo chunk_method naive + layout_recognize DoXA

## Giai doan 3: Noi vao Lane B

- Them doxa trong rag/flow/parser/parser.py cho parse_method
- Cap nhat UI parser method trong Canvas
- Test chay Ingestion Pipeline co Parser node = DoXA

## Giai doan 4: UX, i18n, docs

- Sua tooltip parser method theo ngu canh
- Dong bo locale
- Them tai lieu van hanh

## Giai doan 5: Hardening va rollout

- Chay regression test parser cu
- Theo doi metric loi/thoi gian parse
- Bat feature flag neu can

## 7) Test matrix bat buoc

### 7.1 Unit test

- Chon parser dung theo config:
  - Lane A: layout_recognize = DoXA
  - Lane B: parse_method = doxa
- Mapping output dung schema tokenize.
- Fallback khi DoXA unavailable.

### 7.2 Integration test

- Traditional ingest:
  - upload file -> parse -> chunk -> index
- Dataflow ingest:
  - pipeline parser node -> tokenizer -> splitter -> extractor
- So sanh output voi parser hien co tren bo file mau.

### 7.3 Regression

- DeepDOC/MinerU/Docling/TCADP/PaddleOCR khong bi anh huong.
- Khoi tao dataset/document cu khong bi loi config.

## 8) Rui ro va giam thieu

- Rui ro private dependency/khong cai duoc DoXA SDK:
  - Giai phap: optional import + thong bao cai dat ro rang.
- Rui ro sai khac output schema:
  - Giai phap: adapter normalize duy nhat + test mapping.
- Rui ro do tre do parser ngoai:
  - Giai phap: timeout/retry + callback tien do.
- Rui ro UX hieu nham parser scope:
  - Giai phap: tach tooltip theo context.

## 9) Tieu chi hoan thanh (Definition of Done)

- User co the chon DoXA parser trong:
  - Dataset parser config (lane A)
  - Canvas parser node (lane B)
- Parse PDF thanh cong end-to-end o ca 2 lane.
- Khong vo parser cu.
- Co test tu dong cho parser selection + parse flow.
- Co tai lieu van hanh va su co.

## 10) Ke hoach cong viec de implement

- [x] Chot contract API DoXA parser va output schema
- [x] Tao adapter deepdoc/parser/doxa_parser.py
- [x] Noi adapter vao rag/app/naive.py
- [x] Noi adapter vao rag/flow/parser/parser.py
- [x] Cap nhat normalize parser config cho doxa
- [x] Cap nhat UI parser method (Dataset + Canvas)
- [x] Cap nhat tooltip/locale theo context
- [x] Viet unit test
- [x] Viet integration test
- [x] Cap nhat docs
- [x] Chay regression va chuan bi rollout

## 11) Goi y branch va commit strategy

- PR 1: Adapter + lane A backend + test co ban
- PR 2: Lane B backend + frontend parser option + i18n
- PR 3: Hardening, docs, regression fixes

Cach chia nay giup review de hon va rollback nhanh hon neu can.
