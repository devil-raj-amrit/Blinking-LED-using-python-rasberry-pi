# import raspberry pi GPIO module
import RPi.GPIO as GPIO

#import time module for delay
import time

#give all the board pins in list to iterate one by one
pins = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 35, 36, 37, 38, 40]   

#setting each board pins as output pin
for pin in pins:
  
  GPIO.setup(pin, GPIO.OUT)

#checking each pin for even or odd
for i in pins:
  
  if i%2==0:
    
#blinking twice for even pin
    for x in range(2):
      GPIO.output(i, GPIO.HIGH)
      time.sleep(1.0)
      GPIO.output(i, GPIO.LOW)
      time.sleep(1.0)
      
#blinking remaining pin ones as the remaining pins are odd
  else:
    GPIO.output(i, GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(i, GPIO.LOW)
    time.sleep(1.0)
