#!/usr/bin/env python3
"""This module contains the function to_kv"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
        """
        Type-annotated function that string k and an int OR float v
        as arguments and returns a tuple"""
        
        return (k, float(v ** 2))
