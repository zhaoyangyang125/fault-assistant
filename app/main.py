from fastapi import FastAPI, HTTPException


from app.llm.chat_service import ask_model
from app.llm.history_manager import clear_history
from app.core.logging_config import setup_logging
import logging
from pydantic import BaseModel, Field, field_validator



from fastapi.responses import FileResponse


# 中文：聊天请求数据
# session_id：会话ID
# message：用户输入
class ChatRequest(BaseModel):
    session_id: str = Field(min_length=1)
    message: str = Field(min_length=1)

    # 中文：去除字符串前后空格，并禁止纯空格
    @field_validator("session_id", "message")
    @classmethod
    def validate_not_blank(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("不能为空")

        return value

setup_logging()
app = FastAPI()


logger = logging.getLogger(__name__)


@app.get("/")
def index():
    return FileResponse("static/index.html")


# 中文：聊天接口
# 中文：聊天接口
@app.post("/chat")
def chat(request: ChatRequest) -> dict:
    try:
        logger.info(
            "chat request received: session_id=%s",
            request.session_id
        )

        answer = ask_model(
            request.session_id,
            request.message
        )

        logger.info(
            "chat request completed: session_id=%s",
            request.session_id
        )

        return {
            "answer": answer
        }

    except Exception:
        logger.exception(
            "chat request failed: session_id=%s",
            request.session_id
        )

        raise HTTPException(
            status_code=500,
            detail="チャット処理中にエラーが発生しました。"
        )


    
# 中文：清空指定会话的历史记录
@app.post("/sessions/{session_id}/clear")
def clear_session(session_id: str) -> dict:
    clear_history(session_id)

    return {
        "success": True,
        "message": "会話履歴を削除しました。"
    }


