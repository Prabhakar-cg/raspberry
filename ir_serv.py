from gpiozero import Servo,DigitalInputDevice
from time import sleep

servo = Servo(25)
IR_PIN = 17

ir_sensor = DigitalInputDevice(IR_PIN)

try:
    while True:
        if ir_sensor.is_active:
            servo.value = -1
            sleep(0.5)
            print(" Object Detected!")
            print("Moving to max")
        else:
            servo.value = 1
            print("No Object Detected.")
            sleep(0.5)
            print("Moving to min")
            sleep(0.5)  # Adjust the delay as needed

except KeyboardInterrupt:
    print("Program stopped by User")
	