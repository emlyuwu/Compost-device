import packages
import utime as time
# Get packages for display and other shit
clock = 0
def recieve():
    # Get temperature and moisture measurements
    t = 0
    m = 0
    return t, m
def advice(temp, moist):
    # Keep tempurature between 105 and 160 F. Turn if too hot, leave if too cold.
    # Moisture should be between 45-60%. Turn or add dry material if too wet, water lightly if too dry.
    # Compost should be regularly turned a little less than twice a week.
    # Result should be returned as a code. Too wet = 1, too dry = 2, etc.
    if temp > 160 and moist > 60:
        # Hot and moist
        code = 8
        return code
    elif temp > 160 and moist < 45:
        # Hot and dry
        code = 7
        return code
    elif temp < 105 and moist > 60:
        # Cold and wet
        code = 6
        return code
    elif temp < 105 and moist < 45:
        # Cold and dry
        code = 5
        return code
    elif temp < 105 and 45 < moist < 60:
        # Cold
        code = 4
        return code
    elif temp > 160 and 45 < moist < 60:
        # Hot
        code = 3
        return code
    elif 105<temp<160 and moist > 60:
        # Wet
        code = 2
        return code
    elif 105<temp<160 and moist < 45:
        # Dry
        code = 1
        return code
    elif 105<temp<160 and 45<moist<60:
        # Good
        code = 0
        return code
    
    
def refresh(temp, moist, code):
    # format for lcd
    print(f"Temperature is {temp}\nMoisture is {moist}.\n")
    if code == 0:
        #good
        print("Your compost heap has good temperature and moisture.")
    elif code == 1:
        #dry
        print("Your compost is dry. Add some water.")
    elif code == 2:
        #wet
        print("Your compost is too wet. Try turning it and/or adding dry material.")
    elif code == 3:
        #hot
        print("Your compost is too hot. Turn it over soon.")
    elif code == 4:
        #cold
        print("Your compost is too cold. Don't turn it until it stabilizes.")
    elif code == 5:
        # cold and dry
        print("Your compost is cold and dry. Add some water and more organics.")
    elif code == 6:
        # cold and wet
        print("Your compost is cold and wet. Try adding more dry material and let it sit.")
    elif code == 7:
        # hot and dry
        print("Your compost is hot and dry. Add water and turn it.")
    elif code == 8:
        # hot and wet
        print("Your compost is hot and wet. Turn it more, and maybe add dry material.")

def getbutton():
    print("blah blah check which buttons pressed")

def write(moist, temp, clock):
    print("stuff")
    


# Loop for while buttons are unpressed. top left is current, top right is graph
# bottom left is for idle mode


# I LOVE MULTICORE MICROCONTROLLERS!!!!!!!! I WILL RUN THE FRONTEND DISPLAY STUFF ON ONE CORE AND SAVE INFO ON ANOTHER


def current():
    while getbutton() == 1:
        #show the current info
        temp, moist = recieve()
        code = advice(temp, moist)
        refresh(temp, moist, code)
        time.sleep(60)
def graph():
    while getbutton() == 2:
        # show the graph
        # make the graph
        print("graph")
        time.sleep(60)
def idle():
    while getbutton() == 3:
        temp, moist = recieve()

def bgsave():
    while True:
        time.sleep(3600)
        clock =+ 1
        temp, moist = recieve()
        write(moist, temp, clock)
