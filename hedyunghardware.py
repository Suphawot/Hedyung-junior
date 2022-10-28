#นำเข้าไลบารี
import machine
from machine import Pin
from time import sleep

#กำหนดตัวแปร
sensor = Pin(17, Pin.OUT) #ตัวแปรสำหรับเซนเซอร์
sprinkler = Pin(34, Pin.OUT) #ตัวแปรสำหรับสปริงเกอร์
ventilateur=Pin(27, Pin.OUT) #ตัวแปรสำหรับพัดลม

#ลูปอนันต์
while True: #เปิดใช้งานลูปเป็นอนันต์
    #กำหนดการทำงานของอุณหภูมิและความชื้น
    try:
        sleep(0.3) #กำหนดให้ตรวจเช็คทุกๆ 0.3 วินาที
        sensor.measure() #เปิดใช้งานเซนเซอร์
        temp = sensor.temperature() #กำหนดตัวแปร temp = 'อุณหภูมิที่ตรวจจับได้'
        hum = sensor.humidity() #กำหนดตัวแปร hum = 'ความชื้นที่ตรวจจับได้'
        print('Temperature: %3.1f C' %temp) #ให้แสดงผลออกมาเป็น "Temperature: อุณหภูมิที่ตรวจจับได้"
        print('Humidity: %3.1f %%' %hum) #ให้แสดงผลออกมาเป็น "Humidity: อุณหภูมิที่ตรวจจับได้"
        
        #เงื่อนไข
        if temp >32: #เช็คอุณหภูมิหากมากกว่า 32 องศาจะให้เปิดใช้งานเงื่อนไข
            if hum > 80: #เช็คความชื้นหากมากกว่า 80 จะเปิดใช้งานเงื่อนไขต่อไปนี้
                ventilateur.value(0) #ปิดใช้งานพัดลม
                sprinkler(1) #เปิดใช้งานสปริงเกอร์

        else: #หากไม่ตรงตามเงื่อนไข
            ventilateur.value(1) #เปิดใช้งานพัดลม
            sprinkler(0) #ปิดใช้งานสปริงเกอร์
