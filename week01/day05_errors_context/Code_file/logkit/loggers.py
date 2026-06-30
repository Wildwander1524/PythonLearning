"""FileLogger — a file logger usable as a context manager (guaranteed close)."""
from __future__ import annotations  # lets __enter__ annotate its own class (-> FileLogger)

from datetime import datetime
from io import TextIOWrapper
from types import TracebackType

from .errors import LogError, LogLevelError


class FileLogger:
    def __init__(self, path: str, allowed_levels: set[str] | None = None) -> None:
        self.path = path
        # None-sentinel: ask the ONE literal question — "did the caller pass None?"
        # Use `is not None`, NOT `or`/`bool()`. `or` asks "is it truthy?", which would
        # silently clobber an explicit empty set() (a caller saying "allow nothing").
        self.allowed = allowed_levels if allowed_levels is not None else {"INFO", "WARN", "ERROR"}
        # Typed file-or-None: None means "not open"; set to a real handle by __enter__.
        self._file: TextIOWrapper | None = None

    @property
    def file(self) -> TextIOWrapper | None:
        """Read-only view of the underlying handle (lets callers/tests check .closed)."""
        return self._file

    def __enter__(self) -> FileLogger:
        self._file = open(self.path, "a", encoding="utf-8")  # acquire: open in append mode
        return self                                          # bound to the `as` target

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool:
        # Runs on EVERY exit path — normal completion OR an exception — exactly like finally.
        if self._file is not None:   # narrows "file-or-None" -> "file", so .close() is type-safe
            self._file.close()       # release: guaranteed, even when the block raised
        return False                 # falsy -> do NOT suppress; let the exception propagate

    def write(self, level: str, message: str) -> None:
        if self._file is None:       # write() called before __enter__ -> misuse of the API
            raise LogError("logger used outside its 'with' block")
        if level not in self.allowed:  # unknown level -> the package's specific error
            raise LogLevelError(f"unknown level: {level}")
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._file.write(f"{ts} [{level}] {message}\n")


# ── Concept checks ──────────────────────────────────────────────────────────
# 1. Why put close() in __exit__ instead of at the end of the `with` body?
#    __exit__ is GUARANTEED to run on every exit path — normal end OR an exception
#    thrown mid-block. Code written after the body's last line is SKIPPED when the
#    body raises, so the file would leak. It's the rental car that returns itself
#    even after a breakdown.
#
# 2. What would happen if __exit__ returned True? Why is False the right default?
#    Returning True (truthy) SUPPRESSES any exception raised inside the block — the
#    error vanishes silently (M17). False (or None) lets it propagate. We want to
#    clean up but NOT hide bugs, so False is the correct default.
#
# 3. Why does `except LogError` catch LogLevelError, but not vice versa?
#    LogLevelError IS-A LogError (subclass), so it already *is* a LogError —
#    catching the parent catches every child. The reverse fails: a plain LogError is
#    NOT a LogLevelError, so `except LogLevelError` would sail right past it.
