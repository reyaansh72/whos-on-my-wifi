@echo off
title HACKY LAN SCANNER
color 0A
mode con: cols=100 lines=40

:MENU
cls
echo ============================================================
echo                  HACKY LAN SCANNER
echo ============================================================
echo.
echo Select Mode:
echo.
echo 1. Clean Scan (Only Real Devices)
echo 2. Full Scan (Includes Junk + Auto Loop)
echo 3. Exit
echo.
set /p choice=Enter your choice [1-3]: 

if "%choice%"=="1" goto CLEAN
if "%choice%"=="2" goto FULL
if "%choice%"=="3" goto END
echo Invalid choice. Press any key to try again...
pause >nul
goto MENU

:CLEAN
cls
echo ============================================================
echo                  HACKY LAN SCANNER - CLEAN MODE
echo ============================================================
echo.
python main.py
echo.
pause
goto MENU

:FULL
cls
echo ============================================================
echo               HACKY LAN SCANNER - FULL MODE
echo        (Including Junk IPs + Auto Refresh)
echo ============================================================
echo.
python main.py --show-junk --loop
pause
goto MENU

:END
exit