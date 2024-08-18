class CalculatorApp:
    
    def add(self, a, b):
        """Return the sum of two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Return the difference of two numbers."""
        return a - b
    
    def multiply(self, a, b):
        """Return the product of two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Return the quotient of two numbers."""
        if b == 0:
            return "Error! Division by zero."
        return a / b

# Example usage:
if __name__ == "__main__":
    calc = CalculatorApp()

    num1 = float(input("Enter the first no: "))
    num2 = float(input("Enter the second no: "))

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print(f"The result is: {calc.add(num1, num2)}")
    elif choice == '2':
        print(f"The result is: {calc.subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {calc.multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result is: {calc.divide(num1, num2)}")
    else:
        print("Invalid input")
