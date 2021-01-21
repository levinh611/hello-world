from kafka import  KafkaProducer
import time
bootstrap_servers = ['localhost:9092']
topicName = 'newtopic'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

while True:
    producer.send(topicName, b"vinhle", partition=0)
    producer.send(topicName, b"hello", partition=1)
    time.sleep(4)
producer.close()
