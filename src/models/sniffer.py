from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.db_utils.base import Base


class Sniffer(Base):
    __tablename__ = 'sniffer'

    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey("point.id"))
    coverage_id = Column(Integer, ForeignKey("circle.id"))
    location = relationship("Point", foreign_keys=[location_id])
    coverage = relationship("Circle", foreign_keys=[coverage_id])
    mac_addr = Column(String)

    def __init__(self, point_init, circle_init, mac_address_init):
        self.location = point_init
        self.coverage = circle_init
        self.mac_address = mac_address_init

    def __repr__(self):
        return "".join(["Sniffer(", str(self.coverage.center.x), ", ", str(self.coverage.center.y), ", ", str(self.coverage.radius), ", ", str(self.mac_address), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Sniffer):
            return self.mac_address == other.mac_address
            # Si consideramos que dos pueden tener la misma mac
            # return (self.geometry.center.x == other.geometry.center.x) & (self.geometry.center.y == other.geometry.center.y) & (self.geometry.radius == other.geometry.radius) & (self.mac_address == other.mac_address)
        return False
