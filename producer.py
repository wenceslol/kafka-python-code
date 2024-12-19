import time
import json
import random
from datetime import datetime
from data_generator import generate_message 
from kafka import KafkaProducer 

# Mensagens serializadas em JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')

# Produtor Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    api_version=(3,9,0),
    value_serializer=serializer
)

if __name__ == '__main__':
    # Loop infinito até fechar o programa
    while True:
        # Gera uma mensagem
        dummy_message = generate_message()
        # Envia as mensagens para o topico 'messages'
        print(f'Produzindo mensagem @ {datetime.now()} | Mensagem = {str(dummy_message)}')
        producer.send('messages', dummy_message)
        # Timer em segundos
        time_to_sleep = random.randint(1, 11)
        time.sleep(time_to_sleep)