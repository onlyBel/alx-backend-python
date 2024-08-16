#!/usr/bin/env python3
"""
This module adds type annotation to a given function
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                             Union[T, None] = None) -> Union[Any, T]:
    """Add type annotations to the function"""

    if key in dct:
        return dct[key]
    else:
        return default
