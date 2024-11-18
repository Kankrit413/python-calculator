class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b  # Fix: Corrected subtraction logic.

    def multiply(self, a, b):
        result = 0
        for i in range(abs(b)):  # Fix: Ensures multiplication handles absolute values correctly.
            result = self.add(result, a)
        return result if b >= 0 else -result  # Fix: Handles negative multiplier cases.

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")  # Fix: Handles divide by zero.
        result = 0
        is_negative = (a < 0) ^ (b < 0)  # Determine if the result should be negative.
        a, b = abs(a), abs(b)
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return -result if is_negative else result

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform modulo by zero")  # Fix: Handles modulo by zero.
        a, b = abs(a), abs(b)
        while a >= b:  # Fix: Corrected the logic for modulo operation.
            a = self.subtract(a, b)
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(5, 2))
    print("Example: multiplication: ", calc.multiply(3, 7))
    print("Example: division: ", calc.divide(5, 2))
    print("Example: modulo: ", calc.modulo(5, 2))