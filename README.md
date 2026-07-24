# Codex Auto Test

这是一个用于测试 Codex 自动修改和提交代码的最小 Python 项目。

## 功能

统计一段文本中的字符数、非空字符数和单词数，同时支持直接输入文本或读取文本文件。

## 直接统计文本

```bash
python text_counter.py "Hello Codex"
```

预期输出：

```text
字符数: 11
非空字符数: 10
单词数: 2
```

## 统计文件

```bash
python text_counter.py --file README.md
```

## 测试

```bash
python -m unittest -v
```

本项目只使用 Python 标准库，不需要安装额外依赖。
