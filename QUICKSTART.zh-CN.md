# 快速入门指南

欢迎使用本仓库！这是一个帮助您在 5 分钟内快速上手的指南。

## 🎯 您想做什么？

### 选项 A：生成 Python 作业报告（最简单）

**无需安装任何软件！**

1. 点击仓库顶部的 **Actions** 标签
2. 在左侧选择 **Build DOCX**
3. 点击右侧的 **Run workflow** 按钮
4. 填写您的信息：
   - 学年学期：例如 "2025 - 2026学年第1学期"
   - 班级：例如 "2023级物联网工程1班"
   - 学号：例如 "230911005"
   - 姓名：您的姓名
   - 任课教师：例如 "李晓"
5. 点击绿色的 **Run workflow** 按钮
6. 等待 1-2 分钟
7. 刷新页面，查看 `docs/` 目录，您的报告已生成！

✅ **完成！** 下载 `.docx` 文件即可使用。

---

### 选项 B：在本地生成报告

**需要：** Python 3.7 或更高版本

```bash
# 1. 克隆仓库
git clone https://github.com/99381ab/one.git
cd one

# 2. 安装依赖
pip install -r requirements.txt

# 3. 生成报告（修改参数为您的信息）
python report_generator.py \
  --out "我的报告.docx" \
  --term "2025 - 2026学年第1学期" \
  --klass "2023级物联网工程1班" \
  --sid "230911005" \
  --name "您的姓名" \
  --teacher "李晓"

# 4. 打开生成的 我的报告.docx
```

✅ **完成！** 在当前目录找到生成的文档。

---

### 选项 C：进行 VLAN 网络实验

**需要：** Cisco Packet Tracer 7.0+

#### 第一步：准备拓扑

1. 打开 Packet Tracer
2. 添加设备：
   - 1 台 **Cisco 3560** 交换机（命名为 Switch D）
   - 3 台 **Cisco 2960** 交换机（命名为 Switch A, B, C）
   - 9 台 **PC**

#### 第二步：连接设备

按以下方式连接（使用直通线）：

```
Switch A 的 Fa0/24 ←→ Switch D 的 Fa0/1
Switch B 的 Fa0/24 ←→ Switch D 的 Fa0/2
Switch C 的 Fa0/24 ←→ Switch D 的 Fa0/3

Switch A: Fa0/1 ←→ PC (VLAN10)
Switch A: Fa0/2 ←→ PC (VLAN20)
Switch A: Fa0/3 ←→ PC (VLAN30)

Switch B: Fa0/1 ←→ PC (VLAN10)
Switch B: Fa0/2 ←→ PC (VLAN20)
Switch B: Fa0/3 ←→ PC (VLAN30)

Switch C: Fa0/1 ←→ PC (VLAN10)
Switch C: Fa0/2 ←→ PC (VLAN20)
Switch C: Fa0/3 ←→ PC (VLAN30)
```

#### 第三步：配置交换机

1. 点击 **Switch D**，进入 CLI 标签
2. 复制 `pt-vlan-assignment/switch_D_3560.cfg` 的全部内容
3. 粘贴到 CLI 中
4. 输入 `write memory` 保存

重复以上步骤配置其他交换机：
- Switch A → `switch_a_2960.cfg`
- Switch B → `switch_b_2960.cfg`
- Switch C → `switch_c_2960.cfg`

#### 第四步：配置 PC

**Switch A 连接的 PC：**
- PC1: IP `192.168.10.1`，子网掩码 `255.255.255.0`，网关 `192.168.10.254`
- PC2: IP `192.168.20.1`，子网掩码 `255.255.255.0`，网关 `192.168.20.254`
- PC3: IP `192.168.30.1`，子网掩码 `255.255.255.0`，网关 `192.168.30.254`

**Switch B 连接的 PC：**
- PC4: IP `192.168.10.2`，子网掩码 `255.255.255.0`，网关 `192.168.10.254`
- PC5: IP `192.168.20.2`，子网掩码 `255.255.255.0`，网关 `192.168.20.254`
- PC6: IP `192.168.30.2`，子网掩码 `255.255.255.0`，网关 `192.168.30.254`

**Switch C 连接的 PC：**
- PC7: IP `192.168.10.3`，子网掩码 `255.255.255.0`，网关 `192.168.10.254`
- PC8: IP `192.168.20.3`，子网掩码 `255.255.255.0`，网关 `192.168.20.254`
- PC9: IP `192.168.30.3`，子网掩码 `255.255.255.0`，网关 `192.168.30.254`

#### 第五步：测试连通性

在 PC1 上打开 Command Prompt，执行：

```
ping 192.168.10.2    # 应该成功
ping 192.168.20.2    # 应该成功（跨VLAN）
ping 192.168.30.3    # 应该成功（跨VLAN）
```

✅ **完成！** 如果所有 ping 都成功，您的 VLAN 网络已经配置成功！

---

## 📚 需要更多帮助？

- **常见问题？** → 查看 [FAQ](FAQ.zh-CN.md)
- **遇到错误？** → 查看 [故障排查](pt-vlan-assignment/README.zh-CN.md#常见问题排查)
- **想贡献代码？** → 查看 [贡献指南](CONTRIBUTING.md)
- **有其他问题？** → [创建 Issue](https://github.com/99381ab/one/issues)

---

## 💡 小提示

### 报告生成器提示
- 生成的报告可以直接用 Word 打开和编辑
- 您可以在生成后添加运行截图
- 可以修改 `report_generator.py` 来自定义报告内容

### VLAN 实验提示
- 保存您的 Packet Tracer 文件（`.pkt` 格式）
- 使用 `show vlan brief` 查看 VLAN 配置
- 使用 `show ip route` 查看路由表
- 如果 ping 不通，检查网关配置

---

**祝您学习顺利！** 🎓
