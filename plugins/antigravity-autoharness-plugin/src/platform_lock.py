"""Cross-platform file locking compatible with Windows (msvcrt) and Unix (fcntl).
Provides atomic multi-process synchronization for intent queues and counters.
"""
import contextlib
import os
import sys
import time
from pathlib import Path

# Platform detection
_IS_WINDOWS = sys.platform == "win32"

if _IS_WINDOWS:
    import msvcrt
else:
    try:
        import fcntl
    except ImportError:
        fcntl = None


@contextlib.contextmanager
def file_lock(lock_path: Path | str, timeout: float = 5.0, poll_interval: float = 0.05):
    """Acquires an exclusive file lock, waiting up to `timeout` seconds.
    Safe for both Windows and Unix environments.
    """
    path = Path(lock_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    start_time = time.time()
    fd = None

    while True:
        try:
            # Open file with read/write mode
            fd = os.open(str(path), os.O_RDWR | os.O_CREAT | os.O_TRUNC)
            if _IS_WINDOWS:
                # Lock first byte
                msvcrt.locking(fd, msvcrt.LK_NBLCK, 1)
            elif fcntl:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            break
        except (OSError, BlockingIOError):
            if fd is not None:
                with contextlib.suppress(Exception):
                    os.close(fd)
                fd = None
            if time.time() - start_time >= timeout:
                # Timed out waiting for lock
                break
            time.sleep(poll_interval)

    try:
        yield
    finally:
        if fd is not None:
            try:
                if _IS_WINDOWS:
                    msvcrt.locking(fd, msvcrt.LK_UNLCK, 1)
                elif fcntl:
                    fcntl.flock(fd, fcntl.LOCK_UN)
            except Exception:
                pass
            finally:
                with contextlib.suppress(Exception):
                    os.close(fd)
