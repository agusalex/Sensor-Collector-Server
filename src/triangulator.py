from src.models.packet import Packet
from src.db_utils import db_interact
from src.graph import draw
from src.models.circle import Circle
from src.models.point import Point
from src.models.sniffer import Sniffer
from src.models.packet import Packet
from src.models.triangulation import Triangulation
from itertools import islice, chain

ms_threshold = 10  # max permitted interval between packets to be triangulated
packets_list = []  # list with all the packets from all sniffers


def save_triangulation(triangulation):
    db_interact.open_session()
    db_interact.persist(triangulation)
    db_interact.close_session()


def group_packets():
    if len(packets_list) < 3:
        return
    device_packets = filter(lambda packet: packet.mac_address == packets_list[0].mac_address,
                            packets_list)  # get all the packets with the same mac_address as the first packet in the list
    device_packets = sorted(device_packets, key=lambda packet: packet.timestamp)  # order by timestamp
    device_packets = list(dict.fromkeys(device_packets))  # remove duplicates
    for used_packet in device_packets:  # remove from the main list the packets that are going to be analyzed
        packets_list.remove(used_packet)

    while len(device_packets) >= 3:
        first_three = take(3, device_packets)
        if ms_diff(first_three[0], first_three[1]) > ms_threshold or ms_diff(first_three[1],
                                                                             first_three[2]) > ms_threshold:
            device_packets.pop(0)  # if the permitted ms interval is exceeded
        else:
            triangulate(first_three[0], first_three[1], first_three[2])
            for triangulated_packet in first_three:
                device_packets.remove(triangulated_packet)

    # https://docs.python.org/3/library/itertools.html#itertools-recipes

    group_packets()


def triangulate(packet1, packet2, packet3):
    average_timestamp = timestamp_avg(packet1, packet2, packet3)
    sniffer1 = packet1.get_associated_sniffer
    sniffer2 = packet2.get_associated_sniffer
    sniffer3 = packet3.get_associated_sniffer

    #still missing the actual triangulation part

    #https://github.com/gheja/trilateration.js/blob/master/trilateration.js
    #https://github.com/savaki/trilateration/blob/master/trilateration.go
    #https://stackoverflow.com/questions/16485370/wifi-position-triangulation
    save_triangulation(Triangulation(Point(x,y), average_timestamp, packet1.mac_address))




def ms_diff(packet1, packet2):
    diff = abs(packet1.timestamp - packet2.timestamp)
    return diff.total_seconds() * 1000


def timestamp_avg(packet1, packet2, packet3):
    # why not (timestamp1 + timestamp3 + timestamp3 / 3)? --> https://stackoverflow.com/questions/41723105/average-of-two-timestamps-in-python
    timestamp1 = packet1.timestamp
    timestamp2 = packet2.timestamp
    timestamp3 = packet3.timestamp
    return timestamp1 + abs(timestamp3 - timestamp2 - timestamp1) / 3


def get_packets():
    sniffers_list = None  # look for the sniffers in the DB
    for (sniffer in sniffers_list):
        packets_list.append(sniffer.get_associated_packets)


def take(n, iterable):
    return list(islice(iterable, n))


# The received JSON file from a Sniffer will contain a Sniffer ID so we can identify it
# useful link for calculating distance in meters from a RSSI value https://appelsiini.net/2017/trilateration-with-n-points/

if __name__ == '__main__':
    pass
