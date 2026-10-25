# -*- coding: utf-8 -*-
"""参考答案 ex02 · 流程控制与函数（对照练习用，请先自己写）"""
from functools import lru_cache


def classify_roe(roe):
    if roe >= 0.20:
        return "优秀"
    elif roe >= 0.10:
        return "良好"
    elif roe >= 0:
        return "关注"
    return "预警"


def compound(principal, rate, years):
    return principal * (1 + rate) ** years


def first_repeat(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return None


def fizzbuzz(n):
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(i)
    return out


def sum_even(n):
    return sum(i for i in range(1, n + 1) if i % 2 == 0)


def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def apply_default(func, items, default):
    out = []
    for it in items:
        try:
            out.append(func(it))
        except Exception:
            out.append(default)
    return out


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def group_by_length(items):
    groups = {}
    for it in items:
        groups.setdefault(len(it), []).append(it)
    return groups


def count_above(values, threshold):
    return sum(1 for v in values if v > threshold)
