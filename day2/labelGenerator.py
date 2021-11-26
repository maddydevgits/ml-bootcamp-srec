import paho.mqtt.client as mqtt

client=mqtt.Client()
client.connect('broker.hivemq.com',1883)
print ('Broker Connected')

client.subscribe('srec/ml')
label=0
def notification(client,userdata,msg):
    global label
    k=(msg.payload).decode('utf-8')
    k=k.split(',')
    temp=float(k[1])
    hum=float(k[2][:-1])
    if temp<22 and temp>=20:
      label=1
    elif temp<24 and temp>=22:
      label=2
    elif temp<26 and temp>=24:
      label=3
    elif temp<28 and temp>=26:
      label=4
    elif temp<30 and temp>=28:
      label=5
    else:
      label=0

    print(temp,hum,label)

client.on_message=notification
client.loop_forever()
