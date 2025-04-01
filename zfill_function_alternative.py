# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# 1. Ask for user input.
user_input = input("Enter numbers: ")

# 2. Assign a width to fill.
width = 10

# 3. Add zeros to the front if it's under the width.
if len(user_input) < width:
    user_input = "0" * (width - len(user_input)) + user_input

# 4. Print the final output.
print(user_input)