@echo off
echo ========================================
echo Starting Django Chatroom Server
echo Using Daphne (ASGI) for WebSocket support
echo ========================================
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

echo Server will be available at: http://127.0.0.1:8000/
echo WebSocket endpoint: ws://127.0.0.1:8000/ws/chat/[room_name]/
echo.
echo Press CTRL+C to stop the server
echo.

REM Use python -m daphne to ensure we use the venv Python
python -m daphne -b 127.0.0.1 -p 8000 core.asgi:application

