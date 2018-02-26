import pika                                      
from pymongo import MongoClient

if __name__ == '__main__':                                               
    db = MongoClient(host='db', port=27017)['TheFirstTask']

    def callback(channel, method, properties, body):             
        db['messages'].insert({'message': body})                         
                      
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit', port=5672))
    channel = connection.channel()
    channel.queue_declare(queue='queue')          
    channel.basic_consume(callback, queue='queue', no_ack=True)
    channel.start_consuming()