# 📝 Day 5 Homework — Context-Managed Logger + a Package
> 🇨🇳 **第5天作业：上下文管理日志记录器 + 一个包**

> **Goal:** Write a file logger that uses the **context-manager** protocol (guaranteed file close), with a **custom exception hierarchy**, and ship it as a real importable **package** with `__init__.py`.
> **Time:** 3 h  ·  **Read first:** [`LESSON.md`](./LESSON.md)
> 🇨🇳 **目标：** 编写一个使用**上下文管理器**协议（保证文件关闭）的文件日志记录器，附有**自定义异常层次**，并将其打包成一个带有 `__init__.py` 的真正可导入的**包**。
> 🇨🇳 **时间：** 3小时 · **先读：**[`LESSON.md`](./LESSON.md)

---

## 📖 Before you start (5 min)
> 🇨🇳 **开始之前（5分钟）**

Skim these sections of [`LESSON.md`](./LESSON.md):
> 🇨🇳 速览 [`LESSON.md`](./LESSON.md) 的以下几个小节：

- **"Context managers"** (rental-car / self-returning library book) → the *guarantee* you're building: the file closes on **every** exit path.
- **"`__exit__`'s parameters"** + **"returns True/False"** → return `False` so exceptions propagate.
- **"The exception hierarchy"** + **"custom exceptions"** (labeled fuse box) → `LogError` → `LogLevelError`.
- **"Modules & packages"** (labeled drawers, the `__init__.py` index card) → the `logkit` layout.
- **"上下文管理器"**（租车 / 自己归还图书馆的书）→ 你要构建的*保证*：文件在**所有**退出路径上都会关闭。
- **"`__exit__` 的参数"** + **"返回 True/False"** → 返回 `False` 让异常传播。
- **"异常层次结构"** + **"自定义异常"**（带标签的保险丝盒）→ `LogError` → `LogLevelError`。
- **"模块与包"**（带标签的抽屉，`__init__.py` 索引卡）→ `logkit` 的布局。

> 🎯 **The one thing this homework must prove:** the file is closed **even when the `with` block raises**. That's the rental car returning itself after a breakdown. Your key test forces an error inside the block and asserts the file closed anyway.
> 🇨🇳 🎯 **本次作业必须证明的一件事：** 即使 `with` 块中抛出异常，文件**也会关闭**。就像是租车在故障后自行归还。你的关键测试是在 `with` 块内部制造一个错误，并断言文件无论如何都已关闭。

---

## ⏱️ Suggested time budget
> 🇨🇳 **建议时间预算**

| Block | Time | What you do |
|-------|------|-------------|
| **A** | 75 min | `FileLogger` context manager (`__enter__`/`__exit__`) + custom exceptions |
| **B** | 60 min | Turn the folder into a package (`__init__.py`) and import it from a script |
| **C** | 45 min | Tests, run, push |

| 阶段 | 时间 | 任务 |
|------|------|------|
| **A** | 75 分钟 | `FileLogger` 上下文管理器（`__enter__`/`__exit__`）+ 自定义异常 |
| **B** | 60 分钟 | 将文件夹变成包（`__init__.py`）并从脚本中导入使用 |
| **C** | 45 分钟 | 测试、运行、推送 |

## 📁 Files (note the package layout)
> 🇨🇳 **文件结构（注意包的布局）**

```text
week01/day05_errors_context/
├── logkit/                 # ← the package (a labeled drawer of tools)
│   ├── __init__.py         # the index card: exposes FileLogger + exceptions
│   ├── logger.py           # FileLogger class
│   └── errors.py           # LogError hierarchy
├── main.py                 # uses the package: `from logkit import FileLogger`
└── test_logkit.py
```
> 🇨🇳 *[logkit 包的目录结构：包含 `__init__.py` 作为包索引，`logger.py` 和 `errors.py` 模块，以及使用该包的 `main.py` 和测试脚本]*

---

## Part A — `FileLogger` + exceptions (75 min)
> 🇨🇳 **A 部分：`FileLogger` + 异常（75 分钟）**

