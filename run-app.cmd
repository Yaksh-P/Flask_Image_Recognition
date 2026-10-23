@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo The virtual environment is missing. Follow STEP1-SETUP.md first.
  pause
  exit /b 1
)
echo Open http://127.0.0.1:9000 in your browser.
".venv\Scripts\python.exe" -m flask --app app run --port 9000
pause

