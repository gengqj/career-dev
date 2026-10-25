# -*- coding: utf-8 -*-
"""参考答案 ex04 · 数据处理实战（对照练习用，请先自己写）"""
import re
from datetime import datetime

import pandas as pd


def parse_report_date(text):
    m = re.search(r"(\d{4})\D+(\d{1,2})\D+(\d{1,2})", text)
    if not m:
        raise ValueError(f"无法解析日期：{text}")
    y, mo, d = (int(x) for x in m.groups())
    return datetime(y, mo, d)


def clean_prices(raw_rows):
    out = []
    for r in raw_rows:
        try:
            p = float(str(r.get("price", "")).replace(",", "").replace("元", "").strip())
        except (ValueError, TypeError):
            continue
        out.append({"code": str(r.get("code", "")), "price": p,
                    "date": r.get("date", "")})
    return out


def build_dataframe(rows):
    df = pd.DataFrame(rows, columns=["code", "date", "price"])
    df = df.sort_values("date").reset_index(drop=True)
    return df


def add_return_column(df):
    out = df.copy()
    out["ret"] = out.groupby("code")["price"].pct_change()
    return out


def top_gainers(df, n):
    valid = df.dropna(subset=["ret"])
    return valid.sort_values("ret", ascending=False).head(n)


def summarize_by_code(df):
    def _agg(g):
        g = g.sort_values("date")
        prices = g["price"].tolist()
        total_ret = (prices[-1] / prices[0] - 1) if prices and prices[0] else 0.0
        return pd.Series({
            "days": len(g),
            "avg_price": g["price"].mean(),
            "total_return": total_ret,
            "volatility": g["ret"].std(ddof=1) if g["ret"].notna().sum() > 1 else 0.0,
        })

    out = df.groupby("code").apply(_agg, include_groups=False).reset_index()
    return out.sort_values("code").reset_index(drop=True)


def filter_active_codes(df, min_days=20):
    counts = df.groupby("code")["date"].count()
    return sorted(counts[counts >= min_days].index.tolist())


def generate_report(analyzer, text):
    tr = analyzer.total_return()
    mdd = analyzer.max_drawdown()
    vol = analyzer.volatility()
    return (f"区间收益{tr * 100:.2f}%，最大回撤{mdd * 100:.1f}%，"
            f"波动率{vol * 100:.1f}%")
