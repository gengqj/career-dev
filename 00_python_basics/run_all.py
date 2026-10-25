# -*- coding: utf-8 -*-
"""
自动判题器 · career-dev 练习系统

用法：
    python run_all.py            # 判你自己的实现
    python run_all.py --solutions # 跑参考答案（对比用）
    python run_all.py ex01        # 只判指定练习（按前缀匹配）

规则：练习文件底部的 TESTS 区域不要改动。
TESTS 中每个测试函数接收待测模块 m 作为参数，以便在"练习版"和"答案版"之间切换。
"""
import importlib
import importlib.util
import os
import sys
from pathlib import Path

# Windows 控制台中文输出：把输出代码页切到 UTF-8，避免"总分：?/38"这种乱码
if os.name == "nt":
    try:
        import ctypes

        ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    except Exception:
        pass
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
EX_DIR = HERE / "exercises"
SOL_DIR = HERE / "solutions"

# 让 exercises 目录可直接 import 练习模块
if str(EX_DIR) not in sys.path:
    sys.path.insert(0, str(EX_DIR))
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


def load_solution(stem):
    """参考答案用独立模块名加载，避免与练习文件同名冲突。"""
    spec = importlib.util.spec_from_file_location(f"sol_{stem}", SOL_DIR / f"{stem}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_file(stem, use_solutions):
    """返回 (通过数, 总数, 明细列表)"""
    try:
        ex = importlib.import_module(stem)
    except Exception as e:
        return 0, 0, [("导入练习文件失败", f"{type(e).__name__}: {e}")]

    if use_solutions:
        try:
            target = load_solution(stem)
        except Exception as e:
            return 0, 0, [("参考答案加载失败", f"{type(e).__name__}: {e}")]
    else:
        target = ex

    tests = getattr(ex, "TESTS", [])
    details = []
    passed = 0
    for item in tests:
        name, fn, hint = item
        try:
            result = fn(target)
            if result is False:
                details.append((name, f"返回 False（{hint}）"))
            else:
                passed += 1
        except AssertionError as e:
            details.append((name, f"断言失败：{e or hint}"))
        except NotImplementedError:
            details.append((name, "还没实现（NotImplementedError）"))
        except NameError as e:
            details.append((name, f"函数名不存在或没定义：{e}"))
        except Exception as e:
            details.append((name, f"运行出错 {type(e).__name__}: {e}"))
    return passed, len(tests), details


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    use_solutions = "--solutions" in sys.argv
    prefix = args[0] if args else "ex"

    if not EX_DIR.exists():
        print(f"找不到练习目录：{EX_DIR}")
        return 1

    files = sorted(p for p in EX_DIR.glob("ex*.py") if p.stem.startswith(prefix))
    if not files:
        print(f"没有匹配 '{prefix}' 的练习文件")
        return 1

    lines = []
    total_pass = 0
    total_all = 0
    for p in files:
        passed, total, details = run_file(p.stem, use_solutions)
        total_pass += passed
        total_all += total
        mark = "OK " if total and passed == total else "!! "
        lines.append(f"\n{mark}{p.stem}   {passed}/{total} 通过")
        for name, msg in details:
            lines.append(f"    - {name}: {msg}")

    lines.append("\n" + "=" * 46)
    if total_all:
        rate = total_pass / total_all * 100
        lines.append(f"总分：{total_pass}/{total_all}  ({rate:.0f}%)")
        if rate == 100:
            lines.append("全部通过！可以 git add . && git commit -m \"feat: 完成 XXX 练习\"")
        else:
            lines.append("把上面没过的题补完再跑一次。卡住的题去廖雪峰对应章节回看。")
    else:
        lines.append("没有可判的题目。")

    report = "\n".join(lines)
    print(report)
    try:
        (HERE / "last_report.txt").write_text(report, encoding="utf-8")
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
