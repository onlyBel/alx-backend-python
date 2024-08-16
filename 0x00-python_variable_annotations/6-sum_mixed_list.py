#!/usr/bin/env python3
"""This module contains the function sum_mixed_list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
        """
        Returns the sum of floats and integers in the list.
        """
        return sum(mxd_lst)
