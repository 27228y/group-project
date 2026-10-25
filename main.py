def add(x, y):
    return x + y


def subtract(x, y):
    return x + y  # ОШИБКА №1 (логическая): здесь +, а должно быть -


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def calculator():
    print("Python Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return

        if choice == "1":
            print(f"Result: {add(num1, num2)}")
        elif choice == "2":
            # ОШИБКА №2 (NameError): написали nums1 вместо num1
            print(f"Result: {subtract(nums1, num2)}")
        elif choice == "3":
            print(f"Result: {multiply(num1, num2)}")
        elif choice == "4":
            print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid Input")


if name == "__main__":
    calculator()
