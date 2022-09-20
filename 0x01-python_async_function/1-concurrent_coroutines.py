#!/usr/bin/env python3
"""Import wait_random from the previous python file
that you’ve written and write an async routine
called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn
wait_random n times with the specified max_delay."""
import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """random.uniform(a, b) Return a random
    floating point number N"""
    res_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(res_delay)
    return res_delay


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """call funtion wait_ramdon"""
    lista: List[float] = []
    order_list = []
    i = 0
    while i < n:
        lista.append(await wait_random(max_delay))
        i += 1
    lista.sort(key=float)
    return lista
