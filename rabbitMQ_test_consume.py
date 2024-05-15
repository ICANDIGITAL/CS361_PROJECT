import pika

# Establish a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='CS361')

# Define the callback function
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Set up consumption
channel.basic_consume(queue='CS361',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()