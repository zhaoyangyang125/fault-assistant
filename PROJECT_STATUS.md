# Project Status

## 当前阶段

正在开发数据库层。

## 当前分支

feature/database

## 已完成

- GitHub 仓库初始化
- main 分支第一次提交
- SQLite 基础练习
- Function Calling 基础学习
- 多工具调用
- 多轮历史裁剪
- 完成 FaultRepository
- 实现根据 ID 查询故障记录
- 实现根据 severity 查询多条故障记录
- 实现根据 severity 统计故障数量
- Repository 查询功能已实际运行验证

## 下一步

- 创建 Service 层
- 添加 severity 参数校验
- 由 Service 调用 Repository

## 当前技术决定

- 后端：Python + FastAPI
- 数据库：SQLite
- LLM：DashScope qwen3-max
- 用户界面：日语 Web 界面
- 学习优先，暂缓 Codex 编写核心代码