# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Hoàng Văn Tài
> **Mã Sinh Viên / Mã Học viên:** 2A202602400
> **Chủ đề Lựa chọn:** Trợ lý Dịch vụ Khách hàng VinBus: Tra cứu lộ trình tuyến xe bus điện và đăng ký vé tháng

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Agent phân tích yêu cầu, chọn tra cứu tuyến hoặc đăng ký vé và xử lý kết quả tool trước khi trả lời. |
| **2. Tool Interaction** | 5 / 5 | Agent gọi hai tool qua MCP Server: `route_lookup` và `monthly_pass_registration`. |
| **3. Dynamic Decision** | 4 / 5 | Agent quyết định gọi tool theo intent; kết quả `SUCCESS` hoặc `NOT_FOUND` quyết định nội dung phản hồi. |
| **4. Long Horizon Goal** | 3 / 5 | Quy trình có thể mở rộng từ tra cứu đến đăng ký vé, nhưng phiên bản hiện tại chưa duy trì nhiều lượt hành động cho một yêu cầu. |
| **TỔNG ĐIỂM AGENTIC FIT** | **16 / 20** | Bài toán vượt ngưỡng 12/20 và phù hợp triển khai Agentic System. |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền API key thật và chọn `LLM_PROVIDER=groq` hoặc `LLM_PROVIDER=gemini` trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "action_type": "TOOL_EXECUTION",
    "tool_name": "route_lookup",
    "arguments": {"route_number": "E01"},
    "observation": {
      "status": "SUCCESS",
      "route_number": "E01",
      "data": {
        "route_name": "Bến xe Mỹ Đình - VinUni",
        "operating_hours": "05:30 - 22:00"
      }
    },
    "latency_ms": 120.5
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy trên Groq API thật.
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 3 lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
