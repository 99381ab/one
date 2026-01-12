# 贡献指南 (Contributing Guide)

感谢您考虑为本项目做出贡献！

[English version below](#english-version)

## 中文版

### 如何贡献

我们欢迎各种形式的贡献，包括但不限于：

- 🐛 报告 Bug
- 💡 提出新功能建议
- 📝 改进文档
- 🔧 提交代码修复或新功能
- ✨ 优化现有代码

### 报告 Bug

如果您发现了 Bug，请创建一个 Issue 并包含以下信息：

1. **清晰的标题** - 简要描述问题
2. **重现步骤** - 详细说明如何重现该问题
3. **预期行为** - 说明您期望发生什么
4. **实际行为** - 说明实际发生了什么
5. **环境信息** - 包括：
   - 操作系统（如：Windows 10, Ubuntu 22.04）
   - Python 版本（如：Python 3.11.0）
   - 相关软件版本（如：Packet Tracer 8.0）
6. **截图或日志** - 如果适用，提供截图或错误日志

### 提出新功能

如果您有新功能的想法，请创建一个 Issue 并说明：

1. **功能描述** - 详细描述您想要的功能
2. **使用场景** - 说明这个功能在什么情况下有用
3. **建议的实现方式** - 如果您有想法，可以描述如何实现
4. **替代方案** - 是否考虑过其他解决方案

### 提交代码

#### 开发流程

1. **Fork 仓库**
   ```bash
   # 在 GitHub 上点击 Fork 按钮
   git clone https://github.com/<your-username>/one.git
   cd one
   ```

2. **创建分支**
   ```bash
   git checkout -b feature/your-feature-name
   # 或
   git checkout -b fix/your-bug-fix
   ```

3. **进行更改**
   - 编写代码
   - 确保代码风格一致
   - 添加必要的注释
   - 更新相关文档

4. **测试您的更改**
   ```bash
   # 对于 Python 报告生成器
   python report_generator.py --out test.docx
   
   # 确保生成的文档正确
   ```

5. **提交更改**
   ```bash
   git add .
   git commit -m "feat: 添加新功能的描述"
   # 或
   git commit -m "fix: 修复某个问题的描述"
   ```

6. **推送到您的 Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **创建 Pull Request**
   - 前往 GitHub 上的原仓库
   - 点击 "New Pull Request"
   - 选择您的分支
   - 填写 PR 描述

#### 提交信息规范

我们使用约定式提交（Conventional Commits）规范：

- `feat:` - 新功能
- `fix:` - Bug 修复
- `docs:` - 文档更改
- `style:` - 代码格式调整（不影响功能）
- `refactor:` - 代码重构
- `test:` - 添加或修改测试
- `chore:` - 构建过程或辅助工具的变动

**示例：**
```
feat: 添加自定义字体支持
fix: 修复表格边框显示问题
docs: 更新 README 中的安装说明
```

#### 代码风格

**Python 代码：**
- 遵循 PEP 8 规范
- 使用 4 个空格缩进
- 函数和变量使用 snake_case
- 类使用 PascalCase
- 添加适当的类型提示（Type Hints）
- 添加文档字符串（Docstrings）

**示例：**
```python
def generate_report(name: str, student_id: str) -> str:
    """
    生成学生报告
    
    Args:
        name: 学生姓名
        student_id: 学号
        
    Returns:
        生成的报告文件路径
    """
    # 实现代码
    pass
```

**配置文件：**
- 保持现有格式
- 添加适当的注释说明

### 改进文档

文档改进同样重要！您可以：

- 修正拼写或语法错误
- 改进现有说明的清晰度
- 添加更多示例
- 翻译文档到其他语言
- 添加常见问题解答

### Pull Request 检查清单

提交 PR 前，请确保：

- [ ] 代码已经过测试
- [ ] 遵循了代码风格指南
- [ ] 更新了相关文档
- [ ] 提交信息清晰且遵循规范
- [ ] PR 描述详细说明了更改内容
- [ ] 没有引入新的警告或错误

### 行为准则

参与本项目时，请：

- ✅ 保持友好和尊重
- ✅ 欢迎不同的观点和经验
- ✅ 接受建设性的批评
- ✅ 关注对社区最有利的事情
- ❌ 不要使用攻击性语言
- ❌ 不要骚扰他人

### 问题和帮助

如果您有任何疑问：

1. 查看 [FAQ](FAQ.zh-CN.md)
2. 搜索现有的 [Issues](https://github.com/99381ab/one/issues)
3. 创建新的 Issue 提问

### 许可

通过贡献代码，您同意您的贡献将在与本项目相同的许可下发布。

---

## English Version

### How to Contribute

We welcome all forms of contributions, including but not limited to:

- 🐛 Reporting bugs
- 💡 Suggesting new features
- 📝 Improving documentation
- 🔧 Submitting code fixes or new features
- ✨ Optimizing existing code

### Reporting Bugs

If you find a bug, please create an Issue with the following information:

1. **Clear title** - Briefly describe the issue
2. **Steps to reproduce** - Detailed steps to reproduce the problem
3. **Expected behavior** - What you expected to happen
4. **Actual behavior** - What actually happened
5. **Environment information** - Including:
   - Operating system (e.g., Windows 10, Ubuntu 22.04)
   - Python version (e.g., Python 3.11.0)
   - Relevant software versions (e.g., Packet Tracer 8.0)
6. **Screenshots or logs** - If applicable, provide screenshots or error logs

### Suggesting Features

If you have an idea for a new feature, please create an Issue explaining:

1. **Feature description** - Detailed description of the desired feature
2. **Use case** - Explain when this feature would be useful
3. **Suggested implementation** - If you have ideas, describe how to implement it
4. **Alternatives** - Have you considered other solutions

### Submitting Code

#### Development Workflow

1. **Fork the repository**
   ```bash
   # Click Fork button on GitHub
   git clone https://github.com/your-username/one.git
   cd one
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

3. **Make changes**
   - Write code
   - Ensure consistent code style
   - Add necessary comments
   - Update relevant documentation

4. **Test your changes**
   ```bash
   # For Python report generator
   python report_generator.py --out test.docx
   
   # Ensure the generated document is correct
   ```

5. **Commit changes**
   ```bash
   git add .
   git commit -m "feat: description of new feature"
   # or
   git commit -m "fix: description of bug fix"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your branch
   - Fill in PR description

#### Commit Message Convention

We use Conventional Commits specification:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code formatting (no functional changes)
- `refactor:` - Code refactoring
- `test:` - Adding or modifying tests
- `chore:` - Build process or auxiliary tool changes

**Examples:**
```
feat: add custom font support
fix: fix table border display issue
docs: update installation instructions in README
```

#### Code Style

**Python Code:**
- Follow PEP 8 guidelines
- Use 4 spaces for indentation
- Use snake_case for functions and variables
- Use PascalCase for classes
- Add appropriate type hints
- Add docstrings

**Example:**
```python
def generate_report(name: str, student_id: str) -> str:
    """
    Generate student report
    
    Args:
        name: Student name
        student_id: Student ID
        
    Returns:
        Path to the generated report file
    """
    # Implementation
    pass
```

**Configuration Files:**
- Maintain existing format
- Add appropriate explanatory comments

### Improving Documentation

Documentation improvements are equally important! You can:

- Fix spelling or grammar errors
- Improve clarity of existing instructions
- Add more examples
- Translate documentation to other languages
- Add FAQ entries

### Pull Request Checklist

Before submitting a PR, ensure:

- [ ] Code has been tested
- [ ] Code style guidelines are followed
- [ ] Relevant documentation is updated
- [ ] Commit messages are clear and follow conventions
- [ ] PR description details the changes
- [ ] No new warnings or errors introduced

### Code of Conduct

When participating in this project, please:

- ✅ Be friendly and respectful
- ✅ Welcome different viewpoints and experiences
- ✅ Accept constructive criticism
- ✅ Focus on what's best for the community
- ❌ Don't use offensive language
- ❌ Don't harass others

### Questions and Help

If you have any questions:

1. Check the [FAQ](FAQ.md)
2. Search existing [Issues](https://github.com/99381ab/one/issues)
3. Create a new Issue to ask

### License

By contributing code, you agree that your contributions will be released under the same license as this project.

---

Thank you for your contribution! 感谢您的贡献！
