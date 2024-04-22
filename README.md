# Python-kafka-SQLServer
Generated Real time data using python lib Faker and Kafka and store that data into SQLServer
# Requirements
1) Kafka
    bin/kafka-server-start.sh config/server.properties
2) Zookeeper
   bin/zookeeper.server.sh config/zookeeper.properties
5) java # install java
6) pip install kafka-python sqlalchemy pymssql
7) Faker install Faker lib using pip
8) SQL Server

   These above requirements are required according to their compatible versions


   Its a simple code for understanding how kafka producer produce data using Faker and then how kafak consumer consume data.
   After that how we can store these data into database that we use SQL Server.

# we have three files in python written
1) data.py
Generated data by using 3 fields as menstion in data.py
2) producer.py
produce data using Faker lib in producer kafak
3) consumer.py
   Consume data and store in SQL Server 
