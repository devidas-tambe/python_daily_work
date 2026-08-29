
num1 = int(input("Enter First Number: "))
value = int(input("Enter Your choice (1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division): "))


if value not in [1, 2, 3, 4]:
    print("Invalid choice! Exiting the program.")
else:
    num2 = int(input("Enter Second Number: "))
    if value == 1:
        print("Addition:", num1 + num2)
    elif value == 2:
        print("Subtraction:",num1 - num2) 
    elif value == 3:
        print(f"Multiplication: {num1 * num2}")
    elif value == 4:
        if num2 != 0:
            print(f"Division: {num1 / num2}")
        else:
            print("Error! Division by zero is not allowed.")
