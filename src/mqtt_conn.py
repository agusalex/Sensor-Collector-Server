import paho.mqtt.client as mqtt
from src.parser import parse_and_save


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print('Connected with result code %s' % rc)
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed. There are other methods to achieve this.
    client.subscribe("arduino")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("We got a message!")
    print('%s %s' % (msg.topic, msg.payload))
    parse_and_save(msg.payload)


client = mqtt.Client(client_id='triangulation-subs', clean_session=False)
client.on_connect = on_connect
client.on_message = on_message

# client.connect("iot.eclipse.org", 1883, 60)
client.connect(host='127.0.0.1', port=1883)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()




# import sys
#
# import paho.mqtt.client
# from src.parser import parse_and_save
#
#
# def on_connect(client, userdata, flags, rc):
#     print('connected (%s)' % client._client_id)
#     client.subscribe(topic='arduino', qos=2)
#
#
# def on_message(client, userdata, message):
#     print('------------------------------')
#     print('topic: %s' % message.topic)
#     print('payload: %s' % message.payload)
#     print('qos: %d' % message.qos)
#     parse_and_save(message.payload)
#
#
# def main():
#     client = paho.mqtt.client.Client(client_id='triangulation-subs', clean_session=False)
#     client.on_connect = on_connect
#     client.on_message = on_message
#     client.connect(host='127.0.0.1', port=1883)
#     client.loop_forever()
#
#
# if __name__ == '__main__':
#     main()
#
# sys.exit(0)
