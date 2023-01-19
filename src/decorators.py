import functools
from myfitnesspal import Client


def mfp(func):
    """Connect to myfitnesspal"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        client = Client()
        kwargs['client'] = client
        return func(*args, **kwargs)
    return wrapper
