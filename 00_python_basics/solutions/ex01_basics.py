# -*- coding: utf-8 -*-
"""参考答案 ex01 · 基础语法与数据类型（对照练习用，请先自己写）"""


def normalize_code(code):
    return code.strip().upper()


def split_tags(text):
    return [t.strip() for t in text.split(",") if t.strip()]


def calc_return(pct_start, pct_end):
    if pct_start == 0:
        return 0.0
    return (pct_end - pct_start) / pct_start


def top_n(nums, n):
    return sorted(sorted(nums, reverse=True)[:n])


def moving_average(values, window):
    return [sum(values[i:i + window]) / window for i in range(len(values) - window + 1)]


def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged


def dedupe(items):
    seen = set()
    out = []
    for it in items:
        if it not in seen:
            seen.add(it)
            out.append(it)
    return out


def parse_amount(text):
    try:
        return float(text.replace(",", "").replace("元", "").strip())
    except (ValueError, AttributeError):
        return None


def flatten_2d(mat):
    return [x for row in mat for x in row]


def word_counts(text):
    counts = {}
    for w in text.split():
        k = w.lower()
        counts[k] = counts.get(k, 0) + 1
    return counts
