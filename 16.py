def get_age():
    age = int(input('enter age :'))
    if age < 0 :
        raise ValueError("age cant be negative")


try:
    get_age()
    except ValueError as e:
    print(e.args)
