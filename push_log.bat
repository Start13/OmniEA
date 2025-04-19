@echo off
cd /d "%~dp0"
echo [*] Spostato in cartella: %cd%

REM Esegui lo script Python per push su GitHub
python fast_push.py

pause
