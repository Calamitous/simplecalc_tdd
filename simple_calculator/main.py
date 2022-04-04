# -*- coding: utf-8 -*-
from functools import reduce
import math


class SimpleCalculator:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        if not all(args):
            raise ValueError

        return reduce(lambda a, b:  a*b, args)

    def div(self, a, b):
        if not b:
            return float('inf')

        return a / b

    def avg(self, iter, lt=None, ut=None):
        if ut is not None:
            iter = list(filter(lambda x : x <= ut, iter))

        if lt is not None:
            iter = list(filter(lambda x : x >= lt, iter))

        if not iter:
            return 0

        return sum(iter) / len(iter)

    def sqrt(self, square):
        return math.sqrt(square)

    def exp(self, num, exponent):
        return num ** exponent

    def exponential(self, exponential):
        return self.exp(10, exponential)

    def factorial(self, num):
        return math.factorial(num)
