def is_name_exist(name_for_search, name_array_param):
    if name_for_search in name_array_param:
        print('exist')
    else:
        print('not exist')


def input_example():
    age = int(input('what is your name '))
    if 0 < age < 30:
        print('young')


def compare_array(first_array, second_array):
    if first_array == second_array:
        print('equal')
    if first_array is second_array:
        print('is')


def get_type_example(param):
    print(type(param))


def range_example(start, to, step):
    print(list(range(start, to, step)))


def loop_example():
    for i in range(5):
        print(i)
    for name in ['name1', 'name2']:
        print(f"hello {name}")
    arr = ['name1', 'name2']
    for i in range(len(arr)): {
        print(arr[i])
    }

    a = 0

    while a < 5:
        print(a)
        a = a + 1

    for i in range(5):
        print(i)
    else:
        print('loop ended without break')


def advanced_loop():
    n = [1, 2, 3, 4, 5]
    result = [num * 2 for num in n if num > 2]
    print(result)


advanced_loop()
# range_example(10,100,5)
# get_type_example(1)
# name_array = ["asaf", "dvir"]
# is_name_exist('asaf', name_array)
# input_example()