**`errors.py`** — a small exception hierarchy (Day-2 inheritance, applied to errors):
> 🇨🇳 **`errors.py`** — 一个小的异常层次结构（第2天的继承应用于错误场景）：

- [ ] `LogError(Exception)` — base class for everything in this package
- [ ] `LogLevelError(LogError)` — raised for an unknown level
- [ ] `LogError(Exception)` — 该包中所有异常的基类
- [ ] `LogLevelError(LogError)` — 对未知日志级别抛出

**`logger.py`** — `FileLogger` usable as a context manager:
> 🇨🇳 **`logger.py`** — 可用作上下文管理器的 `FileLogger`：

```python
with FileLogger("app.log") as log:
    log.write("INFO", "started")
    log.write("ERROR", "something broke")
# file flushed & closed here automatically — even if the block raised
```
> 🇨🇳 *[演示 FileLogger 作为上下文管理器：即使块内出错，文件也会自动刷新并关闭]*

- [ ] `__init__(self, path, allowed_levels=None)` — store path; default levels `{"INFO","WARN","ERROR"}` (use the `None`-sentinel pattern, **not** a mutable default).
- [ ] `__enter__` opens the file (append mode) and returns `self` (the `as` target).
- [ ] `__exit__(self, exc_type, exc_val, exc_tb)` closes the file — **even if the block raised** — and returns `False` (don't suppress the exception).
- [ ] `write(level, message)` — raise `LogLevelError` if `level` not allowed; else write `2026-06-20 14:05:01 [INFO] started` (use `datetime.now()`).
- [ ] `write` *before* `__enter__` (file not open) raises `LogError` with a clear message.
- [ ] `__init__(self, path, allowed_levels=None)` — 存储路径；默认级别为 `{"INFO","WARN","ERROR"}`（使用 `None` 哨兵模式，**不要**用可变默认值）。
- [ ] `__enter__` 以追加模式打开文件，并返回 `self`（作为 `as` 的目标）。
- [ ] `__exit__(self, exc_type, exc_val, exc_tb)` 关闭文件 — **即使块中抛出异常** — 并返回 `False`（不抑制异常）。
- [ ] `write(level, message)` — 如果 `level` 不在允许的级别中，抛出 `LogLevelError`；否则写入类似 `2026-06-20 14:05:01 [INFO] started` 的格式（使用 `datetime.now()`）。
- [ ] 在进入上下文（`__enter__`）*之前*调用 `write` 时抛出 `LogError`，并附带清晰的消息。

> 💡 **The proof (write this test):** raise an exception *inside* the `with` block and afterward assert `log._file.closed is True`. If it's closed, your `__exit__` did its job on the failure path — the rental car returned itself.
> 🇨🇳 💡 **证据（写下这个测试）：** 在 `with` 块*内部*引发一个异常，之后断言 `log._file.closed is True`。如果文件已关闭，说明你的 `__exit__` 在失败路径上完成了工作 — 租车自己归还了。

## Part B — make it a package (60 min)
> 🇨🇳 **B 部分：把它变成一个包（60 分钟）**

- [ ] Add `__init__.py` so `logkit` is a package.
- [ ] In `__init__.py`, re-export the public API (the index card):
  ```python
  from .logger import FileLogger
  from .errors import LogError, LogLevelError
  ```
- [ ] `main.py` (sibling of `logkit/`) uses it cleanly: `from logkit import FileLogger, LogLevelError`.
- [ ] Confirm `python main.py` runs and writes a log file.
- [ ] 添加 `__init__.py` 使得 `logkit` 成为一个包。
- [ ] 在 `__init__.py` 中重新导出公共 API（索引卡）：
  ```python
  from .logger import FileLogger
  from .errors import LogError, LogLevelError
  ```
  > 🇨🇳 *[`__init__.py` 中重新导出 `FileLogger` 和异常类的代码]*
- [ ] `main.py`（与 `logkit/` 同级）干净地导入：`from logkit import FileLogger, LogLevelError`。
- [ ] 确认 `python main.py` 能够运行并写出日志文件。

## Part C — tests (45 min)
> 🇨🇳 **C 部分：测试（45 分钟）**

- [ ] `with FileLogger(...)` writes lines; the file exists with the expected number of lines
- [ ] An unknown level (`log.write("DEBUG", ...)`) raises `LogLevelError`
- [ ] **The file is closed after the `with` block even when the block raises** (the key test)
- [ ] `write()` before entering the context raises `LogError`
- [ ] `LogLevelError` is catchable as `LogError` (proves the hierarchy — catch the parent, get the child)
- [ ] `with FileLogger(...)` 写入行；文件存在且行数符合预期
- [ ] 未知级别（`log.write("DEBUG", ...)`）引发 `LogLevelError`
- [ ] **即使 `with` 块中抛出异常，文件在块结束后也已关闭**（关键测试）
- [ ] 在进入上下文之前调用 `write()` 引发 `LogError`
- [ ] `LogLevelError` 可以被当作 `LogError` 捕获（证明层次结构 — 捕获父类，拿到子类）

> 💡 Use a temp filename in tests and delete it at the end (`os.remove`), or write to `test.log` and `.gitignore` it.
> 🇨🇳 💡 在测试中使用临时文件名，并在结束后删除（`os.remove`），或者写入 `test.log` 并将其加入 `.gitignore`。

---

## 🧠 Concept checks (comment at the bottom of `logger.py`)
> 🇨🇳 **概念检查（写在 `logger.py` 底部的注释中）**

1. Why put `self._file.close()` logic in `__exit__` rather than at the end of the `with` block? (Rental-car reasoning.)
2. What would happen if `__exit__` returned `True`? Why is `False` the right default here?
3. Why does catching `LogError` also catch `LogLevelError`, but not vice versa?
1. 为什么要把 `self._file.close()` 的逻辑放在 `__exit__` 中，而不是放在 `with` 块的末尾？（租车的类比推理。）
2. 如果 `__exit__` 返回 `True` 会发生什么？为什么这里的默认值 `False` 是正确的？
3. 为什么捕获 `LogError` 也能捕获 `LogLevelError`，反之则不行？

## ✅ Definition of done
> 🇨🇳 **完成标准**

- [ ] `FileLogger` works as a context manager and **always closes** the file (proven by the error-path test)
- [ ] Custom exception hierarchy used and tested
- [ ] `logkit` is a real package importable via `from logkit import FileLogger`
- [ ] All tests pass; concept checks answered; pushed to GitHub
- [ ] `FileLogger` 可作为上下文管理器使用，并**总是关闭**文件（通过错误路径测试证明）
- [ ] 自定义异常层次结构已使用并经过测试
- [ ] `logkit` 是一个真正的包，可通过 `from logkit import FileLogger` 导入
- [ ] 所有测试通过；概念检查已回答；已推送到 GitHub

## 🌟 Stretch
> 🇨🇳 **进阶挑战**

- Add a `contextlib.contextmanager` generator version and compare it to the class version (the shortcut from `LEARNING.md`).
- Support a severity **threshold** (only write messages at/above a minimum level — `INFO < WARN < ERROR`).
- Add `__repr__` showing path + open/closed state (Day-3 skill).
- Make the logger reusable across multiple `with` blocks (re-open on each `__enter__`).
- 添加一个 `contextlib.contextmanager` 生成器版本，并与类版本进行比较（来自 `LEARNING.md` 的快捷方式）。
- 支持严重级别**阈值**（仅写入达到/高于最低级别的消息 — `INFO < WARN < ERROR`）。
- 添加 `__repr__` 显示路径和打开/关闭状态（第3天技能）。
- 使记录器可在多个 `with` 块中重复使用（每次 `__enter__` 时重新打开）。

---

## 🚀 Submit
> 🇨🇳 **提交**

```bash
git add week01/day05_errors_context
git commit -m "add: Week1 D5 context-managed logger package"
git push
```
> 🇨🇳 *[提交和推送作业的 Git 命令]*

➡️ Then [`RECALL.md`](./RECALL.md), and again cold before Day 6.
> 🇨🇳 然后转到 [`RECALL.md`](./RECALL.md)，并在第6天之前再次冷回顾。
