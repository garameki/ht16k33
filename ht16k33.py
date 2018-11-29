#!/usr/bin/env python3
_*_ coding:utf-8 _*_

#https://www.javadrive.jp/python/string/index9.html
#数値を文字列に変換(str)


import smbus

import time
from datetime import datetime

class H16k33:
	D = [0] * 10
	D[0] = 0x3F
	D[1] = 0x06
	D[2] = 0x5B
	D[3] = 0x4F
	D[4] = 0x66
	D[5] = 0x6D
	D[6] = 0x7D
	D[7] = 0x27
	D[8] = 0x7F
	D[9] = 0x6F

	bus = None
	addr = None
	def __init__(self,dev_bus,dev_addr):
		#(hex) dev_bus
		#(hex) dev_addr
		bus = smbus.SMBus(dev_bus)
		addr = dev_addr
		bus.write_byte(addr,0x21)
		bus.write_byte(addr,0x81)
		bus.write_byte(addr,0xE0)

		#light strength
	def strength(self,value):
		#(hex) value : 0x0～0xF
		value = int(value)
		if value > 0xF:
			value = 0xF
		elif value < 0x0:
			value = 0x0
		value = value + 0xE0;
		bus.write_byte(addr,value)

	def print(self,sValue="0000",fColon=False):
		#(String) sValue
		#(boolean) fColon : 0:disappear  1:appear
		d4 = int(sValue[-1])
		d3 =  int(sValue[-2])
		d2 =  int(sValue[-3])
		d1 =  int(sValue[-4])
		if fColon == True:
			coron = 0xf
		else:
			coron = 0x0
		data = [D[d1],0,D[d2],0,coron,0,D[d3],0,D[d4]]
		bus.write_i2c_block_data(addr,0x00,data)

	def close(self):
		print("you don't have to close smbus")

if __name__ == "__main__":

	DEVICE_BUS = 1
	DEVICE_ADDR0 = 0x70
	DEVICE_ADDR1 = 0x71

	h1 = H16k33(DEVICE_BUS,DEVICE_ADDR0)
	h2 = H16k33(DEVICE_BUS,DEVICE_ADDR1)

	coron = 0
	count = 1 
	flag = True
	while True:
		try:
			count += 1
			if count == 2:
				ms = datetime.now().strftime("%M%S")
				mult = "0000"+str(int(m) * int(s))

				count = 0
			if flag:
				flag = False
				coron = !flag
			else:
				flag = True
				coron = !flag
			h1.print(ms,coron)
			h2.print(mult,coron)

			time.sleep(0.5)

		except KeyboardInterrupt:
			break

