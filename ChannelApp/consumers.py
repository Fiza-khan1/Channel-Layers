from channels.generic.websocket import AsyncWebsocketConsumer
import json
import random
class myAsyncConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
        print("Websocket connected...", event)
        # Join a group (you can use any group name, here "chat_group")
        print("CHANEL_LAYER",self.channel_layer)
        print("CHANEL_NAME",self.channel_name)
        await self.channel_layer.group_add(
            "chat_group",
            self.channel_name
        )
        # self.scope["session"]["seed"] = random.randint(1, 1000)
        await self.accept()

    async def websocket_receive(self, event):
        # Extract the message text from the event
        text_data = event.get('text')
        print("WebSocket received message:", text_data)

        # Broadcast message to the group
        await self.channel_layer.group_send(
            "chat_group",
            {
                'type': 'chat_message',
                'message': text_data
            }
        )

    async def chat_message(self, event):
        # Send message to WebSocket
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def websocket_disconnect(self, event):
        print("Websocket disconnected...", event)
        # Leave the group
        await self.channel_layer.group_discard(
            "chat_group",
            self.channel_name
        )
