import pika
import json

def send_tiket(qr_path: str, telegram_chat_id: str) -> None:
    """
    Создает сообщение и отправляет его в очередь RabitMQ
    """
    credentials = pika.PlainCredentials(username='guest', password='guest')
    parameters = pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='orders', durable=True)

    message = {"qr_path": qr_path, "telegram_chat_id": telegram_chat_id}
    message = json.dumps(message)
    channel.basic_publish(exchange='', routing_key='orders', body=message.encode('utf-8'))
    channel.close()
    connection.close()