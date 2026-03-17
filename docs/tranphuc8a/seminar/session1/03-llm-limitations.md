# 03 - Giới hạn của LLM và vì sao phải có RAG

## Mục tiêu phần này

- Nhận diện đúng các giới hạn kỹ thuật của LLM thuần.
- Liên hệ trực tiếp giới hạn đó với nhu cầu xây dựng RAGFlow.

## 1. Hallucination

- Mô hình có thể tạo câu trôi chảy nhưng sai sự thật.
- Đặc biệt nguy hiểm ở môi trường enterprise cần tính chính xác cao.

## 2. Knowledge cutoff

- Kiến thức của mô hình bị giới hạn theo thời điểm huấn luyện.
- Không tự cập nhật tài liệu nội bộ nếu không có cơ chế retrieval.

## 3. Context window giới hạn

- Không thể nạp "toàn bộ kho tri thức" vào một prompt.
- Cần chọn lọc context liên quan nhất trước khi sinh câu trả lời.

## 4. Thiếu grounding mặc định

- Nếu không được nối với nguồn dữ liệu thật, model không có cơ sở chứng cứ.
- Câu trả lời khó audit và khó giải trình.

## 5. Kết luận phần

Giới hạn của LLM không phải lỗi triển khai riêng của một dự án, mà là bản chất của mô hình sinh. RAG là kiến trúc hệ thống để giảm các rủi ro này.

## Phan tich chuyen sau bo sung

- [03-llm-limitations] Rule 1: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [03-llm-limitations] Check 1: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 1: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 1: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 2: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [03-llm-limitations] Check 2: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 2: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 2: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 3: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [03-llm-limitations] Check 3: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 3: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 3: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 4: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [03-llm-limitations] Check 4: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 4: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 4: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 5: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [03-llm-limitations] Check 5: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 5: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 5: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 6: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [03-llm-limitations] Check 6: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 6: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 6: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 7: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [03-llm-limitations] Check 7: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 7: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 7: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 8: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [03-llm-limitations] Check 8: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 8: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 8: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 9: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [03-llm-limitations] Check 9: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 9: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 9: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 10: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [03-llm-limitations] Check 10: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 10: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 10: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 11: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [03-llm-limitations] Check 11: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 11: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 11: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 12: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [03-llm-limitations] Check 12: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 12: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 12: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 13: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [03-llm-limitations] Check 13: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 13: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 13: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 14: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [03-llm-limitations] Check 14: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 14: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 14: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 15: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [03-llm-limitations] Check 15: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 15: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 15: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 16: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [03-llm-limitations] Check 16: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 16: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 16: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 17: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [03-llm-limitations] Check 17: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 17: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 17: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 18: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [03-llm-limitations] Check 18: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 18: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 18: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 19: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [03-llm-limitations] Check 19: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 19: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 19: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 20: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [03-llm-limitations] Check 20: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 20: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 20: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 21: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [03-llm-limitations] Check 21: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 21: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 21: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 22: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [03-llm-limitations] Check 22: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 22: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 22: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 23: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [03-llm-limitations] Check 23: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 23: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 23: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 24: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [03-llm-limitations] Check 24: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 24: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 24: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 25: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [03-llm-limitations] Check 25: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 25: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 25: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 26: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [03-llm-limitations] Check 26: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 26: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 26: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 27: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [03-llm-limitations] Check 27: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 27: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 27: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 28: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [03-llm-limitations] Check 28: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 28: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 28: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 29: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [03-llm-limitations] Check 29: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 29: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 29: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 30: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [03-llm-limitations] Check 30: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 30: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 30: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 31: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [03-llm-limitations] Check 31: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 31: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 31: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 32: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [03-llm-limitations] Check 32: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 32: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 32: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 33: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [03-llm-limitations] Check 33: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 33: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 33: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 34: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [03-llm-limitations] Check 34: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 34: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 34: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 35: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [03-llm-limitations] Check 35: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 35: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 35: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 36: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [03-llm-limitations] Check 36: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 36: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 36: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 37: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [03-llm-limitations] Check 37: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 37: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 37: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 38: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [03-llm-limitations] Check 38: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 38: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 38: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 39: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [03-llm-limitations] Check 39: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 39: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 39: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 40: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [03-llm-limitations] Check 40: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 40: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 40: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 41: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [03-llm-limitations] Check 41: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 41: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 41: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 42: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [03-llm-limitations] Check 42: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 42: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 42: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 43: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [03-llm-limitations] Check 43: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 43: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 43: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 44: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [03-llm-limitations] Check 44: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 44: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 44: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 45: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [03-llm-limitations] Check 45: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 45: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 45: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 46: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [03-llm-limitations] Check 46: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 46: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 46: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [03-llm-limitations] Rule 47: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [03-llm-limitations] Check 47: ghi ro input, output, metric, baseline, va rollback rule.
- [03-llm-limitations] Ops 47: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [03-llm-limitations] Learn 47: tong ket bai hoc de team dung lai cho cac case tuong tu.
