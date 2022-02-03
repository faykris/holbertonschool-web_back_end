#!/usr/bin/env python3
"""0. Async Generator"""


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ return the 10 random numbers using async_generator"""
    return [i async for i in async_generator()]
