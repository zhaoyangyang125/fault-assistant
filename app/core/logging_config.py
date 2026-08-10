import logging


# 中文：初始化日志配置
# 函数名：setup_logging
def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s "
            "%(levelname)s "
            "%(name)s "
            "%(message)s"
        )
    )