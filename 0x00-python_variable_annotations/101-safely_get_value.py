#!/usr/bin/env python3
"""Given the parameters and the return values,
add type annotations to the function"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
                     -> Union[Any, T]:
    """Args:
            dct: Mapping
            key: Any data type
            default: Default value
        Return:
            Any or T format"""
    if key in dct:
        return dct[key]
    else:
        return default
