# import packages
import utime as time
from machine import ADC, Pin
import display

csv = "stuff.csv"
# Get packages for display and other shit
clock = 0
soil = ADC(Pin(26))
min_moisture=19200
max_moisture=49300

def moistrec():
    moisture = (max_moisture-soil.read_u16())*100/(max_moisture-min_moisture) 
    print("moisture: " + "%.2f" % moisture +"% (adc: "+str(soil.read_u16())+")")
    return moistrec
def temprec():
    print("GET 4.7K OHM CAPACITOR!")
    

def recieve():
    # Get temperature and moisture measurements
    t = 0
    m = moistrec()
    return t, m

btn = 0
def getbutton():
    global btn
    if Pin(15, Pin.IN, Pin.PULL_UP).value() != 1:
        btn = 0
    elif Pin(17, Pin.IN, Pin.PULL_UP).value() != 1:
        btn = 1
    elif Pin(2, Pin.IN, Pin.PULL_UP).value() != 1:
        btn = 2
    elif Pin(3, Pin.IN, Pin.PULL_UP).value() != 1:
        btn = 3
    return btn


# Loop for while buttons are unpressed. top left is current, top right is graph
# bottom left is for idle mode


# I LOVE MULTICORE MICROCONTROLLERS!!!!!!!! I WILL RUN THE FRONTEND DISPLAY STUFF ON ONE CORE AND SAVE INFO ON ANOTHER


def current():
    while getbutton() == 0:
        print("current")
        #show the current info
        # temp, moist = recieve()
        # code = advice(temp, moist)
        # refresh(temp, moist, code)
        time.sleep(5)
def graph():
    while getbutton() == 1:
        # show the graph
        # make the graph
        print("graph")
        time.sleep(5)
def idle():
    while getbutton() == 3 or 4:
        print("IDLE")
        #this should really just be turning off the screen and running background data saving
        time.sleep(5)



def datasize():
    with open(csv) as f:
        line_count = 0
        for line in f:
            line_count += 1
    return line_count

def bgsave():
    while True:
        #save every 3 hours
        time.sleep(10800)
        temp, moist = recieve()
        #-- all saved data is being padded to ensure simple replacement of entries. I.E, oldest data (Say, 12 digits) deleted from end and newest data suffended--
        # JUST KIDDING IM WIPING LINES
        with open(csv, "r") as infile:
            lines = infile.readlines()
        # check csv size to save storage
        # stores for 10 days. if more than 10 days of info are saved, oldest info is wiped.
        if datasize() > 90:
            with open(csv, "w") as outfile:
                for pos, line in enumerate(lines):
                    print("killing oldest data")
                    if pos != 0:
                        outfile.write(line)
        # append new information to csv           
        with open(csv, "a") as addfile:
            addfile.write(f"\n{moist},{temp}")
            print(f"writing {moist},{temp} to csv")
            
# MAKE MAIN LOOP