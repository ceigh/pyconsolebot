import sys
from contextlib import contextmanager
from io import StringIO


@contextmanager
def stdout_io(new_stdout=None):
    old_stdout = sys.stdout
    if new_stdout is None:
        new_stdout = StringIO()
    sys.stdout = new_stdout
    yield new_stdout
    sys.stdout = old_stdout


def get_output(request: str) -> str:
    with stdout_io() as s:
        try:
            exec(request)
            response = s.getvalue()
        except Exception as e:
            response = e
    return response
