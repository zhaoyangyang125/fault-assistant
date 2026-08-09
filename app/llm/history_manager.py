# 中文：最大保存轮数
MAX_ROUNDS = 5


# 中文：保存完整的对话轮次
# round_history：
# [
#     [第一轮的所有消息],
#     [第二轮的所有消息],
# ]
round_history = []


# 中文：保存一轮对话
# 函数名：add_round
# one_round：当前这一轮的所有消息
def add_round(one_round: list) -> None:
    round_history.append(one_round)

    # 如果超过最大轮数，只保留最近 MAX_ROUNDS 轮
    if len(round_history) > MAX_ROUNDS:
        del round_history[0]
    print("当前保存轮数：", len(round_history))


# 中文：根据历史记录构建发送给LLM的messages
# 函数名：build_messages
# system_message：系统消息
# user_input：当前用户输入
def build_messages(system_message: dict, user_input: str) -> list:
    messages = [system_message]

    # 一轮一轮取出历史记录
    for one_round in round_history:
        # extend：把这一轮里的消息逐条加入messages
        messages.extend(one_round)

    # 加入当前用户的问题
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    return messages