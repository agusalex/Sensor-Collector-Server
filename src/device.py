from src.circle import Circle


class Device:
    def __init__(self, x_init, y_init, r_init, mac_address_init):
        self.geometry = Circle(x_init, y_init, r_init)
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
