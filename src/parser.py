import json
import csv
import datetime;
from src.packet import Packet
from src.ssid import Ssid
from src.db_utils import db_interact
jsondir = '../data/received.json'
csvdir = '../data/mac-vendors.csv'


def get_vendor(input_mac):
    reader = csv.reader(open(csvdir), delimiter=',', quotechar='|')
    device_oui = get_oui(input_mac)
    for row in reader:
        if device_oui == row[0]:
            return row[1]


def get_oui(input_mac):
    input_mac = input_mac[:8]
    input_mac = input_mac.replace(':', '')
    return input_mac.upper()


def save_packets(mac_list, decib_list, channel_list):
    timestamp = datetime.datetime.now()
    ssid = Ssid('IDEI')
    type = 'probe_request'

    for mac in mac_list:
        for decib in decib_list:
            for ch in channel_list:
                db_interact.persist(Packet(timestamp, decib, mac, ch, [ssid], type))
                print(timestamp, decib, mac, ch, [ssid], type)
    db_interact.persist(ssid)


with open(jsondir, 'r') as fp:
    obj = json.load(fp)

macs = obj["MAC"]
decibs = obj["RSSI"]
channels = obj["CH"]

print(macs, decibs, channels)

for mac in macs:
    get_vendor(mac)

save_packets(macs, decibs, channels)






# def __init__(self, timestamp_init, decibels_init, mac_address_init, channel_init, ssid_init):
#     self.timestamp = timestamp_init
#     self.decibels = decibels_init
#     self.mac_address = mac_address_init
#     self.channel = channel_init
#
#     class Type(Enum):
#         probe_request = 'probe_request'
#         beacon = 'beacon'
#
#     self.type = Type
#     self.ssid = ssid_init

# def __init__(self, name_init):
#     self.name = name_init