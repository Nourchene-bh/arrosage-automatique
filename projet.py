import RPi.GPIO as GPIO
import datetime
import time


GPIO.setmode(GPIO.BOARD) 

def dernier_arossage():
    try:
        f = open("Arrosage.txt", "r")
        return f.readline()
    except:
        return "jamais!"
      
def get_status(pin = 8):
    GPIO.setup(pin, GPIO.IN) 
    return GPIO.input(pin)

def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)
    
    
    
    
    def pompe_on(pompe_pin = 7, delay = 1):
    init_output(pompe_pin)
    f = open("Arrosage.txt", "w")
    f.write("Arrosage {}".format(datetime.datetime.now()))
    f.close()
    GPIO.output(pompe_pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pompe_pin, GPIO.HIGH)

    
def auto_water(delay = 5, pompe_pin = 7, humi_pin = 8):
    NA = 0
    init_output(pompe_pin)
   
    try:
        while  NA < 10:
            time.sleep(delay)
            mouiller = get_status(pin = humi_pin) == 0
            if not mouiller:
                if NA < 5:
                   pompe_on(pompe_pin, 1)
                NA += 1
            else:
                NA = 0
    except KeyboardInterrupt: 
        GPIO.cleanup() 


