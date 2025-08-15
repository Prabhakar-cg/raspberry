import RPi.GPIO as GPIO
import time
from gpiozero import LightSensor



# Define GPIO to use
LDR_PIN = 21
RELAY_PIN = 15

#ldr = LightSensor(21)  # alter if using a different pin
while True:
    print("Initial ldr", ldr.value)
    ldr_value = ldr

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

def rc_time(ldr_pin):
    count = 0

    # Output on the pin for 
    GPIO.setup(ldr_pin, GPIO.OUT)
    GPIO.output(ldr_pin, GPIO.LOW)
    time.sleep(0.1)

    # Change the pin back to input
    GPIO.setup(ldr_pin, GPIO.IN)

    # Count until the pin goes high
    while (GPIO.input(ldr_pin) == GPIO.LOW):
        count += 1

    return count

try:
    while True:
        ldr_value = LightSensor(21)
        print("LDR Value: ", ldr_value)
        if ldr_value > 1000:  # Adjust threshold as needed
            GPIO.output(RELAY_PIN, GPIO.HIGH)  # Turn on relay
        else:
            GPIO.output(RELAY_PIN, GPIO.LOW)  # Turn off relay
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()