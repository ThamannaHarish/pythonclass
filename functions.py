def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Division by zero is not allowed."

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Modulus by zero is not allowed."


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))


print("\nResults")
print(f"Addition: {add(a, b)}")
print(f"Subtraction: {subtract(a, b)}")
print(f"Multiplication: {multiply(a, b)}")
print(f"Division: {divide(a, b)}")
print(f"Modulus: {modulus(a, b)}")
