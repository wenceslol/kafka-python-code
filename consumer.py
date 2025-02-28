import json 
from kafka import KafkaConsumer 


if __name__ == '__main__':
    # Kafka Consumer
    consumer = KafkaConsumer(
        'messages',
        bootstrap_servers='localhost:9092',
        api_version=(3,9,0),
        auto_offset_reset='earliest'
    )
    for message in consumer:
        print(json.loads(message.value))