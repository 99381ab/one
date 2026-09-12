# One - 学习资源仓库

欢迎来到本仓库！这是一个包含课程作业工具和网络实验配置的学习资源库。

## 📚 仓库内容

本仓库包含以下两个主要部分：

### 1. Python 课程实践作业报告生成器

自动生成符合格式要求的《Python 程序设计》课程实践作业 Word 文档。

**相关文件：**
- 💻 [report_generator.py](report_generator.py) - 主程序源代码
- 📖 [使用说明](1) - 报告生成器文档
- ⚙️ [工作流配置](2) - GitHub Actions 自动化配置

**使用方法：**
```bash
# 方法一：使用 GitHub Actions（推荐）
# 前往 Actions 标签页 → 运行 "Build DOCX" 工作流

# 方法二：本地运行
pip install -r requirements.txt
python report_generator.py --out "docs/《Python程序设计》课程实践作业.docx" \
  --term "2025 - 2026学年第1学期" \
  --klass "2023级物联网工程1班" \
  --sid "230911005" \
  --name "张三" \
  --teacher "李晓"
```

### 2. Packet Tracer VLAN 网络实验

三层交换机实现 VLAN 间通信的完整配置和说明文档。

**查看详情：**
- 📖 [详细说明文档](pt-vlan-assignment/README.zh-CN.md)
- ⚙️ [交换机配置文件](pt-vlan-assignment/)

**实验内容：**
- 配置三层交换机（Cisco 3560）
- 配置多个二层交换机（Cisco 2960）
- 实现 VLAN 10、20、30 之间的互通
- 使用 Trunk 端口和 SVI 进行路由

## 🚀 快速开始

**第一次使用？** 查看 **[快速入门指南](QUICKSTART.zh-CN.md)** 在 5 分钟内上手！

## 🤔 常见问题

有问题？查看我们的 **[常见问题解答 (FAQ)](FAQ.zh-CN.md)**，里面包含：
- 详细的使用指南
- 常见问题解答
- 故障排查步骤
- 技术支持信息

## 🛠️ 技术栈

- **Python 3.11+** - 报告生成脚本
- **python-docx** - Word 文档处理
- **GitHub Actions** - 自动化构建
- **Cisco Packet Tracer** - 网络模拟

## 📝 文件结构

```
.
├── README.md                    # 本文件
├── QUICKSTART.zh-CN.md          # 快速入门指南
├── FAQ.zh-CN.md                 # 常见问题解答（中文）
├── FAQ.md                       # 常见问题解答（英文）
├── CONTRIBUTING.md              # 贡献指南
├── report_generator.py          # 报告生成器主程序
├── requirements.txt             # Python 依赖
├── 1                            # 文档：报告生成器说明
├── 2                            # 文档：GitHub Actions 配置
├── 3                            # 文档：报告生成器源代码备份
└── pt-vlan-assignment/          # VLAN 实验配置
    ├── README.zh-CN.md          # VLAN 实验说明
    ├── switch_D_3560.cfg        # 三层交换机配置
    ├── switch_a_2960.cfg        # 二层交换机 A 配置
    ├── switch_b_2960.cfg        # 二层交换机 B 配置
    └── switch_c_2960.cfg        # 二层交换机 C 配置
```

**注：** 文件 1、2、3 是历史遗留的文档副本，主要使用带描述性名称的文件（如 `report_generator.py`）。

## 🚀 使用指南

1. **克隆仓库**
   ```bash
   git clone https://github.com/99381ab/one.git
   cd one
   ```

2. **选择您需要的功能**
   - 生成 Python 作业报告 → 参考 [快速入门指南](QUICKSTART.zh-CN.md#选项-a生成-python-作业报告最简单)
   - 进行 VLAN 实验 → 参考 [快速入门指南](QUICKSTART.zh-CN.md#选项-c进行-vlan-网络实验)

3. **需要帮助？**
   - 查看 [常见问题解答](FAQ.zh-CN.md)
   - 查看 [快速入门指南](QUICKSTART.zh-CN.md)

## 💡 贡献

欢迎贡献！如果您有改进建议或发现了问题：

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 📞 支持

如有疑问，请：
- 查看 [FAQ](FAQ.zh-CN.md)
- 创建 [Issue](https://github.com/99381ab/one/issues)

---

**祝学习愉快！** 🎓