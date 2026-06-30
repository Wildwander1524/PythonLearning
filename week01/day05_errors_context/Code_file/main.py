"""Demo: use the logkit package to write a log file.

Run from this folder:  python main.py
It writes app.log, then shows the custom exception in action.
"""
from logkit import FileLogger, LogLevelError

if __name__ == "__main__":
    # Normal use: the `with` block guarantees the file is flushed & closed on exit.
    with FileLogger("app.log") as log:
        log.write("INFO", "app started")
        log.write("ERROR", "something broke")
    # <- file is already closed here, automatically.

    # The custom exception hierarchy in action: a bad level raises LogLevelError.
    try:
        with FileLogger("app.log") as log:
            log.write("DEBUG", "this level is not allowed")
    except LogLevelError as e:
        print(f"caught LogLevelError: {e}")

    print("done — see app.log")
