from src.circle import Point, Circle


class Sniffer:
    def __init__(self, x_init, y_init, r_init, mac_address_init):
        self.location = Point(x_init, y_init)
        self.coverage = Circle(self.location.x, self.location.y, r_init)
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
