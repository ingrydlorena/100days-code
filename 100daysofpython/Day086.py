import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the pin where the LED is connected
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        # Turn the LED on
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)  # Wait for 1 second
        # Turn the LED off
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)  # Wait for 1 second
except KeyboardInterrupt:
    pass  # Exit the program gracefully when Ctrl+C is pressed
finally:
    GPIO.cleanup()  # Reset all GPIO settings

# i don't have material to do this task, so the AI returned what do you have to do