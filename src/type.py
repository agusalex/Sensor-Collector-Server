from sqlalchemy import Column,Integer, CHAR, ForeignKey
from src.db_utils.base import Base
from sqlalchemy.orm import relationship


class Type(Base):
    __tablename__ = 'type'

    id = Column(Integer, primary_key=True)
    type = Column(CHAR)

    def __init__(self, type_init):
        self.type = type_init

    def __repr__(self):
        return "".join(["Type(", str(self.type),  ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Type):
            return self.type == other.type
        return False

    def get_type(self):
        if self.type == 'B':
            return 'beacon'
        elif self.type == 'C':
            return 'client'
        elif self.type == 'R':
            return 'random_mac'
