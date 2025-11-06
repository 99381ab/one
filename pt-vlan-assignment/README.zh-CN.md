# 三层交换机实现 VLAN 间通信（Packet Tracer 作业）

本包包含 4 个交换机配置与操作说明。拓扑与 IP 规划：
- VLAN 10: 192.168.10.0/24，网关 192.168.10.254
- VLAN 20: 192.168.20.0/24，网关 192.168.20.254
- VLAN 30: 192.168.30.0/24，网关 192.168.30.254

设备与连线（与课堂截图一致）：
- Switch D（3560，三层）：Fa0/1 -> Switch A Fa0/24，Fa0/2 -> Switch B Fa0/24，Fa0/3 -> Switch C Fa0/24（均为 trunk）
- Switch A/B/C（2960，二层）：Fa0/1 放 VLAN10，Fa0/2 放 VLAN20，Fa0/3 放 VLAN30；Fa0/24 上联到 Switch D

使用步骤：
1) 在 Packet Tracer 放 1 台 3560 (Switch D) 与 3 台 2960 (Switch A/B/C)，以及 9 台 PC。  
2) 连接：A Fa0/24 ↔ D Fa0/1；B Fa0/24 ↔ D Fa0/2；C Fa0/24 ↔ D Fa0/3。  
3) 逐台交换机 CLI 粘贴对应配置文件（switch_D_3560.cfg、switch_a_2960.cfg、switch_b_2960.cfg、switch_c_2960.cfg），执行完 `write memory`。  
4) PC 配置：  
   - A侧：192.168.10.1 /24、192.168.20.1 /24、192.168.30.1 /24；默认网关分别为 192.168.10.254、192.168.20.254、192.168.30.254  
   - B侧：192.168.10.2 /24、192.168.20.2 /24、192.168.30.2 /24  
   - C侧：192.168.10.3 /24、192.168.20.3 /24、192.168.30.3 /24  
5) 测试连通：10.1 ↔ 10.2/10.3；10.1 ↔ 20.3；10.1 ↔ 30.2；均能通即完成。

说明：
- Switch D 启用 `ip routing`，以 SVI 作为三网段网关，提供 VLAN 间路由。  
- 2960 固定 802.1Q，无需设置 encapsulation；3560 上显式设置。  
- 如端口命名不同，修改配置文件中的接口名即可。  

---

## 拓扑（ASCII 示意）
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

## 快速验证命令
在各设备 CLI 执行以下命令，快速确认配置是否生效。

- Switch D（3560）
  - `show ip interface brief | include Vlan`
  - `show ip route`
  - `show vlan brief`
  - `show interfaces trunk`

- Switch A/B/C（2960）
  - `show vlan brief`
  - `show interfaces trunk`
  - `show running-config interface fa0/1`

- PC 端
  - 在 Desktop → Command Prompt：`ping 192.168.10.2`、`ping 192.168.20.3`、`ping 192.168.30.2`

## 常见问题排查
- 无法跨 VLAN 互通：
  - PC 网关需指向对应网段的 .254（例如 VLAN10 用 192.168.10.254）。
  - 在 Switch D 上检查 SVI 是否 up/up（`show ip interface brief`）。
  - Trunk 允许的 VLAN 是否包含 10,20,30（`show interfaces trunk`）。
  - 接入口是否为 access 模式并放在正确的 VLAN（`show running-config interface fa0/x`）。
- 粘贴配置无反应：先 `enable` 进入特权模式，再整段粘贴，执行完 `write memory` 保存。

## 成品导出
1) 在 Packet Tracer 中完成上述配置与连通性测试；
2) File → Save As → 保存为 `pt-vlan-assignment.pkt`；
3) 回到 GitHub 仓库的 `pt-vlan-assignment/` 目录，点击 “Add file” → “Upload files”，上传 `pt-vlan-assignment.pkt`。
