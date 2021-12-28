import pika
from crawler import get_content_items, get_item
import warnings
warnings.filterwarnings("ignore")

USER_NAME = "hoang"
PASSWORD = "hoang"
HOST_ADDR = "192.168.1.55"
BATCH_SIZE = 100

credentials = pika.PlainCredentials(USER_NAME, PASSWORD)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST_ADDR, credentials=credentials))


channel = connection.channel()

channel.queue_declare(queue='foody')

content_items = get_content_items()
print("Number of items found:", len(content_items))


for i in range(0, len(content_items), BATCH_SIZE):
    data = get_item(content_items[i : i + BATCH_SIZE])
    channel.basic_publish(exchange='', routing_key='foody', body=data)
    print(f" [x] Sent items from index {i} to {i + BATCH_SIZE - 1}")
connection.close()




