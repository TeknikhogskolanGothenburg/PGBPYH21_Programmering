import time
from functools import wraps


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f'Call to function {f.__name__} took {end-start:2f} seconds')
        return result
    return wrapper
