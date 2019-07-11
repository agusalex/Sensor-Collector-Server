import json
import csv
import datetime
from src.packet import Packet
from src.type import Type
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
    ssid = 'IDEI'
    type = Type('C')

    db_interact.open_session()
    for mac in mac_list:
        for decib in decib_list:
            for ch in channel_list:
                # db_interact.persist(Packet(timestamp, decib, mac, ch, ssid, type))
                db_interact.persist(Packet(timestamp, decib, mac, ch, ssid, type))
                print(timestamp, decib, mac, ch, ssid, type)
    db_interact.close_session()

with open(jsondir, 'r') as fp:
    obj = json.load(fp)

macs = obj["MAC"]
decibs = obj["RSSI"]
channels = obj["CH"]

print(macs, decibs, channels)

for mac in macs:
    get_vendor(mac)

save_packets(macs, decibs, channels)