# Django WebSocket Chatroom

A real-time chatroom application built with Django 6.0 and Django Channels 4.3.2, featuring WebSocket support for instant messaging.

## Features

- ✅ Real-time messaging via WebSocket
- ✅ Multiple chat rooms support
- ✅ Modern, attractive UI with gradient design
- ✅ Message timestamps
- ✅ Connection status indicator
- ✅ Responsive design
- ✅ Anonymous user support

## Requirements

- Python 3.8+
- Django 6.0
- Django Channels 4.3.2
- Daphne 4.1.0 (ASGI server)

## Installation

1. **Activate your virtual environment:**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

### ⚠️ Important: Use Daphne, not `runserver`

Django's default `runserver` command uses WSGI, which **does not support WebSockets**. You **must** use Daphne (ASGI server) for WebSocket functionality.

### Option 1: Using the batch file (Windows)

```bash
run_server.bat
```

### Option 2: Using Daphne directly

```bash
daphne -b 127.0.0.1 -p 8000 core.asgi:application
```

### Option 3: Using uvicorn (alternative)

```bash
uvicorn core.asgi:application --host 127.0.0.1 --port 8000
```

## Usage

1. **Start the server** using one of the methods above
2. **Open your browser** and navigate to: `http://127.0.0.1:8000/chat/`
3. **Enter a room name** (e.g., "general", "python", "javascript")
4. **Start chatting!** Messages are sent and received in real-time

## Project Structure

```
Chatroom/
├── core/               # Main project configuration
│   ├── asgi.py        # ASGI configuration
│   ├── routing.py     # WebSocket routing
│   ├── settings.py    # Django settings
│   └── urls.py        # URL configuration
├── chat/              # Chat application
│   ├── consumers.py   # WebSocket consumer
│   ├── routing.py     # WebSocket URL patterns
│   ├── templates/     # HTML templates
│   └── views.py       # HTTP views
└── requirements.txt   # Python dependencies
```

## WebSocket Endpoint

The WebSocket endpoint follows this pattern:
```
ws://127.0.0.1:8000/ws/chat/[room_name]/
```

Example:
```
ws://127.0.0.1:8000/ws/chat/general/
```

## Troubleshooting

### WebSocket connection fails (404 error)

- **Make sure you're using Daphne**, not `python manage.py runserver`
- Check that `ASGI_APPLICATION = 'core.routing.application'` is set in `settings.py`
- Verify the WebSocket URL pattern matches: `/ws/chat/[room_name]/`

### Send button is disabled

- Check browser console for WebSocket connection errors
- Verify the server is running with Daphne
- Check that the room name doesn't contain invalid characters

### Messages not appearing

- Open browser console (F12) and check for JavaScript errors
- Verify WebSocket connection status (green indicator = connected)
- Check server logs for any errors

## Development

### Running migrations

```bash
python manage.py migrate
```

### Creating a superuser

```bash
python manage.py createsuperuser
```

### Accessing admin panel

Navigate to: `http://127.0.0.1:8000/admin/`

## Configuration

### Channel Layers

Currently using `InMemoryChannelLayer` for development. For production, use Redis:

```python
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}
```

## License

This project is open source and available for educational purposes.

