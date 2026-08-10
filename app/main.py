from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.llm.chat_service import ask_model
from app.llm.history_manager import clear_history
from app.core.logging_config import setup_logging
import logging


setup_logging()
app = FastAPI()


logger = logging.getLogger(__name__)

# 中文：聊天请求数据
# message：用户输入
class ChatRequest(BaseModel):
    session_id: str
    message: str


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