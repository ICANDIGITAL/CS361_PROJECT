import pika

# Establish a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a queue named 'CS361'
channel.queue_declare(queue='CS361')

# Publish a message to the 'CS361' queue
channel.basic_publish(exchange='',
                      routing_key='CS361',
                      body='A message from CS361')

print(" [x] Sent 'A message from CS361'")

# Close the connection
connection.close()