from sqlalchemy import Column, Text, Integer, Boolean, Float, BIGINT, VARCHAR, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey

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


class Site(Base):
    __tablename_ = 'sites'
    site_id = Column(Integer, primary_key=True)
    site_num = Column(Integer)
    site_name = Column(VARCHAR)
    geo_address = Column(VARCHAR)
    geo_city = Column(VARCHAR)
    geo_state = Column(VARCHAR)
    geo_zipcode = Column(VARCHAR)
    store_phone = Column(BIGINT)
    ems_type = Column(VARCHAR)
    commissioned_date = Column(Date)
    area_sqft = Column(Float)
    ip_address = Column(VARCHAR)
    geo_latitude = Column(Float)
    geo_longitude = Column(Float)
    wstn_primary = Column(Integer)
    wstn_secondary = Column(Integer)
    monitor_status = Column(VARCHAR)
    time_zone = Column(VARCHAR)
    site_email = Column(VARCHAR)
    client_id = Column(Integer, ForeignKey(Client.client_id))
