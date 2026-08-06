from app.database.connection import (
    DATABASE_PATH,
    get_connection,
)


# 中文：创建数据库和faults表
# 日本語：データベースとfaultsテーブルを作成する
def initialize_database() -> None:
    # 确保data目录存在
    DATABASE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS faults (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phenomenon TEXT NOT NULL,
            duration TEXT,
            result TEXT,
            severity TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'unresolved',
            created_at TEXT NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()

    print(
        "データベースを初期化しました："
        f"{DATABASE_PATH}"
    )


if __name__ == "__main__":
    initialize_database()