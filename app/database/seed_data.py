from app.database.connection import get_connection


# 中文：向faults表中添加一条故障记录
# 函数名：insert_data
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

        conn.commit()

        return {
            "success": True,
            "record_id": cursor.lastrowid,
        }

    finally:
        if cursor is not None:
            cursor.close()

        conn.close()


# 中文：数据库为空时插入演示数据
# 函数名：seed_database
def seed_database() -> None:
    conn = get_connection()
    cursor = None

    try:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) AS count FROM faults"
        )

        row = cursor.fetchone()

        if row["count"] > 0:
            return

    finally:
        if cursor is not None:
            cursor.close()

        conn.close()

    insert_data(
        phenomenon="DTV画面が表示されない",
        duration="10秒",
        result="再現",
        severity="high",
        status="unresolved",
        created_at="2026-08-06 22:10:00",
    )