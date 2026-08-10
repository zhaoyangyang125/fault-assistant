# Project Status

## 当前阶段

FastAPI 与 session 会话隔离已完成，准备进入异常处理与日志阶段。

## 当前分支

feature/database

## 已完成

- 完成 SQLite 数据库初始化
- 完成 Repository 层
- 完成 Service 层
- 创建 LLM 层
- 完成 Function Calling 工具定义
- 完成 tool_executor
- 完成 chat_service
- LLM 可调用 Service 查询 SQLite
- 支持按 ID 查询故障
- 支持按 severity 查询故障
- 支持按 severity 统计数量
- 支持普通非工具对话
- Function Calling 全链路已实际运行验证
- 完成多轮对话历史管理
- 使用 round_history 按完整轮次保存历史
- 完成 build_messages
- 普通对话可继承上下文
- Function Calling 对话可继承上下文
- 历史记录最多保留最近 5 轮
- 多轮历史裁剪已实际运行验证
- 完成 POST /chat API
- 使用 Pydantic 定义请求数据
- Swagger /docs 调试成功
- FastAPI 可调用 LLM Function Calling 完整链路
- 请求增加 session_id
- 不同 session 使用独立对话历史
- session 多轮上下文隔离已实际运行验证
- 完成基础异常处理
- 完成 logging 配置
- 完成环境变量配置管理
- 增加 .env.example
- 完成 pytest 基础测试
- 完成 Service 层自动测试
- 完成 FastAPI /chat 接口测试
- 使用 monkeypatch 模拟 LLM 调用
- 完成 session clear 接口测试
- 验证 session 历史实际删除
- Web UI を追加
- /chat API と Web UI を接続
- 会話履歴クリア機能を Web UI から利用可能にした


## 下一步

- Docker 対応
- デプロイ準備
- README 整理

## 当前技术决定

- 后端：Python + FastAPI
- 数据库：SQLite
- LLM：DashScope qwen3-max
- 用户界面：日语 Web 界面
- 学习优先，暂缓 Codex 编写核心代码