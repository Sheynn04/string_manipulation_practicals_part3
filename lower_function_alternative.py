# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# 1. Ask for user input.
string_input = input("Input any string: ")

# 2. Assign a final string variable. 
final_string = ""

# 3. Create a loop to access each character of the input.
for char in string_input:

# 4. Transform all lowercase characters into uppercase.
    if "a" <= char <= "z":
        final_string += chr(ord(char) - 32)
    else:
        final_string += char


# 5. Print the final output. 
print(final_string)