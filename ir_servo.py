#! /usr/bin/env python

from gpiozero import Servo, DistanceSensor
from time import sleep
import RPi.GPIO as GPIO

# Define GPIO pins
IR_PIN = 17  # GPIO pin for IR sensor
SERVO_PIN = 25  # GPIO pin for servo motor

# Create objects for the IR sensor and servo
ir_sensor = DistanceSensor(echo=IR_PIN, trigger=IR_PIN)
servo = Servo(SERVO_PIN)

# Define threshold distance (in meters) for IR sensor
THRESHOLD = 0.3  # Adjust this value based on your needs

def move_servo(angle):
    """Move the servo to the specified angle."""
    servo.value = angle

try:
    print("IR Sensor and Servo are active. Press CTRL+C to exit.")
    while True:
        distance = ir_sensor.distance
        print(f"Distance: {distance:.2f} m")
        
        if distance < THRESHOLD:
            print("Object detected! Moving servo...")
            move_servo(0.5)  # Move servo to 90 degrees (middle position)
        else:
            print("No object detected. Resetting servo...")
            move_servo(-1)  # Move servo to 0 degrees (initial position)
        
        sleep(1)  # Wait for 1 second before next reading

except KeyboardInterrupt:
    print("Program stopped by User")
finally:
    # Clean up
    servo.close()
    ir_sensor.close()
