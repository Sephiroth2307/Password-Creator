import random

def generate_password(length, symbols):
    letters = "abcdefghijk1mnopgrstuvwxyzABCDEFGHIJKLMNOPORSTUVWXYZ"
    numbers = "0123456789"
    combination = letters + numbers + symbols

    password_characters = []

    for i in range(length):
        password_characters.append(random.choice(combination))

    password = "".join(password_characters)

    return password

symbols = input("Enter the symbols do you want in you password: ")
length = int(input("Enter length of your password: "))

password = generate_password(length, symbols)
print(password)
