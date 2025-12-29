import time
from functools import wraps

def timerdecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"The function took {(end_time - start_time) * 1000} milliseconds to execute")
        return result

    return wrapper

def fib(n:int) -> int:
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

@timerdecorator
def timed_fib(n:int) -> int:
    return fib(n)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(timed_fib(n))