#!/usr/bin/env python3
"""
Python module that augments given code"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function setting up duck-typed annotation"""
    
    if lst:
        return lst[0]
    else:
        return None
