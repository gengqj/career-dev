# -*- coding: utf-8 -*-
"""
练习 ex04 · 数据处理实战（pandas 起步）
对应廖雪峰《Python3 教程》：字符串 / 列表 / 字典 / 模块 / 迭代器与生成器 /
                      datetime / 序列化，再叠加 pandas 基础操作

这一份是你从"会写语法"跨到"能做分析"的关键练习。
所有题目都用金融/行情场景，题面即面试题的简化版。

规则：
1. 在本文件中实现下面 8 个函数，名称必须完全一致。
2. 不要改动文件底部的 TESTS 区域。
3. 判题： cd 00_python_basics && python run_all.py ex04
"""

import json
import re
from datetime import datetime

import pandas as pd

# --- 题目区：在下面写你的实现 ---

# 1. parse_report_date(text) -> datetime
#    把 "2024年5月13日" 解析成 datetime 对象。
#    提示：re 提取数字，或 str.replace 后 strptime
#    额外要求：非法输入抛 ValueError

# 2. clean_prices(raw_rows) -> list[dict]
#    输入形如：
#      [{"code": "600000", "price": "1,234.50", "date": "2024-05-13"}, ...]
#    输出：price 去掉逗号并转成 float，去掉 price 为空或无法解析的行，
#          code 转成 str，date 保持原字符串。
#    提示：列表推导式 + try/except + float()

# 3. build_dataframe(rows) -> pd.DataFrame
#    把 clean_prices 的结果转成 DataFrame，列顺序为 code, date, price，
#    并按 date 升序排序，索引重置。

# 4. add_return_column(df) -> pd.DataFrame
#    新增一列 ret 表示相邻两个交易日的价格收益率 (price / prev_price - 1)，
#    第一行填 None。要求按 code 分组计算。返回新 DataFrame（不要改原表）。

# 5. top_gainers(df, n) -> pd.DataFrame
#    取 ret 最大的 n 行，按 ret 降序。忽略 ret 为空的行。

# 6. summarize_by_code(df) -> pd.DataFrame
#    按 code 分组聚合，返回列：code, days(天数), avg_price(均价),
#    total_return(区间涨跌幅 = 末价/首价-1), volatility(收益率标准差, ddof=1)。
#    按 code 升序。

# 7. filter_active_codes(df, min_days=20) -> list
#    返回交易天数 >= min_days 的股票代码列表（升序、去重）。

# 8. generate_report(analyzer, text) -> str
#    写一个"报告生成器"：把 analyzer（第 5 题里的 PerformanceAnalyzer，
#    可从 ex03 导入，也可自己实现一个最小版本）算出的 total_return、
#    max_drawdown、volatility 三个指标，拼成一段中文摘要字符串，
#    格式示例："区间收益-1.00%，最大回撤20.0%，波动率15.3%"
#    要求：三个指标都出现在返回字符串里。


# --- 判题区：不要改动 ---

TESTS = [
    ("parse_report_date", lambda m: m.parse_report_date("2024年5月13日").strftime("%Y-%m-%d") == "2024-05-13",
     "应解析为 2024-05-13"),
    ("clean_prices", lambda m: _clean_smoke(m),
     "价格清洗结果不正确"),
    ("build_dataframe", lambda m: _frame_smoke(m),
     "DataFrame 构建或排序不正确"),
    ("add_return_column", lambda m: _ret_smoke(m),
     "ret 列计算不正确"),
    ("top_gainers", lambda m: _top_smoke(m),
     "top_gainers 排序不正确"),
    ("summarize_by_code", lambda m: _agg_smoke(m),
     "分组聚合结果不正确"),
    ("filter_active_codes", lambda m: m.filter_active_codes(_sample_df(m), 2) == ["000001", "600000"],
     "filter_active_codes 结果不正确"),
    ("generate_report", lambda m: _report_smoke(m),
     "报告字符串应包含三个指标"),
]


def _sample_rows():
    return [
        {"code": "600000", "price": "10.00", "date": "2024-05-13"},
        {"code": "600000", "price": "10.50", "date": "2024-05-14"},
        {"code": "600000", "price": "11.00", "date": "2024-05-15"},
        {"code": "000001", "price": "20.00", "date": "2024-05-13"},
        {"code": "000001", "price": "18.00", "date": "2024-05-14"},
    ]


def _sample_df(m):
    return m.build_dataframe(m.clean_prices(_sample_rows()))


def _clean_smoke(m):
    out = m.clean_prices([
        {"code": 600000, "price": "1,234.50", "date": "2024-05-13"},
        {"code": "000001", "price": "", "date": "2024-05-13"},
        {"code": "000002", "price": "abc", "date": "2024-05-13"},
        {"code": "000003", "price": "9.90", "date": "2024-05-13"},
    ])
    return (len(out) == 2 and out[0]["code"] == "600000"
            and out[0]["price"] == 1234.5 and out[1]["price"] == 9.9)


def _frame_smoke(m):
    df = _sample_df(m)
    return (list(df.columns) == ["code", "date", "price"] and len(df) == 5
            and df["date"].is_monotonic_increasing)


def _ret_smoke(m):
    df = m.add_return_column(_sample_df(m))
    sub = df[df["code"] == "600000"]
    vals = [v for v in sub["ret"].tolist() if v is not None and not pd.isna(v)]
    return (len(vals) == 2 and abs(vals[0] - 0.05) < 1e-9
            and abs(vals[1] - (11.0 / 10.5 - 1)) < 1e-9)


def _top_smoke(m):
    df = m.add_return_column(_sample_df(m))
    top = m.top_gainers(df, 2)
    return len(top) == 2 and top["ret"].iloc[0] >= top["ret"].iloc[1]


def _agg_smoke(m):
    df = m.add_return_column(_sample_df(m))
    agg = m.summarize_by_code(df)
    row = agg[agg["code"] == "600000"].iloc[0]
    return (set(["code", "days", "avg_price", "total_return", "volatility"]).issubset(set(agg.columns))
            and int(row["days"]) == 3
            and abs(row["avg_price"] - 10.5) < 1e-9
            and abs(row["total_return"] - 0.1) < 1e-9)


def _report_smoke(m):
    class _A:
        def total_return(self): return -0.01
        def max_drawdown(self): return 0.2
        def volatility(self): return 0.153
    s = m.generate_report(_A(), "样本文本")
    return all(k in s for k in ["-1", "20", "15"])
