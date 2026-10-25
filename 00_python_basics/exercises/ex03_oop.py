# -*- coding: utf-8 -*-
"""
练习 ex03 · 面向对象与工程化
对应廖雪峰《Python3 教程》：类和实例 / 继承 / 多态 / 模块 / 导入模块 /
                      错误处理（try except）/ 常用标准库（datetime, json, re）

规则：
1. 在本文件中实现下面 10 个函数/类，名称必须完全一致。
2. 不要改动文件底部的 TESTS 区域。
3. 判题： cd 00_python_basics && python run_all.py ex03
"""

import json
import os
import re
import tempfile
from dataclasses import dataclass
from datetime import datetime

# --- 题目区：在下面写你的实现 ---

# 1. @dataclass class Stock
#    字段：code (str)、name (str)、price (float)、shares (int)
#    方法：market_value() 返回 price * shares
#    要求：能用 Stock("600000", "浦发银行", 10.0, 100) 构造

# 2. class Portfolio
#    方法：
#      add_stock(stock)        追加持仓
#      total_market_value()    合计市值
#      cost_basis()            合计成本（用持仓均价字段 cost）
#      holding_codes()         返回持仓代码列表
#    要求：内部用 list 保存持仓

# 3. class InsufficientFundsError(Exception)
#    自定义异常，构造时带上余额与所需金额两个信息

# 4. class BankAccount
#    构造：BankAccount(balance)
#    方法：
#      withdraw(amount)  余额不足时 raise InsufficientFundsError，否则扣减并返回新余额
#      deposit(amount)   存钱并返回新余额

# 5. class PerformanceAnalyzer
#    构造：PerformanceAnalyzer(prices)  prices 是价格列表
#    方法：
#      total_return()      区间涨跌幅 (末-首)/首
#      max_drawdown()      最大回撤：遍历求 (peak - cur) / peak 的最大值，>=0
#      volatility()        日收益率的标准差（population，statistics.pstdev）
#    提示：statistics 模块

# 6. class DataExporter
#    构造：DataExporter(output_dir)
#    方法：
#      export_json(filename, data)  把 data 写成 JSON 文件，返回完整文件路径
#      export_csv(filename, rows)    把 list[dict] 写成 CSV（表头取所有 key），返回路径
#    提示：os.path.join、csv.DictWriter

# 7. class ReportParser
#    构造：ReportParser(text)
#    方法：
#      extract_numbers(pattern)  用正则找出文本中所有数字，返回 float 列表
#      extract_percentages()     找出所有百分数（如 12.5%），返回 float 列表
#    提示：re.findall + 正则

# 8. class PriceFormatter
#    构造：PriceFormatter(locale="cn")
#    方法：
#      format(value, unit="元")  按 locale 格式化价格
#         cn：1234.5 -> "1,234.50元"
#         us：1234.5 -> "$1,234.50"
#      提示：format 的千分位语法 f"{value:,.2f}"

# 9. @dataclass class Trade
#    字段：date (str)、code (str)、side (str)、price (float)、volume (int)
#    方法：
#      is_buy()          side == "BUY"
#      signed_value()    买入为正、卖出为负：price * volume，带方向
#      to_dict()         返回 dict

# 10. def summarize_trades(trades) -> dict
#     统计所有 Trade：返回 {"total_trades": n, "buy_count": n, "sell_count": n,
#     "total_buy_amount": x, "total_sell_amount": x, "net_amount": x}


# --- 判题区：不要改动 ---

