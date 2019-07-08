from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey, Table
from src.db_utils.base import Base
from sqlalchemy.orm import relationship

packet_ssids_association = Table('packets_ssids', Base.metadata,
                                 Column('packet_id', Integer, ForeignKey('packets.id')),
                                 Column('ssid_id', Integer, ForeignKey('ssids.id'))
                                 )

class Packet(Base):
    __tablename__ = 'packet'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    decibels = Column(Integer)
    mac_address = Column(String)
    channel = Column(Integer)
    type = Column(Enum)
    ssid = relationship("Ssid", secondary=packet_ssids_association)

    def __init__(self, timestamp_init, decibels_init, mac_address_init, channel_init, ssid_init):
        self.timestamp = timestamp_init
        self.decibels = decibels_init
        self.mac_address = mac_address_init
        self.channel = channel_init

        class Type(Enum):
            probe_request = 'probe_request'
            beacon = 'beacon'

        self.type = Type
        self.ssid = ssid_init

    def __repr__(self):
        return "".join(["Packet(", str(self.mac_address), ", ", str(self.timestamp), ", ", str(self.decibels), ",", str(self.type), ",",  str(self.ssid), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Packet):
            return self.timestamp == other.timestamp & self.decibels == other.decibels & self.mac_address == other.mac_address & self.type == other.type
        return False
