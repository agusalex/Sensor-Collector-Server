from sqlalchemy import Column, Integer, String
from src.db_utils.base import Base


class TestObject(Base):
    __tablename__ = 'testobjects'

    id = Column(Integer, primary_key=True)
    mac_addr = Column(String)
    decib = Column(Integer)

    def __init__(self, mac_addr, decib):
        self.mac_addr = mac_addr
        self.decib = decib

    def __repr__(self):
        return "".join(["TestObject(", str(self.mac_addr), ", ", str(self.db), ") "])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, TestObject):
            return self.mac_addr == other.mac_addr
            # Si consideramos que dos pueden tener la misma mac
            # return (self.geometry.center.x == other.geometry.center.x) & (self.geometry.center.y == other.geometry.center.y) & (self.geometry.radius == other.geometry.radius) & (self.mac_address == other.mac_address)
        return False
