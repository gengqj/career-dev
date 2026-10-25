# -*- coding: utf-8 -*-
"""参考答案 ex03 · 面向对象与工程化（对照练习用，请先自己写）"""
import csv
import json
import os
import re
import statistics
from dataclasses import dataclass


@dataclass
class Stock:
    code: str
    name: str
    price: float
    shares: int
    cost: float = 0.0

    def market_value(self):
        return self.price * self.shares


class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def total_market_value(self):
        return sum(s.market_value() for s in self.stocks)

    def cost_basis(self):
        return sum(s.cost * s.shares for s in self.stocks)

    def holding_codes(self):
        return [s.code for s in self.stocks]


class InsufficientFundsError(Exception):
    def __init__(self, balance, required):
        self.balance = balance
        self.required = required
        super().__init__(f"余额不足：当前 {balance}，需要 {required}")


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


class PerformanceAnalyzer:
    def __init__(self, prices):
        self.prices = list(prices)

    def total_return(self):
        if not self.prices or self.prices[0] == 0:
            return 0.0
        return (self.prices[-1] - self.prices[0]) / self.prices[0]

    def max_drawdown(self):
        peak = None
        mdd = 0.0
        for p in self.prices:
            if peak is None or p > peak:
                peak = p
            if peak:
                mdd = max(mdd, (peak - p) / peak)
        return mdd

    def volatility(self):
        if len(self.prices) < 2:
            return 0.0
        rets = [(self.prices[i] - self.prices[i - 1]) / self.prices[i - 1]
                for i in range(1, len(self.prices))]
        return statistics.pstdev(rets)


class DataExporter:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def export_json(self, filename, data):
        path = os.path.join(self.output_dir, filename)
        os.makedirs(self.output_dir, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return path

    def export_csv(self, filename, rows):
        path = os.path.join(self.output_dir, filename)
        os.makedirs(self.output_dir, exist_ok=True)
        if not rows:
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write("")
            return path
        headers = list(rows[0].keys())
        with open(path, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=headers)
            w.writeheader()
            w.writerows(rows)
        return path


class ReportParser:
    def __init__(self, text):
        self.text = text

    def extract_numbers(self, pattern):
        return [float(x) for x in re.findall(pattern, self.text)]

    def extract_percentages(self):
        return [float(x) for x in re.findall(r"(\d+(?:\.\d+)?)\s*%", self.text)]


class PriceFormatter:
    def __init__(self, locale="cn"):
        self.locale = locale

    def format(self, value, unit="元"):
        if self.locale == "us":
            return f"${value:,.2f}"
        return f"{value:,.2f}{unit}"


@dataclass
class Trade:
    date: str
    code: str
    side: str
    price: float
    volume: int

    def is_buy(self):
        return self.side.upper() == "BUY"

    def signed_value(self):
        sign = 1 if self.is_buy() else -1
        return sign * self.price * self.volume

    def to_dict(self):
        return {"date": self.date, "code": self.code, "side": self.side,
                "price": self.price, "volume": self.volume}


def summarize_trades(trades):
    buys = [t for t in trades if t.is_buy()]
    sells = [t for t in trades if not t.is_buy()]
    buy_amt = sum(t.price * t.volume for t in buys)
    sell_amt = sum(t.price * t.volume for t in sells)
    return {
        "total_trades": len(trades),
        "buy_count": len(buys),
        "sell_count": len(sells),
        "total_buy_amount": buy_amt,
        "total_sell_amount": sell_amt,
        "net_amount": buy_amt - sell_amt,
    }
