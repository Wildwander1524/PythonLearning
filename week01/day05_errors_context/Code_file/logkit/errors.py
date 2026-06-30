"""logkit exception hierarchy — Day-2 inheritance applied to errors.

One base class (LogError) so callers can catch the whole family with
`except LogError:`. A specific subclass (LogLevelError) for one precise failure.
"""


class LogError(Exception):
    """Base class for *every* error raised by logkit.

    Subclasses Exception (NOT BaseException — M16): a normal
    `except Exception:` must be able to see it. BaseException is reserved for
    system-exit signals like KeyboardInterrupt / SystemExit.
    """


class LogLevelError(LogError):
    """Raised by write() when the level is outside the allowed set.

    is-a LogError, so `except LogError:` already catches it (see concept-check 3
    in loggers.py).
    """
