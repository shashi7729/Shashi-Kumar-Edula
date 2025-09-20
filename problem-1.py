class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def calculate(self, operation: str):
        if operation == "add":
            return self.a + self.b
        elif operation == "sub":
            return self.a - self.b
        elif operation == "mul":
            return self.a * self.b
        elif operation == "div":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Division by zero not allowed"
        else:
            return "Invalid operation"


a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
op = input("Enter operation (add, sub, mul, div): ").strip().lower()

calc = Calculator(a, b)
print("Result:", calc.calculate(op))
