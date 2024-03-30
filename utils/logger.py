from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwgs):
        try:
            result = func(*args, **kwgs)
        except Exception as ex:
            print(ex)
        print(func.__name__, "- successfully")
        return result

    return wrapper
