@echo off
chcp 65001 > nul
title 每日学习 - career-dev
cd /d C:\Users\28643\career-dev

echo.
echo  ==========================================================
echo    正在打开 VS Code ...  等几秒
echo  ==========================================================
call "C:\Users\28643\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd" "C:\Users\28643\career-dev"
timeout /t 4 > nul

cd /d C:\Users\28643\career-dev\00_python_basics
echo.
echo  =================  上次的成绩  =================
"C:\Users\28643\miniconda3\envs\career\python.exe" run_all.py
echo.
echo  ==========================================================
echo   接下来只做 3 件事：
echo     1) 浏览器打开 https://www.liaoxuefeng.com/books/python/
echo        看今日任务.md 里指定的章节
echo     2) VS Code 里写 00_python_basics\exercises\ 里的题
echo     3) 回来敲  python run_all.py ex01   判题
echo  ----------------------------------------------------------
echo   写完提交（两行）：
echo     git add .
echo     git commit -m "完成 ex01 第1题"
echo  ==========================================================
echo.
pause
