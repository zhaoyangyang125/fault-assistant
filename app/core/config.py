import os

from dotenv import load_dotenv


load_dotenv()


# 中文：LLM模型名称
LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "qwen3-max"
)


# 中文：最大保存对话轮数
MAX_ROUNDS = int(
    os.getenv(
        "MAX_ROUNDS",
        "5"
    )
)


# 中文：DashScope API Key
DASHSCOPE_API_KEY = os.getenv(
    "DASHSCOPE_API_KEY"
)