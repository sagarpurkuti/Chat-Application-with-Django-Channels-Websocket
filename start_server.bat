@echo off
echo.
echo ============================================
echo   Django Chatroom - Starting Server
echo ============================================
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

echo IMPORTANT: Using Daphne (ASGI) for WebSocket support
echo.
echo Server URL: http://127.0.0.1:8000/
echo WebSocket: ws://127.0.0.1:8000/ws/chat/[room_name]/
echo.
echo Press CTRL+C to stop the server
echo.
echo ============================================
echo.

REM Use python -m daphne to ensure we use the venv Python
python -m daphne -b 127.0.0.1 -p 8000 core.asgi:application

