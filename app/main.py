from app.llm.chat_service import ask_model
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# 中文：聊天请求数据
# message：用户输入
class ChatRequest(BaseModel):
    session_id: str
    message: str


# 中文：聊天接口
@app.post("/chat")
def chat(request: ChatRequest) -> dict:
    answer = ask_model(
        request.session_id,
        request.message
    )

    return {
        "answer": answer
    }

