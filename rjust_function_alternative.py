# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

# 1. Ask for user input. 
string_input = input("Enter any string: ")

# 2. Assign a width for the statement.
width = 100

# 3. Add spaces to the user input if it's under the width
if len(string_input) < width:
    string_input = " " * (width - len(string_input)) + string_input

# 4. Print the final output.
print(string_input)