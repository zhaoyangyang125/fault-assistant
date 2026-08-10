# Project Status

## 当前阶段

正在开发数据库层。

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

## 下一步

- 接入 FastAPI
- 创建 POST /chat 接口
- 使用 Swagger 测试 API
- 后续实现 session 会话隔离


## 当前技术决定

- 后端：Python + FastAPI
- 数据库：SQLite
- LLM：DashScope qwen3-max
- 用户界面：日语 Web 界面
- 学习优先，暂缓 Codex 编写核心代码