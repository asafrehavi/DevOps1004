from urls_functions import get_rest_response


def enter_name(file_name):
    names_file = open(file_name, "a")
    current_name = input('enter your name')
    names_file.write(f"{current_name}\n")
    names_file.close()


def print_file(file_name):
    names_file = open(file_name)
    print("file content")
    lines = names_file.readlines()
    for line in lines:
        print(line)


def call_urls():
    with open("urls.txt") as urls:
        for line in urls.readlines():
            get_rest_response(line.strip())


call_urls()
