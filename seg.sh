echo y\n | i2cdump -r 0x00-0x0F 1 0x70 c
echo y\n | i2cdump -r 0x40-0x45 1 0x70 c
i2cset -y 1 0x70 0 0x06 0 0x6d 0 0 0 0x4f 0 0x5b i
