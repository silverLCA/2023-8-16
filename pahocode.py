import paho.mqtt.client as mqtt
import random
import time


MQTT_ADDRESS = "localhost"
MQTT_USER = "pi"
MQTT_PASSWORD = '12345678s'
MQTT_TOPIC_TEMP = 'Temperature'
MQTT_TOPIC_HUMD = 'Humidity'
MQTT_TOPIC_LED = 'LED'

topic = "Temperature"



def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))
    client.subscribe(MQTT_TOPIC_TEMP)
    client.subscribe(MQTT_TOPIC_HUMD)
    client.subscribe(MQTT_TOPIC_LED)


def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))
    x= msg.payload
    y=float(x)
    if (y >= 25):
        print ("hello")
   



 

def main():
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_ADDRESS, 1883)
    mqtt_client.loop_forever()
    

 

if __name__ == '__main__':
    print('MQTT to InfluxDB bridge')
    main()