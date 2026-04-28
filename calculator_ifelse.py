
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
value = int(input("Enter Your choice (1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division): "))



if value == 1:
    print("Addition: is",num1 + num2)
elif value == 2:
    print(f"Subtraction: {num1 - num2}")
elif value == 3:
    print(f"Multiplication: {num1 * num2}")
elif value == 4:
    if num2 != 0:
        print(f"Division: {num1 / num2}")
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid value case!")
