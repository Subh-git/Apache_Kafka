from kafka import KafkaProducer
from time import sleep

#since we are using kafka producer so we applied that and sleep is to give a gap between two inputs.

#describing the producer and the broker to which to connect to.
my_prod = KafkaProducer(bootstrap_servers = ['localhost:9092'])

topic = "PythonTest"

lst = ["Subhadeep", "Rahul", "Shyam", "Jitesh","Ravi"]

for i in lst:
    j= bytes(i,encoding= 'utf8')
    print(j)
    test = my_prod.send(topic,j)
    print("The value of i:",i)
    print(test)
    print("Selected particulars")
    metadata = test.get()
    #print(metadata.topic)
    #print(metadata.partition)
    print(metadata)
    print()
    sleep(4)