from machine import Pin
import dht
from time import sleep

r = Pin(12, Pin.OUT) #ปั้มน้ำ
r2 = Pin(14, Pin.OUT) #พัดลม
#r3 = Pin(26, Pin.OUT) #ไฟกล้อง
s = dht.DHT22(Pin(27)) #sensor
while True:
    r2.value(0)
    try:
        s.measure()
        temp = s.temperature()
        hum = s.humidity()
        print('temperature: ', temp)
        print('humidity: ', hum)
        sleep(2)
        
    except OSError as e:
        print("Faild to read sensor")
