import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer

logger = logging.getLogger(__name__)


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = f'chat_{self.room_name}'
            
            logger.info(f"WebSocket connection attempt for room: {self.room_name}")

            # Join room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            
            # Accept the WebSocket connection
            await self.accept()
            logger.info(f"WebSocket connected successfully for room: {self.room_name}")
            
        except Exception as e:
            logger.error(f"Error during WebSocket connection: {e}")
            await self.close()

    async def disconnect(self, close_code):
        try:
            # Leave room group
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )
            logger.info(f"WebSocket disconnected from room: {self.room_name}")
        except Exception as e:
            logger.error(f"Error during WebSocket disconnection: {e}")

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json.get('message', '')
            username = text_data_json.get('username', 'Anonymous')

            if not message:
                return

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                }
            )
            logger.debug(f"Message received in room {self.room_name} from {username}")
        except json.JSONDecodeError:
            logger.error("Invalid JSON received")
        except Exception as e:
            logger.error(f"Error processing message: {e}")

    async def chat_message(self, event):
        """Receive message from room group and send to WebSocket"""
        try:
            message = event.get('message', '')
            username = event.get('username', 'Anonymous')
            
            # Send message to WebSocket
            await self.send(text_data=json.dumps({
                'message': message,
                'username': username,
            }))
        except Exception as e:
            logger.error(f"Error sending message to WebSocket: {e}")