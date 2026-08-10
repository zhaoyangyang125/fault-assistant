import json
import os

import dashscope
from dashscope import Generation
from dotenv import load_dotenv

from app.llm.tool_definitions import TOOLS
from app.llm.tool_executor import execute_tool
from app.llm.history_manager import build_messages, add_round


load_dotenv()

dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")


# 中文：向LLM发送用户问题
# 函数名：ask_model
# user_input：用户输入
def ask_model(session_id: str, user_input: str) -> str:



    # 系统消息
    system_message = {
        "role": "system",
        "content": "あなたは故障情報を検索するアシスタントです。"
    }

    # 根据历史记录构建messages
    # 内容：
    # system
    # + 以前的对话
    # + 当前用户输入
    messages = build_messages(
        session_id,
        system_message,
        user_input
    )

    # 第一次调用模型
    response = Generation.call(
        model="qwen3-max",
        messages=messages,
        tools=TOOLS,
        result_format="message",
    )

    assistant_message = response.output.choices[0].message

    # 安全获取tool_calls
    # 如果没有tool_calls，则返回None
    tool_calls = getattr(
        assistant_message,
        "tool_calls",
        None,
    )

    # -------------------------
    # 情况1：模型需要调用工具
    # -------------------------
    if tool_calls:

        # 当前这一轮
        # 先保存用户消息
        current_round = [
            {
                "role": "user",
                "content": user_input
            }
        ]

        # 保存assistant的tool_call消息
        messages.append(assistant_message)
        current_round.append(assistant_message)

        # 执行模型请求的所有工具
        for tool_call in tool_calls:

            tool_result = execute_tool(tool_call)

            # 构造tool消息
            tool_message = {
                "role": "tool",
                "tool_call_id": tool_call["id"],
                "content": json.dumps(
                    tool_result,
                    ensure_ascii=False
                )
            }

            # 发给LLM
            messages.append(tool_message)

            # 同时保存到当前轮
            current_round.append(tool_message)

        # 第二次调用模型
        # 让模型根据数据库查询结果生成最终回答
        final_response = Generation.call(
            model="qwen3-max",
            messages=messages,
            tools=TOOLS,
            result_format="message",
        )

        final_message = (
            final_response
            .output
            .choices[0]
            .message
        )

        # 把最终assistant回答也保存到这一轮
        current_round.append(final_message)

        # 保存完整的一轮
        add_round(session_id,current_round)

        return final_message.content

    # -------------------------
    # 情况2：普通聊天，不调用工具
    # -------------------------

    current_round = [
        {
            "role": "user",
            "content": user_input
        },
        assistant_message
    ]

    # 保存这一轮
    add_round(session_id,current_round)

    return assistant_message.content