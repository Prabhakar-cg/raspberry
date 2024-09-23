from gpiozero import Servo
from time import sleep

servo = Servo(25)

try:
	while True:
		servo.value = -1
		sleep(0.5)
		print("Moving to max")
		servo.value = 1
		sleep(0.5)
		print("Moving to min")
except KeyboardInterrupt:
	print("Program stopped")
	