import RPi.GPIO as GPIO
from gpiozero import LED
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
led = LED(15)
while True:
   light = (GPIO.input(21))
   if light == 0:
      led.on()
   else:
      led.off()