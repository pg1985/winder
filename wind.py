import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)

ControlPins = [7,11,13,15]

for pin in ControlPins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin,0)

seq = [[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]

count = 0

count = int(sys.argv[0])

if not count:
	print "Please supply a number of winds"
	return

def wind(count):
	for j in count:
		for i in range(512):
			for halfstep in range(8):
				for pin in range(4):
					GPIO.output(ControlPins[pin], seq[halfstep][pin])
					

	GPIO.cleanup()