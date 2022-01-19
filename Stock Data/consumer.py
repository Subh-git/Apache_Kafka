import json
from kafka import KafkaConsumer
import csv



topic = "PythonTest"
#we can set other options like auto_offset = 'earliest', this will fetch all the messages from the beginning of the 
#topic. We do the loads as we have serialised in json format before sending.

consumer = KafkaConsumer(topic,value_deserializer=lambda x: json.loads(x.decode('utf-8')))


#since we know we the type of data we are expecting and so we modify it to csv format for proper working.

with open('/home/hdoop/TestKafka/CsvStock.csv','w') as file:
    csvwriter = csv.writer(file)    #creating a csv writer object with write prmission

    for messages in consumer:
        val = messages.value
        print(val)                  #to print and show in the console 
        csvwriter.writerow(val)     #to store the data in csv format



  
        




