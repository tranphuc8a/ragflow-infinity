# 06 - Demo Suggestion, Checklist Quan sát và Key Takeaways

## Mục tiêu phần này

- Có kịch bản demo cụ thể để đội mới nhìn thấy tác động của parser/ingest.
- Có checklist đo lường để demo không chỉ dừng ở "cảm giác".

## 1. Kịch bản demo đề xuất (40-50 phút)

## 1.1 Chuẩn bị dữ liệu

- Dataset A: PDF text thuần.
- Dataset B: PDF scan có bảng và bố cục phức tạp.
- Cả hai dataset dùng cùng embedding model để so sánh công bằng.

## 1.2 Các bước chạy demo

1. Upload tài liệu vào dataset.
2. Chạy parse/ingest hoàn chỉnh.
3. Mở chunk preview để quan sát chất lượng phân mảnh.
4. Chạy nhóm câu hỏi:
   - Câu hỏi fact có số liệu trong bảng.
   - Câu hỏi semantic paraphrase.
   - Câu hỏi cần nối nhiều đoạn trong tài liệu.
5. So sánh kết quả giữa dataset/parser profile.

## 2. Checklist quan sát trong demo

- Số chunk sinh ra có hợp lý theo độ dài tài liệu không.
- Chunk có giữ đúng ngữ nghĩa section/table không.
- Có metadata vị trí/chứng cứ để trích dẫn không.
- Câu trả lời có grounded vào tài liệu hay "nói theo trí nhớ".
- Độ ổn định retrieval khi thay đổi cách đặt câu hỏi.

## 3. Checklist kỹ thuật sau demo

- Thu thập log thời gian từng chặng ingest.
- Ghi nhận tỉ lệ lỗi parse theo định dạng file.
- Rút ra cấu hình parser/chunk phù hợp theo từng loại dữ liệu.
- Lập backlog cải thiện ingest trước khi tối ưu prompt/LLM.

## 4. Key Takeaways của Session 2

- Ingest pipeline là móng của chất lượng query pipeline.
- Parser là thành phần chiến lược, không phải bước phụ.
- DeepDoc cho thấy lợi ích rõ khi xử lý tài liệu enterprise phức tạp.
- Muốn tối ưu RAG hiệu quả, bắt đầu từ dữ liệu và ingest quality trước.

## 5. Cầu nối sang Session 3

Session 3 sẽ đi sâu vào ba khối kỹ thuật quyết định retrieval performance:
- Chunking strategy
- Embedding space
- Vector index/ANN trade-off

## Phan tich chuyen sau bo sung

- [06-demo-checklist-and-takeaways] Rule 1: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [06-demo-checklist-and-takeaways] Check 1: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 1: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 1: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 2: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [06-demo-checklist-and-takeaways] Check 2: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 2: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 2: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 3: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [06-demo-checklist-and-takeaways] Check 3: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 3: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 3: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 4: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [06-demo-checklist-and-takeaways] Check 4: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 4: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 4: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 5: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [06-demo-checklist-and-takeaways] Check 5: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 5: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 5: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 6: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [06-demo-checklist-and-takeaways] Check 6: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 6: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 6: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 7: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [06-demo-checklist-and-takeaways] Check 7: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 7: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 7: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 8: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [06-demo-checklist-and-takeaways] Check 8: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 8: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 8: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 9: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [06-demo-checklist-and-takeaways] Check 9: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 9: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 9: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 10: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [06-demo-checklist-and-takeaways] Check 10: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 10: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 10: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 11: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [06-demo-checklist-and-takeaways] Check 11: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 11: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 11: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 12: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [06-demo-checklist-and-takeaways] Check 12: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 12: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 12: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 13: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [06-demo-checklist-and-takeaways] Check 13: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 13: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 13: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 14: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [06-demo-checklist-and-takeaways] Check 14: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 14: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 14: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 15: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [06-demo-checklist-and-takeaways] Check 15: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 15: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 15: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 16: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [06-demo-checklist-and-takeaways] Check 16: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 16: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 16: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 17: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [06-demo-checklist-and-takeaways] Check 17: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 17: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 17: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 18: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [06-demo-checklist-and-takeaways] Check 18: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 18: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 18: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 19: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [06-demo-checklist-and-takeaways] Check 19: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 19: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 19: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 20: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [06-demo-checklist-and-takeaways] Check 20: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 20: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 20: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 21: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [06-demo-checklist-and-takeaways] Check 21: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 21: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 21: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 22: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [06-demo-checklist-and-takeaways] Check 22: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 22: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 22: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 23: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [06-demo-checklist-and-takeaways] Check 23: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 23: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 23: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 24: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [06-demo-checklist-and-takeaways] Check 24: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 24: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 24: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 25: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [06-demo-checklist-and-takeaways] Check 25: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 25: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 25: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 26: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [06-demo-checklist-and-takeaways] Check 26: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 26: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 26: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 27: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [06-demo-checklist-and-takeaways] Check 27: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 27: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 27: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 28: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [06-demo-checklist-and-takeaways] Check 28: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 28: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 28: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 29: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [06-demo-checklist-and-takeaways] Check 29: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 29: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 29: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 30: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [06-demo-checklist-and-takeaways] Check 30: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 30: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 30: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 31: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [06-demo-checklist-and-takeaways] Check 31: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 31: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 31: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 32: Phan tich sau: lien ket thanh phan nay voi chat luong grounded answer va citation.
- [06-demo-checklist-and-takeaways] Check 32: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 32: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 32: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 33: Phan tich sau: xac dinh metric nao thay doi truoc khi ket luan toi uu thanh cong.
- [06-demo-checklist-and-takeaways] Check 33: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 33: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 33: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 34: Phan tich sau: danh gia trade-off giua do tre, chi phi, va do chinh xac retrieval.
- [06-demo-checklist-and-takeaways] Check 34: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 34: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 34: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 35: Phan tich sau: lap baseline va rollback rule truoc khi thay doi trong production.
- [06-demo-checklist-and-takeaways] Check 35: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 35: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 35: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 36: Phan tich sau: tim failure mode, cach phat hien som, va cach khoanh vung nguyen nhan.
- [06-demo-checklist-and-takeaways] Check 36: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 36: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 36: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 37: Phan tich sau: toi uu upstream neu muon giam noise cho downstream generation.
- [06-demo-checklist-and-takeaways] Check 37: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 37: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 37: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 38: Phan tich sau: doi chieu ket qua ky thuat voi muc tieu business va SLA.
- [06-demo-checklist-and-takeaways] Check 38: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 38: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 38: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 39: Phan tich sau: bo sung checklist test de dam bao ket qua co the tai lap.
- [06-demo-checklist-and-takeaways] Check 39: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 39: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 39: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 40: Phan tich sau: lap vong lap do luong -> cai tien -> kiem chung -> chuan hoa.
- [06-demo-checklist-and-takeaways] Check 40: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 40: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 40: tong ket bai hoc de team dung lai cho cac case tuong tu.
- [06-demo-checklist-and-takeaways] Rule 41: Phan tich sau: xac dinh ro value cua thanh phan nay trong toan bo he thong RAG.
- [06-demo-checklist-and-takeaways] Check 41: ghi ro input, output, metric, baseline, va rollback rule.
- [06-demo-checklist-and-takeaways] Ops 41: moi thay doi can guardrail, alert, va runbook xu ly su co.
- [06-demo-checklist-and-takeaways] Learn 41: tong ket bai hoc de team dung lai cho cac case tuong tu.
