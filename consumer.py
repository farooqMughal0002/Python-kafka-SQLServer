from kafka import KafkaConsumer
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
# Kafka consumer settings
bootstrap_servers = '172.16.255.247:9092'
topic = 'test2'

# Database connection settings for SQL Server
db_url = 'mssql+pymssql://ABC-PC:123@127.0.0.1/Test'

# Kafka consumer
consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers,api_version=(0,10))

# SQLAlchemy setup
Base = declarative_base()


# Define your database schema
class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer,autoincrement=True,primary_key=True)
    name = Column(String)
    address = Column(String)
    created_at = Column(String)


# Create database engine and tables
engine = create_engine(db_url)
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Consume messages from Kafka and write to the database
for msg in consumer:
    # Decode message value
    message_data = json.loads(msg.value.decode('utf-8'))
    name = message_data['name']
    address = message_data['address']
    created_at = message_data['created_at']
    print(message_data)

    # Create a new Message object and add it to the session
    message = Message(name=name, address=address, created_at=created_at)
    session.add(message)
    # Commit the session periodically to write to the database
    session.commit()

# Close the Kafka consumer and session
consumer.close()
session.close()
