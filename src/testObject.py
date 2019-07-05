class TestObject:
    def __init__(self, mac_address_init, db_init):
        self.mac_address = mac_address_init
        self.db = db_init

    def __repr__(self):
        return "".join(["TestObject(", str(self.mac_address), ", ", str(self.db), ") "])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, TestObject):
            return self.mac_address == other.mac_address
            # Si consideramos que dos pueden tener la misma mac
            # return (self.geometry.center.x == other.geometry.center.x) & (self.geometry.center.y == other.geometry.center.y) & (self.geometry.radius == other.geometry.radius) & (self.mac_address == other.mac_address)
        return False
