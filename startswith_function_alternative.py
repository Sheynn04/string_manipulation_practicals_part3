# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

# 1. Ask for user input.
string_input = input("Enter a string: ")

# 2. Assign a variable for the prefix or the start with.
starts_with = "dy"

# 3. Check if the user input starts with the prefix. Print True if yes, print False if no.
if string_input[:len(starts_with)] == starts_with:
    print("True")

else:
    print("False")
