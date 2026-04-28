# Universal-Code-Refiner
# 💎 Universal-Code-Refiner

<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/2103/2103811.png" width="120" height="120" alt="Logo">
  <h1>AI-Native Data Engineering Agent</h1>
  <p><b>下一代代码资产提纯引擎 —— 释放代码中蕴含的逻辑潜能</b></p>

  [![GitHub Stars](https://img.shields.io/github/stars/fhaih379590-cell/Universal-Code-Refiner?style=flat-square&color=ffd700)](https://github.com/fhaih379590-cell/Universal-Code-Refiner/stargazers)
  [![Build Status](https://img.shields.io/github/actions/workflow/status/fhaih379590-cell/Universal-Code-Refiner/refine.yml?style=flat-square&label=Build)](https://github.com/fhaih379590-cell/Universal-Code-Refiner/actions)
  [![Cockpit](https://img.shields.io/badge/Cockpit-Live_Demo-58a6ff?style=flat-square)](https://fhaih379590-cell.github.io/Universal-Code-Refiner/)
  [![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
</div>

---

## 📖 项目简介 (Overview)

**Universal-Code-Refiner** 模仿 OpenClaw 对复杂资源的系统化管理逻辑，通过大语言模型（LLM）的深度推理能力，将混乱、原始的 Legacy Code 自动转化为高质量、结构化的训练语料。

我们不仅是重构代码，更是利用 **Chain-of-Thought (CoT)** 提取代码背后的“逻辑基因”，为构建更懂代码的 AI 模型提供数据支撑。

### ✨ 核心亮点
- 🛠 **自动化流水线**: 深度集成 GitHub Actions，实现“提交即提纯”的无感体验。
- 🧠 **推理链提取**: 自动生成代码修改的逻辑路径，适配 SFT（微调）数据格式。
- 🖥 **可视化监控**: 借鉴专业游戏引擎控制台设计的全屏驾驶舱界面。
- 🔐 **安全脱敏**: 自动识别并清洗代码中的敏感基因。

---

## 🛠 快速开始 (Quick Start)

想要体验 Agent 的炼金术？只需简单三步：

1. **Fork 本仓库** 到你的 GitHub 账号。
2. **配置密钥**: 在 `Settings > Secrets > Actions` 中添加 `LLM_API_KEY`（支持 OpenAI/DeepSeek 格式）。
3. **投放代码**: 将任何待处理的 `.py` 文件上传至 `data/input/` 目录。
   - *Agent 会自动识别变动并生成结果到 `data/output/`。*

---

## 📂 项目结构 (Project Structure)

```text
Universal-Code-Refiner/
├── .github/workflows/    # 自动化炼丹炉 (GitHub Actions)
├── data/
│   ├── input/            # 原始代码投放区 (Raw Assets)
│   └── output/           # 提纯后的代码与报告 (Refined Results)
├── scripts/
│   └── refine.py         # 核心推理引擎 (LLM Logic)
├── index.html            # 实时驾驶舱前端 (Cockpit UI)
└── README.md             # 项目蓝图


## 🗺 进化路线图 (Evolution Roadmap)

- [x] **v0.2 Beta**: 核心重构流水线与可视化驾驶舱。
- [ ] **v0.5 (智能升级)**: 
  - **集成验证器**: 自动运行 pytest 确保重构前后的逻辑等价。
  - **隐私基因过滤**: 深度扫描并遮蔽泄露的 API Keys 和内网 IP。
- [ ] **v0.8 (数据生产)**:
  - **SFT 语料库生成**: 自动导出 (Raw -> Thought -> Refined) 三元组数据集。
  - **RAG 规范接入**: 支持加载自定义 `.md` 规范文档。
- [ ] **v1.0 (多 Agent 协作)**:
  - 模拟 OpenClaw 的资源管理，引入“架构师-编码员-审计员”三位一体的 Agent 协作模式。

