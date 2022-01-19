import sys
from kafka import KafkaConsumer

#specifying the sample topic
consumer = KafkaConsumer("PythonTest")

#if we don't specify the bootstrap_server in the argument of kafkaconsumer, the default port/broker it will point to is
#the localhost:9092, otherwise-
#consumer = KafkaConsumer(topicname, bootstrap_server= localhost:9092)

try:
    for message in consumer:
        print(message) #prints the complete message object along with all the metadata
        print(message.value.decode(), message.topic)    #prints only the value after decoding along with the topic.
        print()

except KeyboardInterrupt:
    sys.exit()

