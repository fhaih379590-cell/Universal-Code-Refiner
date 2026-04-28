# 💎 Universal-Code-Refiner

<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/2103/2103811.png" width="120" height="120" alt="UCR-Logo">
  <h1>AI-Native Data Engineering Agent</h1>
  <p><b>下一代代码资产提纯引擎 —— 将原始代码炼制为高质量 AI 训练语料</b></p>

  [![GitHub Stars](https://img.shields.io/github/stars/fhaih379590-cell/Universal-Code-Refiner?style=flat-square&color=ffd700)](https://github.com/fhaih379590-cell/Universal-Code-Refiner/stargazers)
  [![Build Status](https://img.shields.io/github/actions/workflow/status/fhaih379590-cell/Universal-Code-Refiner/refine.yml?style=flat-square&label=Build&color=2ea44f)](https://github.com/fhaih379590-cell/Universal-Code-Refiner/actions)
  [![Cockpit](https://img.shields.io/badge/Cockpit-Live_Demo-58a6ff?style=flat-square)](https://fhaih379590-cell.github.io/Universal-Code-Refiner/)
  [![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
  [![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
</div>

---

## 📖 项目简介 (Overview)

**Universal-Code-Refiner (UCR)** 是一个全自动的代码资产重构与提纯平台。借鉴了专业开源项目（如 OpenClaw）的资源管理思路，UCR 利用大语言模型（LLM）的深度推理能力，不仅能修复代码缺陷，更能通过 **Chain-of-Thought (CoT)** 自动提取代码逻辑背后的思考链条。

我们的目标是：**让代码不仅仅能运行，更能作为高质量的数据资产，反哺 AI 模型的微调与训练。**

---

## ✨ 核心特性 (Key Features)

* 🚀 **Push-to-Refine**: 深度集成 GitHub Actions，实现“代码提交即触发重构”的自动化闭环。
* 🧠 **逻辑基因提取**: 自动生成推理过程（Reasoning），支持导出为符合 SFT（指令微调）格式的 JSONL 数据集。
* 🛡️ **安全脱敏隔离**: 深度扫描敏感基因，自动过滤并遮蔽 API Keys、个人隐私（PII）及内部 IP 地址。
* 🖥️ **可视化驾驶舱**: 借鉴游戏引擎设计的全屏深色系 UI，实时监控 Agent 的思考路径与 Token 消耗。
* 🧪 **自动验证 (Beta)**: 重构后自动尝试生成单元测试，确保代码逻辑的一致性。

---

## 🏗️ 系统架构 (Architecture)

```mermaid
graph TD
    A[User Push Code] -->|Trigger| B(GitHub Actions)
    subgraph Refinery Engine
        B --> C{Agent Analyzer}
        C -->|CoT Reasoning| D[Logic Extraction]
        C -->|Code Rewrite| E[Safe & Clean Code]
    end
    D & E --> F[Push to data/output/]
    F --> G((Final Asset))
    G --> H[Live Cockpit Dashboard]
