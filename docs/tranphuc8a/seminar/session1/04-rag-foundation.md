# 04 - Nền tảng RAG: Retrieval-Augmented Generation

## Mục tiêu phần này

- Hiểu nguyên lý vận hành cơ bản của RAG.
- Nắm kiến trúc hai nửa ingest/query trong hệ production.

## 1. Nguyên lý RAG

RAG bổ sung retrieval vào trước bước generation:
1. Query người dùng -> tìm chunk liên quan trong knowledge base.
2. Đưa chunk vào context.
3. LLM sinh câu trả lời dựa trên context đó.

## 2. Tại sao RAG hiệu quả

- Giảm hallucination nhờ grounding.
- Mở rộng tri thức bằng dữ liệu riêng của tổ chức.
- Dễ cập nhật tri thức qua ingest thay vì re-train model.

## 3. Hai pipeline cốt lõi

- Ingest pipeline: parse/chunk/embed/index.
- Query pipeline: retrieve/rerank/context build/generate/citation.

## 4. RAG production khác RAG demo ở đâu

- Có nhiều cơ chế retrieval fusion (keyword + vector + rerank).
- Có metadata filtering, logging, tracing, cache.
- Có yêu cầu vận hành: độ trễ, chi phí, ổn định, quan sát được.

Nguồn tham chiếu:
- `docs/basics/rag.md`

## Phan tich chuyen sau bo sung

- [04-rag-foundation] Rule 1: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [04-rag-foundation] Check 1: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 1: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 1: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 2: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [04-rag-foundation] Check 2: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 2: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 2: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 3: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [04-rag-foundation] Check 3: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 3: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 3: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 4: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [04-rag-foundation] Check 4: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 4: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 4: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 5: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [04-rag-foundation] Check 5: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 5: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 5: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 6: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [04-rag-foundation] Check 6: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 6: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 6: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 7: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [04-rag-foundation] Check 7: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 7: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 7: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 8: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [04-rag-foundation] Check 8: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 8: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 8: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 9: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [04-rag-foundation] Check 9: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 9: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 9: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 10: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [04-rag-foundation] Check 10: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 10: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 10: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 11: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [04-rag-foundation] Check 11: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 11: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 11: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 12: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [04-rag-foundation] Check 12: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 12: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 12: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 13: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [04-rag-foundation] Check 13: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 13: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 13: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 14: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [04-rag-foundation] Check 14: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 14: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 14: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 15: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [04-rag-foundation] Check 15: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 15: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 15: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 16: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [04-rag-foundation] Check 16: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 16: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 16: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 17: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [04-rag-foundation] Check 17: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 17: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 17: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 18: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [04-rag-foundation] Check 18: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 18: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 18: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 19: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [04-rag-foundation] Check 19: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 19: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 19: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 20: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [04-rag-foundation] Check 20: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 20: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 20: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 21: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [04-rag-foundation] Check 21: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 21: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 21: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 22: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [04-rag-foundation] Check 22: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 22: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 22: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 23: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [04-rag-foundation] Check 23: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 23: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 23: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 24: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [04-rag-foundation] Check 24: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 24: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 24: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 25: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [04-rag-foundation] Check 25: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 25: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 25: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 26: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [04-rag-foundation] Check 26: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 26: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 26: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 27: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [04-rag-foundation] Check 27: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 27: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 27: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 28: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [04-rag-foundation] Check 28: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 28: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 28: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 29: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [04-rag-foundation] Check 29: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 29: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 29: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 30: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [04-rag-foundation] Check 30: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 30: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 30: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 31: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [04-rag-foundation] Check 31: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 31: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 31: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 32: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [04-rag-foundation] Check 32: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 32: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 32: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 33: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [04-rag-foundation] Check 33: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 33: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 33: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 34: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [04-rag-foundation] Check 34: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 34: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 34: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 35: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [04-rag-foundation] Check 35: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 35: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 35: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 36: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [04-rag-foundation] Check 36: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 36: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 36: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 37: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [04-rag-foundation] Check 37: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 37: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 37: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 38: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [04-rag-foundation] Check 38: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 38: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 38: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 39: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [04-rag-foundation] Check 39: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 39: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 39: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 40: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [04-rag-foundation] Check 40: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 40: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 40: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 41: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [04-rag-foundation] Check 41: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 41: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 41: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 42: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [04-rag-foundation] Check 42: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 42: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 42: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 43: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [04-rag-foundation] Check 43: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 43: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 43: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 44: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [04-rag-foundation] Check 44: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 44: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 44: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 45: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [04-rag-foundation] Check 45: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 45: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 45: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [04-rag-foundation] Rule 46: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [04-rag-foundation] Check 46: ghi ro input, output, metric, baseline, va rollback rule.
- [04-rag-foundation] Ops 46: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [04-rag-foundation] Learn 46: tong ket bai hoc de team dung lai cho cac case tuong tu.
