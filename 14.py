def koko():
    try:
        # print(5/0)
        r = open('file_not_exist.txt')
    except ZeroDivisionError as e:
        print(e.args)
    except FileNotFoundError as e:
        print(e.args)
koko()