import paho.mqtt.client as mqtt
import os
import keyboard
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("test")
	client.subscribe("topic")
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	if msg.payload == "on":
		print "Received PARKING message!"
		os.system("python /home/pi/GeoPark-laite/koodit/Testikoodit/TiedonLisaysTietokantaan_v1.py")
	if msg.payload == "vstart":
		print "Received VIDEO START message!"
		os.system("python /home/pi/GeoPark-laite/koodit/Testikoodit/mqtt_nauhoitus_lahetys.py")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("172.20.240.52")
client.loop_forever()
