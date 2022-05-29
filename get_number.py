def get_number():
    a= input("enter decimal")
    if a.isdecimal():
        return int(a)
    return -1
