# 00_python_basics · 廖雪峰配套练习系统

廖雪峰《Python教程》是**教材**，不是题库——它教你语法，但每章只有示例，没有练习。
这个目录是我给你补的"题库 + 判题器"：**先自己写 → 跑判题 → 卡住回看教程对应章节 → 再改**。

## 怎么用（3 条命令）

```powershell
cd C:\Users\28643\career-dev\00_python_basics

# 1) 判你自己的实现（平时就这一条）
python run_all.py

# 2) 只判某一份练习
python run_all.py ex01

# 3) 跑参考答案（卡住之后用来对照思路，先自己写再看！）
python run_all.py --solutions
```

判题结果会同时打印到屏幕，并写一份到 `last_report.txt`。

## 目录结构

```
00_python_basics/
├── run_all.py              # 判题器：自动跑测试、给提示、统计分数
├── env_check.py            # 环境自检（pandas/numpy/sklearn 版本）
├── last_report.txt         # 最近一次判题结果
├── exercises/              # ← 你在这里写代码（题目区）
│   ├── ex01_basics.py      #   基础语法与数据结构   10 题
│   ├── ex02_control_flow.py#   流程控制与函数       10 题
│   ├── ex03_oop.py         #   面向对象与工程化     10 题
│   └── ex04_data_handling.py # pandas 数据处理实战  8 题
└── solutions/              # 参考答案（卡住后才看）
    ├── ex01_basics.py
    ├── ex02_control_flow.py
    ├── ex03_oop.py
    └── ex04_data_handling.py
```

## 硬性规则

1. **只改 `exercises/` 里的"题目区"**（文件顶部 `# --- 题目区 ---` 之后、判题区之前）。判题区（TESTS）不要动。
2. **函数名必须完全一致**，题目区注释里写得很清楚。
3. **先写再参考**。看答案不是作弊，是卡住之后的降级方案；但先看答案再写，等于没练。
4. **每题必须能口头讲清楚**："这题考的是什么、我的思路是什么、错了为什么错"。讲不出来就是没懂。
5. **一次一题**：不要一口气写 10 题。写完一题跑一次判题，改完再下一题。

## 题目 → 廖雪峰教程章节对照

| 练习文件 | 对应教程章节 | 核心知识点 |
| --- | --- | --- |
| ex01_basics | 5.1 数据类型和变量、5.2 字符串和编码、5.3 list 和 tuple、5.7 dict 和 set | 类型转换、字符串切片、列表推导、字典合并、去重 |
| ex02_control_flow | 5.4 条件判断、5.5 模式匹配、5.6 循环、6 函数（6.1-6.4） | if/elif 分档、for/while、函数参数、递归、异常处理 |
| ex03_oop | 10 面向对象编程、11 面向对象高级编程、12.1 错误处理 | dataclass、类方法、继承、自定义异常、property |
| ex04_data_handling | 13.4 序列化、15 正则表达式、16.1 datetime、9 模块 | 正则抽数、datetime 解析、CSV/JSON、pandas 清洗与聚合 |

**重要提醒**：廖雪峰 2025 版教程（473 页）偏 Web/系统方向，**没有 numpy / pandas / 建模章节**。
pandas 部分必须靠 `ex04` + 官方文档 + Kaggle Learn 补，别指望看完廖雪峰就会做数据分析。

## 每次提交 git（这条最容易被忽略，但秋招时最值钱）

```powershell
cd C:\Users\28643\career-dev
git add .
git commit -m "feat(ex01): 完成 ex01 基础语法 10/10"
git push
```

提交信息建议格式：`feat(ex0X): 完成 ex0X 第 N 题 —— <这题考什么>`
秋招时你的 GitHub 提交历史本身就是学习曲线，比简历上写"熟练 Python"有说服力得多。
