
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
    if code == 0:
        #good
    if code == 1:
        #dry
    if code == 2:
        #wet
    if code == 3:
        #hot
    if code == 4:
        #cold
    if code == 5:
        # cold and dry
    if code == 6:
        # cold and wet
    if code == 7:
        # hot and dry
    if code == 8:
        # hot and wet
    