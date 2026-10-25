# 02_pandas · 数据处理与初步分析

**目标**：能独立完成"读数据 → 清洗 → 分组聚合 → 透视/拼接 → 出图 → 导出报告"的全流程。

**教材**
- Kaggle Learn Pandas（4 小时，free）：https://www.kaggle.com/learn/pandas
- Kaggle Learn Feature Engineering（free）：https://www.kaggle.com/learn/feature-engineering
- pandas 官方文档（查 API）：https://pandas.pydata.org/docs/
- 本仓库 `00_python_basics/exercises/ex04_data_handling.py`（8 题，自建实战题）

**核心 API 清单**（背下来，够用一整年）
- 读写：`read_csv` / `read_excel` / `to_csv`
- 选择：`loc` / `iloc` / 条件筛选 / `query`
- 缺失与重复：`isna` / `fillna` / `drop_duplicates`
- 分组：`groupby().agg()` / `value_counts` / `pivot_table`
- 变换：`apply` / `map` / `transform`
- 时间序列：`to_datetime` / `set_index` / `rolling` / `pct_change` / `resample`
- 拼接：`concat` / `merge`（join）

**节奏**：P1 阶段（11.30–2.21）每周 2 次 pandas 练习，跟 `03_project_practice` 同步。

**红线**：不要为了刷 API 而刷 API，每个 API 至少在真实数据集上用过一次。
