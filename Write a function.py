def is_leap(year):
    leap = False    
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    elif year % 4 != 0:
        return False
    return leap

