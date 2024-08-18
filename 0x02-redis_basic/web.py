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
    def wrapper(url):
        """wrapper"""
        r.incr(f'count:{url}')
        cached_page = r.get(url)
        if cached_page:
            return cached_page.decode('utf-8')

        html_page = method(url)
        r.setex(url, 10, html_page)
        return html_page
    return wrapper


@counter
def get_page(url: str) -> str:
    """get the page data from its url"""
    response = requests.get(url)
    return response.text
