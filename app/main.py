from app.llm.chat_service import ask_model


# 中文：程序入口
def main() -> None:
    while True:
        user_input = input(
            "\n質問を入力してください（exitで終了）："
        ).strip()

        if user_input.lower() == "exit":
            print("終了します。")
            break

        if not user_input:
            print("質問を入力してください。")
            continue

        answer = ask_model(user_input)

        print("\n回答：")
        print(answer)


if __name__ == "__main__":
    main()