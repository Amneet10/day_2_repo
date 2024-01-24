# Function to multiply two numbers
def multiply_numbers(num1, num2):
    result = num1 * num2
    return result

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calling the function to multiply the numbers
product = multiply_numbers(num1, num2)

# Displaying the result
print(f"The product of {num1} and {num2} is: {product}")

# Function to multiply three numbers
def multiply_three_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calling the function to multiply the numbers
product = multiply_three_numbers(num1, num2, num3)

# Displaying the result
print(f"The product of {num1}, {num2}, and {num3} is: {product}")

