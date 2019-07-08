from math import sin, cos, sqrt, atan2, radians
from sqlalchemy import Column, Float, Integer
from src.db_utils.base import Base


class Coordinate(Base):
    __tablename__ = 'coordinate'

    id = Column(Integer, primary_key=True)
    lat = Column(Float)
    lon = Column(Float)

    def __init__(self, lat_init, lon_init):
        self.lat = lat_init
        self.lon = lon_init

    def __repr__(self):
        return "".join(["Point(", str(self.lat), ",", str(self.lon), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Coordinate):
            return (self.lat == other.lat) & (self.lon == other.lon)
        return False

    def shift(self, lat, lon):
        self.lat += lat
        self.lon += lon

    def distance(self, coorb):
        r = 6373.0  # Earth's radius

        lat1 = radians(self.lat)
        lon1 = radians(self.lon)
        lat2 = radians(coorb.lat)
        lon2 = radians(coorb.lon)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return r * c
