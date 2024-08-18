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
        # if not r.exists(f'count:{url}'):
        #     r.setex(f'count:{url}', 10, 0)
        # r.incr(f'count:{url}')

        r.incr(f'count:{url}')
        cashed_data = r.get(f'{url}')
        if cashed_data:
            return cashed_data.decode('utf-8')
        
        
        html_page =  method(*args, **kwargs)
        r.setex(f'{url}', 10, html_page)
        return html_page
    return wrapper


@counter
def get_page(url: str) -> str:
    """get the page data from its url"""
    response = requests.get(url)
    return response.text


print(get_page('http://127.0.0.1:80'))
