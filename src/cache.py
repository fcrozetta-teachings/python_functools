import functools, time
from utils.print_result import CompareTableResult, t


@functools.cache
def long_calculation_cached(x: int):
    print(f"Running my expensive calculation for {x}")
    time.sleep(10)
    return x * x


if __name__ == "__main__":
    table = CompareTableResult("Cache comparison", [" Call #1 (secs)", " Cache info "])
    table.addRow(
        [t(long_calculation_cached, 10), str(long_calculation_cached.cache_info())]
    )
    # table.addRow(["3", t(long_calculation_cached, 3), t(long_calculation_cached, 3)])
    print(table)
