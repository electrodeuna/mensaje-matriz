"""
Código creado por Electro de Una
Youtube: Electronica de Una
2021
"""

import max7219
from machine import Pin, SPI, UART
from time import sleep
spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)

length = 0
msg = ''
display = max7219.Matrix8x8(spi, ss, 1)
display.brightness(5)   # ajustar brillo 1 a 15
display.fill(1)
display.show()
sleep(0.5)
display.fill(0)
display.show()
sleep(0.2)

uart = UART(0, 9600)

while True:
    
    if uart.any():
        msg = uart.readline()
        print(msg)
        length = len(msg)
        length = (length*8)
        
    for x in range(32, -length, -1):
        display.text(msg ,x,0,1)
        display.show()
        sleep(0.10)
        display.fill(0)