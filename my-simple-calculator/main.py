import math

# Function to perform the operations
def calculator():
    print("Welcome to the Simple Calculator!")
    
    try:
        # Input the first number
        num1 = float(input("Enter the first number: "))
        
        # Input the operation
        operation = input("Enter the operation (+, -, *, /): ")
        
        # Input the second number
        num2 = float(input("Enter the second number: "))
        
        # Perform the calculation
        if operation == '+':
            result = math.fsum([num1, num2])
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Division by zero is not allowed.")
                return
        else:
            print("Invalid operation. Please use +, -, *, or /.")
            return
        
        # Display the result
        print(f"The result is: {result}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values only.")

# Call the calculator function
calculator()
