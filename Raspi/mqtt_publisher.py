import paho.mqtt.publish as publish

publish.single("test","on",hostname="ryhma2")
print("DONE")
