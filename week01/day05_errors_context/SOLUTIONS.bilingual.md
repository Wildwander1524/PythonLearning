# ✅ Day 5 — SOLUTIONS
> 🇨🇳 **第 5 天 — 解决方案**

> After a real attempt only.
> 🇨🇳 请仅在真正尝试之后查阅。

## Reference — `logkit/`
> 🇨🇳 **参考 — `logkit/`**

```python
# logkit/errors.py
class LogError(Exception): ...                  # base for the package
class LogLevelError(LogError): ...              # unknown level (is-a LogError)

# logkit/logger.py
from datetime import datetime
from .errors import LogError, LogLevelError

class FileLogger:
    def __init__(self, path, allowed_levels=None):
        self.path = path
        self.allowed = allowed_levels or {"INFO", "WARN", "ERROR"}   # None-sentinel, not mutable default
        self._file = None
    def __enter__(self):
        self._file = open(self.path, "a", encoding="utf-8")          # acquire
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._file:
            self._file.close()                                       # release — runs even on error
        return False                                                 # don't suppress the exception
    def write(self, level, message):
        if self._file is None:
            raise LogError("logger used outside its 'with' block")
        if level not in self.allowed:
            raise LogLevelError(f"unknown level: {level}")
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._file.write(f"{ts} [{level}] {message}\n")

# logkit/__init__.py  (the index card)
from .logger import FileLogger
from .errors import LogError, LogLevelError
```
> 🇨🇳 *[定义日志包的错误类型和文件日志器，支持上下文管理器与级别过滤]*

**The key proof (error-path test):**
> 🇨🇳 **关键证明（错误路径测试）：**

```python
def test_file_closed_even_on_error():
    log = FileLogger("test.log")
    try:
        with log:
            log.write("INFO", "x")
            raise ValueError("boom")        # force a failure inside the block
    except ValueError:
        pass
    assert log._file.closed is True         # __exit__ closed it anyway ✅
```
> 🇨🇳 *[测试即使在 `with` 块内抛出异常，文件仍能正确关闭]*

## RECALL answers
> 🇨🇳 **回顾答案**

**Spaced:** S1 raise at the cause so the failure is close to where it's understandable (raise
early, catch late); later it's harder to diagnose. S2 `__iter__` (best via `yield`), or
`__getitem__` indexed until `IndexError`. S3 one list created at `def`-time, shared across calls;
fix = `None`-sentinel / `field(default_factory=list)`.
> 🇨🇳 **Spaced（间隔复习）:** S1 在原因处抛出异常，使失败靠近可理解的位置（早抛出，晚捕获）；拖后更难诊断。S2 实现 `__iter__`（最好通过 `yield`），或通过 `__getitem__` 索引直到 `IndexError`。S3 在 `def` 时创建一个列表，跨调用共享；解决方法：使用 `None` 哨兵值 / `field(default_factory=list)`。

**A:** It guarantees a resource is set up on entry and **torn down on exit by any path** (success,
exception, early return). Methods: `__enter__` and `__exit__`. Analogy: a rental car that returns
itself even after a breakdown.
> 🇨🇳 **A:** 它保证资源在进入时设置，并在**任何出口路径**（成功、异常、提前返回）下拆除。方法：`__enter__` 和 `__exit__`。类比：租来的车，即使发生故障也会自动归还。

**B** 1. `except` runs on a matching raise; `else` only if the try raised nothing; `finally`
always. 2. EAFP avoids the gap between checking and using (the resource could change in between)
and is cleaner. 3. A hierarchy lets a caller catch the *specific* error (precise recovery) **or**
the base (broad handling); one `Exception` forces "something failed" with no granularity. 4.
`True` suppresses the exception (swallows it) — dangerous default; `False` lets real errors
propagate. 5. An `__init__.py` makes the folder a package; the `__main__` guard runs a block only
when the file is executed directly, not imported.
> 🇨🇳 **B** 1. `except` 在匹配异常时执行；`else` 仅在 `try` 块没有引发任何异常时运行；`finally` 总是执行。2. EAFP 避免了检查和使用之间的间隙（资源可能在其间变化），且更简洁。3. 异常层次结构允许调用者捕获**特定**错误（精确恢复）**或**基类（宽泛处理）；只用一个 `Exception` 只能表示"出了点问题"，没有粒度。4. `True` 会抑制异常（吞掉错误）——危险的默认值；`False` 让真实错误继续传播。5. `__init__.py` 使文件夹成为包；`__main__` 守卫使代码块仅在直接执行文件时运行，而非导入时。

**C · Predict:** prints `enter`, `body`, `exit`, then the `ValueError` propagates — so `"after"`
**does not** print. `__exit__` runs (prints `exit`) on the error path but returns `False`, so the
exception keeps going and aborts before `print("after")`.
> 🇨🇳 **C · 预测:** 打印 `enter`、`body`、`exit`，然后 `ValueError` 继续传播——因此 `"after"` **不会**打印。`__exit__` 在错误路径上运行（打印 `exit`），但返回 `False`，所以异常继续传播并在 `print("after")` 之前终止程序。

**D · Micro-build:**
> 🇨🇳 **D · 微型构建：**

```python
import os, tempfile
class TempFile:
    def __enter__(self):
        fd, self.path = tempfile.mkstemp()
        os.close(fd)
        return self.path
    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.path)         # ← guarantees deletion on EVERY exit path, incl. exceptions
        return False
# Deletion is guaranteed because os.remove lives in __exit__, which Python calls
# regardless of how the with-block ends.
```
> 🇨🇳 *[实现 `TempFile` 上下文管理器，在 `__exit__` 中确保删除临时文件，覆盖所有退出路径]*

**E · Math:** 1. `7·[1,0] + (-2)·[0,1]`. 2. **Independent** (different directions) → they span the
whole 2-D plane. 3. `span([0,0]) = {[0,0]}` — scaling the zero vector always gives zero; it's just
the origin.
> 🇨🇳 **E · 数学:** 1. `7·[1,0] + (-2)·[0,1]`。2. **线性无关**（不同方向）→ 它们张成整个二维平面。3. `span([0,0]) = {[0,0]}` —— 缩放零向量始终得到零向量；它只是原点。

## Concept-check answers (homework)
> 🇨🇳 **概念检查答案（家庭作业）**

1. `__exit__` runs on *every* exit path (incl. exceptions), so cleanup at the end of the `with`
   body would be skipped if the body raised first — the file would leak. 2. `True` would swallow
   every exception inside the block, hiding bugs; logging shouldn't hide the program's real
   errors, so `False`. 3. `LogLevelError` **is a** `LogError` (subclass), so catching the base
   catches the child; not vice-versa because a `LogError` isn't necessarily a `LogLevelError`.
> 🇨🇳 1. `__exit__` 在**每个**出口路径上运行（包括异常），因此如果将清理代码放在 `with` 块末尾，一旦块内先抛出异常，清理就会被跳过——导致文件泄露。2. `True` 会吞掉块内的所有异常，隐藏错误；日志记录不应掩盖程序的真实错误，所以用 `False`。3. `LogLevelError` **是** `LogError`（子类），因此捕获基类也会捕获子类；反之不行，因为 `LogError` 实例不一定是 `LogLevelError`。

> 📝 Record: did the `__exit__`-on-error behavior (C) surprise you? It's a Day-6 capstone reuse.
> 🇨🇳 📝 记录：`__exit__` 在错误时的行为（C 部分）让你感到意外吗？这是第 6 天的重点复用内容。
