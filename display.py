# WS 320x240 display example
from machine import Pin,SPI,PWM
import framebuf
import time
import os

BL = 13
DC = 8
RST = 12
MOSI = 11
SCK = 10
CS = 9
csv = "data.csv"

class LCD_1inch3(framebuf.FrameBuffer): # For 320x240 display
    def __init__(self):
        self.width = 320
        self.height = 240
        
        self.cs = Pin(CS,Pin.OUT)
        self.rst = Pin(RST,Pin.OUT)
        
        self.cs(1)
        self.spi = SPI(1)
        self.spi = SPI(1,1000_000)
        self.spi = SPI(1,100000_000,polarity=0, phase=0,sck=Pin(SCK),mosi=Pin(MOSI),miso=None)
        self.dc = Pin(DC,Pin.OUT)
        self.dc(1)
        self.buffer = bytearray(self.height * self.width * 2)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        self.init_display()
        
        self.RED   =   0x07E0
        self.GREEN =   0x001f
        self.BLUE  =   0xf800
        self.WHITE =   0xffff
        self.BLACK =   0x0000
        self.PURPLE  =   0xdddd
        self.GRYISH = 0x5555
        
    def write_cmd(self, cmd):
        self.cs(1)
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def write_data(self, buf):
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(bytearray([buf]))
        self.cs(1)

    def init_display(self):
        """Initialize display"""  
        self.rst(1)
        self.rst(0)
        self.rst(1)
        
        self.write_cmd(0x36)
        self.write_data(0x70)

        self.write_cmd(0x3A) 
        self.write_data(0x05)

        self.write_cmd(0xB2)
        self.write_data(0x0C)
        self.write_data(0x0C)
        self.write_data(0x00)
        self.write_data(0x33)
        self.write_data(0x33)

        self.write_cmd(0xB7)
        self.write_data(0x35) 

        self.write_cmd(0xBB)
        self.write_data(0x19)

        self.write_cmd(0xC0)
        self.write_data(0x2C)

        self.write_cmd(0xC2)
        self.write_data(0x01)

        self.write_cmd(0xC3)
        self.write_data(0x12)   

        self.write_cmd(0xC4)
        self.write_data(0x20)

        self.write_cmd(0xC6)
        self.write_data(0x0F) 

        self.write_cmd(0xD0)
        self.write_data(0xA4)
        self.write_data(0xA1)

        self.write_cmd(0xE0)
        self.write_data(0xD0)
        self.write_data(0x04)
        self.write_data(0x0D)
        self.write_data(0x11)
        self.write_data(0x13)
        self.write_data(0x2B)
        self.write_data(0x3F)
        self.write_data(0x54)
        self.write_data(0x4C)
        self.write_data(0x18)
        self.write_data(0x0D)
        self.write_data(0x0B)
        self.write_data(0x1F)
        self.write_data(0x23)

        self.write_cmd(0xE1)
        self.write_data(0xD0)
        self.write_data(0x04)
        self.write_data(0x0C)
        self.write_data(0x11)
        self.write_data(0x13)
        self.write_data(0x2C)
        self.write_data(0x3F)
        self.write_data(0x44)
        self.write_data(0x51)
        self.write_data(0x2F)
        self.write_data(0x1F)
        self.write_data(0x1F)
        self.write_data(0x20)
        self.write_data(0x23)
        
        self.write_cmd(0x21)

        self.write_cmd(0x11)

        self.write_cmd(0x29)

    def show(self):
        self.write_cmd(0x2A)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x01)
        self.write_data(0x3f)
        
        self.write_cmd(0x2B)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0xEF)
        
        self.write_cmd(0x2C)
        
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(self.buffer)
        self.cs(1)
        
def refresh(temp, moist):
    # format for lcd
    print(f"Temperature is {temp}\nMoisture is {moist}.\n")
    if 105<temp<160 and 45<moist<60:
        #good
        return(f"Your compost heap has good temperature"),("and moisture.")
    elif 105<temp<160 and moist < 45:
        #dry
        return(f"Your compost is dry. Add some water."),("")
    elif 105<temp<160 and moist > 60:
        #wet
        return(f"Your compost is too wet. Try turning it"),("and/or adding dry material.")
    elif temp > 160 and 45 < moist < 60:
        #hot
        return(f"Your compost is too hot."),("Turn it over soon.")
    elif temp < 105 and 45 < moist < 60:
        #cold
        return(f"Your compost is too cold. Don't turn it"),("until it warms up.")
    elif temp < 105 and moist < 45:
        # cold and dry
        return(f"Your compost is cold and dry. Add some"),("water and more organics.")
    elif temp < 105 and moist > 60:
        # cold and wet
        return(f"Your compost is cold and wet. Try adding"),("more dry material and let it sit.")
    elif temp > 160 and moist < 45:
        # hot and dry
        return(f"Your compost is hot and dry. Add water"),("and turn it.")
    elif temp > 160 and moist > 60:
        # hot and wet
        return(f"Your compost is hot and wet. Turn it"),("and consider adding dry material.")

def current(temp, moist):
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(32768)#max 65535

    LCD = LCD_1inch3()
    #color BRG
    LCD.fill(LCD.WHITE)
    LCD.show()
    while True:
        adv1, adv2 = refresh(temp, moist)
        time.sleep(0.1)
        LCD.fill_rect(0,0,160,24,LCD.GRYISH)
        LCD.rect(0,0,160,24,LCD.GRYISH)
        LCD.text("Temperature",2,8,LCD.WHITE)
        
        LCD.fill_rect(160,0,320,24,LCD.PURPLE)
        LCD.rect(160,0,320,24,LCD.PURPLE)
        LCD.text(f"{temp} F",162,8,LCD.WHITE)
        
        LCD.show()
        time.sleep(1)
        LCD.fill_rect(0,24,160,26,LCD.GREEN)
        LCD.rect(0,24,160,26,LCD.GREEN)
        LCD.text("Moisture",2,30,LCD.WHITE)
        
        LCD.fill_rect(160,24,320,26,LCD.BLUE)
        LCD.rect(160,24,320,26,LCD.BLUE)
        LCD.text(f"{moist} %",162,30,LCD.WHITE)
        LCD.show()
        time.sleep(1)
        LCD.show()
        

        LCD.text(f"{adv1}",2,54,LCD.BLACK)
        LCD.text(f"{adv2}",2,64,LCD.BLACK)
        LCD.show()
        time.sleep(0.1)
        LCD.show()

def graph():
    #initialize display
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(32768)#max 65535
    
    LCD = LCD_1inch3()
    #color BRG
    LCD.fill(LCD.BLACK)
    LCD.show()

    # draw graph frame
    LCD.line(20,8,20,220, LCD.WHITE)
    LCD.line(20,220,300,220, LCD.WHITE)
    LCD.text("215 f, 75% m", 0,0,LCD.WHITE)
    LCD.text("50 f, 30% m", 10,230,LCD.WHITE)
    #pull data from csv
    # graph moisture from 30-75
    # graph temp from 50 - 215
    # graph height is 212
    # graph width is 270, each value is 3 pixels wide
    # 5 pixel buffer zone on X axis of graph.
    # each degree of temp is 1.284848 pixels. Just round both?
    # each percent of moisture is 4.7111 pixels
    
    time.sleep(1)
    with open(csv) as f:
        for line in f:
            print(line.split(","))
            time.sleep(5)
            
        
    # LCD.line(160,120,LCD.WHITE)
    # LCD.show()
    print("pixel changed")
    
graph()

