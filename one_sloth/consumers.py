import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AlertConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Все страницы /alert присоединяются к одной группе "alert_group"
        self.group_name = "alert_group"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # Метод для получения сообщений из группы
    async def alert_message(self, event):
        # Отправляем полученное сообщение в WebSocket клиента (браузера)
        await self.send(text_data=json.dumps({
            "type": "alert",
            "achievement": event["achievement"]
        }))