# ✅ Day 5 — SOLUTIONS

> After a real attempt only.

## Reference — `logkit/`
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
**The key proof (error-path test):**
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

## RECALL answers
**Spaced:** S1 raise at the cause so the failure is close to where it's understandable (raise
early, catch late); later it's harder to diagnose. S2 `__iter__` (best via `yield`), or
`__getitem__` indexed until `IndexError`. S3 one list created at `def`-time, shared across calls;
fix = `None`-sentinel / `field(default_factory=list)`.

**A:** It guarantees a resource is set up on entry and **torn down on exit by any path** (success,
exception, early return). Methods: `__enter__` and `__exit__`. Analogy: a rental car that returns
itself even after a breakdown.

**B** 1. `except` runs on a matching raise; `else` only if the try raised nothing; `finally`
always. 2. EAFP avoids the gap between checking and using (the resource could change in between)
and is cleaner. 3. A hierarchy lets a caller catch the *specific* error (precise recovery) **or**
the base (broad handling); one `Exception` forces "something failed" with no granularity. 4.
`True` suppresses the exception (swallows it) — dangerous default; `False` lets real errors
propagate. 5. An `__init__.py` makes the folder a package; the `__main__` guard runs a block only
when the file is executed directly, not imported.

**C · Predict:** prints `enter`, `body`, `exit`, then the `ValueError` propagates — so `"after"`
**does not** print. `__exit__` runs (prints `exit`) on the error path but returns `False`, so the
exception keeps going and aborts before `print("after")`.

**D · Micro-build:**
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

**E · Math:** 1. `7·[1,0] + (-2)·[0,1]`. 2. **Independent** (different directions) → they span the
whole 2-D plane. 3. `span([0,0]) = {[0,0]}` — scaling the zero vector always gives zero; it's just
the origin.

## Concept-check answers (homework)
1. `__exit__` runs on *every* exit path (incl. exceptions), so cleanup at the end of the `with`
   body would be skipped if the body raised first — the file would leak. 2. `True` would swallow
   every exception inside the block, hiding bugs; logging shouldn't hide the program's real
   errors, so `False`. 3. `LogLevelError` **is a** `LogError` (subclass), so catching the base
   catches the child; not vice-versa because a `LogError` isn't necessarily a `LogLevelError`.

> 📝 Record: did the `__exit__`-on-error behavior (C) surprise you? It's a Day-6 capstone reuse.
