# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import inspect


def find_dependencies(_dependencies,fcn):
    args=inspect.getargspec(fcn)[0]
    return [_dependencies[a] for a in args if a in _dependencies]
