#!/usr/bin/env python3
"""count requests"""
import requests
import redis
from typing import Callable
from functools import wraps


r = redis.Redis()


def counter(method: Callable) -> Callable:
    """counter decorator"""
    @wraps(method)
    def wrapper(*args, **kwargs):
        """wrapper"""
        url = args[0]
        cached_page = r.get(url)
        if not cached_page:
            html_page = method(*args, **kwargs)
            r.setex(url, 10, html_page)
            return html_page

        r.incr(f'count:{url}')
        return cached_page.decode('utf-8')
    return wrapper


@counter
def get_page(url: str) -> str:
    """get the page data from its url"""
    response = requests.get(url)
    return response.text


print(get_page('http://127.0.0.1:80'))
