# -*- coding: utf-8 -*-
"""
练习 ex01 · 基础语法与数据类型
对应廖雪峰《Python3 教程》：变量与字符串 / 注释 / 运算符 / 字符串与编码 /
                      list 与 tuple / 字典与集合 / 切片 / 列表推导式

规则：
1. 在本文件中实现下面 10 个函数，函数名与参数必须完全一致。
2. 不要改动文件底部的 TESTS 区域。
3. 判题： cd 00_python_basics && python run_all.py ex01
"""

# --- 题目区：在下面写你的实现 ---

# 1. normalize_code(code) -> str
#    去掉首尾空白并转成大写。例如 "  sh600000 " -> "SH600000"
#    提示：str.strip()、str.upper()

# 2. split_tags(text) -> list[str]
#    按英文逗号切分标签，去掉每个标签两端的空白，丢弃空标签。
#    例如 "消费, 科技 ,,白酒" -> ["消费", "科技", "白酒"]
#    提示：str.split(",") + 列表推导式 + if 判断

# 3. calc_return(pct_start, pct_end) -> float
#    计算区间涨跌幅 = (终值 - 起值) / 起值。100 -> 110 返回 0.1
#    提示：注意除零

# 4. top_n(nums, n) -> list
#    返回最大的 n 个数，按从小到大排列。top_n([3,9,1,7,5], 3) -> [5, 7, 9]
#    提示：sorted(..., reverse=True) 取前 n 个再 reverse

# 5. moving_average(values, window) -> list[float]
#    简单移动平均。moving_average([1,2,3,4], 2) -> [1.5, 2.5, 3.5]
#    提示：切片 + sum + 列表推导式

# 6. merge_dicts(d1, d2) -> dict
#    合并两个字典，d2 中同名键覆盖 d1。
#    提示：{**d1, **d2} 或 d1.copy() 后 update

# 7. dedupe(items) -> list
#    去重并保持原有顺序。["a","b","a","c"] -> ["a","b","c"]
#    提示：dict.fromkeys 或 set + 过滤

# 8. parse_amount(text) -> float | None
#    把 "1,234.50元" 解析成 1234.5；无法解析时返回 None。
#    提示：去掉逗号和"元"，float() 包在 try 里

# 9. flatten_2d(mat) -> list
#    展平二维列表。[[1,2],[3]] -> [1,2,3]
#    提示：列表推导式嵌套循环

# 10. word_counts(text) -> dict
#    统计单词出现次数，忽略大小写。"A a B" -> {"a": 2, "b": 1}
#    提示：text.split() + lower() + dict


# --- 判题区：不要改动 ---

TESTS = [
    ("normalize_code", lambda m: m.normalize_code("  sh600000 ") == "SH600000",
     "normalize_code('  sh600000 ') 应为 'SH600000'"),
    ("split_tags", lambda m: m.split_tags("消费, 科技 ,,白酒") == ["消费", "科技", "白酒"],
     "split_tags 结果应去掉空标签并去空格"),
    ("calc_return", lambda m: abs(m.calc_return(100, 110) - 0.1) < 1e-9,
     "calc_return(100, 110) 应为 0.1"),
    ("top_n", lambda m: m.top_n([3, 9, 1, 7, 5], 3) == [5, 7, 9],
     "top_n([3,9,1,7,5], 3) 应为 [5, 7, 9]"),
    ("moving_average", lambda m: m.moving_average([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5],
     "moving_average([1,2,3,4], 2) 应为 [1.5, 2.5, 3.5]"),
    ("merge_dicts", lambda m: m.merge_dicts({"a": 1}, {"a": 2, "b": 3}) == {"a": 2, "b": 3},
     "merge_dicts 应让 d2 覆盖 d1"),
    ("dedupe", lambda m: m.dedupe(["a", "b", "a", "c"]) == ["a", "b", "c"],
     "dedupe 应保持原顺序"),
    ("parse_amount", lambda m: m.parse_amount("1,234.50元") == 1234.5 and m.parse_amount("abc") is None,
     "parse_amount('1,234.50元') 应为 1234.5，非法输入应为 None"),
    ("flatten_2d", lambda m: m.flatten_2d([[1, 2], [3]]) == [1, 2, 3],
     "flatten_2d([[1,2],[3]]) 应为 [1,2,3]"),
    ("word_counts", lambda m: m.word_counts("A a B") == {"a": 2, "b": 1},
     "word_counts 应忽略大小写"),
]
