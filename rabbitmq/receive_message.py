import pika

mq_host = '35.226.138.244'
mq_user = 'test'
mq_pass = 'abc@123'

def get_message(queue_name):
    credentials = pika.PlainCredentials(mq_user, mq_pass)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=mq_host, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    
    method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)
    connection.close()
    
    if method_frame:
        return body.decode("utf-8")
        
        
print(get_message('q1'))