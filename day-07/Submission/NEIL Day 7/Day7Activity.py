file =  open('user_info.txt', 'w')

user_input = input("What is your name? ")

file.write(user_input)

file.close()