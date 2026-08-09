# Project Status

## 当前阶段

正在开发数据库层。

## 当前分支

feature/database

## 已完成

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

## 下一步

- 提交并推送 LLM 层代码
- 开始多轮对话历史管理
- 将之前学习过的按轮 history trimming 接入正式项目

## 当前技术决定

- 后端：Python + FastAPI
- 数据库：SQLite
- LLM：DashScope qwen3-max
- 用户界面：日语 Web 界面
- 学习优先，暂缓 Codex 编写核心代码