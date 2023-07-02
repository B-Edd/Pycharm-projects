import random

file = open('sentences.txt', 'a')
read_file = open('sentences.txt', 'r')
starting = ["Hi! How may I help you today?", "Wassap?", "Yo.", "Hello!"]


def dict_of_file(read_file):
    dict_data = {}
    for line in read_file:
        stripped_line = [s.rstrip() for s in line.split(": ")]
        if len(stripped_line) == 2:
            key = stripped_line[0]
            value = stripped_line[1]
            dict_data[key] = value

    return dict_data


def append_to_f(k, v):
    file.write(str(k) + ": " + str(v) + "\n")


def check_file(user_turn):
    dictionary = dict_of_file(read_file)
    if user_turn in dictionary:
        values = dictionary[user_turn]
        if isinstance(values, list):
            random_value = random.choice(values)
            print(random_value)
        else:
            print(values)
    else:
        dictionary_yn = input("Answer not in dictionary. Do you want to add one(y/n)?: ")
        if dictionary_yn.lower() == 'y':
            say = input("What should I say?: ")
            append_to_f(user_turn, say)
            print(say)
        else:
            print("Continue...")


print(random.choice(starting))

boolean = True
while boolean:
    user = input()
    if user == "exit":
        print("Thank you for talking with me!")
        boolean = False
    check_file(user)


read_file.close()
file.close()
