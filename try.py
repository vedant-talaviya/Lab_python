try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = number1 / number2
    
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    
except ValueError:
    print("Error: Please enter a valid number.")
    
else:
    print("division successful. Result:", result)
    
finally:
    print("This block always executes.")