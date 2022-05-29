names_file = open("HEB.txt", "a")
current_name = input('enter your name')
names_file.write(f"{current_name}\n")
names_file.close()