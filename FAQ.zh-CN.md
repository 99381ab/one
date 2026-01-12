# 常见问题解答 (FAQ)

欢迎！这里整理了关于本仓库的常见问题和解答。

## 目录
- [关于本仓库](#关于本仓库)
- [Python 报告生成器](#python-报告生成器)
- [VLAN 网络配置](#vlan-网络配置)
- [常见问题](#常见问题)

---

## 关于本仓库

### 这个仓库包含什么内容？

本仓库主要包含两个部分：

1. **Python 课程实践作业报告自动生成工具** - 使用 Python 脚本自动生成符合格式要求的 Word 文档
2. **Packet Tracer VLAN 实验配置** - 三层交换机实现 VLAN 间通信的配置文件和说明文档

### 这个仓库适合谁使用？

- 需要提交《Python 程序设计》课程实践作业的学生
- 学习计算机网络和 VLAN 配置的学生
- 需要快速生成标准格式报告的用户

---

## Python 报告生成器

### 如何使用报告生成器？

有两种方式：

**方式一：GitHub Actions（推荐，无需本地环境）**

1. 进入仓库的 Actions 标签页
2. 选择 "Build DOCX" 工作流
3. 点击 "Run workflow" 按钮
4. 填写以下信息（或使用默认值）：
   - 学年学期（默认：2025 - 2026学年第1学期）
   - 班级（默认：2023级物联网工程1班）
   - 学号（默认：230911005）
   - 姓名（默认：张三）
   - 任课教师（默认：李晓）
5. 等待 1-2 分钟，文档会自动生成并提交到 `docs/` 目录

**方式二：本地运行**

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行脚本
python report_generator.py --out "docs/《Python程序设计》课程实践作业.docx" \
  --term "2025 - 2026学年第1学期" \
  --klass "2023级物联网工程1班" \
  --sid "230911005" \
  --name "张三" \
  --teacher "李晓"
```

### 生成的报告包含什么内容？

生成的报告是一个完整的课程实践作业文档，包含：

- 封面页（班级、学号、姓名、成绩栏）
- 课程信息页
- 课程实践要求
- 乒乓球模拟比赛程序示例
- 程序设计思路详解
- 完整程序代码（带注释）
- 实验结果展示区域
- 结果分析与问题总结

### 我可以修改生成的内容吗？

可以！有两种方式：

1. **修改脚本参数** - 通过命令行参数自定义个人信息
2. **修改源代码** - 编辑 `report_generator.py` 来自定义报告内容、格式和代码示例（注：仓库中的文件 `3` 是 `report_generator.py` 的备份副本）

### 生成的文档在哪里？

- GitHub Actions 运行：文档会提交到 `docs/《Python程序设计》课程实践作业.docx`
- 本地运行：根据 `--out` 参数指定的路径

### 需要什么 Python 版本？

- Python 3.11 或更高版本（GitHub Actions 使用 3.11）
- Python 3.7+ 应该也能工作

### 依赖包是什么？

只需要一个依赖包：
- `python-docx>=1.1.0` - 用于生成和操作 Word 文档

---

## VLAN 网络配置

### Packet Tracer 实验是什么？

这是一个三层交换机实现 VLAN 间通信的实验，演示如何：
- 配置多个 VLAN（VLAN 10、20、30）
- 使用三层交换机（3560）作为网关
- 通过 Trunk 端口连接多个二层交换机（2960）
- 实现不同 VLAN 之间的互通

### 实验拓扑结构是什么？

```
PC10.1   PC20.1   PC30.1           PC10.2   PC20.2   PC30.2           PC10.3   PC20.3   PC30.3
  |        |        |                 |        |        |                 |        |        |
Fa0/1   Fa0/2   Fa0/3              Fa0/1   Fa0/2   Fa0/3              Fa0/1   Fa0/2   Fa0/3
  \       |       /                   \       |       /                   \       |       /
  Switch A (2960)                       Switch B (2960)                       Switch C (2960)
        Fa0/24                                 Fa0/24                                 Fa0/24
           |                                       |                                     |
        Fa0/1                                   Fa0/2                                 Fa0/3
                       \           Switch D (3560)           /
                                 (SVI: Vlan10/20/30)
```

### IP 地址规划是什么？

- **VLAN 10**: 192.168.10.0/24，网关 192.168.10.254
- **VLAN 20**: 192.168.20.0/24，网关 192.168.20.254
- **VLAN 30**: 192.168.30.0/24，网关 192.168.30.254

### 如何使用配置文件？

1. 在 Packet Tracer 中创建拓扑（1 台 3560 + 3 台 2960 + 9 台 PC）
2. 按拓扑图连接设备
3. 在每台交换机的 CLI 中粘贴对应的配置文件：
   - Switch D (3560)：`switch_D_3560.cfg`
   - Switch A (2960)：`switch_a_2960.cfg`
   - Switch B (2960)：`switch_b_2960.cfg`
   - Switch C (2960)：`switch_c_2960.cfg`
4. 执行 `write memory` 保存配置
5. 配置各 PC 的 IP 地址和网关
6. 测试连通性

### 如何验证配置是否成功？

**在交换机上：**
```
# Switch D (3560)
show ip interface brief | include Vlan
show ip route
show vlan brief
show interfaces trunk

# Switch A/B/C (2960)
show vlan brief
show interfaces trunk
```

**在 PC 上：**
```
ping 192.168.10.2
ping 192.168.20.3
ping 192.168.30.2
```

如果不同 VLAN 的 PC 之间可以互通，说明配置成功。

### 常见问题排查

**Q: 无法跨 VLAN 互通？**

A: 检查以下几点：
- PC 网关是否正确（应指向对应网段的 .254）
- Switch D 的 SVI 是否 up/up
- Trunk 是否允许 VLAN 10,20,30
- Access 端口是否在正确的 VLAN 中

**Q: 粘贴配置没有反应？**

A: 确保：
- 先执行 `enable` 进入特权模式
- 整段粘贴配置
- 最后执行 `write memory` 保存

---

## 常见问题

### 如何克隆这个仓库？

```bash
git clone https://github.com/99381ab/one.git
cd one
```

### 我可以修改代码吗？

当然可以！这个仓库是开源的，欢迎：
- Fork 这个仓库
- 创建您的功能分支
- 提交您的改进
- 发起 Pull Request

### 文件 1、2、3 是什么？

这些是仓库中的辅助文件：
- **文件 1**: 报告生成器使用说明文档
- **文件 2**: GitHub Actions 工作流 YAML 配置
- **文件 3**: Python 报告生成器源代码（`report_generator.py` 的备份副本）

注：主要使用 `report_generator.py`，文件 1-3 是为了便于查看而保留的独立文档副本。

### 需要什么软件？

- **Python 报告生成器**：Python 3.7+ 和 pip
- **VLAN 实验**：Cisco Packet Tracer（建议 7.0 或更高版本）

### 我还有其他问题怎么办？

如果您有任何问题、建议或发现了 bug，欢迎：
1. 在 GitHub 仓库中创建 Issue
2. 查看现有的 Issues 看是否已有相关讨论
3. 直接修改代码并提交 Pull Request

---

## 技术支持

如果您在使用过程中遇到问题，请：
1. 仔细阅读本 FAQ 文档
2. 查看相关的 README 文档（`README.md`、`pt-vlan-assignment/README.zh-CN.md`）
3. 检查 GitHub Issues 是否有类似问题
4. 创建新的 Issue 描述您的问题

祝您使用愉快！
