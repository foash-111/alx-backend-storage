#!/usr/bin/env python3
"""count requests"""
import requests
import redis
from typing import Callable
from functools import wraps


def counter(method: Callable) -> Callable:
    """counter decorator"""
    @wraps(method)
    def wrapper(*args, **kwargs):
        r = redis.Redis()
        url = args[0]
        if not r.exists(f'count:{url}'):
            r.setex(f'count:{url}', 10, 0)
        r.incr(f'count:{url}')
        return method(*args, **kwargs)
    return wrapper


@counter
def get_page(url: str) -> str:
    """get the page data from its url"""
    response = requests.get(url)
    data = response.text
    return data


print(get_page('http://127.0.0.1:80'))
