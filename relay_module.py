import RPi.GPIO as GPIO

import time

Relay_Ch1 = 14

Relay_Ch2 = 15

Relay_Ch3 = 18

Relay_Ch4 = 23

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay_Ch1,GPIO.OUT)
GPIO.setup(Relay_Ch2,GPIO.OUT)
GPIO.setup(Relay_Ch3,GPIO.OUT)
GPIO.setup(Relay_Ch4,GPIO.OUT)


print("Setup The Relay Module is [success]")

try:
    while True:

#Control the Channel 1

      GPIO.output(Relay_Ch1,GPIO.LOW)

      print("Channel 1:The Common Contact is access to the Normal Open Contact!")

      time.sleep(1)

      GPIO.output(Relay_Ch1,GPIO.HIGH)

      print("Channel 1:The Common Contact is access to the Normal Closed Contact!\n")

      time.sleep(1)

#Control the Channel 2

      GPIO.output(Relay_Ch2,GPIO.LOW)

      print("Channel 2:The Common Contact is access to the Normal Open Contact!")

      time.sleep(1)

      GPIO.output(Relay_Ch2,GPIO.HIGH)

      print("Channel 2:The Common Contact is access to the Normal Closed Contact!\n")

      time.sleep(1)

#Control the Channel 3

      GPIO.output(Relay_Ch3,GPIO.LOW)

      print("Channel 3:The Common Contact is access to the Normal Open Contact!")

      time.sleep(1)

      GPIO.output(Relay_Ch3,GPIO.HIGH)

      print("Channel 3:The Common Contact is access to the Normal Closed Contact!\n")

      time.sleep(1)

#Control the Channel 4

      GPIO.output(Relay_Ch4,GPIO.LOW)

      print("Channel 4:The Common Contact is access to the Normal Open Contact!")

      time.sleep(1)

      GPIO.output(Relay_Ch4,GPIO.HIGH)

      print("Channel 4:The Common Contact is access to the Normal Closed Contact!\n")

      time.sleep(1)

except:

      print("except")

GPIO.cleanup()