#!/usr/bin/env python3
"""This module contains the function add"""


import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
        typing.List[typing.Tuple[typing.Sequence, int]]:
        """
        Returns a list of tuples containing elements
        and their lengths.
        """

        return [(i, len(i)) for i in lst]
