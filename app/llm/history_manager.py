# 中文：最大保存轮数
MAX_ROUNDS = 5


# 中文：保存所有会话的历史
# key：session_id
# value：该session对应的多轮历史
session_histories = {}


# 中文：获取指定session的历史
# 函数名：get_history
# session_id：会话ID
def get_history(session_id: str) -> list:
    if session_id not in session_histories:
        session_histories[session_id] = []

    return session_histories[session_id]


# 中文：保存一轮对话
# 函数名：add_round
# session_id：会话ID
# one_round：当前这一轮的所有消息
def add_round(session_id: str, one_round: list) -> None:
    round_history = get_history(session_id)

    round_history.append(one_round)

    if len(round_history) > MAX_ROUNDS:
        del round_history[0]


# 中文：根据历史记录构建发送给LLM的messages
# 函数名：build_messages
# session_id：会话ID
# system_message：系统消息
# user_input：当前用户输入
def build_messages(
    session_id: str,
    system_message: dict,
    user_input: str
) -> list:
    messages = [system_message]

    round_history = get_history(session_id)

    for one_round in round_history:
        messages.extend(one_round)

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    return messages

def clear_history(session_id: str) -> None:
    if session_id in session_histories:
        del session_histories[session_id]