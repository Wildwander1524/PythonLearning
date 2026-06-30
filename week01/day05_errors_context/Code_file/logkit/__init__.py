"""logkit — a tiny context-managed file logger package.

The package's "index card": re-export the public API so callers can write
`from logkit import FileLogger, LogError, LogLevelError` without knowing which
module each name lives in.
"""
from .loggers import FileLogger
from .errors import LogError, LogLevelError

__all__ = ["FileLogger", "LogError", "LogLevelError"]
