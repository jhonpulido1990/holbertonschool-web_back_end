#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed
list which takes a list mxd_lst of integers
and floats and returns their sum as a float.
You need to keep the same order to pass
the checks (Union[int, float]).
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Union type; Union[X, Y] is equivalent to X | Y and
    means either X or Y."""
    res: float = 0
    for n in mxd_lst:
        res += n
    return res
