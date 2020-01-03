from pyfcm import FCMNotification

import time

from grovepi import *

from grove_rgb_lcd import *

import RPi.GPIO as GPIO

 

pin=18

led=24

                               

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin,GPIO.OUT)

GPIO.setup(led,GPIO.IN)

p=GPIO.PWM(pin,50)

p.start(0)

cnt=0

push_service = FCMNotification(api_key="AAAAqPYubo0:APA91bGV1-EbpRxxa1KmLfVx-Cm0gbU7wxnRDhXn52DeUqxoG3iML4KMcfnl670n234HbCbEn3gnLTtnoD63VZbbl3ZXwIrOHw80Hfs6LSu5b_ptttnJmKUqhDmD2PXzMibyzU3bJ7oD")

GPIO.setup(led,GPIO.OUT)

 

buzzer_pin=6

ultrasonic_ranger=8

 

pinMode(buzzer_pin,"OUTPUT")

time.sleep(1)

 

while True:

    try:

        distant = ultrasonicRead(ultrasonic_ranger)

        inputled=GPIO.input(24)

        if inputled==True:

            

 

            p.ChangeDutyCycle(9)

            if distant > 4:

                digitalWrite(buzzer_pin,1)

                print(distant)

                registration_id = "eJNp6RtzX3E:APA91bGNn48DONuHecmg0J_UN7BVvP6ubuyKKg-PxiI7Ihb9377ZAWxDcMXPaqqfXQGhod8ZL3hhO-Im9f_RnsvokJktKArsvIpPta1Yhbf7QSraQvsi2Gt-U5LLIDbKjqrX078DjLZo"

                message_title = "Smart PostBox Service"

                message_body = "Smart PostBox open! Please Check Camera Streaming!"

                result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

            else:

                digitalWrite(buzzer_pin,0)

                print(distant)

 

        else:

            p.ChangeDutyCycle(5)

            digitalWrite(buzzer_pin,0)

            

    except KeyboardInterrupt:

        GPIO.output(led,GPIO.LOW)

        digitalWrite(buzzer_pin,0)

        

        break

    except IOError:

        print("Error")

        p.stop()

     

GPIO.cleanup()
