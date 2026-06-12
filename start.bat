@echo off
rem Launch the Ruen Bongkot website — double-click this file or run "start.bat"
cd /d "%~dp0"
python run.py %*
if errorlevel 1 pause