TESTS = [
    ("Stock.market_value", lambda m: m.Stock("600000", "浦发", 10.0, 100).market_value() == 1000.0,
     "market_value 应为 price * shares"),
    ("Portfolio", lambda m: _portfolio_smoke(m),
     "Portfolio 增删查算不正确"),
    ("BankAccount.withdraw", lambda m: _account_smoke(m),
     "余额不足应抛 InsufficientFundsError"),
    ("PerformanceAnalyzer", lambda m: _analyzer_smoke(m),
     "total_return / max_drawdown / volatility 计算不正确"),
    ("DataExporter", lambda m: _exporter_smoke(m),
     "导出 JSON / CSV 不正确"),
    ("ReportParser", lambda m: _parser_smoke(m),
     "数字/百分数提取不正确"),
    ("PriceFormatter", lambda m: m.PriceFormatter().format(1234.5) == "1,234.50元"
     and m.PriceFormatter("us").format(1234.5) == "$1,234.50",
     "价格格式化结果不正确"),
    ("Trade", lambda m: _trade_smoke(m),
     "Trade 方法不正确"),
    ("summarize_trades", lambda m: _summarize_smoke(m),
     "交易汇总结果不正确"),
    ("异常继承", lambda m: issubclass(m.InsufficientFundsError, Exception),
     "InsufficientFundsError 应继承 Exception"),
]


def _portfolio_smoke(m):
    p = m.Portfolio()
    p.add_stock(m.Stock("600000", "浦发", 10.0, 100, 10.0))
    p.add_stock(m.Stock("000001", "平安", 20.0, 50, 20.0))
    return (p.total_market_value() == 2000.0 and p.cost_basis() == 2000.0
            and sorted(p.holding_codes()) == ["000001", "600000"])


def _account_smoke(m):
    acc = m.BankAccount(100)
    assert acc.withdraw(50) == 50
    try:
        acc.withdraw(1000)
    except m.InsufficientFundsError:
        return True
    return False


def _analyzer_smoke(m):
    a = m.PerformanceAnalyzer([100, 110, 88, 99])
    assert abs(a.total_return() - (-0.01)) < 1e-9, "total_return"
    assert abs(a.max_drawdown() - 0.2) < 1e-9, "max_drawdown 应为 0.2"
    assert a.volatility() > 0, "volatility"
    return True


def _exporter_smoke(m):
    d = tempfile.mkdtemp()
    ex = m.DataExporter(d)
    p1 = ex.export_json("a.json", {"x": 1})
    assert os.path.exists(p1), "json 未生成"
    with open(p1, encoding="utf-8") as f:
        assert json.load(f) == {"x": 1}, "json 内容不对"
    p2 = ex.export_csv("b.csv", [{"a": 1, "b": 2}, {"a": 3, "b": 4}])
    with open(p2, encoding="utf-8", newline="") as f:
        rows = f.read().strip().splitlines()
    assert rows[0] == "a,b", "csv 表头不对"
    assert len(rows) == 3, "csv 行数不对"
    return True


def _parser_smoke(m):
    p = m.ReportParser("2024年装机317GW，增速12.5%，成本3.2元/W。")
    nums = p.extract_numbers(r"\d+\.?\d*")
    assert 317.0 in nums, "未抓到 317"
    pcts = p.extract_percentages()
    assert abs(pcts[0] - 12.5) < 1e-9, "未抓到 12.5%"
    return True


def _trade_smoke(m):
    t = m.Trade("2024-05-13", "600000", "BUY", 10.0, 100)
    assert t.is_buy() and t.signed_value() == 1000.0
    t2 = m.Trade("2024-05-14", "600000", "SELL", 12.0, 100)
    assert not t2.is_buy() and t2.signed_value() == -1200.0
    assert t.to_dict()["code"] == "600000"
    return True


def _summarize_smoke(m):
    ts = [m.Trade("2024-05-13", "600000", "BUY", 10.0, 100),
          m.Trade("2024-05-14", "000001", "SELL", 20.0, 50)]
    r = m.summarize_trades(ts)
    return (r["total_trades"] == 2 and r["buy_count"] == 1 and r["sell_count"] == 1
            and abs(r["total_buy_amount"] - 1000.0) < 1e-9
            and abs(r["total_sell_amount"] - 1000.0) < 1e-9
            and abs(r["net_amount"]) < 1e-9)
