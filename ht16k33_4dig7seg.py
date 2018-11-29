#!/usr/bin/env python3

import smbus

import time
from datetime import datetime

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

DEVICE_BUS = 1
DEVICE_ADDR = 0x70
bus = smbus.SMBus(DEVICE_BUS)
bus.write_byte(DEVICE_ADDR,0x21)
bus.write_byte(DEVICE_ADDR,0x81)
bus.write_byte(DEVICE_ADDR,0xE0)
coron = 0
count = 1 
flag = True
while True:
	try:
		count += 1
		if count == 2:
			ms = datetime.now().strftime("%M%S")
			d1 = int(ms[0])
			d2 = int(ms[1])
			d3 = int(ms[2])
			d4 = int(ms[3])
			count = 0
		if flag:
			coron = 2
			flag = False
		else:
			coron = 0
			flag = True
		data = [D[d1],0,D[d2],0,coron,0,D[d3],0,D[d4]]
		bus.write_i2c_block_data(DEVICE_ADDR,0x00,data)
		time.sleep(0.5)

	except KeyboardInterrupt:
		break

