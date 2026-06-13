def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b


def calculator():
    print("=" * 40)
    print("        SIMPLE CALCULATOR")
    print("=" * 40)

    while True:
        print("\nOperations:")
        print("  1. Addition       (+)")
        print("  2. Subtraction    (-)")
        print("  3. Multiplication (*)")
        print("  4. Division       (/)")
        print("  5. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == '5':
            print("\nThank you for using the Calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please enter a number between 1 and 5.")
            continue

        try:
            num1 = float(input("Enter first number  : "))
            num2 = float(input("Enter second number : "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if choice == '1':
            result = add(num1, num2)
            symbol = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            symbol = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            symbol = '*'
        elif choice == '4':
            result = divide(num1, num2)
            symbol = '/'

        print("-" * 40)
        if isinstance(result, str):
            print(f"Result : {result}")
        else:
            print(f"Result : {num1} {symbol} {num2} = {result}")
        print("-" * 40)


calculator()
