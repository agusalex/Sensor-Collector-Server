from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from src.db_utils.base import Base
from sqlalchemy.orm import relationship


class Packet(Base):
    __tablename__ = 'packet'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    decibels = Column(Integer)
    mac_address = Column(String)
    channel = Column(Integer)
    type_id = Column(Integer, ForeignKey('type.id'))
    type = relationship('Type')
    destination = Column(String)

    def __init__(self, timestamp_init, decibels_init, mac_address_init, channel_init, destination_init, type_init):
        self.timestamp = timestamp_init
        self.decibels = decibels_init
        self.mac_address = mac_address_init
        self.channel = channel_init
        self.type = type_init
        self.destination = destination_init

    def __repr__(self):
        return "".join(["Packet(", str(self.mac_address), ", ", str(self.timestamp), ", ", str(self.decibels), ",", str(self.type), ",",  str(self.ssids), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Packet):
            return self.timestamp == other.timestamp & self.decibels == other.decibels & self.mac_address == other.mac_address & self.type == other.type
        return False
