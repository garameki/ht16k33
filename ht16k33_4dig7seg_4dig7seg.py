#!/usr/bin/env python3

#https://www.javadrive.jp/python/string/index9.html
#数値を文字列に変換(str)




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
DEVICE_ADDR0 = 0x70
DEVICE_ADDR1 = 0x71
bus = smbus.SMBus(DEVICE_BUS)
bus.write_byte(DEVICE_ADDR0,0x21)
bus.write_byte(DEVICE_ADDR0,0x81)
bus.write_byte(DEVICE_ADDR0,0xE0)
bus.write_byte(DEVICE_ADDR1,0x21)
bus.write_byte(DEVICE_ADDR1,0x81)
bus.write_byte(DEVICE_ADDR1,0xE0)
coron = 0
count = 1 
flag = True
while True:
	try:
		count += 1
		if count == 2:
			m = datetime.now().strftime("%M")
			s = datetime.now().strftime("%S")
			d01 = int(m[0])
			d02 = int(m[1])
			d03 = int(s[0])
			d04 = int(s[1])
			a = "0000"+str(int(m) * int(s))
			d11 = int(a[-4])
			d12 = int(a[-3])
			d13 = int(a[-2])
			d14 = int(a[-1])

			count = 0
		if flag:
			coron = 2
			flag = False
		else:
			coron = 0
			flag = True
		data0 = [D[d01],0,D[d02],0,coron,0,D[d03],0,D[d04]]
		data1 = [D[d11],0,D[d12],0,0,0,D[d13],0,D[d14]]
		bus.write_i2c_block_data(DEVICE_ADDR0,0x00,data0)
		bus.write_i2c_block_data(DEVICE_ADDR1,0x00,data1)

		time.sleep(0.5)

	except KeyboardInterrupt:
		break

