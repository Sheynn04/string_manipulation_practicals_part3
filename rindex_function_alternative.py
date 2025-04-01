# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

#1. Ask for the user input.
user_input = input("Input any string: ")

# 2. Get the letter to find from the user.
index = input("Letter to find: ")

# 3. Count the characters before the indexed character.
position = -1

for i in range(len(user_input) -1,-1,-1):
    if user_input[i] == index:
        position = i
        break

# 4. Print the length of characters before the indexed character.
print(position)