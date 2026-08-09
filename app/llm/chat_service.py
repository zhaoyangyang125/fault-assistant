import json
import os

import dashscope
from dashscope import Generation
from dotenv import load_dotenv

from app.llm.tool_definitions import TOOLS
from app.llm.tool_executor import execute_tool


load_dotenv()

dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")


# 中文：向LLM发送用户问题
# 函数名：ask_model
# user_input：用户输入
def ask_model(user_input: str) -> str:
    messages = [
        {
            "role": "system",
            "content": "あなたは故障情報を検索するアシスタントです。"
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    # 第一次调用模型
    response = Generation.call(
        model="qwen3-max",
        messages=messages,
        tools=TOOLS,
        result_format="message",
    )

    assistant_message = response.output.choices[0].message

    tool_calls = getattr(
        assistant_message,
        "tool_calls",
        None,
    )

    if tool_calls:
        messages.append(assistant_message)

        for tool_call in tool_calls:
            tool_result = execute_tool(tool_call)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call["id"],
                    "content": json.dumps(
                        tool_result,
                        ensure_ascii=False
                    )
                }
            )

        final_response = Generation.call(
            model="qwen3-max",
            messages=messages,
            tools=TOOLS,
            result_format="message",
        )

        return final_response.output.choices[0].message.content

    return assistant_message.content