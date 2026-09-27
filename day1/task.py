# Strings
print("Hello, World!")

# New line character
print("Hello, World!\nHello, World!\nHello, World!")

# String concatenation
print("Hello, " + "World!")

# Input from user
print("Hello, " + input("Enter your name: ") + "!")

#variable assignment
name = input("Enter your name: ")
print("Hello, " + name + "!")
print(len(name))

# Pythoic swap
a = 5
b = 10
a, b = b, a
print(a, b)


# Project 1 Band Name Generator
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + pet + ".")