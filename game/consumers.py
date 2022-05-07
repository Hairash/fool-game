import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from game.models import Game


class WSConsumer(WebsocketConsumer):
    def __init__(self):
        super().__init__()
        self.game = None

    def connect(self):
        print('* channel_name', self.channel_name)
        async_to_sync(self.channel_layer.group_add)(
            'main',
            self.channel_name,
        )
        user = self.scope['user']
        print('* user', user)
        async_to_sync(self.channel_layer.group_add)(
            f'user_{user.username}',
            self.channel_name,
        )

        self.game = Game.get_game()
        if user.is_authenticated:
            self.game.players.add(user)
            self.game.save()
        print('* players:', self.game.players.all())

        self.accept()

        async_to_sync(self.channel_layer.group_send)(
            'main',
            {
                'type': 'players',
                'data': len(list(self.game.players.all()))
            }
        )

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            'main',
            self.channel_name,
        )

    def select_recipient_group(self) -> str:
        user_name = self.game.players.first().username
        return f'user_{user_name}'

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json['type']
        data = text_data_json['data']

        if message_type == 'message':
            ctr = int(data) + 1
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                'main',
                {
                    'type': 'message',
                    'data': ctr
                }
            )

        elif message_type == 'private_message':
            async_to_sync(self.channel_layer.group_send)(
                self.select_recipient_group(),
                {
                    'type': 'private_message',
                    'data': data,
                }
            )

        else:
            raise Exception('Unknown message type')

    # Receive message from room group
    def message(self, event):
        data = event['data']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type': 'message',
            'data': data,
        }))

    def players(self, event):
        data = event['data']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type': 'players',
            'data': data,
        }))

    def private_message(self, event):
        data = event['data']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type': 'private_message',
            'data': data,
        }))
