# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# 1. Ask for user input. 
string_input = input("Input any string: ")

# 2. Assign True to lower case letters.
is_lower = True

# 3. Access each character in the input.
for char in string_input:

# 4. Check if characters are lower. If yes print true, if no print false.
    if not ("a" <= char <= "z"):
        is_lower = False
        break
print(is_lower)