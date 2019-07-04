from enum import Enum


class Packet:
    def __init__(self, timestamp_init, decibels_init, mac_address_init):
        self.timestamp = timestamp_init
        self.decibels = decibels_init
        self.mac_address = mac_address_init

        class Type(Enum):
            probe_request = 'probe_request'
            beacon = 'beacon'

        self.type = Type
        self.ssid = []

    def __repr__(self):
        return "".join(["Packet(", str(self.mac_address), ", ", str(self.timestamp), ", ", str(self.decibels), ",", str(self.type), ",",  str(self.ssid), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Packet):
            return self.timestamp == other.timestamp & self.decibels == other.decibels & self.mac_address == other.mac_address & self.type == other.type
        return False
