from fastapi.testclient import TestClient
from app.llm.history_manager import session_histories
from app.main import app


client = TestClient(app)


# 中文：测试聊天接口
def test_chat_success(monkeypatch):

    # 中文：模拟 ask_model，不真的调用LLM API
    def fake_ask_model(session_id: str, message: str) -> str:
        return "テスト回答"

    # 中文：把 app.main.ask_model 临时替换成 fake_ask_model
    monkeypatch.setattr(
        "app.main.ask_model",
        fake_ask_model
    )

    response = client.post(
        "/chat",
        json={
            "session_id": "test-user",
            "message": "こんにちは"
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "answer": "テスト回答"
    }

# 中文：测试清空session历史接口
def test_clear_session():
    response = client.post(
        "/sessions/test-user/clear"
    )

    assert response.status_code == 200
    assert response.json()["success"] is True


# 中文：测试清空session后历史确实被删除
def test_clear_session_removes_history():
    session_histories["test-user"] = [
        [
            {
                "role": "user",
                "content": "こんにちは"
            }
        ]
    ]

    response = client.post(
        "/sessions/test-user/clear"
    )

    assert response.status_code == 200
    assert "test-user" not in session_histories