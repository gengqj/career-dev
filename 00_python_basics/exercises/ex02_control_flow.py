# -*- coding: utf-8 -*-
"""
练习 ex02 · 流程控制与函数
对应廖雪峰《Python3 教程》：条件语句 / 循环语句 / range / 函数定义 /
                      函数的参数 / 函数的返回值 / 作用域

规则：
1. 在本文件中实现下面 10 个函数，函数名与参数必须完全一致。
2. 不要改动文件底部的 TESTS 区域。
3. 判题： cd 00_python_basics && python run_all.py ex02
"""

# --- 题目区：在下面写你的实现 ---

# 1. classify_roe(roe) -> str
#    按 ROE 给公司打分：>=0.20 "优秀"；>=0.10 "良好"；>=0 "关注"；<0 "预警"
#    提示：if / elif / else

# 2. compound(principal, rate, years) -> float
#    复利终值 = principal * (1 + rate) ** years
#    compound(100, 0.05, 2) -> 110.25

# 3. first_repeat(s) -> str | None
#    返回字符串中第一个重复出现的字符；没有重复返回 None。
#    first_repeat("abcbad") -> "b"；first_repeat("abc") -> None
#    提示：遍历 + set 记录已出现字符

# 4. fizzbuzz(n) -> list
#    1 到 n 的列表，3 的倍数写 "Fizz"，5 的倍数写 "Buzz"，15 的倍数写 "FizzBuzz"
#    fizzbuzz(5) -> [1, 2, "Fizz", 4, "Buzz"]

# 5. sum_even(n) -> int
#    1 到 n 之间所有偶数之和。sum_even(10) -> 30

# 6. safe_div(a, b) -> float | None
#    除法，除数为 0 时返回 None（不要抛异常）

# 7. apply_default(func, items, default) -> list
#    对 items 中每个元素调用 func；调用抛异常时用 default 代替该位置。
#    apply_default(lambda x: 10 // x, [2, 0], -1) -> [5, -1]
#    提示：try / except + 列表推导式

# 8. fib(n) -> int
#    斐波那契数列第 n 项（fib(0)=0, fib(1)=1）。fib(10) -> 55
#    提示：递归 + 记忆化（functools.lru_cache 或手写 dict）

# 9. group_by_length(items) -> dict
#    按字符串长度分组。group_by_length(["a","bb","c"]) -> {1: ["a","c"], 2: ["bb"]}
#    提示：setdefault

# 10. count_above(values, threshold) -> int
    #    统计列表中严格大于 threshold 的元素个数。count_above([1,5,2], 2) -> 1


# --- 判题区：不要改动 ---

TESTS = [
    ("classify_roe", lambda m: m.classify_roe(0.25) == "优秀" and m.classify_roe(0.12) == "良好"
     and m.classify_roe(0.05) == "关注" and m.classify_roe(-0.01) == "预警",
     "classify_roe 四档判断不正确"),
    ("compound", lambda m: abs(m.compound(100, 0.05, 2) - 110.25) < 1e-9,
     "compound(100, 0.05, 2) 应为 110.25"),
    ("first_repeat", lambda m: m.first_repeat("abcbad") == "b" and m.first_repeat("abc") is None,
     "first_repeat 应返回首个重复字符，无重复返回 None"),
    ("fizzbuzz", lambda m: m.fizzbuzz(5) == [1, 2, "Fizz", 4, "Buzz"] and m.fizzbuzz(15)[-1] == "FizzBuzz",
     "fizzbuzz 规则不正确"),
    ("sum_even", lambda m: m.sum_even(10) == 30 and m.sum_even(1) == 0,
     "sum_even(10) 应为 30"),
    ("safe_div", lambda m: m.safe_div(6, 3) == 2 and m.safe_div(1, 0) is None,
     "safe_div 除零应返回 None"),
    ("apply_default", lambda m: m.apply_default(lambda x: 10 // x, [2, 0], -1) == [5, -1],
     "apply_default 应在异常位置使用 default"),
    ("fib", lambda m: m.fib(10) == 55 and m.fib(0) == 0 and m.fib(1) == 1,
     "fib(10) 应为 55"),
    ("group_by_length", lambda m: m.group_by_length(["a", "bb", "c"]) == {1: ["a", "c"], 2: ["bb"]},
     "group_by_length 分组结果不正确"),
    ("count_above", lambda m: m.count_above([1, 5, 2], 2) == 1 and m.count_above([], 0) == 0,
     "count_above 计数不正确"),
]
