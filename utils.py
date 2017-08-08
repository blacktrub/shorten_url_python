from functools import wraps


def logging_view(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        print(f'got request from {request.url}')
        return func(*args, **kwargs)
    return wrapper
