import paho.mqtt.client as mqtt
import os

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("test")
	client.subscribe("topic")
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	if msg.payload == "on":
		print "Received message!"
		os.system("python /home/pi/GeoPark-laite/koodit/Testikoodit/TiedonLisaysTietokantaan_v1.py")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("ryhma2")
client.loop_forever()
