from math import hypot
from sqlalchemy import Column, Float, Integer
from src.db_utils.base import Base


class Point(Base):
    __tablename__ = 'point'

    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column(Float)

    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Point):
            return (self.x == other.x) & (self.y == other.y)
        return False

    def __hash__(self):
        return hash(str(self))

    def shift(self, x, y):
        self.x += x
        self.y += y

    def distance(self, b):
        return hypot(self.x - b.x, self.y - b.y)
