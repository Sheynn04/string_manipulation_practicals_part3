# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

# 1. Ask for the user inout.
string_input = input("Input any string: ")

# 2. Assign a suffix
suffix = "dy"

# 3. Create an if statement and use endswith() function as an alternative for removesuffix().
if string_input.endswith(suffix):

# 4. Print the result.
    print(string_input[:-len(suffix)])
else:
    print(string_input)