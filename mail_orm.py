from sqlalchemy import Column, Text, Integer, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Message(Base):
    __tablename__ = 'messages'
    message_id = Column(Integer, primary_key=True)
    source = Column(Text)
    sender = Column(Text)
    recipients = Column(Text)
    body = Column(Text)
    message_read = Column(Boolean, default=False)
    time_received = Column(Float, default=0)
    ttl_ts = Column(Float, default=0)

class Client(Base):
    __tablename__ = 'clients'
    client_id = Column(Integer, primary_key=True)
    client_name = Column(Text)
    client_email = Column(Text)
    synonym1 = Column(Text)
    synonym2 = Column(Text)
    synonym3 = Column(Text)
