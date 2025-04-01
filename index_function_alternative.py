# Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

#1. Ask for the user input.
user_input = input("Input any string: ")

# 2. Get the letter to find from the user.
index = input("What letter to find? : ")

# 3. Count the characters before the indexed character.
position = 0
for char in user_input:
    if char != index:
        position += 1
    elif char == index:
        break

# 4. Print the length of characters before the indexed character.
print(position)