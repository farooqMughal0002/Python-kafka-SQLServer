from kafka import KafkaProducer
import json
from data import *
import time
def json_serializer(data):
    return json.dumps(data).encode("utf-8")
producer = KafkaProducer(bootstrap_servers =['172.16.255.247:9092'],api_version=(0,10),value_serializer = json_serializer)


if __name__ == "__main__":
    while 1 == 1 :
        registered_users = get_registered_user()
        print(registered_users)
        producer.send("test2",registered_users)
        #time.sleep(4)
