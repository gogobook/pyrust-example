# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ._pyrust_example import example_fn

__all__ = ['py_example_fn', 'example_fn']


def py_example_fn(input_str):
    return len(input_str)
