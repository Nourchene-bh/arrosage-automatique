import RPi.GPIO as GPIO
import datetime
import time


GPIO.setmode(GPIO.BOARD) 

def get_last_watered():
    try:
        f = open("last_watered.txt", "r")
        return f.readline()
    except:
        return "NEVER!"
      
def get_status(pin = 8):
    GPIO.setup(pin, GPIO.IN) 
    return GPIO.input(pin)

def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)
    
def auto_water(delay = 5, pump_pin = 7, humi_pin = 8):
    wc = 0
    init_output(pump_pin)
   
    try:
        while  wc < 10:
            time.sleep(delay)
            wet = get_status(pin = humi_pin) == 0
            if not wet:
                if wc < 5:
                    pump_on(pump_pin, 1)
                wc += 1
            else:
                wc = 0
    except KeyboardInterrupt: 
        GPIO.cleanup() 

def pump_on(pump_pin = 7, delay = 1):
    init_output(pump_pin)
    f = open("last_watered.txt", "w")
    f.write("Last watered {}".format(datetime.datetime.now()))
    f.close()
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pump_pin, GPIO.HIGH)
