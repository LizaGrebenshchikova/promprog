import pika
from time import sleep

if __name__ == '__main__':                                                      
 
    fin = open('input.txt')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit', port=5672))

    channel = connection.channel()
    channel.queue_declare(queue='queue')

    for line in fin.readlines():
        line = line.strip()
        channel.basic_publish(exchange='', routing_key='queue', body=line)

    fin.close()
    connection.close()