num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Enter the operation (+, -, *, /): ")

result = (
    int(num1) + int(num2) if operation == "+"  else
    int(num1) - int(num2) if operation == "-"  else
    int(num1) * int(num2) if operation == "*" else
    int(num1) / int(num2) if operation == "/" else
    "Error - invalid input" )

print(f"The result is: {result}")