import functools, time

@functools.cache
def factorial(n):
    return n * factorial(n-1) if n else 1

def factorial_no_cache(n):
    return n * factorial_no_cache(n-1) if n else 1

if __name__ == "__main__":
    print("Starting cached function")

    s1 = time.perf_counter()
    factorial(100)
    e1 = time.perf_counter()
    print(f"factorial(100) took: {e1 - s1}")

    s2 = time.perf_counter()
    factorial(50)
    e2 = time.perf_counter()
    print(f"factorial(100) took: {e2 - s2}")

    s3 = time.perf_counter()
    factorial(125)
    e3 = time.perf_counter()
    print(f"factorial(100) took: {e3 - s3}")

    # No cache version
    print("Starting No cached function")

    s1 = time.perf_counter()
    factorial_no_cache(100)
    e1 = time.perf_counter()
    print(f"factorial_no_cache(100) took: {e1 - s1}")

    s2 = time.perf_counter()
    factorial_no_cache(50)
    e2 = time.perf_counter()
    print(f"factorial_no_cache(100) took: {e2 - s2}")

    s3 = time.perf_counter()
    factorial_no_cache(125)
    e3 = time.perf_counter()
    print(f"factorial_no_cache(100) took: {e3 - s3}")