from app.repositories import fault_repository




# 中文：检查severity是否合法
# 函数名：is_valid_severity
# severity：故障严重程度
def is_valid_severity(severity: str) -> bool:
    if severity not in ["high", "medium", "low"]:
        return False
    return True

# 中文：根据严重程度查询故障记录
# 函数名：get_faults_by_severity
# severity：故障严重程度
def get_faults_by_severity(severity: str) -> dict:

    # 检查severity是否合法
    if not is_valid_severity(severity):
        return {
            "success": False,
            "message": "severity必须是high、medium或low"
        }

    # 调用Repository查询数据库
    return fault_repository.get_faults_by_severity(severity)

# 中文：根据故障记录ID查询故障
# 函数名：get_fault_by_id
# record_id：故障记录ID
def get_fault_by_id(record_id: int) -> dict:
    if not isinstance(record_id, int) or record_id <= 0:
        return {
            "success": False,
            "message": "record_id必须是正整数"
        }

    return fault_repository.get_fault_by_id(record_id)

# 中文：根据严重程度统计故障数量
# 函数名：count_faults_by_severity
# severity：故障严重程度
def count_faults_by_severity(severity: str) -> dict:

    # 检查severity是否合法
    if not is_valid_severity(severity):
        return {
            "success": False,
            "message": "severity必须是high、medium或low"
        }

    # 调用Repository查询数据库
    return fault_repository.count_faults_by_severity(severity)


if __name__ == "__main__":
    print(get_fault_by_id(1))
    print(get_fault_by_id(-1))

    print(get_faults_by_severity("high"))
    print(get_faults_by_severity("abc"))

    print(count_faults_by_severity("high"))
    print(count_faults_by_severity("abc"))
