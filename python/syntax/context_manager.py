import time
from datetime import UTC, datetime


class Measure:
    def __init__(self, msg: str):
        self._msg = msg
        self.time = None

    def __enter__(self):
        print(">>> {}".format(self._msg))
        self.time = datetime.now(UTC)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end = datetime.now(UTC)
        self.time = end - self.time
        print("<<< {} ({} sec)".format(self._msg, self.time.total_seconds()))
        if traceback:
            print(exc_type)
            print(exc_value)
            print(traceback)


def some_heavy_calc():
    time.sleep(1)

    return 10


with Measure("some_heavy_calc"):
    some_heavy_calc()
