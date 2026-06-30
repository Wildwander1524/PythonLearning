"""Tests for logkit — the PROOF that the file always closes, plus the hierarchy.

pytest auto-discovers every `test_*` function. We use the `tmp_path` fixture so
each test writes to a fresh throwaway dir (no leftover files, nothing to .gitignore).
The key idiom: `with pytest.raises(SomeError):` asserts that the block raises that
error — call the failing line *inside* it (don't call it then `assert False`, because
the exception escapes before that assert ever runs).
"""
import re
from pathlib import Path

import pytest

from logkit import FileLogger, LogError, LogLevelError


def test_write_lines(tmp_path: Path) -> None:
    path = tmp_path / "app.log"
    with FileLogger(str(path)) as log:
        log.write("INFO", "line 1")
        log.write("WARN", "line 2")
    # Context exited -> file flushed & closed. It was opened append-only, so to READ
    # the contents we re-open the path (here via Path.read_text), not the logger handle.
    lines = path.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 2
    assert re.match(r"\d{4}-\d\d-\d\d \d\d:\d\d:\d\d \[INFO\] line 1", lines[0])


def test_unknown_level_raises(tmp_path: Path) -> None:
    with FileLogger(str(tmp_path / "app.log")) as log:
        with pytest.raises(LogLevelError):
            log.write("DEBUG", "x")          # DEBUG is not in the allowed set


def test_write_before_enter_raises_logerror(tmp_path: Path) -> None:
    log = FileLogger(str(tmp_path / "app.log"))
    with pytest.raises(LogError):
        log.write("INFO", "x")               # used outside its 'with' block -> LogError


def test_loglevelerror_is_caught_as_logerror(tmp_path: Path) -> None:
    # Proves the hierarchy: catching the PARENT (LogError) also catches the CHILD.
    with pytest.raises(LogError):
        with FileLogger(str(tmp_path / "app.log")) as log:
            log.write("DEBUG", "x")          # raises LogLevelError, which is-a LogError


def test_file_closed_even_on_error(tmp_path: Path) -> None:
    # THE key test: force a failure inside the block, assert the file closed anyway.
    log = FileLogger(str(tmp_path / "app.log"))
    with pytest.raises(ValueError):
        with log:
            log.write("INFO", "x")
            raise ValueError("boom")         # failure mid-block
    f = log.file
    assert f is not None                     # narrow file-or-None for the next line
    assert f.closed is True                  # __exit__ closed it on the error path
