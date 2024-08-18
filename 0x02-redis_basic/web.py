#!/usr/bin/env python3
"""count requests"""
import requests
import redis
from typing import Callable
from functools import wraps


r = redis.Redis()


def counter(method: Callable) -> Callable:
    """Counter decorator to cache the result and count requests"""
    @wraps(method)
    def wrapper(url: str):
        """Wrapper function"""
        # Increment the count for the given URL
        r.incr(f'count:{url}')
        
        # Check if the content is already cached
        cached_page = r.get(url)
        if cached_page:
            print(f"Returning cached page for {url}")
            return cached_page.decode('utf-8')

        # Fetch and cache the page content
        html_page = method(url)
        r.setex(url, 10, html_page)
        print(f"Cached page for {url} for 10 seconds")
        return html_page
    return wrapper


@counter
def get_page(url: str) -> str:
    """get the page data from its url"""
    response = requests.get(url)
    return response.text
