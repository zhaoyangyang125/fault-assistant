import sqlite3
from pathlib import Path


# 中文：项目根目录
# 日本語：プロジェクトのルートディレクトリ
BASE_DIR = Path(__file__).resolve().parents[2]


# 中文：SQLite数据库文件路径
# 日本語：SQLiteデータベースファイルのパス
DATABASE_PATH = BASE_DIR / "data" / "faults.db"


# 中文：创建SQLite数据库连接
# 日本語：SQLiteデータベース接続を作成する
def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(
        DATABASE_PATH
    )

    # 查询结果可以通过字段名读取
    connection.row_factory = sqlite3.Row

    return connection