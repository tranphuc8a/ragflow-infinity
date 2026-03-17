# 05 - RAGFlow triển khai Chunking/Embedding/Retrieval như thế nào

## 1. Khối chunking

- Cấu hình parser/chunk từ `api/utils/api_utils.py`.
- Xử lý chunk trong `rag/svr/task_executor.py`.

## 2. Khối embedding

- Encode theo batch trong `embedding(...)`.
- Gán vector theo dimension field.

## 3. Khối retrieval liên quan

- `rag/nlp/search.py` thực hiện tìm kiếm vector + term.
- Có cơ chế rerank/rerank_by_model.

```mermaid
flowchart LR
    P[Parsed units] --> C[Chunking]
    C --> E[Embedding]
    E --> V[(Vector index)]
    Q[Query] --> R[Hybrid retrieval]
    V --> R
    R --> N[Top-N context]
```

## 4. Kết luận

RAGFlow hiện thực đúng tinh thần production: retrieval là tổ hợp nhiều kỹ thuật, không phụ thuộc một thuật toán đơn lẻ.

## Phan tich chuyen sau bo sung

- [05-ragflow-implementation] Rule 1: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [05-ragflow-implementation] Check 1: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 1: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 1: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 2: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [05-ragflow-implementation] Check 2: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 2: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 2: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 3: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [05-ragflow-implementation] Check 3: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 3: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 3: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 4: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [05-ragflow-implementation] Check 4: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 4: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 4: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 5: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [05-ragflow-implementation] Check 5: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 5: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 5: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 6: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [05-ragflow-implementation] Check 6: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 6: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 6: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 7: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [05-ragflow-implementation] Check 7: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 7: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 7: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 8: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [05-ragflow-implementation] Check 8: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 8: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 8: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 9: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [05-ragflow-implementation] Check 9: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 9: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 9: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 10: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [05-ragflow-implementation] Check 10: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 10: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 10: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 11: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [05-ragflow-implementation] Check 11: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 11: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 11: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 12: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [05-ragflow-implementation] Check 12: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 12: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 12: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 13: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [05-ragflow-implementation] Check 13: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 13: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 13: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 14: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [05-ragflow-implementation] Check 14: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 14: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 14: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 15: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [05-ragflow-implementation] Check 15: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 15: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 15: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 16: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [05-ragflow-implementation] Check 16: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 16: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 16: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 17: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [05-ragflow-implementation] Check 17: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 17: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 17: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 18: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [05-ragflow-implementation] Check 18: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 18: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 18: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 19: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [05-ragflow-implementation] Check 19: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 19: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 19: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 20: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [05-ragflow-implementation] Check 20: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 20: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 20: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 21: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [05-ragflow-implementation] Check 21: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 21: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 21: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 22: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [05-ragflow-implementation] Check 22: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 22: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 22: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 23: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [05-ragflow-implementation] Check 23: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 23: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 23: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 24: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [05-ragflow-implementation] Check 24: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 24: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 24: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 25: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [05-ragflow-implementation] Check 25: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 25: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 25: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 26: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [05-ragflow-implementation] Check 26: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 26: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 26: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 27: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [05-ragflow-implementation] Check 27: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 27: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 27: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 28: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [05-ragflow-implementation] Check 28: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 28: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 28: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 29: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [05-ragflow-implementation] Check 29: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 29: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 29: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 30: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [05-ragflow-implementation] Check 30: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 30: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 30: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 31: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [05-ragflow-implementation] Check 31: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 31: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 31: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 32: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [05-ragflow-implementation] Check 32: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 32: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 32: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 33: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [05-ragflow-implementation] Check 33: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 33: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 33: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 34: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [05-ragflow-implementation] Check 34: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 34: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 34: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 35: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [05-ragflow-implementation] Check 35: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 35: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 35: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 36: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [05-ragflow-implementation] Check 36: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 36: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 36: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 37: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [05-ragflow-implementation] Check 37: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 37: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 37: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 38: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [05-ragflow-implementation] Check 38: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 38: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 38: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 39: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [05-ragflow-implementation] Check 39: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 39: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 39: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 40: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [05-ragflow-implementation] Check 40: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 40: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 40: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 41: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [05-ragflow-implementation] Check 41: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 41: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 41: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 42: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [05-ragflow-implementation] Check 42: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 42: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 42: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 43: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [05-ragflow-implementation] Check 43: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 43: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 43: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 44: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [05-ragflow-implementation] Check 44: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 44: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 44: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 45: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [05-ragflow-implementation] Check 45: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 45: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 45: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 46: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [05-ragflow-implementation] Check 46: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 46: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 46: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-ragflow-implementation] Rule 47: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [05-ragflow-implementation] Check 47: ghi ro input, output, metric, baseline, va rollback rule.
- [05-ragflow-implementation] Ops 47: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-ragflow-implementation] Learn 47: tong ket bai hoc de team dung lai cho cac case tuong tu.
