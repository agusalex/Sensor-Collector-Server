from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.db_utils.base import Base


class Device(Base):
    __tablename__ = 'device'

    id = Column(Integer, primary_key=True)
    geometry_id = Column(Integer, ForeignKey("circle.id"))
    geometry = relationship("Circle", foreign_keys=[geometry_id])
    mac_addr = Column(String)

    def __init__(self, circle_init, mac_address_init):
        self.geometry = circle_init
        self.mac_address = mac_address_init

    def __repr__(self):
        return "".join(["Device(", str(self.geometry.center.x), ", ", str(self.geometry.center.y), ", ", str(self.geometry.radius), ", ", str(self.mac_address), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Device):
            return self.mac_address == other.mac_address
            # Si consideramos que dos pueden tener la misma mac
            # return (self.geometry.center.x == other.geometry.center.x) & (self.geometry.center.y == other.geometry.center.y) & (self.geometry.radius == other.geometry.radius) & (self.mac_address == other.mac_address)
        return False
