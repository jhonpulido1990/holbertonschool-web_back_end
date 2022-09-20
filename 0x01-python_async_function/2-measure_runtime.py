#!/usr/bin/env python3
"""Import wait_random from the previous python file
that you’ve written and write an async routine
called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn
wait_random n times with the specified max_delay."""
import asyncio
from cProfile import run
import random
import time
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """random.uniform(a, b) Return a random
    floating point number N"""
    res_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(res_delay)
    return res_delay


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """wait_n should return the list of all the delays
    (float values). The list of the delays should be in
    ascending order without using sort() because of
    concurrency."""
    lista: List[float] = []
    order_list: List[float] = []
    for i in range(n):
        lista.append(wait_random(max_delay))
    for x in asyncio.as_completed(lista):
        get_number = await x
        order_list.append(get_number)
    return order_list


def measure_time(n: int, max_delay: int) -> float:
    """Create a measure_time function with integers n
    and max_delay as arguments that measures the total
    execution time for wait_n(n, max_delay), and
    returns total_time / n. Your function should
    return a float."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    all_time = end - start
    return all_time / n
