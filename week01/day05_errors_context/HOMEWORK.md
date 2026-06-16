# 📝 Day 5 Homework — Context-Managed Logger + a Package

> **Goal:** Write a file logger that uses the **context-manager** protocol (guaranteed file close), with a **custom exception hierarchy**, and ship it as a real importable **package** with `__init__.py`.
> **Time:** 3 h  ·  **Read first:** [`LEARNING.md`](./LEARNING.md)

---

## 📖 Before you start (5 min)

Skim these sections of [`LEARNING.md`](./LEARNING.md):
- **"Context managers"** (rental-car / self-returning library book) → the *guarantee* you're building: the file closes on **every** exit path.
- **"`__exit__`'s parameters"** + **"returns True/False"** → return `False` so exceptions propagate.
- **"The exception hierarchy"** + **"custom exceptions"** (labeled fuse box) → `LogError` → `LogLevelError`.
- **"Modules & packages"** (labeled drawers, the `__init__.py` index card) → the `logkit` layout.

> 🎯 **The one thing this homework must prove:** the file is closed **even when the `with` block raises**. That's the rental car returning itself after a breakdown. Your key test forces an error inside the block and asserts the file closed anyway.

---

## ⏱️ Suggested time budget

| Block | Time | What you do |
|-------|------|-------------|
| **A** | 75 min | `FileLogger` context manager (`__enter__`/`__exit__`) + custom exceptions |
| **B** | 60 min | Turn the folder into a package (`__init__.py`) and import it from a script |
| **C** | 45 min | Tests, run, push |

## 📁 Files (note the package layout)

```text
week01/day05_errors_context/
├── logkit/                 # ← the package (a labeled drawer of tools)
│   ├── __init__.py         # the index card: exposes FileLogger + exceptions
│   ├── logger.py           # FileLogger class
│   └── errors.py           # LogError hierarchy
├── main.py                 # uses the package: `from logkit import FileLogger`
└── test_logkit.py
```

---

## Part A — `FileLogger` + exceptions (75 min)

**`errors.py`** — a small exception hierarchy (Day-2 inheritance, applied to errors):
- [ ] `LogError(Exception)` — base class for everything in this package
- [ ] `LogLevelError(LogError)` — raised for an unknown level

**`logger.py`** — `FileLogger` usable as a context manager:

```python
with FileLogger("app.log") as log:
    log.write("INFO", "started")
    log.write("ERROR", "something broke")
# file flushed & closed here automatically — even if the block raised
```

- [ ] `__init__(self, path, allowed_levels=None)` — store path; default levels `{"INFO","WARN","ERROR"}` (use the `None`-sentinel pattern, **not** a mutable default).
- [ ] `__enter__` opens the file (append mode) and returns `self` (the `as` target).
- [ ] `__exit__(self, exc_type, exc_val, exc_tb)` closes the file — **even if the block raised** — and returns `False` (don't suppress the exception).
- [ ] `write(level, message)` — raise `LogLevelError` if `level` not allowed; else write `2026-06-20 14:05:01 [INFO] started` (use `datetime.now()`).
- [ ] `write` *before* `__enter__` (file not open) raises `LogError` with a clear message.

> 💡 **The proof (write this test):** raise an exception *inside* the `with` block and afterward assert `log._file.closed is True`. If it's closed, your `__exit__` did its job on the failure path — the rental car returned itself.

## Part B — make it a package (60 min)

- [ ] Add `__init__.py` so `logkit` is a package.
- [ ] In `__init__.py`, re-export the public API (the index card):
  ```python
  from .logger import FileLogger
  from .errors import LogError, LogLevelError
  ```
- [ ] `main.py` (sibling of `logkit/`) uses it cleanly: `from logkit import FileLogger, LogLevelError`.
- [ ] Confirm `python main.py` runs and writes a log file.

## Part C — tests (45 min)

- [ ] `with FileLogger(...)` writes lines; the file exists with the expected number of lines
- [ ] An unknown level (`log.write("DEBUG", ...)`) raises `LogLevelError`
- [ ] **The file is closed after the `with` block even when the block raises** (the key test)
- [ ] `write()` before entering the context raises `LogError`
- [ ] `LogLevelError` is catchable as `LogError` (proves the hierarchy — catch the parent, get the child)

> 💡 Use a temp filename in tests and delete it at the end (`os.remove`), or write to `test.log` and `.gitignore` it.

---

## 🧠 Concept checks (comment at the bottom of `logger.py`)

1. Why put `self._file.close()` logic in `__exit__` rather than at the end of the `with` block? (Rental-car reasoning.)
2. What would happen if `__exit__` returned `True`? Why is `False` the right default here?
3. Why does catching `LogError` also catch `LogLevelError`, but not vice versa?

## ✅ Definition of done

- [ ] `FileLogger` works as a context manager and **always closes** the file (proven by the error-path test)
- [ ] Custom exception hierarchy used and tested
- [ ] `logkit` is a real package importable via `from logkit import FileLogger`
- [ ] All tests pass; concept checks answered; pushed to GitHub

## 🌟 Stretch

- Add a `contextlib.contextmanager` generator version and compare it to the class version (the shortcut from `LEARNING.md`).
- Support a severity **threshold** (only write messages at/above a minimum level — `INFO < WARN < ERROR`).
- Add `__repr__` showing path + open/closed state (Day-3 skill).
- Make the logger reusable across multiple `with` blocks (re-open on each `__enter__`).

---

## 🚀 Submit

```bash
git add week01/day05_errors_context
git commit -m "add: Week1 D5 context-managed logger package"
git push
```
