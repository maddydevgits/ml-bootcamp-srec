import paho.mqtt.client as mqtt

client=mqtt.Client()
while True:
  k=input()
  client.connect('broker.hivemq.com',1883)
  print ('Broker Connected')
  client.publish('srec/ml',k)
