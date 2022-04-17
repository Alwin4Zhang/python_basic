import time
import logging
from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        cost_time = time.time() - start
        logger_str = "finished:<%s> cost time:<%s>" % (func.__name__, cost_time)
        print(logger_str)
        logging.info(logger_str)
        return res

    return wrapped_func


@decorator
def test(num):
    res = 0
    for _ in range(num):
        res += 1
    return res


res = test(1000)
print(res)
