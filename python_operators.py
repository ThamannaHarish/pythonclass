# Simple Python Program Demonstrating All Operators

a=int(input("Enter the operand:"))
b=int(input("Enter the operand:"))
x, y = True, False

print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

print("\nAssignment Operators:")
x1 = 5
x1 += 2; print("x += 2:", x1)
x1 -= 1; print("x -= 1:", x1)
x1 *= 3; print("x *= 3:", x1)
x1 /= 2; print("x /= 2:", x1)
x1 %= 4; print("x %= 4:", x1)
x1 **= 2; print("x **= 2:", x1)
x1 //= 2; print("x //= 2:", x1)

print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\nLogical Operators:")
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

print("\nBitwise Operators:")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)

print("\nSpecial Operators:")
l1 = [1, 2]
l2 = l1
l3 = [1, 2]
print("l1 is l2:", l1 is l2)
print("l1 is l3:", l1 is l3)
print("l1 is not l3:", l1 is not l3)
print("'a' in 'apple':", 'a' in 'apple')
print("'x' not in 'apple':", 'x' not in 'apple')
