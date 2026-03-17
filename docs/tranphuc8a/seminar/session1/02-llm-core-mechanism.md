# 02 - Cơ chế hoạt động cốt lõi của LLM

## Mục tiêu phần này

- Hiểu đúng bản chất "mô hình sinh xác suất" của LLM.
- Giải thích được vì sao cùng một câu hỏi có thể sinh câu trả lời khác nhau.

## 1. Quy trình sinh văn bản cơ bản

1. Tokenization: chuyển văn bản thành token.
2. Encoding theo transformer layers.
3. Dự đoán xác suất token kế tiếp.
4. Sampling theo chiến lược (temperature, top_p...).
5. Lặp lại đến khi dừng.

## 2. Hệ quả quan trọng cho production

- LLM không truy vấn sự thật như DB.
- LLM sinh câu dựa trên xác suất phù hợp ngữ cảnh.
- Tính đúng sai phụ thuộc mạnh vào context được cấp.

## 3. Ảnh hưởng của tham số sinh

- `temperature` cao: đa dạng hơn nhưng rủi ro nhiễu cao hơn.
- `temperature` thấp: ổn định hơn nhưng dễ cứng và thiếu linh hoạt.
- `max_tokens`: ảnh hưởng độ dài và chi phí.

## 4. Ý nghĩa cho thiết kế RAG

Vì LLM là bộ sinh xác suất, hệ thống cần:
- Cấp context đáng tin cậy.
- Ràng buộc nhiệm vụ rõ ràng trong system prompt.
- Có cơ chế trích dẫn/chứng cứ để kiểm chứng.

## Phan tich chuyen sau bo sung

- [02-llm-core-mechanism] Rule 1: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [02-llm-core-mechanism] Check 1: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 1: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 1: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 2: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [02-llm-core-mechanism] Check 2: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 2: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 2: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 3: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [02-llm-core-mechanism] Check 3: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 3: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 3: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 4: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [02-llm-core-mechanism] Check 4: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 4: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 4: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 5: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [02-llm-core-mechanism] Check 5: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 5: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 5: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 6: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [02-llm-core-mechanism] Check 6: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 6: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 6: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 7: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [02-llm-core-mechanism] Check 7: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 7: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 7: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 8: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [02-llm-core-mechanism] Check 8: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 8: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 8: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 9: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [02-llm-core-mechanism] Check 9: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 9: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 9: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 10: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [02-llm-core-mechanism] Check 10: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 10: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 10: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 11: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [02-llm-core-mechanism] Check 11: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 11: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 11: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 12: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [02-llm-core-mechanism] Check 12: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 12: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 12: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 13: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [02-llm-core-mechanism] Check 13: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 13: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 13: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 14: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [02-llm-core-mechanism] Check 14: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 14: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 14: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 15: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [02-llm-core-mechanism] Check 15: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 15: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 15: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 16: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [02-llm-core-mechanism] Check 16: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 16: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 16: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 17: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [02-llm-core-mechanism] Check 17: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 17: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 17: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 18: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [02-llm-core-mechanism] Check 18: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 18: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 18: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 19: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [02-llm-core-mechanism] Check 19: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 19: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 19: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 20: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [02-llm-core-mechanism] Check 20: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 20: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 20: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 21: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [02-llm-core-mechanism] Check 21: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 21: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 21: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 22: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [02-llm-core-mechanism] Check 22: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 22: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 22: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 23: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [02-llm-core-mechanism] Check 23: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 23: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 23: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 24: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [02-llm-core-mechanism] Check 24: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 24: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 24: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 25: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [02-llm-core-mechanism] Check 25: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 25: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 25: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 26: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [02-llm-core-mechanism] Check 26: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 26: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 26: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 27: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [02-llm-core-mechanism] Check 27: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 27: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 27: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 28: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [02-llm-core-mechanism] Check 28: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 28: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 28: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 29: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [02-llm-core-mechanism] Check 29: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 29: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 29: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 30: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [02-llm-core-mechanism] Check 30: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 30: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 30: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 31: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [02-llm-core-mechanism] Check 31: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 31: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 31: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 32: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [02-llm-core-mechanism] Check 32: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 32: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 32: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 33: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [02-llm-core-mechanism] Check 33: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 33: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 33: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 34: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [02-llm-core-mechanism] Check 34: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 34: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 34: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 35: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [02-llm-core-mechanism] Check 35: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 35: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 35: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 36: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [02-llm-core-mechanism] Check 36: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 36: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 36: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 37: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [02-llm-core-mechanism] Check 37: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 37: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 37: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 38: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [02-llm-core-mechanism] Check 38: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 38: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 38: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 39: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [02-llm-core-mechanism] Check 39: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 39: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 39: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 40: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [02-llm-core-mechanism] Check 40: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 40: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 40: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 41: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [02-llm-core-mechanism] Check 41: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 41: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 41: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 42: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [02-llm-core-mechanism] Check 42: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 42: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 42: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 43: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [02-llm-core-mechanism] Check 43: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 43: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 43: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 44: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [02-llm-core-mechanism] Check 44: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 44: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 44: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 45: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [02-llm-core-mechanism] Check 45: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 45: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 45: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [02-llm-core-mechanism] Rule 46: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [02-llm-core-mechanism] Check 46: ghi ro input, output, metric, baseline, va rollback rule.
- [02-llm-core-mechanism] Ops 46: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [02-llm-core-mechanism] Learn 46: tong ket bai hoc de team dung lai cho cac case tuong tu.
