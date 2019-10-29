import os
from dotenv import load_dotenv
from kafka import KafkaProducer
from kafka.errors import KafkaError

load_dotenv()

producer = KafkaProducer(bootstrap_servers=os.getenv('KAFKA'))


class Controller:

    @staticmethod
    async def handle_websocket(topic_id, asset_id, websocket):
        while True:
            data = await websocket.receive()
            producer.send(topic_id, key=asset_id.encode('utf-8'), value=data.encode('utf-8'))
            producer.flush()

    @staticmethod
    async def handle_topic_request(request, response):
        print('Topic Request')
