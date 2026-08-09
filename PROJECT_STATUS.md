# Project Status

## 当前阶段

正在开发数据库层。

## 当前分支

feature/database

## 已完成

- 完成 SQLite 数据库初始化
- 完成 FaultRepository
- 实现根据 ID 查询故障记录
- 实现根据 severity 查询多条故障记录
- 实现根据 severity 统计故障数量
- 创建 Service 层
- Service 实现 record_id 参数校验
- Service 实现 severity 参数校验
- 抽取 is_valid_severity 公共校验函数
- Service 层已实际运行验证

## 下一步

- 整理 Repository 中重复的参数校验
- 创建 LLM 层
- 定义正式 Function Calling tools
- 让 LLM 调用 Service，而不是直接调用 Repository

## 当前技术决定

- 后端：Python + FastAPI
- 数据库：SQLite
- LLM：DashScope qwen3-max
- 用户界面：日语 Web 界面
- 学习优先，暂缓 Codex 编写核心代码