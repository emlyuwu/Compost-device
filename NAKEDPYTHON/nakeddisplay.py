# WS 320x240 display example
import time
import random
csv = "data.csv"
        
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
def datasize():
    with open(csv) as f:
        line_count = 0
        for line in f:
            line_count += 1
    return line_count

def fillshit():
    while True:
        #save every 3 hours
        time.sleep(0.1)
        temp = random.randint(0,100)
        moist = random.randint(0,100)
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

def current(temp, moist):

    #color BRG
    
    while True:
        adv1, adv2 = refresh(temp, moist)
        time.sleep(0.1)
        
        time.sleep(1)
        
        time.sleep(1)
        
        time.sleep(0.1)
        

def graph():
    #initialize display
    
    # draw graph frame
    
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
        prev = [0,0]
        print("doing things")
        for index, line in enumerate(f):
            a,b = (line.split(","))
            print(index, a,b)
            time.sleep(.3)
            x = (3*index)+28
            my = a
            ty = b
            #LCD.line(x-3,prev[0],x,my, LCD.GREEN)
            #LCD.line(x-3,pref[1],x,ty, LCD.ORANGE)
            prev = a,b
            
            
        
    # LCD.line(160,120,LCD.WHITE)
    # LCD.show()
    print("pixel changed")
    
graph()

