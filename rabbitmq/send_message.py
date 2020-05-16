import pika

mq_host = '35.226.138.244'
mq_user = 'test'
mq_pass = 'abc@123'

def send_message(queue_name, message):
    credentials = pika.PlainCredentials(mq_user, mq_pass)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=mq_host, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)
    connection.close()
    
send_message('q1', 'Hello rabbit!')    