from machine import Pin, SoftI2C
import dht
from time import sleep
import ssd1306

r1 = Pin(14, Pin.OUT) #ปั้มน้ำ
r2 = Pin(27, Pin.OUT) #พัดลม
#r3 = Pin(26, Pin.OUT) #ไฟกล้อง
s = dht.DHT22(Pin(25)) #sensor
i2c = SoftI2C(scl=Pin(22),sda=Pin(21)) #Set Oled แสดงผล

oled_width =128 #ขนาดจอ
oled_hight =64 #ขนาดจอ
oled = ssd1306.SSD1306_I2C(oled_width, oled_hight, i2c)
def call_dht():
    s.measure()
    global temp
    global hum
    temp = s.temperature()
    hum = s.humidity()
    print('temperature', temp)
    print('humidity: ', hum)
    sleep(5)
def show_oled():
    oled.text('Temp: ', 0, 5,)
    oled.text(str(temp), 50, 5)
    oled.text('C', 85, 5)
    oled.text('Hum: ', 0, 25)
    oled.text(str(hum), 50, 25)
    oled.text('%', 85, 25)
#     oled.fill(0)
    oled.show()
    sleep(2)
while True:
    call_dht()
    show_oled()
    try:
        if hum > 85 :
            r1.value(0)
            r2.value(1)
            sleep(10)
        else:
            if hum < 70 :
                r1.value(1)
                r2.value(0)
                sleep(10)
            elif temp > 32:
                r1.value(0)
                r2.value(1)
                sleep(10)
            elif temp < 25:
                r1.value(1)
                r2.value(0)
                sleep(10)
                
        
    except OSError as e:
        print("Faild to read sensor")
    
