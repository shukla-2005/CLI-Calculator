# Making a calculator that perform basic operations(+,-,*,/)

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract y from x."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide x by y. Handles division by zero."""
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def get_operation_choice():
    """Display menu and get user's operation choice."""
    print("\n--- Calculator Menu ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    
    while True:
        choice = input("Enter your choice (1-5): ").strip()
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        print("Invalid choice. Please enter 1-5.")

def get_numbers():
    """Get two numbers from user input."""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def main():
    """Main function to run the calculator loop."""
    print("Welcome to the Simple Calculator!")
    
    while True:
        choice = get_operation_choice()
        
        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        num1, num2 = get_numbers()
        
        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        
        # to ask user to perform more operation or not
        continue_choice = input("\nDo you want to perform another operation? (y/n): ").strip().lower()
        if continue_choice != 'y':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()