# Frequently Asked Questions (FAQ)

Welcome! This document contains frequently asked questions and answers about this repository.

## Table of Contents
- [About This Repository](#about-this-repository)
- [Python Report Generator](#python-report-generator)
- [VLAN Network Configuration](#vlan-network-configuration)
- [Common Questions](#common-questions)

---

## About This Repository

### What does this repository contain?

This repository mainly contains two parts:

1. **Python Course Practice Assignment Report Auto-Generator** - A Python script that automatically generates Word documents in the required format
2. **Packet Tracer VLAN Experiment Configuration** - Configuration files and documentation for implementing VLAN inter-communication using Layer 3 switches

### Who is this repository for?

- Students who need to submit "Python Programming" course practice assignments
- Students learning computer networking and VLAN configuration
- Users who need to quickly generate standard format reports

---

## Python Report Generator

### How do I use the report generator?

There are two methods:

**Method 1: GitHub Actions (Recommended, no local environment needed)**

1. Go to the repository's Actions tab
2. Select the "Build DOCX" workflow
3. Click the "Run workflow" button
4. Fill in the following information (or use default values):
   - Term (Default: 2025 - 2026学年第1学期)
   - Class (Default: 2023级物联网工程1班)
   - Student ID (Default: 230911005)
   - Name (Default: 张三)
   - Teacher (Default: 李晓)
5. Wait 1-2 minutes, the document will be automatically generated and committed to the `docs/` directory

**Method 2: Run Locally**

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the script
python report_generator.py --out "docs/《Python程序设计》课程实践作业.docx" \
  --term "2025 - 2026学年第1学期" \
  --klass "2023级物联网工程1班" \
  --sid "230911005" \
  --name "张三" \
  --teacher "李晓"
```

### What does the generated report contain?

The generated report is a complete course practice assignment document, including:

- Cover page (class, student ID, name, grade field)
- Course information page
- Course practice requirements
- Ping-pong simulation program example
- Detailed program design ideas
- Complete program code (with comments)
- Experimental results display area
- Results analysis and problem summary

### Can I modify the generated content?

Yes! There are two ways:

1. **Modify script parameters** - Customize personal information through command-line parameters
2. **Modify source code** - Edit `report_generator.py` to customize report content, format, and code examples (Note: file `3` in the repository is a backup copy of `report_generator.py`)

### Where is the generated document?

- GitHub Actions run: Document will be committed to `docs/《Python程序设计》课程实践作业.docx`
- Local run: According to the path specified by the `--out` parameter

### What Python version is required?

- Python 3.11 or higher (GitHub Actions uses 3.11)
- Python 3.7+ should also work

### What are the dependencies?

Only one dependency package is needed:
- `python-docx>=1.1.0` - For generating and manipulating Word documents

---

## VLAN Network Configuration

### What is the Packet Tracer experiment?

This is an experiment on implementing VLAN inter-communication using Layer 3 switches, demonstrating how to:
- Configure multiple VLANs (VLAN 10, 20, 30)
- Use a Layer 3 switch (3560) as the gateway
- Connect multiple Layer 2 switches (2960) through Trunk ports
- Enable communication between different VLANs

### What is the experiment topology?

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

### What is the IP address plan?

- **VLAN 10**: 192.168.10.0/24, gateway 192.168.10.254
- **VLAN 20**: 192.168.20.0/24, gateway 192.168.20.254
- **VLAN 30**: 192.168.30.0/24, gateway 192.168.30.254

### How do I use the configuration files?

1. Create the topology in Packet Tracer (1 x 3560 + 3 x 2960 + 9 x PC)
2. Connect devices according to the topology diagram
3. Paste the corresponding configuration file in each switch's CLI:
   - Switch D (3560): `switch_D_3560.cfg`
   - Switch A (2960): `switch_a_2960.cfg`
   - Switch B (2960): `switch_b_2960.cfg`
   - Switch C (2960): `switch_c_2960.cfg`
4. Execute `write memory` to save the configuration
5. Configure IP addresses and gateways for each PC
6. Test connectivity

### How do I verify the configuration is successful?

**On switches:**
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

**On PCs:**
```
ping 192.168.10.2
ping 192.168.20.3
ping 192.168.30.2
```

If PCs in different VLANs can communicate with each other, the configuration is successful.

### Troubleshooting

**Q: Unable to communicate across VLANs?**

A: Check the following:
- Is the PC gateway correct (should point to .254 of the corresponding network segment)
- Is Switch D's SVI up/up
- Does the Trunk allow VLANs 10,20,30
- Are Access ports in the correct VLAN

**Q: No response when pasting configuration?**

A: Make sure to:
- First execute `enable` to enter privileged mode
- Paste the entire configuration
- Finally execute `write memory` to save

---

## Common Questions

### How do I clone this repository?

```bash
git clone https://github.com/99381ab/one.git
cd one
```

### Can I modify the code?

Of course! This repository is open source, welcome to:
- Fork this repository
- Create your feature branch
- Submit your improvements
- Initiate a Pull Request

### What are files 1, 2, 3?

These are auxiliary files in the repository:
- **File 1**: Report generator usage documentation
- **File 2**: GitHub Actions workflow YAML configuration
- **File 3**: Python report generator source code (backup copy of `report_generator.py`)

Note: Primarily use `report_generator.py`. Files 1-3 are separate document copies retained for easy viewing.

### What software is needed?

- **Python Report Generator**: Python 3.7+ and pip
- **VLAN Experiment**: Cisco Packet Tracer (version 7.0 or higher recommended)

### What if I have other questions?

If you have any questions, suggestions, or found a bug, welcome to:
1. Create an Issue in the GitHub repository
2. Check existing Issues to see if there's already a related discussion
3. Directly modify the code and submit a Pull Request

---

## Technical Support

If you encounter problems during use, please:
1. Carefully read this FAQ document
2. Check the relevant README documents (`README.md`, `pt-vlan-assignment/README.zh-CN.md`)
3. Check GitHub Issues for similar problems
4. Create a new Issue describing your problem

Happy using!
