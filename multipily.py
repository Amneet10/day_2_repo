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

