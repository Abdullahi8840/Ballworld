from microbit import *
from machine import *
import neopixel

trig = pin1
echo = pin2

left_IR = pin13
right_IR = pin14

left_LED = pin8
right_LED = pin12

class Maqueen:

	def __init__(self):
		self.rgbleds = neopixel.NeoPixel(pin15, 4)
		print("MAQUEEN initialized")

	def set_led(self, sel_LED, sel_state):

		if sel_LED == 0:
			left_LED.write_digital(sel_state) # type: ignore
		elif sel_LED == 1:
			right_LED.write_digital(sel_state) # type: ignore

	def read_distance(self):

		trig.write_digital(1) # type: ignore
		trig.write_digital(0) # type: ignore
		# measuring the pin to turn 1 and converting it to seconds from ms
		pulse_recived = (time_pulse_us(echo, 1))/1000000  # type: ignore

		dist_cm = (pulse_recived/2)*34100
		return dist_cm

	def read_IR(self, IR):
		"""
		Reads IR sensor
		"""
		selected_IR = left_IR if IR == 0 else right_IR

		return selected_IR

	def set_motor(self, motor, speed):
		"""
		Controls motor
		motor: 0 - left motor, 1 - right motor
		speed: -255 to +255, the sign means direction
		"""
		data = bytearray(3)
		if motor == 0:  # left motor
			data[0] = 0
		else:
			data[0] = 2  # right motor is 2
		if speed < 0:  # ccw direction
			data[1] = 1
			speed = -1*speed
		data[2] = speed
		i2c.write(0x10, data, False)  # 0x10 is i2c address of motor driver

	def motor_stop_all(self):
		self.set_motor(0, 0)
		self.set_motor(1, 0)