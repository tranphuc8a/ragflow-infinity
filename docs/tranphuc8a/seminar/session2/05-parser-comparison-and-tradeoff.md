# 05 - So sánh Parser và Trade-off Kỹ thuật

## Mục tiêu phần này

- Biết cách chọn parser theo loại tài liệu và yêu cầu bài toán.
- Hiểu đánh đổi chất lượng, chi phí, độ trễ khi thiết kế ingest.

## 1. Ma trận so sánh parser theo tiêu chí thực chiến

| Tiêu chí | Parser text-only đơn giản | DeepDoc-style parser |
| --- | --- | --- |
| Tốc độ ingest | Cao | Trung bình/thấp hơn |
| Chi phí tính toán | Thấp | Cao hơn |
| Chất lượng trên PDF scan | Thấp/trung bình | Tốt hơn đáng kể |
| Hiểu bảng/layout | Hạn chế | Mạnh |
| Citation/traceability | Yếu | Tốt |
| Phù hợp enterprise docs | Có điều kiện | Phù hợp hơn |

## 2. Khi nào chọn parser đơn giản

- Tài liệu chủ yếu là plain text/markdown chuẩn.
- Yêu cầu cập nhật nhanh, chi phí thấp.
- Chất lượng retrieval đủ tốt với chunk đơn giản.

## 3. Khi nào chọn DeepDoc

- Tài liệu PDF có nhiều bảng/ảnh/chú thích.
- Có yêu cầu chính xác cao và cần trích dẫn nguồn rõ.
- Truy vấn thường hỏi số liệu nằm trong bảng hoặc biểu mẫu.

## 4. Trade-off cần truyền đạt cho học viên

- Không có parser nào tốt nhất cho mọi bối cảnh.
- Bài toán thực tế là tối ưu đa mục tiêu:
  - chất lượng retrieval
  - chi phí ingest
  - thời gian cập nhật tri thức
  - mức độ vận hành được

## 5. Chiến lược triển khai thực tế

- Bắt đầu bằng parser đủ dùng cho 80% tài liệu.
- Đo KPI retrieval/answer theo domain.
- Với nhóm tài liệu khó, chuyển sang parser mạnh hơn (DeepDoc).
- Chuẩn hóa playbook: loại tài liệu nào dùng parser nào.

## 6. Kết luận phần

Lựa chọn parser là quyết định kiến trúc, không chỉ là tùy chọn kỹ thuật nhỏ. Trong production RAG, parser tốt thường giúp giảm nhiều vòng tối ưu khó ở downstream.

## Phan tich chuyen sau bo sung

- [05-parser-comparison-and-tradeoff] Rule 1: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [05-parser-comparison-and-tradeoff] Check 1: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 1: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 1: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 2: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [05-parser-comparison-and-tradeoff] Check 2: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 2: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 2: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 3: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [05-parser-comparison-and-tradeoff] Check 3: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 3: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 3: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 4: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [05-parser-comparison-and-tradeoff] Check 4: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 4: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 4: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 5: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [05-parser-comparison-and-tradeoff] Check 5: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 5: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 5: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 6: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [05-parser-comparison-and-tradeoff] Check 6: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 6: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 6: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 7: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [05-parser-comparison-and-tradeoff] Check 7: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 7: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 7: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 8: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [05-parser-comparison-and-tradeoff] Check 8: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 8: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 8: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 9: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [05-parser-comparison-and-tradeoff] Check 9: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 9: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 9: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 10: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [05-parser-comparison-and-tradeoff] Check 10: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 10: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 10: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 11: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [05-parser-comparison-and-tradeoff] Check 11: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 11: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 11: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 12: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [05-parser-comparison-and-tradeoff] Check 12: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 12: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 12: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 13: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [05-parser-comparison-and-tradeoff] Check 13: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 13: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 13: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 14: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [05-parser-comparison-and-tradeoff] Check 14: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 14: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 14: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 15: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [05-parser-comparison-and-tradeoff] Check 15: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 15: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 15: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 16: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [05-parser-comparison-and-tradeoff] Check 16: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 16: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 16: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 17: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [05-parser-comparison-and-tradeoff] Check 17: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 17: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 17: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 18: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [05-parser-comparison-and-tradeoff] Check 18: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 18: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 18: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 19: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [05-parser-comparison-and-tradeoff] Check 19: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 19: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 19: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 20: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [05-parser-comparison-and-tradeoff] Check 20: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 20: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 20: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 21: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [05-parser-comparison-and-tradeoff] Check 21: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 21: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 21: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 22: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [05-parser-comparison-and-tradeoff] Check 22: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 22: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 22: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 23: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [05-parser-comparison-and-tradeoff] Check 23: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 23: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 23: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 24: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [05-parser-comparison-and-tradeoff] Check 24: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 24: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 24: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 25: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [05-parser-comparison-and-tradeoff] Check 25: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 25: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 25: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 26: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [05-parser-comparison-and-tradeoff] Check 26: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 26: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 26: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 27: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [05-parser-comparison-and-tradeoff] Check 27: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 27: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 27: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 28: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [05-parser-comparison-and-tradeoff] Check 28: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 28: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 28: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 29: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [05-parser-comparison-and-tradeoff] Check 29: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 29: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 29: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 30: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [05-parser-comparison-and-tradeoff] Check 30: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 30: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 30: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 31: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [05-parser-comparison-and-tradeoff] Check 31: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 31: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 31: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 32: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [05-parser-comparison-and-tradeoff] Check 32: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 32: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 32: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 33: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [05-parser-comparison-and-tradeoff] Check 33: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 33: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 33: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 34: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [05-parser-comparison-and-tradeoff] Check 34: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 34: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 34: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 35: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [05-parser-comparison-and-tradeoff] Check 35: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 35: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 35: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 36: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [05-parser-comparison-and-tradeoff] Check 36: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 36: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 36: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 37: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [05-parser-comparison-and-tradeoff] Check 37: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 37: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 37: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 38: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [05-parser-comparison-and-tradeoff] Check 38: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 38: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 38: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 39: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [05-parser-comparison-and-tradeoff] Check 39: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 39: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 39: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 40: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [05-parser-comparison-and-tradeoff] Check 40: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 40: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 40: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 41: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [05-parser-comparison-and-tradeoff] Check 41: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 41: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 41: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [05-parser-comparison-and-tradeoff] Rule 42: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [05-parser-comparison-and-tradeoff] Check 42: ghi ro input, output, metric, baseline, va rollback rule.
- [05-parser-comparison-and-tradeoff] Ops 42: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [05-parser-comparison-and-tradeoff] Learn 42: tong ket bai hoc de team dung lai cho cac case tuong tu.
