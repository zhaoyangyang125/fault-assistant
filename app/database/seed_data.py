from app.database.connection import get_connection


# 中文：向faults表中添加一条故障记录
# 函数名：insert_data
# lastrowid：刚刚添加的数据ID
def insert_data(
    phenomenon: str,
    duration: str,
    result: str,
    severity: str,
    status: str,
    created_at: str,
) -> dict:
    conn = get_connection()
    cursor = None

    try:
        cursor = conn.cursor()

        sql = """
        INSERT INTO faults (
            phenomenon,
            duration,
            result,
            severity,
            status,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """

        values = (
            phenomenon,
            duration,
            result,
            severity,
            status,
            created_at,
        )

        cursor.execute(sql, values)

        # 保存数据库修改
        conn.commit()

        # 获取刚刚自动生成的故障记录ID
        record_id = cursor.lastrowid

        return {
            "success": True,
            "message": "信息添加成功",
            "record_id": record_id,
        }

    except Exception as error:
        # 发生异常时撤销本次数据库操作
        conn.rollback()

        return {
            "success": False,
            "message": f"信息添加失败：{error}",
        }

    finally:
        if cursor is not None:
            cursor.close()

        conn.close()

if __name__ == "__main__":
    result = insert_data(
        phenomenon="DTV画面が表示されない",
        duration="10秒",
        result="再現",
        severity="high",
        status="unresolved",
        created_at="2026-08-06 22:10:00",
    )

    print(result)