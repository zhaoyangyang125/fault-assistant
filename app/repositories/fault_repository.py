from app.database.connection import get_connection





# 中文：根据严重程度统计故障数量
# 函数名：count_faults_by_severity
# severity：故障严重程度
# COUNT(*)：统计符合条件的记录数量
def count_faults_by_severity(severity: str) -> dict:
    conn = get_connection()
    cursor = None
    try:
        cursor = conn.cursor()

        sql= """
        SELECT COUNT(*) AS count
        FROM faults
        WHERE severity = ?
        """
        cursor.execute(sql, (severity,))

        row = cursor.fetchone()


        count = row["count"]


        return {
            "success": True,
            "severity": severity,
            "count":count,
        }

    finally:
        # 先关闭游标，再关闭数据库连接
        if cursor is not None:
            cursor.close()

        conn.close() 








# 中文：根据故障记录ID查询一条记录
# 函数名：get_fault_by_id
# record_id：故障记录ID
# fetchone：获取一条查询结果
def get_fault_by_id(record_id: int) -> dict:
    # 参数必须是正整数
    if not isinstance(record_id, int) or record_id <= 0:
        return {
            "success": False,
            "message": "record_id必须是正整数"
        }

    conn = get_connection()
    cursor = None

    try:
        # 创建游标
        cursor = conn.cursor()

        # 根据ID查询故障记录
        sql = """
        SELECT id, phenomenon, severity, status
        FROM faults
        WHERE id = ?
        """

        # 单个参数必须写成 (record_id,)
        cursor.execute(sql, (record_id,))

        row = cursor.fetchone()

        if row is None:
            return {
                "success": False,
                "message": "没有找到对应的故障记录"
            }

        return {
            "success": True,
            "fault": {
                "id": row["id"],
                "phenomenon": row["phenomenon"],
                "severity": row["severity"],
                "status": row["status"],
            }
        }
    finally:
        # 先关闭游标，再关闭数据库连接
        if cursor is not None:
            cursor.close()

        conn.close() 

def get_faults_by_severity(severity) -> dict:
    conn = get_connection()
    cursor = None
    try:
        cursor = conn.cursor()

        sql= """
        SELECT id, phenomenon, severity, status
        FROM faults
        WHERE severity = ?
        """
        cursor.execute(sql, (severity,))

        rows = cursor.fetchall()

        if  not rows :
            return {
                "success": False,
                "message": "没有找到对应的故障记录"
            }

        faults  = []
        for row in rows:
            fault = {
                "id": row["id"],
                "phenomenon": row["phenomenon"],
                "severity": row["severity"],
                "status": row["status"],
            }
            faults.append(fault)

        return {
            "success": True,
            "faults": faults,
        }

    finally:
        # 先关闭游标，再关闭数据库连接
        if cursor is not None:
            cursor.close()

        conn.close() 



if __name__ == "__main__":
    result = count_faults_by_severity("high")
    print(result)

    result = count_faults_by_severity("unknown")
    print(result)