from machine import Pin, PWM, ADC
from ssd1306 import SSD1306_I2C
import time


pot = ADC(0)
led = PWM(Pin(2))

sda = machine.Pin(4)
scl = machine.Pin(5)
i2c = machine.I2C(sda=sda, scl=scl, freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.text('ESP 8266 LEVEL',0, 0)
oled.show()
time.sleep(1)

while True:
    level_value = int((pot.read_u16())/500)
    led.duty(pot.read())
    
    oled.fill_rect(1, 20, level_value, 20, 1)#20=ขนาดความกว้างแถบบาร์
    oled.show()
    oled.fill_rect(1, 20, level_value, 20, 0)
    time.sleep(0.1)
    
    
    
    
    
    