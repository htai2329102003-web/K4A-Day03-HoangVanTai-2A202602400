"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Tra cứu lộ trình tuyến VinBus
    {
        "name": "route_lookup",
        "description": "Tra cứu lộ trình, điểm dừng và giờ hoạt động của tuyến xe bus điện VinBus.",
        "parameters": {
            "type": "object",
            "properties": {
                "route_number": {
                    "type": "string",
                    "description": "Mã tuyến VinBus cần tra cứu (ví dụ: 'E01')"
                }
            },
            "required": ["route_number"]
        }
    },
    
    # --------------------------------------------------------------------------
    # Tool 2: Đăng ký vé tháng VinBus
    # --------------------------------------------------------------------------
    {
        "name": "monthly_pass_registration",
        "description": "Đăng ký vé tháng VinBus cho hành khách theo tuyến và thời hạn lựa chọn.",
        "parameters": {
            "type": "object",
            "properties": {
                "passenger_name": {"type": "string", "description": "Họ tên hành khách đăng ký vé"},
                "phone_number": {"type": "string", "description": "Số điện thoại nhận thông tin đăng ký"},
                "route_number": {"type": "string", "description": "Mã tuyến VinBus muốn đăng ký (ví dụ: 'E01')"},
                "duration_months": {"type": "integer", "description": "Số tháng đăng ký vé"}
            },
            "required": ["passenger_name", "phone_number", "route_number", "duration_months"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "E01": {
        "route_name": "Bến xe Mỹ Đình - VinUni",
        "stops": ["Mỹ Đình", "Cầu Giấy", "Khu đô thị Ocean Park", "VinUni"],
        "operating_hours": "05:30 - 22:00",
        "frequency": "15 - 20 phút/chuyến"
    },
    "E02": {
        "route_name": "Công viên Cầu Giấy - VinUni",
        "stops": ["Công viên Cầu Giấy", "Times City", "Gia Lâm", "VinUni"],
        "operating_hours": "06:00 - 21:30",
        "frequency": "20 phút/chuyến"
    }
}


def execute_route_lookup(route_number: str) -> str:
    """Tra cứu lộ trình VinBus theo mã tuyến."""
    route = MOCK_DATABASE.get(route_number.strip().upper())
    if route:
        return json.dumps({
            "status": "SUCCESS",
            "route_number": route_number.strip().upper(),
            "data": route
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy tuyến VinBus có mã '{route_number}'."
        }, ensure_ascii=False)


def execute_monthly_pass_registration(passenger_name: str, phone_number: str, route_number: str, duration_months: int) -> str:
    """Mô phỏng đăng ký vé tháng VinBus."""
    return json.dumps({
        "status": "SUCCESS",
        "registration_id": f"VB-{phone_number[-4:]}-99",
        "passenger_name": passenger_name,
        "phone_number": phone_number,
        "route_number": route_number.strip().upper(),
        "duration_months": duration_months,
        "message": f"Đăng ký vé tháng thành công cho {passenger_name}, tuyến {route_number.upper()}, thời hạn {duration_months} tháng."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "route_lookup": execute_route_lookup,
    "monthly_pass_registration": execute_monthly_pass_registration
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
