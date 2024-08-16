#!/usr/bin/env python3
"""This module contains the function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
        """
        Type-annotated function that returns a function thatmultiplies a float by the given multiplier."""
        
        def multiplier_function(x: float) -> float:
            """Function returning float multiplier """
            return x * multiplier
            return multiplier_function
