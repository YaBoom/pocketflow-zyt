# PocketFlow：100行代码的极简LLM框架

> 实验性项目，基于 [PocketFlow](https://github.com/The-Pocket/PocketFlow) 的探索和学习记录

## 📝 说明

这只是初步探索代码，还有很多不足，欢迎指点！

## 🚀 快速开始

### 1. 下载核心文件

```bash
wget https://raw.githubusercontent.com/The-Pocket/PocketFlow/main/pocketflow.py
```

### 2. 安装依赖

```bash
pip install openai
```

### 3. 运行示例

```bash
export OPENAI_API_KEY="your-key"
python examples/basic_chatbot.py
```

## 📁 项目结构

```
.
├── pocketflow.py              # PocketFlow核心（100行）
├── src/
│   ├── nodes/
│   │   ├── gpt_node.py       # GPT调用节点
│   │   ├── analyzer_node.py  # 需求分析节点
│   │   └── generator_node.py # 代码生成节点
│   └── flows/
│       └── auto_codegen.py   # 自动代码生成流程
├── examples/
│   ├── basic_chatbot.py      # 基础聊天机器人
│   ├── rag_pipeline.py       # RAG流水线（TODO）
│   └── multi_agent.py        # 多智能体协作（TODO）
└── experiments/
    └── trial_001.py          # 我的各种试错版本
```

## 🔬 实验记录

### Trial 001：基础Node测试
- ✅ 能跑通
- ⚠️ 错误处理缺失

### Trial 002：多Node串联
- ✅ 共享状态传递正常
- ⚠️ 类型不一致会导致后续Node崩溃

### Trial 003：代码生成智能体
- ✅ 能生成可运行代码
- ⚠️ 上下文传递不够智能
- 💡 加了ContextRefiner节点后有所改善

### Trial 004：并行执行（TODO）
- 还没搞定，asyncio有点复杂

## 🐛 已知问题

1. **错误处理太原始** - 没有重试、没有降级
2. **并发支持弱** - 需要自己实现async逻辑
3. **共享状态风险** - 类型不一致会崩
4. **缺少监控** - 不知道流程跑到哪一步了

## 💡 我的想法（不一定对）

- 也许可以基于PocketFlow封装一个轻量级wrapper，提供基础的错误处理和日志
- 上下文设计是个难题，可能需要引入类似LangChain的Memory概念
- 100行代码确实极简，但实际用起来发现缺的基础设施太多

## 📚 参考

- [PocketFlow 官方仓库](https://github.com/The-Pocket/PocketFlow)
- [我的知乎探索笔记](https://zhuanlan.zhihu.com/p/2005221888620777895)

## ⚠️ 免责声明

这只是实验代码，**不要直接上生产**！

## 🙏 致谢

感谢PocketFlow作者的极简设计理念，让我重新思考"框架"的定义。

---

*最后更新：2026-02-12*

*状态：还在摸索中...*
