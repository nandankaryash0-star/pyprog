# Basic calculator
try:
    operator = input("Enter an operator (+ - * /): ")

    num1 = float(input("Enter 1st Number: "))
    num2 = float(input("Enter 2nd Number: "))

    if operator == "+":
        result = num1 + num2
        print(round(result))

    elif operator == "-":
        result = num1 - num2
        print(round(result))

    elif operator == "*":
        result = num1 * num2
        print(round(result))

    elif operator == "/":
        result = num1 / num2
        print(round(result))

    else:
        print(f"{operator} is not valid operator ")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Please Enter the number only, not text")