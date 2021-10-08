from io import StringIO
import sys
from contextlib import contextmanager


class CaptureOutput:
    def __init__(self):
        self.new_out = StringIO()
        self.new_err = StringIO()
        self.old_out = sys.stdout
        self.old_err = sys.stderr

    def __enter__(self):
        sys.stdout = self.new_out
        sys.stderr = self.new_err
        return sys.stdout, sys.stderr

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.old_out
        sys.stderr = self.old_err
        return True


@contextmanager
def capture_output():
    new_out = StringIO()
    new_err = StringIO()
    old_out = sys.stdout
    old_err = sys.stderr
    try:
        sys.stdout = new_out
        sys.stderr = new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout = old_out
        sys.stderr = old_err