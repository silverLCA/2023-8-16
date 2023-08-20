import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)   ##define PINS Mode 


GPIO_read   = 27
GPIO.setup(GPIO_read,GPIO.IN)

# MQTT broker details
broker = "localhost"
port = 1883
username = "pi"
password = "12345678s"

# Create a MQTT client
client = mqtt.Client()

# Connect to the broker
client.username_pw_set(username, password)
client.connect(broker, port)

# Publish a message
if(GPIO.input(27)==False):
        # Create a MQTT client
        GPIO27last=GPIO.input(27)
        print (GPIO27last)
        client = mqtt.Client()

        # Connect to the broker
        client.username_pw_set(username, password)
        client.connect(broker, port)

        # Publish a message
        topic = "LED"
        message = "LED ON"
        client.publish(topic, message)

        # Disconnect from the broker
        client.disconnect()