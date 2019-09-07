from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.db_utils.base import Base


class Triangulation(Base):
    __tablename__ = 'triangulation'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    location_id = Column(Integer, ForeignKey("point.id"))
    location = relationship("Point", foreign_keys=[location_id])
    mac_addr = Column(String)

    def __init__(self, point_init, timestamp_init, mac_addr_init):
        self.timestamp = timestamp_init
        self.location = point_init
        self.mac_addr = mac_addr_init

    def __repr__(self):
        return "".join(["Triangulation(", str(self.timestamp), ", ", str(self.location.x), ", ", str(self.location.y), ", ", str(self.mac_addr), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Triangulation):
            return self.mac_addr == other.mac_addr & self.timestamp == other.timestamp
        return False
