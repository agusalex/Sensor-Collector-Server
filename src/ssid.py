from sqlalchemy import Column, String, Integer
from src.db_utils.base import Base
from sqlalchemy.orm import relationship


class Ssid(Base):
    __tablename__ = 'ssid'

    id = Column(Integer, primary_key=True)

    name = Column(String)

    def __init__(self, name_init):
        self.name = name_init

    def __repr__(self):
        return "".join(["SSID(", str(self.name),  ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Ssid):
            return self.name == other.name
            # Si consideramos que dos pueden tener la misma mac
            # return (self.geometry.center.x == other.geometry.center.x) & (self.geometry.center.y == other.geometry.center.y) & (self.geometry.radius == other.geometry.radius) & (self.mac_address == other.mac_address)
        return False

    def __hash__(self):
        return hash(str(self.name))