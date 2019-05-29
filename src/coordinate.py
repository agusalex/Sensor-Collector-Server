from math import sin, cos, sqrt, atan2, radians


class Coordinate:
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


def distance(coora, coorb):
    r = 6373.0  # Earth's radius

    lat1 = radians(coora.lat)
    lon1 = radians(coora.lon)
    lat2 = radians(coorb.lat)
    lon2 = radians(coorb.lon)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return r * c
