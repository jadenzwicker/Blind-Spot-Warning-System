
#!/usr/bin/env python
"""
	Detects motion and outputs a sound via a piezo buzzer. 
"""

import RPi.GPIO as GPIO
import time

pir_sensor = 8   #PIN 8
piezo = 7	  #PIN 7
haptic_driver = 13  #PIN 13

GPIO.setmode(GPIO.BOARD)

GPIO.setup(piezo, GPIO.OUT)

GPIO.setup(pir_sensor, GPIO.IN)

GPIO.setup(haptic_driver, GPIO.OUT)

current_state = 0
try:
    while True:
        time.sleep(0.1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            print("MOTION DETECTED")
            GPIO.output(piezo,True)
            GPIO.output(haptic_driver,True)
            time.sleep(.2)
            GPIO.output(piezo,False)
            GPIO.output(haptic_driver,False)
except KeyboardInterrupt:
    pass
finally:
    GPIO.output(piezo,False)
    GPIO.output(haptic_driver,False)
    GPIO.cleanup()
