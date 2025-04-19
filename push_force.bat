@echo off
cd /d "%~dp0"
echo [*] Spostato in cartella: %cd%

REM Esegui push forzato
python fast_push.py

echo.
echo ✅ Push completato con forza su GitHub!
pause
