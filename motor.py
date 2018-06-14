import pigpio
import sys
import time

pi = pigpio.pi()
while True:
  pi.set_servo_pulsewidth(7,550)
  time.sleep(1)
  pi.set_servo_pulsewidth(7,2000)
  time.sleep(1)
