# Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

# 1. Ask for user input.
string_input = input("Enter any string: ")

# 2. Assign which character to count and the numbers of count.
to_count = "e"
count = 0
# 3. Create a loop to access every character in the input. 
for char in string_input:

# 4. Count the character you assigned from the user input.
    if char == to_count:
        count += 1

# 5. Print the count.
print('"e" appeared: ', count)