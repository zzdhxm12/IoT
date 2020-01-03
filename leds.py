from flask import Flask, render_template, request

import RPi.GPIO as GPIO

 

app= Flask(__name__)

 

GPIO.setmode(GPIO.BCM)

 

leds = {

            24 : {'name' : 'Security Mode','state' : GPIO.LOW}

            }

 

for led in leds :

         GPIO.setup(led, GPIO.OUT)

         GPIO.output(led, GPIO.LOW)

 

def getGpioState() :

        for led in leds :

                    leds[led]['state'] = GPIO.input(led)

 

        return leds

 

@app.route("/")

def main():

 

        ledState = getGpioState()

 

        gpioState = {

                    'leds' :  ledState

        }

 

        return render_template('gpio.html', **gpioState)

 

@app.route("/<led>/<act>")

def action(led, act):

    led= int(led)

    leds= getGpioState()

    dev = leds[led]['name']

 

    if act == "on" :

                GPIO.output(led, GPIO.HIGH)

                msg = "Turned"+ dev + "on."

 

    elif act == "off":

                GPIO.output(led, GPIO.LOW)

                msg = "Turned"+ dev + "off."

    elif act == "toggle":

                GPIO.output(led, not GPIO.input(led))

                msg = "Toggled"+ dev + "."

 

    else:

                msg = "Undefined action!"

 

 

    leds = getGpioState()

 

    gpioState = {

        'msg' : msg,

        'leds' : leds

    }

 

    return render_template('gpio.html', **gpioState)

 

if __name__ == "__main__" :

            app.run(host='0.0.0.0', port=8888 , debug=True)
