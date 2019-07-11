from sqlalchemy import Column,Integer, CHAR, ForeignKey
from src.db_utils.base import Base
from sqlalchemy.orm import relationship


class Type(Base):
    __tablename__ = 'type'

    id = Column(Integer, primary_key=True)
    # packet_id = Column(Integer, ForeignKey('packet.id'))
    # packet = relationship('Packet', back_populates='type')
    type = Column(CHAR)

    def __init__(self, type_init):
        self.type = type_init

    def __repr__(self):
        return "".join(["Type(", str(self.type),  ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Type):
            return self.type == other.type
            # Si consideramos que dos pueden tener la misma mac
            # return (self.geometry.center.x == other.geometry.center.x) & (self.geometry.center.y == other.geometry.center.y) & (self.geometry.radius == other.geometry.radius) & (self.mac_address == other.mac_address)
        return False

    def get_type(self):
        if self.type == 'B':
            return 'beacon'
        elif self.type == 'C':
            return 'client'
        elif self.type == 'R':
            return 'random_mac'
