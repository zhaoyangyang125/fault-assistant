import json

from app.services import fault_service


# 中文：执行LLM请求的工具调用
# 函数名：execute_tool
# tool_call：LLM返回的单个工具调用信息
def execute_tool(tool_call: dict) -> dict:
    # 获取模型选择的工具名
    function_name = tool_call["function"]["name"]

    # arguments原本是JSON字符串，转换成Python字典
    arguments = json.loads(
        tool_call["function"]["arguments"]
    )

    if function_name == "get_fault_by_id":
        record_id = arguments["record_id"]

        return fault_service.get_fault_by_id(
            record_id
        )

    elif function_name == "get_faults_by_severity":
        severity = arguments["severity"]

        return fault_service.get_faults_by_severity(
            severity
        )

    elif function_name == "count_faults_by_severity":
        severity = arguments["severity"]

        return fault_service.count_faults_by_severity(
            severity
        )

    return {
        "success": False,
        "message": f"未対応の関数です：{function_name}",
    }