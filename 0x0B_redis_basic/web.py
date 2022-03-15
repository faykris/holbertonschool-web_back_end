#!/usr/bin/env python3
"""5. Implementing an expiring web cache and tracker"""

from functools import wraps
import redis
import requests
from typing import Callable

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """count_request - increases counter value each request"""

    @wraps(method)
    def wrapper(url):
        """wrapper"""
        r.incr(f"count:{url}")
        c_html = r.get(f"cached:{url}")
        if c_html:
            return c_html.decode("utf-8")
        html_text = method(url)
        r.setex(f"cached:{url}", 10, html_text)
        return html_text

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """get-page returns in text format a HTML page from request"""
    req = requests.get(url)
    return req.text
