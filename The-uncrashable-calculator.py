try:
    num1 = int(input("Enter the top number: "))
    num2 = int(input("Enter the bottom number: "))

    result = num1 / num2
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: please enter the number only.")

print("Calculation finished")