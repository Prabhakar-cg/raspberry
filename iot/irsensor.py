from gpiozero import DigitalInputDevice
from time import sleep

# Define the GPIO pin where the IR sensor is connected
IR_PIN = 17  # Change this to your GPIO pin

# Initialize the IR sensor
ir_sensor = DigitalInputDevice(IR_PIN)

try:
    while True:
        if ir_sensor.is_active:
            print("No Object Detected!")
        else:
            print("Object Detected.")
        sleep(1)  # Adjust the delay as needed

except KeyboardInterrupt:
    print("Program stopped by User")

