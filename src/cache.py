import functools
from utils.print_result import CompareTableResult, t


@functools.cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


def factorial_no_cache(n):
    return n * factorial_no_cache(n - 1) if n else 1


if __name__ == "__main__":
    print("Starting...")
    table = CompareTableResult(
        "Cache Comparation", ["Factorial", " Cached (sec) ", " Not Cached (sec) "]
    )

    table.addRow(["100", t(factorial, 100), t(factorial_no_cache, 100)])
    table.addRow(["50", t(factorial, 50), t(factorial_no_cache, 50)])
    table.addRow(["125", t(factorial, 125), t(factorial_no_cache, 125)])
    print(table)
