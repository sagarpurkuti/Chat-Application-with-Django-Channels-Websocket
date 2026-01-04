# 🚀 QUICK START - WebSocket Chatroom

## ✅ Easy Way: Use `python manage.py runserver`
<!-- daphne -b 127.0.0.1 -p 8000 core.asgi:application -->

**Good news!** This project includes a custom `runserver` command that automatically uses ASGI (Daphne) when `ASGI_APPLICATION` is configured. This means you can use the familiar Django command:

```bash
python manage.py runserver
```

The custom command will automatically:
- ✅ Detect that `ASGI_APPLICATION` is set in `settings.py`
- ✅ Use Daphne (ASGI server) for WebSocket support
- ✅ Show a clear message indicating WebSocket support is enabled

## 🎯 Alternative Methods

### Option A: Use the batch file
```bash
start_server.bat
```

### Option B: Run Daphne directly
```bash
daphne -b 127.0.0.1 -p 8000 core.asgi:application
```

### Option C: Using Python module
```bash
python -m daphne -b 127.0.0.1 -p 8000 core.asgi:application
```

## 📋 What You Should See

When using `python manage.py runserver`, you'll see:
```
======================================================================
Starting ASGI/Channels development server at http://127.0.0.1:8000/
Using ASGI application: core.routing.application
WebSocket support: ✅ ENABLED
Quit the server with CTRL-BREAK.
======================================================================
```

When using Daphne directly, you'll see:
```
Starting server at tcp:port=8000:interface=127.0.0.1
```

## 🧪 Test It

1. Start server with Daphne (using one of the methods above)
2. Open browser: `http://127.0.0.1:8000/chat/`
3. Enter a room name (e.g., "test")
4. Check browser console (F12) - you should see:
   - `WebSocket connection opened successfully`
   - Green status indicator
   - Send button enabled

## ✅ How It Works

The custom `runserver` command automatically:
1. Checks if `ASGI_APPLICATION` is configured in `settings.py`
2. If yes → Uses Daphne (ASGI) with WebSocket support
3. If no → Falls back to regular WSGI server

## ❌ Common Mistakes

- ❌ Not having `ASGI_APPLICATION` set in `settings.py` → Will use WSGI (no WebSockets)
- ✅ Having `ASGI_APPLICATION = 'core.routing.application'` → Will use ASGI (WebSockets work!)

## 🔍 Verify Daphne is Installed in Venv

```bash
venv\Scripts\python.exe -m pip show daphne
```

If not installed in venv:
```bash
venv\Scripts\python.exe -m pip install daphne==4.1.0
```

**Important:** Make sure daphne is installed in your virtual environment, not just globally!

## 📝 Summary

| Command | WebSocket Support | Status |
|---------|------------------|--------|
| `python manage.py runserver` | ✅ YES | **Use this!** (Custom command) |
| `daphne ...` | ✅ YES | Also works! |
| `start_server.bat` | ✅ YES | Convenient batch file |

---

**The custom `runserver` command makes it easy - just use `python manage.py runserver` as usual!**

